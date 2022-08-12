import paho.mqtt.client as mqtt

print("Starting publisher...")

topic=input("Enter the topic to publish : ")
QoS=0

client=mqtt.Client()

client.connect("127.0.0.1",1883)

client.loop_start()
try:
	while 1:
		message=input("Message to send : ")
		(rc,mid)=client.publish(topic,message,QoS)
		if rc==0:
			print("--Message Sent--")
except KeyboardInterrupt:
	client.disconnect()
	client.loop_stop()
