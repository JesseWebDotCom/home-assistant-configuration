# SETUP

- [Intital Setup](#intital-setup)
- [Add-ons](#add-ons)
- [Code Editing](#code-editing)

## Intital Setup
Once the install has completed:
- Screen 1: Create an account
- Screen 2: Click "Detect" and set your time zone and unit system
- Screen 3: Click Finish and then click "Save Login"

- Then click Supervisor | System| Reboot


## Add-ons
Install the following add-ons, setting usernames and passwords appropriately.

Add-on | Description
--|--
Samba share | Gives you direct Samba/SMB access to you instance's default shares
SSH & Web Terminal | Gives you SSH access (with optional web interface) to your instance

## Code Editing
We'll use Visual Studio Code as our Home Assistant code editor as it has several advantages:

- It's free
- Home Assistant extensions for VS Code add features like auto completion
- The editor can be run from your Home Assistant instance if running on an Intel NUC

1. Follow [these instructions](https://github.com/SeanPM5/homeassistant-config/wiki/Editing-Home-Assistant-in-Visual-Studio-Code) to install VS Code and relevant extensions
2. Open Home Asisstant, click on the circled user account icon (bottom left), and create a Long-lived access token
3. Open VS Code and configure the Home Assistant extension with the URL to your Home Assistant server and the long lived access token you just created.

![HA Extension Settings](../images/vscode_ha.png)


***

[Previous](install-nuc.md) | [Next](gui.md) |
[Table of Contents](../README.md#table-of-contents)