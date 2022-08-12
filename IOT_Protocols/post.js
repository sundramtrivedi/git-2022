const axios = require('axios').default;	// axios import for program

axios({
	method: 'post',	// api's like get , post , put , delete , etc
	url: 'https://connect.cloud.kaaiot.com:443/kp1/call0o0n7nk35lghpd4g-v01/dcx/lfWPtLp6WZ/json',	// url which we want to see output
	data: {
		"API_KEY": "LwELW8v1Wii18LW",	// api key in above url -> api -> api key copy
		"type": "Kitchen",
		"tag": "Arduino",
		"value": 50,
		"Payal":22,
		"Sundram":27,
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
