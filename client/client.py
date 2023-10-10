import paho.mqtt.publish as publish

# Настройки MQTT сервера
broker_address = "mosquitto"  # IP-адрес брокера MQTT
port = 1883  # Порт MQTT сервера
topic = "request"  # Тема для отправки сообщения

# Отправка сообщения на сервер MQTT
try:
    while True:
        message = input()
        publish.single(topic, message, hostname=broker_address, port=1883)
except KeyboardInterrupt:
    pass


