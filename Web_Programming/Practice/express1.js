let express = require('express')
let app = express()
// get function have minimum 2 arguments get("url", callback function)
app.get("/", function(req, resp)		
{
	let d1 = new Date()
	let str = "<h1>Get Hello World!</h1>"
	str += "Today is" + d1.toString()
	let obj = {Name:"Payal",Age:"23",PRN:"220340126022"}
	resp.send(obj)
	resp.send(str)
})
app.post("/", function(req, resp)
{
	resp.send("<h1>Post Hello World!</h1>")
})
app.put("/", function(req, resp)
{
	resp.send("<h1>Put Hello World!</h1>")
})
app.delete("/", function(req, resp)
{
	resp.send("<h1>Delete Hello World!</h1>")
})
app.listen(3000, function()
{
	console.log("Server is listning on localhost : 3000")
})