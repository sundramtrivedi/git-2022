const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://localhost:1883',
{
	protocolVersion: 4,
	protocolId: 'MQTT',
	clean: true,	//canalso be false
	clientId: 'diot_device_1',
	will:
	{
		topic: "device/dead",
		payload: Buffer.from("I am dead bro!!")
	},
	keepalive: 0
})
const TOPIC = "diot";
client.on('connect', function ()
{
	//subscribe only after success connection with broker
	client.subscribe(TOPIC, function (err)
	{
		if(!err)
		{
			console.log(`Successfully subscribed to ${TOPIC}`)
		}
	})
})
client.on('message', function (topic, message)
{
	//message is buffer
	console.log(message.toString())
	client.end()
})
