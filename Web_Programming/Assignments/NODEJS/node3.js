class Circle
{
    constructor(radius)
    {
        this.radius = radius
    }
    calcAreaCircle()
    {
        console.log("Area Of Circle : " + (Math.PI * this.radius * this.radius))
    }
    calcCircumference()
    {
        console.log("Circumference Of Circel :" + (2 * (Math.PI * this.radius)))
    }
    calcDiameter()
    {
        console.log("Diameter Of Circle : " + (this.radius * 2))
    }
}
class Rectangle
{
    constructor(l,b)
    {
        this.l = l
        this.b = b
    }
    calcAreaRectangle()
    {
        console.log("Area Of Rectangle : " + (this.l * this.b))
    }
    calcPerimeterRectangle()
    {
        console.log("Perimeter Of Rectangle : " + (2 * (this.l + this.b)))
    }
}
class Triangle
{
    constructor(side1,side2,side3)
    {
        this.side1 = side1
        this.side2 = side2
        this.side3 = side3
    }
    isEquilaterial()
    {
        if(this.side1 == this.side2 && this.side2 == this.side3)
        {
            console.log("The given triangle is Equilaterial")
        }
        else
        {
            console.log("The given trianle is not Equilaterial")
        }
    }
    calcPerimeter()
    {
        console.log("Perimeter Of Triangle : " + (this.side1 + this.side2 + this.side3))
    }
}
exports.circle = Circle
exports.rectangle = Rectangle
exports.triangle = Triangle