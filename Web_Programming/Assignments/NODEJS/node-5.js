let fs = require("fs")
fs.readFile("q5_data.txt",function(err,data){
	if(err)
		console.log("error while writing into file "+err.message)
		let sum = 0 
		let arr = data.toString().split("\n")
		for(i=0;i<arr.length;i++)
		{
			let record = arr[i].split(":")
			for(j=0;j<record.length;j++)
			{
				sum += parseInt(record[3])
			}
		}
		console.log("Sum of sal : ",sum)
})