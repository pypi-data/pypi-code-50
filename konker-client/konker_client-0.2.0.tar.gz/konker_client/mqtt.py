import paho.mqtt.client as mqtt
import json
from konker_client.client import Client


class Mqtt(Client):

    def __init__(self, user, password):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.is_connected = False
        self.client.username_pw_set(user, password)
        self.client.connect('mqtt.demo.konkerlabs.net', 1883)
        self.client.loop_start()

    def send_message(self, channel: str, message: dict):
        message = json.dumps(message)
        self.client.publish(channel, message)

    def on_connect(self, client, userdata, flags, rc):
        self.is_connected = True
        if self.is_connected:
            print("Conectado com sucesso, aguardando mensagem.")
            self.client.subscribe("sub/426psued49pa/temp")

    def on_disconnect(self, client, userdata, rc):
        self.is_connected = False

    def on_message(self, client, data, msg):
        print(msg.topic + " " + str(msg.payload))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        print(f'Subscribe: {userdata}')
