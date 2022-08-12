let express = require('express')
const res = require('express/lib/response')
let app = express()
let books = 
			[
				{id:"1",bname:"Core Java",price:"400"},
				{id:"2",bname:"Core JSP",price:"500"},
				{id:"3",bname:"ExpressJS",price:"450"}
			]
app.get("/books",function(req, resp)
{
	let str = ""
	str += "<table border=1><tr><th>ID</th><th>Book Name</th><th>Price</th></tr>"
	for(i=0;i<books.length;i++)
	{
		str += "<tr><td>" + books[i].id + "</td><td>" + books[i].bname + "</td><td>" + books[i].price + "</td></tr>"
	}
	str += "</table>"
	resp.send(200, str)
})
app.listen(3001, function()
{
	console.log("Server is listning on localhost : 3000")
})