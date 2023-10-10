import paho.mqtt.publish as publish

# MQTT server settings
broker_address = "mosquitto"
port = 1883
topic = "request"

# Sending a message to the MQTT server
try:
    while True:
        message = input()
        publish.single(topic, message, hostname=broker_address, port=1883)
except KeyboardInterrupt:
    pass


