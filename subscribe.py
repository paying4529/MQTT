import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    topic = "test/#"
    client.subscribe(topic)
    print("topic: ", topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    print(topic+" "+payload)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

broker_ip = "172.20.10.3"
client.connect(broker_ip)
client.loop_forever()