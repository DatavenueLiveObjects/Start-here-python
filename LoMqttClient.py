"""
Copyright (C) 2016-2020 Orange

This software is distributed under the terms and conditions of the 'BSD 3'
license which can be found in the file 'LICENSE.txt' in this package distribution 
"""

import paho.mqtt.client as mqtt
import re
import ssl

class LoMqttClient(mqtt.Client):
    def __init__(self, server, port, apiKey, client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv31):
        mqtt.Client.__init__(self)
        self.server = server
        self.port = port
        self.apiKey = apiKey
        mqtt.Client.username_pw_set(self, username="application", password=self.apiKey)
        self._subTopics = {}
        mqtt.Client.tls_set(self, ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                tls_version=ssl.PROTOCOL_TLS, ciphers=None)

    def connect(self):
        print("MQTT connect "+str(self.server)+" "+str(self.port)+" "+str(self.apiKey))
        return mqtt.Client.connect(self, self.server, self.port, 10)    

    def unsubscribe(self, topic):
        (error, mid) = mqtt.Client.unsubscribe(self, topic)
        if error == mqtt.MQTT_ERR_SUCCESS and topic in self._subTopics:
            del self._subTopics[topic]
        return (error, mid)

    def subscribe(self, topic, qos=10, callback=None, callbackArg=None ):
        (error, mid) = mqtt.Client.subscribe(self, topic, qos=0)
        if error == mqtt.MQTT_ERR_SUCCESS:
            self._subTopics[topic] = {
                "request_qos":qos,
                "subMID":mid,
                "callback":callback,
                "callbackArg":callbackArg,
                "regex": re.compile(topic.replace("+", "[^/]+")),
            }
        return (error, mid)
