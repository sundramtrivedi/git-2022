const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://localhost:1883')
const TOPIC = "diot"
client.on('connect', function () 
{
	//subscribe only after successful connection with broker
	client.subscribe(TOPIC, function (err)
	{
		if(!err)
		{
			console.log(`Successfully subscribed to ${TOPIC}`);
		}
	})
})

client.on('message', function(topic, message)
{
	//message is buffer
	console.log(message.toString())
	client.end()
})
