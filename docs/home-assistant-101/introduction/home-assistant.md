# INTRODUCTION: HOME ASSISTANT

- [Benefits](#benefits)
- [Disadvantages](#disadvantages)
- [Key Terms](#key-terms)
- [Key Shares](#key-shares)
- [Default Config Files & Folders](#default-config-files--folders)
- [Getting Smarter](#getting-smarter)

Home Assistant is an automation platform with the following benefits over popular 3rd party alternatives like Google Home, Samsung Smartthings, and Apple HomeKit.

## Benefits
Home Assistant has many advantages over 3rd party home automation platforms.

| Home Assistant | 3rd Party (Ex. Apple, Google) | 
|:--------------:|:------:|
Free | Pay
Open source | Closed
Local privacy | Cloud stored datahome-assistant.log
Hardware Independent | Hardware Dependent
Cloud Independent | Cloud Dependent
\> 1,500 integrations | < 1,000 integrations
Extensible | Limited

## Disadvantages
But it also has some key disadvantages:

Disadvantage | Description | Mitigation
--|--|--
Availability | You're bound to encounter downtime at some point (ex. through a code change, an update, or just bad luck).  These often come at inopportune times and can create some disgruntled users (ex. like when family members can't open the garage). | Take backups often, especially before making changes; Perform changes when users aren't dependent on the system and when you have time to remediate any issues
Skills, time, & patience required | As with any DIY project, there will always be a demand for skills, time, and patience. | Acceptance 

## Key Terms

Term | Definition
--|--
[Home Assistant](https://www.home-assistant.io/faq/ha-vs-hassio/) | The Home Assistant project, program (aka Home Assistant Core), or standalone installer (formerly known as Hassio) which installs the Home Assistant Operating system, Home Assistant Core, add-on store, and more
[Home Assistant Core](https://www.home-assistant.io/faq/ha-vs-hassio/) | The raw Home Assistant Python program
[Home Assistant Cloud](https://www.nabucasa.com) | Aka Nuba Casa, a pay service to support the core development team and ease setup of certain components
[Home Assistant Companion](https://companion.home-assistant.io) | The mobile app
Entities | Every device connected to Home Assistant is represented by an "entity".  Some devices have multiple features (ex. Battery level, Smoke Level) which may be represented by additional entities.
[Integrations](https://www.home-assistant.io/integrations/) | (formally known as components) Connectors to popular data sources, device types, and services
[Yaml](https://www.home-assistant.io/docs/configuration/yaml/) | A common markup language Home Assistant uses

## Key Shares

Name | Stores
--|--
addons | custom add-ons
backup | snapshot backups
config | coded configurations
share | unknown
ssl | SSL certificates

## Default Config Files & Folders

Name | Purpose
--|--
[automations.yaml](https://www.home-assistant.io/integrations/automation/) | (I used Node-RED instead, click for more info) Home Assistant yaml based automations
[configuration.yaml](https://www.home-assistant.io/docs/configuration/) | The core configuration file where everything is loaded and configured
[/deps](https://www.home-assistant.io/faq/dependencies/) | Storage area for automatically downloaded and updated dependency files
[groups.yaml](https://www.home-assistant.io/integrations/group/) | (being phased out) Creates named collections of entities (ex. Upstairs Lights)
[home-assistant_v2.db](https://www.home-assistant.io/docs/backend/database/) | Primary database location for event history (configurable throug the [recorder integration](https://www.home-assistant.io/integrations/recorder/))
home-assistant.log | Primary log file (configurable through the [logger integration](https://www.home-assistant.io/integrations/logger/))
[scenes.yaml](https://www.home-assistant.io/integrations/scene/) | Stores "scenes" - set specfic device states by name (ex. "Reading" - sets the table lamp to 50% and turns off the recessed lighting)
[scripts.yaml](https://www.home-assistant.io/integrations/script/) | Stores "scripts" - custom sequence of actions you can execute by name (ex. "alarm" - flashes lights, sounds the siren, and sends an alert)
[secrets.yaml](https://www.home-assistant.io/docs/configuration/secrets/) | Stores sensitive data (ex. passwords) you can reference by name (ex. my_password)
[/tts](https://www.home-assistant.io/integrations/tts/) | Text to speech engine

## Getting Smarter
* [Website](https://home-assistant.io/) - Main site and reference
* [YouTube Channel](https://www.youtube.com/channel/UCbX3YkedQunLt7EQAdVxh7w) - Youtube Channel (tutorials, talks, etc)
* [GitHub Examples](https://github.com) - Find examples by searching for "home-assistant configuration"
* [Community](https://community.home-assistant.io/) - Community posts
* [Chat](https://discordapp.com/invite/c5DvZ4e) - Misc chat
* [Reddit](https://www.reddit.com/r/homeassistant/) - Misc posts
  
***

[Previous](home-automation.md) | [Next](../the-hub/install-pi.md) |
[Table of Contents](../README.md#table-of-contents)
