const axios = require('axios').default;	// axios import for program

axios({
	method: 'delete',	// api's like get , post , put , delete , etc
	url: 'https://sleepy-island-07017.herokuapp.com/sensor',	// url which we want to see output
	data: {
		"API_KEY": "LwELW8v1Wii18LW",	// api key in above url -> api -> api key copy
		"type": "Kitchen",
		"tag": "ESP32",
		"value": 50,
		"unit": "C"
	},
	headers:{
		"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2Mjk4YzcwNjg0NGFhZTAwMTdhOTBmMGUiLCJpYXQiOjE2NTQxNzk1OTB9.-Nn2zpPRBakvulKRSPzW97Xr4NwEfFvCJVTMYH3DR6k"	// for authorization to get rid of 401 error
	}
	})
	.then(function (response) {
		console.log(response);	// function response
	})
	.catch(function (error) {
		console.log(error);	// function error
	});
