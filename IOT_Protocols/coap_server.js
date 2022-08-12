const coap = require('coap')
const server = coap.createServer()

server.on('request', (req, res) => {
	//print req res
	//req url
	if(req.url == "/temp")
	{
		//some random temperature values
		res.end('Temp : 24.5');
	}
	else
	{
		res.end('Hello ' + req.url.split('/')[1] + '\n')
	}
	console.log(req);
	//console.log(res);
	res.end('Hello ' + req.url.split('/')[1] + '\n')
})

//the default CoAP port is 5683
server.listen(() => {
	console.log("CoAP server started ...");
})
