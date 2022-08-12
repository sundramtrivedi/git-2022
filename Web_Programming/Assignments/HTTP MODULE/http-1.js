var http = require('http')
var fs = require('fs')
function process_request(req,resp)
{
	fs.readFile('welcome.html', function(err,data)
	{
		resp.writeHead(200, {'content-Type' : 'text/html'})
		resp.write(data)
		resp.end()
	})
}
var s = http.createServer(process_request)
s.listen(3000,function()
{
	console.log('Payal')
})