num = "5,2,3,9,5,6,11,8,9"
lst = num.split(",")
print(lst)

print("-"*80)
print("Question : 1")
print("\n")
l = 0
for i in lst:
	l = l + (lambda i : int(i))(i)
print(l)

print("-"*80)
print("Question : 2")
print("\n")
l = 0
for j in lst:
	if(int(j) % 2 == 0):
		l = l + (lambda i : int(i))(j)
print(l)
