var express = require('express')
var app = express()
app.get("/rectPage", function(req, resp)
{
	resp.sendFile("rectangle.html", {root: __dirname})
})
app.get("/rect", function(req, resp)
{
	var length = parseInt(req.query.l)
	var breadth = parseInt(req.query.b)
	let area = length * breadth
	let perimeter = 2 * (length + breadth)
	resp.send("Area is : " + area + " " + "and Perimeter is : "+ perimeter)
})
app.listen(3000,function()
{
	console.log('Payal')
})