"""
Combination of multiple media players into one for a universal controller.

For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/media_player.universal/
"""
import logging
from copy import copy

import voluptuous as vol

from homeassistant.components.media_player import (
    MediaPlayerDevice, PLATFORM_SCHEMA)
from homeassistant.components.media_player.const import (
    ATTR_APP_ID, ATTR_APP_NAME, ATTR_INPUT_SOURCE, ATTR_INPUT_SOURCE_LIST,
    ATTR_MEDIA_ALBUM_ARTIST, ATTR_MEDIA_ALBUM_NAME, ATTR_MEDIA_ARTIST,
    ATTR_MEDIA_CHANNEL, ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE,
    ATTR_MEDIA_DURATION, ATTR_MEDIA_EPISODE, ATTR_MEDIA_PLAYLIST,
    ATTR_MEDIA_POSITION, ATTR_MEDIA_POSITION_UPDATED_AT, ATTR_MEDIA_SEASON,
    ATTR_MEDIA_SEEK_POSITION, ATTR_MEDIA_SERIES_TITLE, ATTR_MEDIA_SHUFFLE,
    ATTR_MEDIA_TITLE, ATTR_MEDIA_TRACK, ATTR_MEDIA_VOLUME_LEVEL,
    ATTR_MEDIA_VOLUME_MUTED, DOMAIN, SERVICE_CLEAR_PLAYLIST,
    SERVICE_PLAY_MEDIA, SERVICE_SELECT_SOURCE, SUPPORT_CLEAR_PLAYLIST,
    SUPPORT_SELECT_SOURCE, SUPPORT_SHUFFLE_SET, SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON, SUPPORT_VOLUME_MUTE, SUPPORT_VOLUME_SET,
    SUPPORT_VOLUME_STEP)
from homeassistant.const import (
    ATTR_ENTITY_ID, ATTR_ENTITY_PICTURE, ATTR_SUPPORTED_FEATURES, CONF_NAME,
    CONF_STATE, CONF_STATE_TEMPLATE, SERVICE_MEDIA_NEXT_TRACK,
    SERVICE_MEDIA_PAUSE, SERVICE_MEDIA_PLAY, SERVICE_MEDIA_PLAY_PAUSE,
    SERVICE_MEDIA_PREVIOUS_TRACK, SERVICE_MEDIA_SEEK, SERVICE_MEDIA_STOP,
    SERVICE_SHUFFLE_SET, SERVICE_TURN_OFF, SERVICE_TURN_ON,
    SERVICE_VOLUME_DOWN, SERVICE_VOLUME_MUTE, SERVICE_VOLUME_SET,
    SERVICE_VOLUME_UP, STATE_IDLE, STATE_OFF, STATE_ON, STATE_UNAVAILABLE)
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.service import async_call_from_config

_LOGGER = logging.getLogger(__name__)

ATTR_ACTIVE_CHILD = 'active_child'
ATTR_DATA = 'data'

CONF_ATTRS = 'attributes'
CONF_CHILDREN = 'children'
CONF_COMMANDS = 'commands'
CONF_SERVICE = 'service'
CONF_SERVICE_DATA = 'service_data'

OFF_STATES = [STATE_IDLE, STATE_OFF, STATE_UNAVAILABLE]

ATTRS_SCHEMA = cv.schema_with_slug_keys(cv.string)
CMD_SCHEMA = cv.schema_with_slug_keys(cv.SERVICE_SCHEMA)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Optional(CONF_CHILDREN, default=[]): cv.entity_ids,
    vol.Optional(CONF_COMMANDS, default={}): CMD_SCHEMA,
    vol.Optional(CONF_ATTRS, default={}):
        vol.Or(cv.ensure_list(ATTRS_SCHEMA), ATTRS_SCHEMA),
    vol.Optional(CONF_STATE_TEMPLATE): cv.template
}, extra=vol.REMOVE_EXTRA)


async def async_setup_platform(hass, config, async_add_entities,
                               discovery_info=None):
    """Set up the universal media players."""
    player = UniversalMediaPlayer(
        hass,
        config.get(CONF_NAME),
        config.get(CONF_CHILDREN),
        config.get(CONF_COMMANDS),
        config.get(CONF_ATTRS),
        config.get(CONF_STATE_TEMPLATE)
    )

    async_add_entities([player])


