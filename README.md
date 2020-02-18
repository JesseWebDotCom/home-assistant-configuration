# Home-Assistant Configuration

This is my personal home automation configuration using Home Assistant (http://home-assistant.io) - hereby referred to as HA.  My configuration is built off of many online docs, tips, and examples over many grueling hours of trial and error.  I've tried to document what I've learned so hopefully it will help others (and prevent me from making the same mistakes twice).

**NOTE:** Sensitive files (ex. secrets.yaml) and folders (ex. www) have been excluded from this repository.

- [Home Assistant 101](#home-assistant-101)
- [My Server](#my-server)
- [My Devices](#my-devices)
- [Issues & Fixes](#issues--fixes)
  - [Hassio fails to boot with error "Failed to start Docker Application Container Engine."](#hassio-fails-to-boot-with-error-failed-to-start-docker-application-container-engine)
  - [Hassio boots into the 4 menu option (autoboot, boot 1, boot 2, shell)](#hassio-boots-into-the-4-menu-option-autoboot-boot-1-boot-2-shell)
- [Misc Tips](#misc-tips)
  - [HOMEKIT](#homekit)
  - [Yeelight](#yeelight)

## Home Assistant 101
Check out my [concise guide](/docs/home-assistant-101/README.md) on getting into the world of Home Automation, standing up your own Home Assistant server, building your own sensors, and more.

## My Server
Here are my exact components:
* Intel NUC NUC7i5DNKE Core i5-7300U 8GB RAM 128GB SSD
* [GoControl CECOMINOD016164 HUSBZB-1 USB Hub](https://www.amazon.com/gp/product/B01GJ826F8/)

## My Devices
Some of my devices integrated, accessed, and or controlled by the HA server:
* Audio
  * [ChromeCast Audio v1](https://www.google.com/chromecast/speakers/)
  * [Pyle PDIC Speakers](https://www.amazon.com/gp/product/B00LRTLYIA/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00LRTLYIA&linkId=c30676c46d8baf9d458bbb27ad0168a9)
  * [Pyle PFA300 Amp](https://www.amazon.com/gp/product/B0071HZ5LE/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0071HZ5LE&linkId=a49e6464f65ec04e99262e100e6198d6)
* Assistants (Speakers, Hubs)
  * [Google Mini](https://store.google.com/us/product/google_home_mini)
  * [Google Nest Hub](https://store.google.com/us/product/google_nest_hub)
* Cars
  * BMW i3
  * Volvo xc90 
* Door/Window
  * [Google Nest Hello Video Doorbell](https://store.google.com/us/product/nest_hello_doorbell)
  * [Aeotec by Aeon Labs ZW089 Recessed Door Sensor, Small, White](https://www.amazon.com/gp/product/B0151Z49BO/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0151Z49BO&linkId=bf87da2400f219a73c7069df63801449)
  * [Ecolink Door/Window Sensor](https://www.amazon.com/gp/product/B00HPIYJWU/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00HPIYJWU&linkId=b1a47dbe6a4844bd6648aa50e8bb637a)
  * [Dome Door/Window Sensor](https://www.amazon.com/Dome-Automation-Miniature-Z-Wave-DMWD1/dp/B01JGMZNNG/ref=sr_1_2?keywords=Dome+DMWD1&qid=1550276960&s=electronics&sr=1-2)
* Garage Door
  * [GoControl/Linear GD00Z-4 Z-Wave Garage Door Opener Remote Controller](https://www.amazon.com/GoControl-Linear-GD00Z-4-Z-Wave-Controller/dp/B00M75TEIU/)
  * [LINEAR FS20Z-1 Z-Wave 20-amp Isolated Contact Fixture Module](https://www.amazon.com/gp/product/B00EPTMFH8/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00EPTMFH8&linkId=5540f1fc78284934a4396cce562eb12b)
  * [Ecolink Garage Door Tilt Sensor](https://www.amazon.com/gp/product/B01MRZB0NT/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01MRZB0NT&linkId=68a681219a55c26f1b4560a2d0dbfb78)
* Leaks
  * [Dome Leak Sensor](https://www.amazon.com/gp/product/B01LXR0B8Q/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01LXR0B8Q&linkCode=as2&tag=jessewebdotco-20&linkId=7bdb96807d874cd6c4e3353a225b0503)
  * [Aeotec Water Sensor](https://www.amazon.com/Aeotec-Water-Sensor-Z-Wave-Flood/dp/B00H3TJ3P4)
* Lighting
  * [Leviton DZS15-1BZ Decora Z-Wave Controls 15-Amp Scene Capable Switch](https://www.amazon.com/gp/product/B01GONGX98/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
  * [EVOLVE LRM-AS Z-Wave Lighting Control Dimmer Switch](https://www.amazon.com/dp/B0072RT9UQ?tag=findbestdeals1-20)
  * [GE 45606 Z-Wave Technology 2-Way Dimmer Switch](https://www.amazon.com/GE-45606-Z-Wave-Technology-Dimmer/dp/B0013V3C4Q/ref=cm_cr_arp_d_product_top?ie=UTF8)
  * [Leviton VRI10-1LZ Vizia RF+ Incandescent Dimmer 1000W](https://www.amazon.com/Leviton-VRI10-1LZ-Incandescent-Dimmer-Z-Wave/dp/B001HT0P8U)
  * [GE 45613 Z-Wave Wireless Lighting Control Three-Way Dimmer Kit](https://www.amazon.com/GE-45613-Wireless-Lighting-Three-Way/dp/B0013V58K2)
  * [GE Smart Fan Control, Z-Wave, In-Wall, 12730](https://www.amazon.com/GE-Control-Z-Wave-12730-Amazon/dp/B00PYMGVVQ)
* Media
  * [Plex](https://plex.tv/)
* Motion Sensors
  * [GE 34193 Enbrighten Z-Wave Plus Smart Motion Sensor](https://www.amazon.com/gp/product/B01KQDIU52)
  * [MultiSensor 6, ZW100-A, by Aeotec, Cert ID: ZC10-15070011](https://www.amazon.com/gp/product/B0151Z8ZQY/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0151Z8ZQY&linkId=24d3c72d09df4c49aef399d0836c2eb8)
* Network
  * [Ubiquiti Unifi AC](https://www.ubnt.com/unifi/unifi-ac/)
* Outlets/Plugs
  * [Linear PS15Z-2 Z-Wave Plug-In Remote On/Off Appliance Module, Small, White](https://www.amazon.com/gp/product/B00E1P15M2/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00E1P15M2&linkId=68c00fd4e25c81d4c5019f700cd8a164)
  * [GoControl WO15Z-1 Z-Wave Single Wall Outlet, White](https://www.amazon.com/gp/product/B00JFK1YRE/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)
  * [Inovelli Indoor Dual Z-Wave Plug](https://inovelli.com/shop/smart-plugs/2-channel-smart-plug/)
  * [Inovelli Outdoor Dual Z-Wave Plug](https://inovelli.com/shop/outdoor-smart-plugs/outdoor-zwave-plugin-module-2-channel/)
  * [GE 40 Amp Smart Switch](https://www.amazon.com/gp/product/B00YTCZZF0/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00YTCZZF0&linkId=5a2e3150dcfa58f4c68d1eeb2d36c834)
  * [GE Outdoor Smart Plug Switch](https://www.amazon.com/gp/product/B06W9NWFM3/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B06W9NWFM3&linkId=4b7e2f8e3467cb000fe406d1b4973eb0)
* Personal Devices
  * [Apple iPhone](http://www.apple.com/iphone/)
  * [Apple iPad](http://www.apple.com/ipad/)
* Remotes
  * [Logitech Harmony Ultimate Home Black - With Harmony Home Hub](http://www.bestbuy.com/site/logitech-harmony-ultimate-home-black/8203175.p?skuId=8203175)
* Surveillance
  * [Blue Iris Software](https://www.amazon.com/gp/product/B005DMX1OM/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B005DMX1OM&linkId=b77e3eb5ffa4d7ba52814fc3bb25874a)
  * [Reolink 5MP PoE Camera RLC-410-5MP](https://www.amazon.com/gp/product/B07DFKTKGG/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
  * [Reolink PoE Camera 5MP Super HD 4X Optical Zoom RLC-511](https://www.amazon.com/gp/product/B07GNFSWCS/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
  * [Foscam C1 Indoor HD 720P Wireless IP Camera with Night Vision](https://www.amazon.com/gp/product/B00T7NX6SY/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00T7NX6SY&linkId=706e619ae45dbafcaed04ef76106ca22)
* Valves
  * [WaterCop Z-Wave Shut-Off Valve Actuator and 3/4" Valve Smart Leak Prevention Kit](https://www.amazon.com/gp/product/B07C91B69P/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B07C91B69P&linkId=585d18af2c7d1f5509b783b00e5deabc)

## Issues & Fixes
### Hassio fails to boot with error "Failed to start Docker Application Container Engine."
See issue "Hassio boots into the 4 menu option"

### Hassio boots into the 4 menu option (autoboot, boot 1, boot 2, shell)
This issue occured because my system drive was full (HA database, snapshots, etc).  To fix:
1. Follow steps 1 and 2 above of [Image the NUC](#image-the-nuc)
2. Open a terminal, run "sudo nautilus", and delete unneeded snapshots from hassos-data/supervisor/backup
3. Reboot

## Misc Tips
### HOMEKIT
* To reset HomeKit, delete /config/.homekit.state

### Yeelight
* How to enable yeelight developer mode:
https://getyeti.co/posts/how-to-control-yeelight-and-your-smarthome-with-yeti