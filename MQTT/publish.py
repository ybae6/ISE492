# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish


publish.single("CoreElectronics/test", "Julio", hostname="test.mosquitto.org")
publish.single("CoreElectronics/topic", "Poop", hostname="test.mosquitto.org")
print("Done")