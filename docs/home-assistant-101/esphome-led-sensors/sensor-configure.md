# SENSOR: CONFIGURE

**/config/esphome/esp32_kitchen.yaml**
```yaml
# setup esp32 board
esphome:
  name: esp32_kitchen
  platform: ESP32
  board: esp-wrover-kit

# setup wifi
wifi:
  ssid: "SSID_NAME"
  password: "SSID_PASSWORD"

  # Enable fallback hotspot (captive portal) in case wifi connection ever fails
  ap:
    ssid: "Esp32 Kitchen Fallback Hotspot"
    password: "SSID_PASSWORD"

captive_portal:

# Enable logging
logger:

# Enable Home Assistant API
api:
  password: "NEW_PASSWORD"

ota:
  password: "NEW_PASSWORD"

binary_sensor:
  - platform: gpio
    pin: GPIO21
    name: "Kitchen Motion Sensor"
    device_class: motion  
    
sensor:
  - platform: dht
    pin: GPIO22
    model: DHT22
    temperature:
      name: "Kitchen Temperature"
    humidity:
      name: "Kitchen Humidity"
    update_interval: 5s

light:
  # https://esphome.io/components/light/fastled.html?highlight=fastled_clockless#clockless
  - platform: fastled_clockless
    chipset:  WS2813
    pin: GPIO05
    num_leds: 60
    rgb_order: GRB
    name: "Kitchen LED"
    # https://esphome.io/components/light/index.html#light-effects
    effects:
      - random:
      - flicker:
      - addressable_color_wipe:
      - strobe:
      - addressable_rainbow:
      - addressable_scan:
      - addressable_twinkle:
      - addressable_random_twinkle:
      - addressable_fireworks:
      - addressable_flicker:
```

***

[Previous](sensor-build.md) | [Next](sensor-automate.md) |
[Table of Contents](../README.md#table-of-contents)