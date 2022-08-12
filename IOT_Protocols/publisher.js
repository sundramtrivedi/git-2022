const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://localhost:1883')
const TOPIC = "diot"
client.on('connect', function()
{
	console.log("Broker connected")
	client .publish( TOPIC, '{temp: 24.5 c}')
});
