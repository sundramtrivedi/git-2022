emp_list = []
team_list = []
member_list = []

def join_date():
	day = int(input("Enter the join day of date :"))
	month = int(input("Enter the join month of date :"))
	year = int(input("Enter the join year of date :"))
	join_date = str(day)+"/"+str(month)+"/"+str(year)
	return join_date

def add_emp():
	emp_data = {}
	emp_data["emp_id"] = int(input("Enter the Employee ID :"))
	emp_data["emp_name"] = input("Enter the Employee Name :")
	emp_data["emp_age"] = int(input("Enter the Employee's Age :"))
	emp_data["emp_gender"] = input("Enter the Employee's Gender :")
	emp_data["emp_place"] = input("Enter the Employee's City :")
	emp_data["emp_salary"] = int(input("Enter the Employee's Salary :"))
	emp_data["emp_company"] = input("Enter the Employee's Previous Company :")
	emp_data["emp_join"] = join_date()
	emp_list.append(emp_data)

def delete_emp():
	emp_id = int(input("Enter the Employee ID to delete :"))
	for i in emp_list:
		if i["emp_id"] == emp_id:
			emp_list.remove(i)

def search_by_name():
	emp_name = input("Enter the Name to search : ")
	for i in emp_list:
		if i["emp_name"] == emp_name:
			print(i)

def search_by_empid():
	emp_id = int(input("Enter the Employee ID to search :"))
	for i in emp_list:
		if i["emp_id"] == emp_id:
			print(i)

def search_by_salary():
	emp_salary = int(input("Enter the Employee Salary to search :"))
	for i in emp_list:
		if i["emp_salary"] == emp_salary:
			print(i)

def change_by_name():
	emp_name = input("Enter the Employee Name to change : ")
	new_name = input("Enter the New Employee Name :")
	for i in emp_list:
		if i["emp_name"] == emp_name:
			i["emp_name"] = new_name

def change_by_gender():
	emp_name = input("Enter the Employee Name : ")
	new_gender = input("Enter the Employee gender :")
	for i in emp_list:
		if i["emp_name"] == emp_name:
			i["emp_gender"] = new_gender

def change_by_empid():
	emp_id = int(input("Enter the Employee ID to change : "))
	new_id = int(input("Enter the New Employee ID :"))
	for i in emp_list:
		if i["emp_id"] == emp_id:
			i["emp_id"] = emp_id

def change_by_salary():
	emp_name = input("Enter the Employee Name : ")
	new_salary = int(input("Enter the New Employee Salary :"))
	for i in emp_list:
		if i["emp_name"] == emp_name:
			i["emp_salary"] = new_salary

def display_emp():
	for i in emp_list:
		print("Employee List :",emp_list)

def create_team():
	team = {}
	empid_list = []
	team_name = input("Enter the Team Name :")
	flag = 0
	k = 2
	while k != 0:
		empid = int(input("Enter the empid :"))
		for i in emp_list:
			if i["emp_id"] == empid:
				flag = 1
			if flag ==1 :
				empid_list.append(empid)
			else:
				print("Employee ID is not valid")
			k = k - 1
			team[team_name] = empid_list
	create_date = input("Enter the Team Create Date (separate date with /) :")
	member_add = int(input("Enter how many members you want to add in Team :"))
	team_list.append(team)

def display_team():
	for i in team_list:
		print("Team List :",team_list)

def delete_team():
	team_name = input("Enter the Team Name to delete :")
	for i in team_list:
		if i["team_name"] == team_name:
			team_list.remove(i)

def rename_team():
	team_name = input("Enter the Team Name to change : ")
	new_name = input("Enter the New Team Name :")
	for i in team_list:
		if i["team_name"] == team_name:
			i["team_name"] = new_name

def display_member():
	for i in member_list:
		print("Member List :",member_list)

def add_member():
	member = {}
	emp_id_list = []
	flag = 0
	k = 2
	while k != 0:
		empid = int(input("Enter the empid :"))
		for i in emp_list:
			if i["emp_id"] == empid:
				flag = 1
			if flag ==1 :
				emp_id_list.append(empid)
			else:
				print("Employee ID is not valid")
			k = k - 1
			member[member_name] = emp_id_list
	member["member_name"] = input("Enter the Member Name :")
	member["member_emp_id"] = int(input("Enter the Member's Employee ID :"))
	member["member_edu"] = input("Enter the Member Education :")
	member["member_post"] = input("Enter the Employee Post :")
	member_list.append(member)

def delete_member():
	member_name = input("Enter the Member Name to delete :")
	for i in member_list:
		if i["member_name"] == member_name:
			member_list.remove(i)

menu4 = {
	"1" : rename_team ,
	"2" : display_member ,
	"3" : add_member ,
	"4" : delete_member
	}

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

menu3 = {
	"1" : create_team ,
	"2" : display_team ,
	"3" : manage_team ,
	"4" : delete_team
	}

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

menu2 = {
	"1" : change_by_name ,
	"2" : change_by_empid ,
	"3" : change_by_gender,
	"4" : change_by_salary
	}

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

menu1 = {
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

menu =	{
	"1" : add_emp ,
	"2" : delete_emp ,
	"3" : search_emp ,
	"4" : change_emp ,
	"5" : display_emp ,
	"6" : emp_manage_team
	}

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
