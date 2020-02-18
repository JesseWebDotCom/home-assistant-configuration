# Tensorflow

A common feature of cloud based security cameras like Nest is the ability to detect and alert when certain objects are detected (ex. Someone is at the front door, A package is at the front door).  This typically works by 1) a camera detects motion, 2) cloud based image processing analyzes the current frame or frames for desired objects, and 3) an alert is sent if the analysis has high confidence it sees objects it cares about.

We can easily do the same through Home Assistant and use Tensorflow as the image processing engine.

## Installation
1. Install and run the tensorflow addon:
   1. Add the [tensorflow Hass.io add-ons repository](https://github.com/hunterjm/hassio-addons) to your Hass.io instance
   2. Install the "TensorFlow Installer" add-on
   3. Start the "TensorFlow Installer" add-on
   4. Check the logs of the "TensorFlow Installer" add-on to see if everything went well
   5. Restart Home Assistant for changes to take effect
2. Download and extract this: https://github.com/robmarkcole/tensorflow_files_for_home_assistant_component
3. Put the tensorflow folder on /config dir
4. Download and extract this: http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
5. Rename the folder "ssd_mobilenet_v2_coco_2018_03_29" to "model"
6. Put the ‘model’ folder into /config/tensorflow dir
7. Add the following to configuration.yaml (modifying _scan interval to # of seconds tensorflow should update and an entity_id for each of your cameras):
```
image_processing:
 - platform: tensorflow
   scan_interval: 1
   source:
     - entity_id: camera.front_door
   model:
     graph: /config/tensorflow/model/frozen_inference_graph.pb
```

***

[Home](../README.md)