# INTRODUCTION: HOME AUTOMATION

- [The Math](#the-math)
  - [Device Control](#device-control)
  - [Home Control](#home-control)
  - [Home Automation](#home-automation)
  - [Smart Home](#smart-home)
- [Benefits and Possibilities](#benefits-and-possibilities)
  - [Convenience](#convenience)
  - [Climate](#climate)
  - [Multimedia](#multimedia)
  - [Savings](#savings)
  - [Surveillance](#surveillance)
  - [Safety](#safety)
  - [Security](#security)

## The Math
Inspired by the [Home Assistant breakdown of the Smart Home](https://www.home-assistant.io/blog/2014/12/26/home-control-home-automation-and-the-smart-home/), here is my breakdown of how we get from single device control to the smart home of tomorrow.
```bash
IOT Device + Controller = Device Control
IOT Devices + Common Controller = Home Control
Home Control + Triggers + Conditions = Home Automation
Home Automation + Self Learning = Smart Home
```

### Device Control
```bash
IOT Device + Controller = Device Control
```

IOT (Internet of Things) are networked devices you can remotely control (ex. Phillips Hue Bulb, Nest Thermostat).

Unfortunately there is no common IOT communication standard, so consumers are left individually controlling their devices through separate apps and or hubs (i.e. local hardware that manages devices).

### Home Control
```bash
IOT Devices + Common Controller = Home Control
```

The ideal solution is to have all devices communicate using a common standard.  While [efforts in this direction](https://www.connectedhomeip.com) have started, its unknown when or if it will be delivered, whether it will be effective, and whether it will be compatible with your existing and or future devices.   

Until then, the next ideal solution (this is where Home Assistant shines) is to have a single controller (app, hub) capable of speaking to all your devices in the various communication standards they expect.

### Home Automation
```bash
Home Control + Triggers + Conditions = Home Automation
```
Automatically controlling devices (ex. turn on driveway light) when an event occurs (ex. garage opens) under specific conditions (ex. when its dark) enables home automation.  This can even include  automations that appear to be the result of futuristic artifical intelligence but are nothing more than complex, predefined logic.

This is the most we can expect from any system today.

### Smart Home
```bash
Home Automation + Self Learning = Smart Home
```
Many people equate "smart home" with "home automation" but a true smart home is one that continuously learns and adapts.  It recognizes our patterns, filters out noise, and make accurate predicitions (better than we would make ourselves).

There is no system today that truly delivers on this smart home vision.


## Benefits and Possibilities
With a true smart home beyond our grasp, we can still build a  powerful, automated home.  Here are a few examples of what's possible.

### Convenience
* **Garage**
    * _**Open/Close Alerts**_ | Sends push notifications when garage opens or closes
    * _**Automatic Lighting**_ | Turn outdoor and indoor lights (near the garage) on and off when the garage door opens or closes (ex. Light up the driveway when I open the garage late at night)
* **Lighting**
    * _**Motion Lighting**_ | Turn on lights when motion detected (via motion sensor or camera)
* **People Alerts**
    * _**Anyone**_ | Alert when anyone is at the front door, garage, back yard, etc
    * _**Family & Friends**_ | Alert when specific people arrive or depart
- Control devices with your voice
- Control everything from a single app

### Climate
* **Temperature**
    * _**Alerting**_ | Get alerts when temperature in any room gets too hot or too cold (know when your HVAC is malfunctoning)
* **Cooling**
    * _**Automatic Cooling**_
        * _**Sleeping**_ | Turn the fan on or off depending on if you are getting in or out of bed
        * _**Gaming**_ | Turn down the temperature when playing a specific video game
    * _**Air Conditioner**_ | Turn AC on/off
    * _**Fan Control**_ | Turn fans on/off, control speed
* **Humidity**
    * _**Automatic Venting**_ | Automatically turn on bathroom fan when humidity is high (i.e. someone is showering)

### Multimedia
* **Control**
    * _**Room/Whole House Control**_ | Control audio and video streaming in any room, change volume, track, etc, view who is streaming what, and more
* **Audio**
    * _**Room/Whole House Audio**_ | Play music per room, in room groups, or across the entire house
* **Video**
    * _**Game Time / Movie Night**_ | Sit back, use your TV remote to watch TV or play a game, and have the lights dim or turn off.  Have them turn on when you turn off the TV.
    * _**Smart Motion Lighting**_ | Lights turn on and off whenever motion is detected - but not when you are playing a game or watching a movie.

### Savings
- Automatically turn off lights, TVs, computers, and more when they are not in use
* **Lighting**
    * _**Awareness**_ | Instantly see total lights on, which ones, etc
    * _**Indoor Light Saver**_ | Automatically turns off certain lights left on too long (ex. turn off attic lights after 15 minutes)
- Alert when the refrigerator/freezer door was left open

### Surveillance
* _**Fee & Cloud Free**_ | Eliminate monthly/yearly fees and cloud availability and privacy issues by running and storing recorded video locally
* _**Video Monitoring**_ | Watch live video feeds
* _**Continuous Recording**_ | Records everything, 24x7

### Safety
- Alert when there's smoke, fire, CO, leaks, etc
- Alert when your kids get to the bus stop, school, home, etc
- Alert when you've left your car unlocked or windows open
- Alert when its raining, snowing, or hailing and you've left your car doors open
- Automatically turn on lights where its dark inside and outside

### Security
- Alert when an animal or vehicle is outside
- Alert when a person is inside or outside
- Send alerts that will get your attention (text, siren, flash lights, etc)


***

[Next](home-assistant.md) |
[Table of Contents](../README.md#table-of-contents)