import math
class Rectangle:
	def __init__(self,l,b):
		self.l = l
		self.b = b
	def area(self):
		return self.l * self.b
	def __str__(self):
		return "Rectangle :" + str(self.l) + " " + str(self.b)
	def __add__(self):
		return self.l + self.b
t = Rectangle(10,20)
print(t.area())
print(t)
x = Rectangle(10,20)
y = t + x
print(y)
