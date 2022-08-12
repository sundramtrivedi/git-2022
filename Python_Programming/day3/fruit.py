frt = []
def frt_input():
	frt = {}
	frt["frtID"] = int(input("Fruit ID :"))
	frt["name"] = input("Fruit Name :")
	frt["rate"] = int(input("Rate of Fruit :"))
	frt["imp_from"] = input("Fruit imported from :")
	frt["imp_date"] = {}
	frt["imp_date"]["day"] = input("Enter the day of date :")
	frt["imp_date"]["month"] = input("Enter the month of date :")
	frt["imp_date"]["year"] = input("Enter the year of date :")
	frt["price"] = int(input("Fruit buy price :"))
	return frt
def frt_add():
	temp = {}
	temp["frtID"] = int(input("Fruit ID :"))
	temp["name"] = input("Fruit Name :")
	temp["rate"] = int(input("Rate of Fruit :"))
	temp["imp_from"] = input("Fruit imported from :")
	temp["imp_date"] = {}
	temp["imp_date"]["day"] = input("Enter the day of date :")
	temp["imp_date"]["month"] = input("Enter the month of date :")
	temp["imp_date"]["year"] = input("Enter the year of date :")
	temp["price"] = int(input("Fruit buy price :"))
	frt.append(temp)
def frt_delete():
	name = input("Enter the Fruit Name to delete : ")
	for i in frt:
		if i["name"] == name:
			frt.remove(i)
def frt_display():
	print(frt)
def frt_search_name():
	name = input("Enter the Fruit Name : ")
	for i in frt:
		if i["name"] == name:
			print(i)
def frt_search_rate():
	rate = int(input("Enter the Fruit Rate to search : "))
	for i in frt:
		if i["rate"] == rate:
			print(i)
def frt_change_name():
	name = input("Enter the Fruit Name to change : ")
	new_name = input("Enter the New Fruit Name :")
	for i in frt:
		if i["name"] == name:
			i["name"] = new_name
def frt_change_rate():
	rate = int(input("Enter the Fruit Rate to change : "))
	new_rate = int(input("Enter the New Fruit Rate :"))
	for i in frt:
		if i["rate"] == rate:
			i["rate"] = new_rate
def menu():
	print("[1] Add Fruit")
	print("[2] Delete Fruit by name")
	print("[3] Display Fruit")
	print("[4] Search Fruit by name")
	print("[5] Search Fruit by rate")
	print("[6] Change Fruit name")
	print("[7] Change Fruit rate")
	print("[8] Exit")
while True:
	menu()
	ch = int(input("Enter the choice :"))
	if ch == 1:
		frt_add()
	elif ch == 2:
		frt_delete()
	elif ch == 3:
		frt_display()
	elif ch == 4:
		frt_search_name()
	elif ch == 5:
		frt_search_rate()
	elif ch == 6:
		frt_change_name()
	elif ch == 7:
		frt_change_rate()
	elif ch == 8:
		break;
	else:
		print("Wrong choice")
