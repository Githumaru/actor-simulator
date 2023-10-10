import paho.mqtt.client as mqtt


# Define an actor class to represent devices
class actor:
    def __init__(self, name):
        self.state = 'Off'
        self.name = name

    def setstate(self, state):
        self.state = state

    def getstate(self):
        client.publish(f"{self.name}", self.state)

# Callback for handling MQTT connection
def on_connect(client, userdata, flags, rc):
    # Подписываемся на тему "request"
    client.subscribe("request")


# Callback for handling received MQTT messages
def on_message(client, userdata, message):
    name, func, state, *_ = message.payload.decode().split() + ['']
    if func == 'get':
        devices[name].getstate()
    elif func == 'set':
        devices[name].setstate(state)
        client.publish(f'{name}', f'State of valve changed to {devices[name].state}')




# Create an MQTT client for the server
client = mqtt.Client()

# Create instances of devices (actors)
Valve = actor('Valve')
Switch = actor('Switch')

# Store devices in a dictionary
devices = {
    Valve.name: Valve,
    Switch.name: Switch,
}

# Set up MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

broker_address = "mosquitto"  # IP address of the MQTT broker
port = 1883  # Port of the MQTT server

# Connect to the MQTT broker
client.connect(broker_address, port, 60)

# Main loop for handling messages
try:
    client.loop_forever()
except KeyboardInterrupt:
    pass




