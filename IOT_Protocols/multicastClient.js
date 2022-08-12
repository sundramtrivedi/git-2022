const coap = require('coap') // or coap

// Send multicast message
coap.request({
	pathname: '/temp',
	host: '224.0.1.186',
	multicast: true,
	multicastTimeout: 2000
}).end()
