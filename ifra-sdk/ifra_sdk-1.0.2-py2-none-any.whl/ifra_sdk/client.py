
from kpn_senml import *
import paho.mqtt.client as mqtt
import time
import resource_monitoring as rm

IFRA_MQTT_SERVER = "hub.ifra.io"

class IfraSDK():
  def __init__(self, channel, device_id,device_secret):
    self.channel = channel
    self.device_id = device_id
    self.device_secret = device_secret
    self.pack = SenmlPack("")
    self.client = mqtt.Client("makerio_mqtt") 
    self.client.username_pw_set(username=self.device_id,password=self.device_secret)
    self.client.connect("hub.ifra.io", 1883) 

    self.client.on_message = self.on_message 
    self.client.loop_start() 
 
  def on_log(mqttc, obj, level, string):
        print(string)
    # The callback for when the client receives a CONNACK response from the server.
  def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.client.subscribe("organization/"+self.channel+"/messages") 

  def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))


  def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")
  def addActuator(self,sensor_name,unit,value):
     pass

  def addSensor(self,sensor_name,unit,value):
     self.pack.add(SenmlRecord(sensor_name, unit=unit, value=value))

  def send(self):
     topic = "organization/"+self.channel+"/messages"
     self.client.publish(topic, self.pack.to_json(), qos=0, retain=False) 
     self.pack.clear()
  def toJson(self):
     return self.pack.to_json()


