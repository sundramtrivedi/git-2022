let express = require('express')
let app = express()
app.get("/radPage", function(req, resp)
{
	resp.sendFile("circle.html", {root: __dirname})
})
app.get("/rad", function(req, resp)
{
	radius = parseFloat(req.query.radius)
	let area = Math.PI * radius * radius
	resp.send("Area is : " + area)
})
app.listen(3000, function()
{
	console.log("Payal")
})