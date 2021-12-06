import time
import json
import datetime
import paho.mqtt.client as mqtt

client = mqtt.Client()

broker_ip = "172.20.10.3"
client.connect(broker_ip)
client.loop_start()

topic = "test/b"

while True:
    t = datetime.datetime.now().strftime("%m/%d %H:%M:%S")
    payload = {"time": t}
    print(json.dumps(payload))
    client.publish(topic, json.dumps(payload))
    time.sleep(1)