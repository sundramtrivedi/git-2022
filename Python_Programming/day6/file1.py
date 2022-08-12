string = """A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"""
print(string)
'''
fd = open("data1.txt","r+")
fd.write(string)
'''
'''
lst = string.split()
new_lst = []
word = []
fd = open("data2.txt","r+")
def check(i):
	if lst.index(i) % 2 == 0 :
		return new_lst.append(i)
	else:
		return word.append(i)
l = list(map(lambda i : check(i) , lst ))
print("-"*80)
print("new_lst :",new_lst)
print("-"*80)
print("word :",word)
fd.write(" ".join(new_lst))
fd.write("\n")
fd.write(" ".join(word))
'''
lst = ["1.txt","2.txt","3.txt","4.txt","5.txt","6.txt","7.txt","8.txt","9.txt","10.txt"]
for i in lst:
	file = open(i,"w+")
	file.write(string)

