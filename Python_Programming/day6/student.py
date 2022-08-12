# 1 : Siddhant : 100
# 2 : Name : 32
fd = open("student_data.txt","r+")
def user_input():
	prn = int(input("Enter the PRN :"))
	name = input("Enter the Name :")
	marks = int(input("Enter the Marks :"))
	fd.write(f"{prn} : {name} : {marks} \n")
	
def read_data():
	fd.seek(0,0)
	for line in fd:
		lst = line.split(":")
		print(f"Name : {lst[1]} \t Prn : {lst[0]} \t Marks : {lst[2]}")
read_data()
user_input()
user_input()
