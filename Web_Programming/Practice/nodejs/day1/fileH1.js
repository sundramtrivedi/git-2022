let fs = require("fs")
// fs.writeFileSync("test.txt","Hello,Welcome to File Handling");   // create a txt file and write on that text file
// console.log(fs.readFileSync("test.txt","utf8"))     // read text file
// console.log(contents)
fs.readFile("test.txt",function(err, data)
{
    if(err)
        console.error("Error in reading file")
    else
        console.log("Async :", data.toString())
})
var data = fs.readFileSync('test.txt')
console.log("Sync :", data.toString())