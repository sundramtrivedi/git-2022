class Fruit:
	def __init__(self,fruit_id = 0,fruit_name = "",rate = 0,buy_price = 0):
		self.fruit_id = fruit_id
		self.fruit_name = fruit_name
		self.rate = rate
		self.buy_price = buy_price
	def display(self):
		print("Fruit_id :",self.fruit_id)
		print("Fruit_name :",self.fruit_name)
		print("Fruit rate :",self.rate)
		print("Fruit buy price :",self.buy_price)
fruit_lst = []
cart = []
def menu():
	print("-"*30)
	print("[1] Add Fruit")
	print("[2] Delete Fruit")
	print("[3] Display Fruit")
	print("[4] Buy Fruit")
	print("[5] Display cart")
	print("[6] Exit")
	print("-"*30)
def add_fruit():
	fruit_id = int(input("Enter fruit id :"))
	fruit_name = input("Enter the fruit name :")
	rate = int(input("Enter fruit rate :"))
	buy_price = int(input("Enter fruit buy price :"))
	f = Fruit(fruit_id,fruit_name,rate,buy_price)
	fruit_lst.append(f)
def display_fruits():
	for i in fruit_lst:
		i.display()
def delete_fruit():
	fruit_id = int(input("Enter the fruit id to delete :"))
	for i in fruit_lst:
		if fruit_id == i.fruit_id:
			fruit_lst.remove(i)
def buy_fruit():
	display_fruits()
	fruit_id = int(input(":::Add fruit to cart by fruit id :"))
	for i in fruit_lst:
		if(fruit_id == i.fruit_id):
			cart.append(i)
def display_cart():
	for i in cart:
		i.display()	
while True:
	menu()
	ch = int(input("Enter the choice :"))
	if ch == 1:
		print("-"*30)
		add_fruit()
	elif ch == 2:
		print("-"*30)
		delete_fruit()
	elif ch == 3:
		print("-"*30)
		display_fruits()
	elif ch == 4:
		print("-"*30)
		buy_fruit()
	elif ch == 5:
		print("-"*30)
		display_cart()
	elif ch == 6:
		break
	else:
		print("Wrong Choice")
