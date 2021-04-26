from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError, LeaderNotAvailable
import time
from itertools import islice
from flask import Flask, render_template, Response

def get_kafka_client():
    return KafkaClient(hosts="localhost:9092")

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/topic/<topicname>')
def get_message(topicname):
    client = get_kafka_client()
    print(client)
    def events():
        topic = client.topics[topicname]
        consumer = topic.get_simple_consumer()

        for message in consumer:
            yield 'data:{0}\n\n'.format(message.value.decode("utf-8", "ignore"))
    return Response(events(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

'''
client = KafkaClient()
topic = client.topics['RAM']
consumer = topic.get_simple_consumer()
print(consumer)


for message in consumer:
    print("Kafka consumer receive msg numero : ", message.offset, " with value : ", message.value.decode("utf-8", "ignore"))

try:
    consumer.consume()
except (SocketDisconnectedError) as e:
    consumer = topic.get_simple_consumer()
    # use either the above method or the following:
    consumer.stop()
    consumer.start()


'''

