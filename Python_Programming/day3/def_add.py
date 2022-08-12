def add(x,y):
	print("Addition is =" , x+y) 
def sub(x,y):
	return x - y
def sqr_add(x):
	s = x * x
	e = s + x
	return s,e
a = int(input("Enter the number x :"))
b = int(input("Enter the number y :"))
add(a,b)
c = sub(a,b)
print("Substrction is =",c)
d,f = sqr_add(a)
print("Square is =",d,"Addition is =",f)
