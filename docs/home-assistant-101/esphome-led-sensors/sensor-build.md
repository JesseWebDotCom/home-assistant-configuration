# SENSOR: BUILD

![Bruh Multisensor Mod](../images/jwdc_bruh_mod.svg)

## Tools Needed
To minimize the assembly time, skill level, and tooling required, you will only need a pair of scissors and electrical tape (to strip and secure wires/connections).  If you have experience, tools, and time, you can choose to solder and or crimp connections instead.

## LED Strip

| Step | Illustrations | 
|--------------|------|
<ul><li>Cut off the USB Type A connector</li><li>Strip back the shield, exposing the 4 inner wires</li><li>Cut off the white and green wires</li><li>Strip back the shield on the red (+5V) and black (GND) wires</li></ul> | ![LED USB Prep](../images/led_usb_prep.png)
<ul><li>Determine your desired strip length</li><li>Cut along the copper contacts</li></ul> | ![LED USB Prep](../images/led_cut.png)
<ul><li>Open the connector</li><li>Slide the cut strip into the connector and under the contacts</li><li>Ensure correct contact to wire placement (5V=blue wire, BI=red wire, DI=green wire, GND=black wire)</li><li>Close the connector</li></ul> | ![LED USB Prep](../images/led_connector.png)
<ul><li>Strip all 4 wires on the connector and on a 4 foot, 4 wire extension cable</li><li>Connect the connector's and extension's red and green wires all together (these are for data redudancy)</li><li>Connect the connector's and extension's blue wires to the USB red wire</li><li>Connect the connector's and extension's black wires to the USB black wire</li></ul> | ![LED USB Prep](../images/led_wire_1.png)
<ul><li>Insert the blue/red wire bundle into the power plug's positive (+) terminal and screw secure</li><li>Insert the black wire bundle into the power plug's negative (-) terminal and screw secure</li></ul> | ![LED USB Prep](../images/led_wire_2.png)
<ul><li>Tape up the green/red bundle and then the wires connecting to the plug</li><li>Tape around the plug and all wires</li></ul> | ![LED USB Prep](../images/led_tape_1.png)![LED USB Prep](../images/led_tape_2.png)
<ul><li>Strip the black, green, and red wires on the other end of the extension cable</li><li>Strip the end of 2 female dupont connector wires</li></ul> | ![LED USB Prep](../images/led_wire_3.png)
<ul><li>Connect the black extension wire to one dupont wire and connect the red+green extension wires to the other dupont wire</li></ul> | ![LED USB Prep](../images/led_wire_4.png)
<ul><li>Connect the black extension/dupont connector to ESP32 pin 2 (GND)</li><li>Connect the red+green extension/dupont connector to ESP32 pin 8 (GPIO05)</li></ul> | ![LED USB Prep](../images/led_connect.png)

## Human, Temperature, & Humidity Sensors

| Step | Illustrations | 
|--------------|------|
<ul><li>Strip the end of 6 female dupont connetor wires</li></ul> | ![LED USB Prep](../images/y_wires.png)
<ul><li>Connect and tape 3 stripped wires together; Connect 1 end to DHT22 positive(+), 1 to AM312 positive(+), and 1 to ESP32 pin 8 (GPIO05)</li></ul> | ![LED USB Prep](../images/y_connected.png)
<ul><li>Connect and tape the remaining 3 stripped wires together; Connect 1 end to DHT22 negative(-), 1 to AM312 negative(-), and 1 to ESP32 pin 2 (GND)</li></ul> | ![LED USB Prep](../images/y_connected.png)
<ul><li>Connect a female dupont wire to DHT22 data pin and another to AM312 data pin</li></ul> | 
<ul><li>Insert a 4.7k ohm resistor between the DHT22's positive(+) and data pins</li></ul> | ![LED USB Prep](../images/dht_resistor.png)

***

[Previous](esphome.md) | [Next](sensor-configure.md) |
[Table of Contents](../README.md#table-of-contents)