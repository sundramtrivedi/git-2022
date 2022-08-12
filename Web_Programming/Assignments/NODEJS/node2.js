class Arithmetic
{
	constructor(num1, num2, num3, arr)
	{
		this.num1 = num1
		this.num2 = num2
		this.num3 = num3
		this.arr = arr
	}
	add()
	{
		console.log("Addition is : "+ (this.num1 + this.num2))
	}
	substract()
	{
		console.log("Substract is : "+ (this.num1 - this.num2))
	}
	multiply()
	{
		console.log("Addition is : "+ (this.num1 * this.num2))
	}
	divide()
	{
		console.log("Division is : "+ (this.num1 / this.num2))
	}
	square()
	{
		console.log("Square is : "+ (this.num1 * this.num1))
	}
	sum()
	{
		var total = 0
		for(var i = 0 ; i< (this.arr) ; i++)
		{
			total += this.arr[i]
		}
		console.log("Total of array is : "+ total)
	}
	min()
	{
		if(this.num1 < this.num2 && this.num1 < this.num3)
		{
			console.log("The minimum value is : "+ this.num1)
		}
		else if(this.num2 < this.num3)
		{
			console.log("The minimum value is : "+ this.num2)
		}
		else
		{
			console.log("The minimum value is : "+ this.num3)
		}
	}
	max()
	{
		if(this.num1 > this.num2 && this.num1 > this.num3)
		{
			console.log("The maximum value is : "+ this.num1)
		}
		else if(this.num2 > this.num3)
		{
			console.log("The maximum value is : "+ this.num2)
		}
		else
		{
			console.log("The maximum value is : "+ this.num3)
		}
	}
}
exports.arithmetic = Arithmetic