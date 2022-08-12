import math
class Circle:
	def __init__(self,rad):
		self.rad = rad
	def area(self):
		return math.pi * self.rad * self.rad
	def __str__(self):	#convert the string
		return "Circle :" + str(self.rad)
	def __add__(self,temp):
		return Circle(self.rad + temp.rad)
class Rectangle:
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return self.l * self.b
	def __str__(self):	#convert the string
		return "Rectangle :" + str(self.l) + " " + str(self.b)
p = Circle(10)
q = Rectangle(10,30)
# printing area
print(p.area())
print(q.area())
# printing object
print(p)
print(q)
# with_operator
#print(p + q)
#+= operator
x = Circle(20)
y = p + x
print(y)
print(p == x)

#__add__(self,arg) +
#__eq__(self,arg) ==
#__ne__(self,arg) !=
#__gt__(self,arg) >
#__lt__(self,arg) <
#__le__(self,arg) <=
#__ge__(self,arg) >=
#__len__(self) len()
#__mul__(self,arg) *
#__contains__(self,arg) in
#__str__(self) convert to string
#__doc__= value #for documentation
#__dir__(self) dir()
