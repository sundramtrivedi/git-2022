class Student
{
    constructor(sname, prn)
    {
        this.sname = sname
        this.prn = prn
    }
    display()
    {
        console.log(this.sname, this.prn)
    }
}
// exports.person = {name : "Payal" , age : "23"}
module.exports = Student