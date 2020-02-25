# SENSOR: AUTOMATE

**/config/automations.yaml**
```yaml
- id: '1578361757420'
  alias: Turn on light when motion detected
  description: ''
  trigger:
  - entity_id: binary_sensor.kitchen_motion_sensor
    platform: state
    to: 'on'
  condition: []
  action:
  - data:
      brightness: 255
      effect: rainbow
    entity_id: light.kitchen_led
    service: light.turn_on
- id: '1578361849455'
  alias: Turn off light when motion off
  description: ''
  trigger:
  - entity_id: binary_sensor.kitchen_motion_sensor
    platform: state
    to: 'off'
  condition: []
  action:
  - entity_id: light.kitchen_led
    service: light.turn_off
```

***

[Previous](sensor-configure.md) | [Next](../node-red/install.md) |
[Table of Contents](../README.md#table-of-contents)