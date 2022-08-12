var express = require('express')
var app = express()
app.get("/si", function(req, resp)
{
	resp.sendFile("interest.html", {root: __dirname})
})
app.get("/siPage", function(req, resp)
{
	var principal = req.query.p1
	var rate = req.query.p2
	var time = req.query.p3
	var sinterest = ((principal*rate*time)/100)
	resp.send("Simple Interest : " + sinterest)
})
app.listen(3000,function()
{
	console.log('Payal')
})