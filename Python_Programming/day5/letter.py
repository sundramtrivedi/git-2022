string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
lst = string.split()
print("lst :",lst)
new_l = []
l = list(map(lambda i : i[0] , lst ))
print("-"*80)
print("l :",l)
for j in l:
	if j not in new_l:
		new_l.append(j)
print("new_l :",new_l)
