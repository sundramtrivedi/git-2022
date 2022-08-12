data = """The internet of things, or IOT, is a system of interrelated computing devices, mechanical and digital machines, objects, animals or people that are provided with unique identifiers (UID) and the ability to transfer data over a network requiring human to human or human to computer interaction"""
print(data)
substr = input("Enter the substring :")
idx = data.find(substr)
if(idx != -1):
	print("Substring found")
	print(data[idx:idx+5].upper())
else:
	print("Substring not found")
