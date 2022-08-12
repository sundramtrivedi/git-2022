# default argument
num = {}
def process_num(start,end):
	for i in range(start=1,end=1):
		num[i] = i * i
# start = int(input("Enter some number :"))
n = int(input("Enter some number :"))
# precess_num(start,end)
process_num(start,end = n)	# keyword based argument
print(num)
process_num(end = n,start = 5)
print(num)
