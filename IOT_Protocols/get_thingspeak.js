const axios = require('axios').default;	// axios import for program
//GET https://api.thingspeak.com/update?api_key=H7TWZHM4YVYTTXZ6&field1=0
axios({
	method: 'get',	// api's like get , post , put , delete , etc
	url: 'https://api.thingspeak.com/update',	// url which we want to see output
	params: {
		api_key : "H7TWZHM4YVYTTXZ6",	// api key in above url -> api -> api key copy
		field1 : 30
	}
	})
	.then(function (response) {
		console.log(response.status);	// function response
	})
	.catch(function (error) {
		console.log(error);	// function error
	});
