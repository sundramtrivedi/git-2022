module.exports =
{
	mqtt:
	{
		authenticate: function(client, username, password, callback)
		{
			// try to print client information here
			var isAuthenticate = (username=="diot" && password.toString() == "diot") 
			if(isAuthenticate)
			{
				// authenticated clients are allowed
				client.user = "diot";
				callback(null, true);
			}
			else
			{
				// authenticated clients are disconnected
				callback(null, false);
			}
		},
		// authorization for publish topics
		authorizePublish: function(client, topic, payload, callback)
		{
			// your logic for authorization
			if(client.user == topic.split("/")[1])
			{
				callback(null, true);
			}
			else
			{
				callback(null, false);
			}
			// payload length > 10
		},
		// authorization for subscribe topics
		authorizeSubscribe: function(client, topic, callback)
		{
			if(client.user == topic.split("/")[1])
			{
				callback(null, true);
			}
			else
			{
				callback(null, false);
			}
		}
	}
}
