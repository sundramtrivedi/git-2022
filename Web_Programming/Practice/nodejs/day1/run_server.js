let http = require("http")
function process_req(req, resp)
{
    let body = "Hello, Welcome to Node server"
    let content_length = body.length
    resp.writeHead(200,
        {
            'Content-Length' : content_length,
            'Content-Type' : 'text/pain'
        })
    resp.write(body);
    resp.end();
}
let server = http.createServer(process_req)
server.listen(3000,"127.0.0.1")    //localhost
console.log("server is running on http://127.0.0.1:3000")