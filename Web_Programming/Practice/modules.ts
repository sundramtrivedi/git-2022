export var sname = "Payal"
export function greet()
{
	console.log("hello",sname)
}
export class Student
{
	sname : string
	prn : number

	constructor(studname:string,prn:number)
	{
		this.sname = studname
		this.prn = prn
	}
	display()
	{
		console.log("Name : ", this.sname, "PRN : ", this.prn)
	}
}