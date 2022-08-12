num = "5,2,3,9,5,6,11,8,9"
print(num)
sum = 0
a = num.split(",")
print(a)
for i in a:
	sum = sum + int(i)
print("Addition of numbers :")
print(sum)

sum_even = 0
for i in a:
	if(int(i) % 2 == 0):
		sum_even = sum_even + int(i)
print("Addition of even numbers :")
print(sum_even)
