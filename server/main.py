import paho.mqtt.client as mqtt



class actor:
    def __init__(self, name):
        self.state = 'Off'
        self.name = name

    def setstate(self, state):
        self.state = state

    def getstate(self):
        client.publish(f"{self.name}", self.state)

# Обработчик подключения к брокеру MQTT
def on_connect(client, userdata, flags, rc):
    # Подписываемся на тему "request"
    client.subscribe("request")


# Обработчик приема сообщения от брокера MQTT
def on_message(client, userdata, message):
    name, func, state, *_ = message.payload.decode().split() + ['']
    if func == 'get':
        devices[name].getstate()
    elif func == 'set':
        devices[name].setstate(state)
        client.publish(f'{name}', f'State of valve changed to {devices[name].state}')




# Создание клиента MQTT для сервера
client = mqtt.Client()

Valve = actor('Valve')
Switch = actor('Switch')

devices = {
    Valve.name: Valve,
    Switch.name: Switch,
}

# Установка обработчиков
client.on_connect = on_connect
client.on_message = on_message

broker_address = "mosquitto"  # IP-адрес брокера MQTT
port = 1883  # Порт MQTT сервера

# Подключение к брокеру MQTT на localhost, порт 1883
client.connect(broker_address, port, 60)

# Основной цикл для обработки сообщений
try:
    client.loop_forever()
except KeyboardInterrupt:
    pass




