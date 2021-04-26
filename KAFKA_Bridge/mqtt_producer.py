import paho.mqtt.client as mqtt
import time
import psutil

# https://mqtt.eclipseprojects.io/
mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("MQTTProducer2")
client.connect(mqttBroker)

while True:
    mem = psutil.virtual_memory()
    # print(mem)
    client.publish("RAM_1", mem.percent)
    print("just published : " + str(mem.percent) + " to topic RAM")
    time.sleep(3)