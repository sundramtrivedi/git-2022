class ERP:
	def __init__(self,emp_id,emp_name,emp_age,emp_gender,emp_place,emp_salary,emp_company,emp_join):
		self.emp_id = emp_id
		self.emp_name = emp_name
		self.emp_age = emp_age
		self.emp_gender = emp_gender
		self.emp_place = emp_place
		self.emp_salary = emp_salary
		self.emp_company = emp_company
		self.emp_join = emp_join
	def display(self):
		print("emp_id :",self.emp_id)
		print("emp_name :",self.emp_name)
		print("emp_age :",self.emp_age)
		print("emp_gender :",self.emp_gender)
		print("emp_place :",self.emp_place)
		print("emp_salary :",self.emp_salary)
		print("emp_company :",self.emp_company)
		print("emp_join :",self.emp_join)
emp_list = []
def add_emp():
	emp_id = int(input("Enter the Employee ID :"))
	emp_name = input("Enter the Employee Name :")
	emp_age = int(input("Enter the Employee's Age :"))
	emp_gender = input("Enter the Employee's Gender :")
	emp_place = input("Enter the Employee's City :")
	emp_salary = int(input("Enter the Employee's Salary :"))
	emp_company = input("Enter the Employee's Previous Company :")
	emp_join = input("Enter the Employee's Joining Date (use / to separate):")
	e = ERP(emp_id,emp_name,emp_age,emp_gender,emp_place,emp_salary,emp_company,emp_join)
	emp_list.append(e)
def delete_emp():
	emp_id = int(input("Enter the Employee ID to delete :"))
	for i in emp_list:
		if emp_id == i.emp_id:
			emp_list.remove(i)
def search_by_name():
	emp_name = input("Enter the Employee Name to search :")
	for i in emp_list:
		if emp_name == i.emp_name:
			i.display()
def search_by_empid():
	emp_id = int(input("Enter the Employee ID to search :"))
	for i in emp_list:
		if emp_id == i.emp_id:
			i.display()
def search_by_salary():
	emp_salary = int(input("Enter the Employee Salary to search :"))
	for i in emp_list:
		if emp_salary =< i.emp_salary:
			i.display()
def change_by_name():
	emp_name = input("Enter the Employee Name to change : ")
	new_name = input("Enter the New Employee Name :")
	for i in emp_list:
		if i.emp_name == emp_name:
			i.emp_name = new_name
def change_by_empid():
	emp_id = int(input("Enter the Employee ID to change : "))
	new_id = int(input("Enter the New Employee ID :"))
	for i in emp_list:
		if i.emp_id == emp_id:
			i.emp_id = new_id
def change_by_salary():
	emp_name = input("Enter the Employee Name : ")
	new_salary = int(input("Enter the New Employee Salary :"))
	for i in emp_list:
		if i.emp_name == emp_name:
			i.emp_salary = new_salary
def display_emp():
	for i in emp_list:
		i.display()
menu1 ={
	"1" : search_by_name ,
	"2" : search_by_empid ,
	"3" : search_by_salary 
}
def search_emp():
	print("[1] Search Employee name")
	print("[2] Search Employee emp id")
	print("[3] Search Employee salary")
	a = input("Enter the choice :")
	if int(a) >= 4 :
		print("Wrong Choice")
	else:
		menu1[a]()
menu2 = {
	"1" : change_by_name ,
	"2" : change_by_empid ,
	"3" : change_by_salary
}
def change_emp():
	print("[1] Change Employee name")
	print("[2] Change Employee emp id")
	print("[3] Change Employee salary")
	b = input("Enter the choice :")
	if int(b) >= 4 :
		print("Wrong Choice")
	else:
		menu2[b]()

menu =	{
	"1" : add_emp ,
	"2" : delete_emp ,
	"3" : search_emp ,
	"4" : change_emp ,
	"5" : display_emp
}
while True:
	print("-"*30)
	print("[1] Add Employee")
	print("[2] Delete Employee")
	print("[3] Search Employee (name,id,salary)")
	print("[4] Change Employee data (name,id,salary)")
	print("[5] Display Employee")
	print("[6] Exit")
	print("-"*30)
	ch = input("Enter the choice :")
	if int(ch) == 6:
		break
	else:	
		menu[ch]()
