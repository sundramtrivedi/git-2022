var express = require('express')
var app = express()
app.get("/string", function(req, resp)
{
	resp.sendFile("expr.html", {root: __dirname})
})
app.get("/stringPage", function(req, resp)
{
	var str1 = req.query.a1
	var str2 = req.query.a2
	var str3 = req.query.a3
	var str4 = req.query.a4
	var str5 = req.query.a5
	resp.send("<ul><li>"+ str1 +"</li><li>"+ str2 +"</li><li>"+ str3 +
		"</li><li>"+ str4 +"</li><li>"+ str5 +"</li></ul>")
})
app.listen(3000,function()
{
	console.log('Payal')
})