class UniversalMediaPlayer(MediaPlayerDevice):
    """Representation of an universal media player."""

    def __init__(self, hass, name, children,
                 commands, attributes, state_template=None):
        """Initialize the Universal media device."""
        self.hass = hass
        self._name = name
        self._children = children
        self._cmds = commands
        self._attrs = {}
        for key, val in attributes.items():
            attr = val.split('|', 1)
            if len(attr) == 1:
                attr.append(None)
            self._attrs[key] = attr
        self._child_state = None
        self._state_template = state_template
        if state_template is not None:
            self._state_template.hass = hass

    async def async_added_to_hass(self):
        """Subscribe to children and template state changes.

        This method must be run in the event loop and returns a coroutine.
        """
        @callback
        def async_on_dependency_update(*_):
            """Update ha state when dependencies update."""
            self.async_schedule_update_ha_state(True)

        depend = copy(self._children)
        for entity in self._attrs.values():
            depend.append(entity[0])
        if self._state_template is not None:
            for entity in self._state_template.extract_entities():
                depend.append(entity)

        self.hass.helpers.event.async_track_state_change(
            list(set(depend)), async_on_dependency_update)

    def _entity_lkp(self, entity_id, state_attr=None):
        """Look up an entity state."""
        state_obj = self.hass.states.get(entity_id)

        if state_obj is None:
            return

        if state_attr:
            return state_obj.attributes.get(state_attr)
        return state_obj.state

    def _override_or_child_attr(self, attr_name):
        """Return either the override or the active child for attr_name."""
        if attr_name in self._attrs:
            return self._entity_lkp(
                self._attrs[attr_name][0], self._attrs[attr_name][1])

        return self._child_attr(attr_name)

    def _child_attr(self, attr_name):
        """Return the active child's attributes."""
        active_child = self._child_state
        return active_child.attributes.get(attr_name) if active_child else None

    async def _async_call_service(self, service_name, service_data=None,
                                  allow_override=False):
        """Call either a specified or active child's service."""
        if service_data is None:
            service_data = {}

        if allow_override and service_name in self._cmds:
            await async_call_from_config(
                self.hass, self._cmds[service_name],
                variables=service_data, blocking=True,
                validate_config=False)
            return

        active_child = self._child_state
        if active_child is None:
            # No child to call service on
            return

        service_data[ATTR_ENTITY_ID] = active_child.entity_id

        await self.hass.services.async_call(
            DOMAIN, service_name, service_data, blocking=True)

    def __plex_or_atv_attr(self, attr_name):
        """Fill in with Plex data as needed."""
        # The ATV media player does not properly display Plex metadata.
        # For example, it doesn't display any data when Plex music is playing,
        # it doesn't display TV show names when Plex TV episodes are playing,
        # it displays the TV show art instead of TV show episode art, etc.
        # This function returns Plex meta-data when Plex is playing or paused.
        # Otherwise it returns ATV metadata.

        plex_state = self.hass.states.get(self._children[1])
        if plex_state is None:
            plex_state = ""
        else:
            plex_state = plex_state.state

        if (plex_state == "playing" or plex_state == "paused"):
            return (self._entity_lkp(self._children[1], attr_name))
        else:
            return (self._entity_lkp(self._children[0], attr_name))

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    @property
    def master_state(self):
        """Return the master state for entity or None."""
        if self._state_template is not None:
            return self._state_template.async_render()
        if CONF_STATE in self._attrs:
            master_state = self._entity_lkp(
                self._attrs[CONF_STATE][0], self._attrs[CONF_STATE][1])
            return master_state if master_state else STATE_OFF

        return None

    @property
    def name(self):
        """Return the name of universal player."""
        return self._name

    @property
    def state(self):
        """Return the current state of media player.

        Off if master state is off
        else Status of first active child
        else master state or off
        """
        master_state = self.master_state  # avoid multiple lookups
        if (master_state == STATE_OFF) or (self._state_template is not None):
            return master_state

        active_child = self._child_state
        if active_child:
            return active_child.state

        return master_state if master_state else STATE_OFF

    @property
    def volume_level(self):
        """Volume level of entity specified in attributes or active child."""
        return self._override_or_child_attr(ATTR_MEDIA_VOLUME_LEVEL)

    @property
    def is_volume_muted(self):
        """Boolean if volume is muted."""
        return self._override_or_child_attr(ATTR_MEDIA_VOLUME_MUTED) \
            in [True, STATE_ON]

    @property
    def media_content_id(self):
        """Return the content ID of current playing media."""
        # return self._child_attr(ATTR_MEDIA_CONTENT_ID)
        return self.__plex_or_atv_attr("media_content_id")

    @property
    def media_content_type(self):
        """Return the content type of current playing media."""
        # return self._child_attr(ATTR_MEDIA_CONTENT_TYPE)
        return self.__plex_or_atv_attr("media_content_type")

    @property
    def media_duration(self):
        """Return the duration of current playing media in seconds."""
        return self._child_attr(ATTR_MEDIA_DURATION)

    @property
    def media_image_url(self):
        """Image url of current playing media."""
        # return self._child_attr(ATTR_ENTITY_PICTURE)
        return self.__plex_or_atv_attr("entity_picture")

    @property
    def entity_picture(self):
        """
        Return image of the media playing.

        The universal media player doesn't use the parent class logic, since
        the url is coming from child entity pictures which have already been
        sent through the API proxy.
        """
        return self.media_image_url

    @property
    def media_title(self):
        """Title of current playing media."""
        # return self._child_attr(ATTR_MEDIA_TITLE)
        return self.__plex_or_atv_attr("media_title")

    @property
    def media_artist(self):
        """Artist of current playing media (Music track only)."""
        # return self._child_attr(ATTR_MEDIA_ARTIST)
        return self.__plex_or_atv_attr("media_artist")

    @property
    def media_album_name(self):
        """Album name of current playing media (Music track only)."""
        # return self._child_attr(ATTR_MEDIA_ALBUM_NAME)
        return self.__plex_or_atv_attr("media_album_name")

    @property
    def media_album_artist(self):
        """Album artist of current playing media (Music track only)."""
        # return self._child_attr(ATTR_MEDIA_ALBUM_ARTIST)
        return self.__plex_or_atv_attr("media_album_artist")

    @property
    def media_track(self):
        """Track number of current playing media (Music track only)."""
        # return self._child_attr(ATTR_MEDIA_TRACK)
        return self.__plex_or_atv_attr("media_track")

    @property
    def media_series_title(self):
        """Return the title of the series of current playing media (TV)."""
        # return self._child_attr(ATTR_MEDIA_SERIES_TITLE)
        return self.__plex_or_atv_attr("media_series_title")

    @property
    def media_season(self):
        """Season of current playing media (TV Show only)."""
        # return self._child_attr(ATTR_MEDIA_SEASON)
        return self.__plex_or_atv_attr("media_season")

    @property
    def media_episode(self):
        """Episode of current playing media (TV Show only)."""
        # return self._child_attr(ATTR_MEDIA_EPISODE)
        return self.__plex_or_atv_attr("media_episode")

    @property
    def media_channel(self):
        """Channel currently playing."""
        # return self._child_attr(ATTR_MEDIA_CHANNEL)
        return self.__plex_or_atv_attr("media_channel")

    @property
    def media_playlist(self):
        """Title of Playlist currently playing."""
        # return self._child_attr(ATTR_MEDIA_PLAYLIST)
        return self.__plex_or_atv_attr("media_playlist")

    @property
    def app_id(self):
        """ID of the current running app."""
        # return self._child_attr(ATTR_APP_ID)
        return self.__plex_or_atv_attr("app_id")

    @property
    def app_name(self):
        """Name of the current running app."""
        # return self._child_attr(ATTR_APP_NAME)
        return self.__plex_or_atv_attr("app_name")

    @property
    def source(self):
        """Return the current input source of the device."""
        # return self._override_or_child_attr(ATTR_INPUT_SOURCE)
        return self.__plex_or_atv_attr("source")

    @property
    def source_list(self):
        """List of available input sources."""
        # return self._override_or_child_attr(ATTR_INPUT_SOURCE_LIST)
        return self.__plex_or_atv_attr("source_list")

    @property
    def shuffle(self):
        """Boolean if shuffling is enabled."""
        return self._override_or_child_attr(ATTR_MEDIA_SHUFFLE)

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        flags = self._child_attr(ATTR_SUPPORTED_FEATURES) or 0

        if SERVICE_TURN_ON in self._cmds:
            flags |= SUPPORT_TURN_ON
        if SERVICE_TURN_OFF in self._cmds:
            flags |= SUPPORT_TURN_OFF

        if any([cmd in self._cmds for cmd in [SERVICE_VOLUME_UP,
                                              SERVICE_VOLUME_DOWN]]):
            flags |= SUPPORT_VOLUME_STEP
            flags &= ~SUPPORT_VOLUME_SET
        elif SERVICE_VOLUME_SET in self._cmds:
            flags |= SUPPORT_VOLUME_SET

        if SERVICE_VOLUME_MUTE in self._cmds and \
                ATTR_MEDIA_VOLUME_MUTED in self._attrs:
            flags |= SUPPORT_VOLUME_MUTE

        if SERVICE_SELECT_SOURCE in self._cmds:
            flags |= SUPPORT_SELECT_SOURCE

        if SERVICE_CLEAR_PLAYLIST in self._cmds:
            flags |= SUPPORT_CLEAR_PLAYLIST

        if SERVICE_SHUFFLE_SET in self._cmds and \
                ATTR_MEDIA_SHUFFLE in self._attrs:
            flags |= SUPPORT_SHUFFLE_SET

        return flags

    @property
    def device_state_attributes(self):
        """Return device specific state attributes."""
        active_child = self._child_state
        return {ATTR_ACTIVE_CHILD: active_child.entity_id} \
            if active_child else {}

    @property
    def media_position(self):
        """Position of current playing media in seconds."""
        return self._child_attr(ATTR_MEDIA_POSITION)

    @property
    def media_position_updated_at(self):
        """When was the position of the current playing media valid."""
        return self._child_attr(ATTR_MEDIA_POSITION_UPDATED_AT)

    def async_turn_on(self):
        """Turn the media player on.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_TURN_ON, allow_override=True)

    def async_turn_off(self):
        """Turn the media player off.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_TURN_OFF, allow_override=True)

    def async_mute_volume(self, mute):
        """Mute the volume.

        This method must be run in the event loop and returns a coroutine.
        """
        data = {ATTR_MEDIA_VOLUME_MUTED: mute}
        return self._async_call_service(
            SERVICE_VOLUME_MUTE, data, allow_override=True)

    def async_set_volume_level(self, volume):
        """Set volume level, range 0..1.

        This method must be run in the event loop and returns a coroutine.
        """
        data = {ATTR_MEDIA_VOLUME_LEVEL: volume}
        return self._async_call_service(
            SERVICE_VOLUME_SET, data, allow_override=True)

    def async_media_play(self):
        """Send play command.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_MEDIA_PLAY)

    def async_media_pause(self):
        """Send pause command.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_MEDIA_PAUSE)

    def async_media_stop(self):
        """Send stop command.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_MEDIA_STOP)

    def async_media_previous_track(self):
        """Send previous track command.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_MEDIA_PREVIOUS_TRACK)

    def async_media_next_track(self):
        """Send next track command.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_MEDIA_NEXT_TRACK)

    def async_media_seek(self, position):
        """Send seek command.

        This method must be run in the event loop and returns a coroutine.
        """
        data = {ATTR_MEDIA_SEEK_POSITION: position}
        return self._async_call_service(SERVICE_MEDIA_SEEK, data)

    def async_play_media(self, media_type, media_id, **kwargs):
        """Play a piece of media.

        This method must be run in the event loop and returns a coroutine.
        """
        data = {ATTR_MEDIA_CONTENT_TYPE: media_type,
                ATTR_MEDIA_CONTENT_ID: media_id}
        return self._async_call_service(SERVICE_PLAY_MEDIA, data)

    def async_volume_up(self):
        """Turn volume up for media player.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_VOLUME_UP, allow_override=True)

    def async_volume_down(self):
        """Turn volume down for media player.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(
            SERVICE_VOLUME_DOWN, allow_override=True)

    def async_media_play_pause(self):
        """Play or pause the media player.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_MEDIA_PLAY_PAUSE)

    def async_select_source(self, source):
        """Set the input source.

        This method must be run in the event loop and returns a coroutine.
        """
        data = {ATTR_INPUT_SOURCE: source}
        return self._async_call_service(
            SERVICE_SELECT_SOURCE, data, allow_override=True)

    def async_clear_playlist(self):
        """Clear players playlist.

        This method must be run in the event loop and returns a coroutine.
        """
        return self._async_call_service(SERVICE_CLEAR_PLAYLIST)

    def async_set_shuffle(self, shuffle):
        """Enable/disable shuffling.

        This method must be run in the event loop and returns a coroutine.
        """
        data = {ATTR_MEDIA_SHUFFLE: shuffle}
        return self._async_call_service(
            SERVICE_SHUFFLE_SET, data, allow_override=True)

    async def async_update(self):
        """Update state in HA."""
        for child_name in self._children:
            child_state = self.hass.states.get(child_name)
            if child_state and child_state.state not in OFF_STATES:
                self._child_state = child_state
                return
        self._child_state = None
