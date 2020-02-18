# Z-Wave
Z-Wave is my system of choice to control (ex. lights, fans, outlets, sirens, etc) and inform on (ex. Water, motion, energy sensors) just about anything in my home.


# Device Configurations
Some devices require specific Z-Wave configurations to work with Home Assistant.  You can also change a device's configuration to tweak its behavior.

Device | Configuration | Details
--|--|--
[Aeotec MultiSensor 6](https://www.amazon.com/gp/product/B0151Z8ZQY/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0151Z8ZQY&linkId=24d3c72d09df4c49aef399d0836c2eb8)  |  On Duration = 2 Minutes (shorter and device always displays as off) | Parameter 3 = 125
[Aeotec MultiSensor 6](https://www.amazon.com/gp/product/B0151Z8ZQY/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0151Z8ZQY&linkId=24d3c72d09df4c49aef399d0836c2eb8)  |  Temperature Sensor Interval = 120 Seconds | Parameter 111 = 120
[Aeotec Recessed Door Sensor](https://www.amazon.com/gp/product/B0151Z49BO/ref=as_li_tl?ie=UTF8&tag=jessewebdotco-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B0151Z49BO&linkId=bf87da2400f219a73c7069df63801449)  |  Report types = Binary and Basic Reports | Parameter 121 = 272
[Aeotec Water Sensor](https://www.amazon.com/Aeotec-Water-Sensor-Z-Wave-Flood/dp/B00H3TJ3P4) | Report types = Sensor Binary and Battery Report | Parameter 121 = 17