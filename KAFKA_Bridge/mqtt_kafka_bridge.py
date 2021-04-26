import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import psutil
import time

# MQTT part :
mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("MQTTBridge")
mqtt_client.connect(mqtt_broker)

# Kafka part :
kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics["RAM_1"]
kafka_producer = kafka_topic.get_sync_producer()

def on_message(client, userdata, message):
    msg_payload = str(message.payload.decode("utf-8", "ignore"))
    print("Receive MQTT message ", msg_payload)
    #Everytime we receive a msg from mqtt_client we send a message to kafka
    kafka_producer.produce(str(msg_payload).encode("utf-8"))
    print("Kafka: Just published " + str(msg_payload) + " to topic RAM")

mqtt_client.loop_start()
mqtt_client.subscribe("RAM_1")
mqtt_client.on_message = on_message
while True:
    time.sleep(30)
