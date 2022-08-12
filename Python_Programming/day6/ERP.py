# creating class ERP
class ERP:		
	def __init__(self,emp_id = 0,emp_name = "",emp_age = 0,emp_gender="",emp_place="",
	emp_salary=0,emp_company="",emp_join="",team_name="",empid_list=[],member_name="",
	member_emp_id=0,member_edu="",member_post=""):
		self.emp_id = emp_id
		self.emp_name = emp_name
		self.emp_age = emp_age
		self.emp_gender = emp_gender
		self.emp_place = emp_place
		self.emp_salary = emp_salary
		self.emp_company = emp_company
		self.emp_join = emp_join
		
		self.team_name = team_name
		self.empid_list = empid_list.copy()
		
		self.member_name = member_name
		self.member_emp_id = member_emp_id
		self.member_edu = member_edu
		self.member_post = member_post
	
	# display function of employee
	def display(self):
		print("emp_id :",self.emp_id)
		print("emp_name :",self.emp_name)
		print("emp_age :",self.emp_age)
		print("emp_gender :",self.emp_gender)
		print("emp_place :",self.emp_place)
		print("emp_salary :",self.emp_salary)
		print("emp_company :",self.emp_company)
		print("emp_join :",self.emp_join)
	
	# display function of team
	def display_emp_team(self):
		print("team_name :",self.team_name)
		#for i in self.empid_list:
		print("empid_list : ", self.empid_list)
	
	# display function of member
	def display_member(self):
		print("member_name :",self.member_name)
		print("member_emp_id :",self.member_emp_id)
		print("member_edu :",self.member_edu)
		print("member_post :",self.member_post)

# creating list
emp_list = []
team_list = []
member_list = []

#emp_list["empid":12, "emp_name":"payal"]
#team_list["mu":[mem, mem, mem]]

# fuction for join date
def join_date():
	day = int(input("Enter the join day of date :"))
	month = int(input("Enter the join month of date :"))
	year = int(input("Enter the join year of date :"))
	join_date = str(day)+"/"+str(month)+"/"+str(year)
	return join_date

# function for add employee
def add_emp():
	emp_id = int(input("Enter the Employee ID :"))
	emp_name = input("Enter the Employee Name :")
	emp_age = int(input("Enter the Employee's Age :"))
	emp_gender = input("Enter the Employee's Gender :")
	emp_place = input("Enter the Employee's City :")
	emp_salary = int(input("Enter the Employee's Salary :"))
	emp_company = input("Enter the Employee's Previous Company :")
	emp_join = join_date()
	e = ERP(emp_id,emp_name,emp_age,emp_gender,emp_place,emp_salary,emp_company,emp_join)
	emp_list.append(e)

# function for delete the employee
def delete_emp():
	emp_id = int(input("Enter the Employee ID to delete :"))
	for i in emp_list:
		if emp_id == i.emp_id:
			emp_list.remove(i)

# function for search the employee by name
def search_by_name():
	emp_name = input("Enter the Employee Name to search :")
	for i in emp_list:
		if emp_name == i.emp_name:
			i.display()

# function for search the employee by emp id
def search_by_empid():
	emp_id = int(input("Enter the Employee ID to search :"))
	for i in emp_list:
		if emp_id == i.emp_id:
			i.display()

# function for search the employee by salary
def search_by_salary():
	emp_salary = int(input("Enter the Employee Salary to search :"))
	for i in emp_list:
		if emp_salary == i.emp_salary:
			i.display()

# function for change the name of employee
def change_by_name():
	emp_name = input("Enter the Employee Name to change : ")
	new_name = input("Enter the New Employee Name :")
	for i in emp_list:
		if i.emp_name == emp_name:
			i.emp_name = new_name

# function for change the gender of employee
def change_by_gender():
	emp_name = input("Enter the Employee Name : ")
	new_gender = input("Enter the Employee gender :")
	for i in emp_list:
		if i.emp_name == emp_name:
			i.emp_gender = new_gender

# function for change the emp id of employee
def change_by_empid():
	emp_id = int(input("Enter the Employee ID to change : "))
	new_id = int(input("Enter the New Employee ID :"))
	for i in emp_list:
		if i.emp_id == emp_id:
			i.emp_id = new_id

