let http = require("http")
let fs = require("fs")
function process_req(req,resp)
{
    fs.readFile("welcome.html",function(err,data)
    {
        resp.writeHead(200,
            {
                'Content-Type' : 'text/html'
            })
            resp.write(data);
            resp.end();
    })
}
let server = http.createServer(process_req)
server.listen(2000,"127.0.0.1")    //localhost
console.log("server is running on http://127.0.0.1:2000")