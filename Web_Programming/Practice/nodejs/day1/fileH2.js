let fs = require("fs")
fs.writeFile("abc.txt","This is Content of abc.txt",function(err)
{
    if(err)
    {
        console.error("File Could not be written into")
    }
})