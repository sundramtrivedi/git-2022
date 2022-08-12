# multiple parent is not allowed
# multiple and hybrid inheritance are not possible in python
class Student:
	def __init__(self,prn=0,name="",marks=0):
		self.prn = prn
		self.name = name
		self.marks = marks
	def display(self):
		print("PRN :",self.prn)
		print("Name :",self.name)
		print("Marks :",self.marks)
		self.x =0
	def set_marks(self,marks):
		self.marks = marks
class IOTStudent(Student):
	def __init__(self,prn=0,name="",marks=0,assigned_hardware=0):
		super().__init__(prn,name,marks)
		self.assigned_hardware = assigned_hardware
	def display(self):
		super().display()
		print("Assigned Hardware :",self.assigned_hardware)
class DACStudent(Student):
	def __init__(self,zoom_id=""):
		self.zoom_id = zoom_id
	def display(self):
		super().display()
		print("Zoom Id :",self.zoom_id)
s1 = IOTStudent()
s2 = DACStudent()

s1.prn = 1
s1.name = "Tushar"
s1.assigned_hardware = 10
s1.set_marks(120)

s2.prn = 1
s2.name = "Aman"
s2.marks = 90
s2.zoom_id = "123123123123123123123"

print("IOT Student")
s1.display()
print("-"*40)
print("DAC Student")
s2.display()

print("-"*40)
print("IOT Student")
s3 = IOTStudent(1,"Siddhant",10,10)
s3.display()

print("-"*40)
del s1.prn
s1.display()
