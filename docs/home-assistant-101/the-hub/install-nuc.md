# INSTALLATION: NUC

- [Update the BIOS](#update-the-bios)
- [Image the NUC](#image-the-nuc)

Running [Home Assistant](http://home-assistant.io) on a NUC vs a Raspberry Pi brings several benefits:

- Everything is significantly faster
- You can run more CPU intensive processes
- You avoid SD card failures

## Update the BIOS
1. Connect a USB stick to a Windows machine (rather than Linux or MAC)
2. Fully format the USB stick to FAT32 (disable quick format option during format)
3. Download the latest BIOS file for your NUC and copy it to the USB stick
4. Connect the USB stick to the NUC and power the NUC on
5. Press F7 and follow the onscreen instructions

## Image the NUC
1. Preparing for installation
   1. Disable NUC Secure Boot (BIOS | Advanced | Boot | Secure Boot)
   2. Download [the Ubuntu Desktop image](http://releases.ubuntu.com/16.04.1/ubuntu-16.04.1-desktop-amd64.iso) and prepare a bootable USB flash drive.
   3. Download [the Home Assistant NUC image](https://www.home-assistant.io/hassio/installation/) and copy the file (…img.gz) to the second flash drive.
2. Boot from the Live USB flash drive
   1. Insert the Live USB Ubuntu Desktop flash drive in the NUC.
   2. Start the NUC and push F10 to enter the boot menu.
   3. Select the USB flash drive as a boot option.
   4. Select "Try Ubuntu without installing".
3. Image the NUC
   1. Once the system is ready, insert the second USB flash drive which contains the Hassio disk image.
   2.  (optional) Wipe the Nuc drive with the following command: `dd if=/dev/zero of=/dev/sda bs=1M`
   3.  Run: 
   `zcat /media/ubuntu/<usb disk label>/hassos_intel-nuc-2.5.img.gz | sudo dd of=/dev/sda bs=32M status=progress; sync`
4. Install Home Assistant
    1.  Reboot the system and remove all USB flash drives when prompted to do so.
    2.  Wait a few minutes (maybe 10) and connect: http://your_nuc_ip_address:8123
    
***

[Previous](install-pi.md) | [Next](setup.md) |
[Table of Contents](../README.md#table-of-contents)
