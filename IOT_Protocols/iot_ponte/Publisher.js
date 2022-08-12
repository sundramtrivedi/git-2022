// publisher with different QoS
const mqtt = require('mqtt');
const client = mqtt.connect('mqtt://localhost:1883',
{
	username: "diot",
	password: "diot",
	protocolversion: 4
});
const TOPIC = "diot";
const OPTIONS = { qos: 0, retain: true};
client.on('connect', function ()
{
	console.log("Broker Connected!!");
	client.publish( TOPIC, '{temp: 25 C}', OPTIONS, function(err)
	{
		if(!err)
		{
			console.log("Published Success!");
		}
	});	// publish method ends
});
client.on("disconnect", () =>
{
	console.log("Publisher disconnected!!");
});
