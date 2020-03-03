LoRa MQTT Client Sample
=======================

__LoRa MQTT Client Sample__ is a code sample for the MQTT protocol, written in Python.

## Quick start

### Download

clone from GitHub:

```
$ git clone https://github.com/Orange-OpenSource/LiveObjects-samples-python.git
```

### Prerequisites

Version of Python: tested with 2.7.10 and 3.5.2

This sample of code use the paho library. You should download the library with the `pip` tool

> pip install paho-mqtt

In order to retrieve data, a valide LoRa device must be provisioned on your account.
You should have a valid API-KEY with BUS_R role.

### First use

1. Open the LoMqttConf.py and replace the API-KEY with yours (with device profile to push data to LiveObjects, or application profile to read data from a FIFO)
2. Open the LoRaMqqtSample.py. In the `on_connect()` function, comment, uncomment or modify subscriptions (all devices PubSub, specific device PubSub or FIFO).
   Create a FIFO (see [Manual - Using FIFO](https://liveobjects.orange-business.com/doc/html/lo_manual_v2.html#BUS)), and update with the FIFO name (instead of "myfifo").
   Create the message routing configuration (see [Manual - Message routing](https://liveobjects.orange-business.com/doc/html/lo_manual_v2.html#MESSAGE_ROUTING)). 
3. Run the LoRaMqttSample.py

### Structure

This sample contains 3 files : 
* LoRaMqttSample.py: The main file, using the LoMqttClient class in order to retrieve LoRa data.
* LoMqttConf.py: The configuration file, filled with your API-KEY
* LoMqttClient.py: A class wrapping the Paho MQTT client, adding the Live Objects specifics. 

## License

Copyright (c) 2015 — 2016 Orange

This code is released under the BSD3 license. See the `LICENSE` file for more information.

## Contact

* Homepage: [liveobjects.orange-business.com](https://liveobjects.orange-business.com/)
