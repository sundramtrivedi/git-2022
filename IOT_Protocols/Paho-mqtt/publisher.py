import paho.mqtt.client as mqtt

print("Starting publisher...")

topic="diot"
QoS=0

client=mqtt.Client()

#client.on_connect=on_connect

def on_connect(client,userdata,flags,rc):
	if rc==0:
		print("connected to Broker")
		client.publish(top,"hello",QoS)

client.on_connect=on_connect
# Send Connect command/request to Broker
client.connect("localhost",1883)