# function for change the salary of employee
def change_by_salary():
	emp_name = input("Enter the Employee Name : ")
	new_salary = int(input("Enter the New Employee Salary :"))
	for i in emp_list:
		if i.emp_name == emp_name:
			i.emp_salary = new_salary

# function for display employee details
def display_emp():
	for i in emp_list:
		i.display()

# function for creating the team 
def create_team():
	team_name = input("Enter the Team Name :")
	member_add = int(input("How many team members you want to add :"))
	empid_list = []
	flag = 0
	while member_add != 0:
		empid = int(input("Enter the empid :"))
		for i in emp_list:
			if i.emp_id == empid:
				empid_list.append(i)
				member_add -= 1
				flag = 1
		if flag == 0:
			print("This emp_id is not valid")
	t = ERP(0,"",0,"","",0,"","",team_name,list(empid_list))
	team_list.append(t)

# function for display team
def display_team():
	for i in team_list:
		i.display_emp_team()

# function for delete team
def delete_team():
	team_name = input("Enter the Team Name to delete :")
	for i in team_list:
		if team_name == i.team_name:
			team_list.remove(i)

# function for rename team
def rename_team():
	team_name = input("Enter the Team Name to change : ")
	new_name = input("Enter the New Team Name :")
	for i in team_list:
		if i.team_name == team_name:
			i.team_name = new_name

# function for display the team member
def display_member():
	for i in member_list:
		i.display_member()

# function for add members in team
def add_member():
	member_name = input("Enter the Member Name :")
	member_emp_id = int(input("Enter the Member's Employee ID :"))
	member_edu = input("Enter the Member Education :")
	member_post = input("Enter the Employee Post :")
	m = ERP(0,"",0,"","",0,"","","","",0,member_name,member_emp_id,member_edu,member_post)
	member_list.append(m)

# function for delete members in team
def delete_member():
	pass
	
# menu driven for members
menu4 = {
	"1" : rename_team ,
	"2" : display_member ,
	"3" : add_member ,
	"4" : delete_member
	}

# function for team management menu driven
def manage_team():
	print("[1] Rename Team")
	print("[2] Display Members")
	print("[3] Add Member")
	print("[4] Delete Member")
	d = input("Enter the choice :")
	if int(d) >= 5 :
		print("Wrong Choice")
	else:
		menu4[d]()

# menu driven for team
menu3 = {
	"1" : create_team ,
	"2" : display_team ,
	"3" : manage_team ,
	"4" : delete_team
	}

# function for team management
def emp_manage_team():
	print("[1] Create Team")
	print("[2] Display Team")
	print("[3] Manage Team(rename,display mem,add mem,delete mem)")
	print("[4] Delete Team")
	c = input("Enter the choice :")
	if int(c) >= 5 :
		print("Wrong Choice")
	else:
		menu3[c]()

# menu driven for change emp details
menu2 = {
	"1" : change_by_name ,
	"2" : change_by_empid ,
	"3" : change_by_gender,
	"4" : change_by_salary
	}

# function for change emp details
def change_emp():
	print("[1] Change Employee name")
	print("[2] Change Employee emp id")
	print("[3] Change Employee gender")
	print("[4] Change Employee salary")
	b = input("Enter the choice :")
	if int(b) >= 5 :
		print("Wrong Choice")
	else:
		menu2[b]()

# menu driven for search emp 
menu1 = {
	"1" : search_by_name ,
	"2" : search_by_empid ,
	"3" : search_by_salary 
	}

# function for change emp
def search_emp():
	print("[1] Search Employee name")
	print("[2] Search Employee emp id")
	print("[3] Search Employee salary")
	a = input("Enter the choice :")
	if int(a) >= 4 :
		print("Wrong Choice")
	else:
		menu1[a]()

# menu driven for employee 
menu =	{
	"1" : add_emp ,
	"2" : delete_emp ,
	"3" : search_emp ,
	"4" : change_emp ,
	"5" : display_emp ,
	"6" : emp_manage_team
	}

# choice
while True:
	print("-"*30)
	print("[1] Add Employee")
	print("[2] Delete Employee")
	print("[3] Search Employee (name,id,salary)")
	print("[4] Change Employee data (name,id,gender,salary)")
	print("[5] Display Employee")
	print("[6] Manage all Teams (create,display,manage,delete)")
	print("[7] Exit")
	print("-"*30)
	ch = input("Enter the choice :")
	if int(ch) == 7:
		break
	else:	
		menu[ch]()
