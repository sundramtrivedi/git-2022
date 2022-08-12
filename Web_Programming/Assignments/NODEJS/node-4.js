let fs = require("fs")
var arr = ["Payal","Sundram","Jeet","Ganesh"]
let str = arr.join("|")
fs.writeFile("name.txt",str,function(err){
	if(err)
		console.log("error while writing into file "+err.message)
})
