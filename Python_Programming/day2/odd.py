# loops
i=0
add=0
while (i<100):
	if ((i%2) != 0):
		add = add + i
	i = i+1
print("Addition of Odd number (while loop)")
print(i)
print(add)

sum=0
for i in range(1,101,2):
	if ((i%2) != 0):
		sum = sum + i
print("Addition of Odd number (for loop)")
print(i)
print(sum)
