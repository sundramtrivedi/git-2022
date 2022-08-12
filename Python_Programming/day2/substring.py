# multiline string
data = """This is siddhant""" # single line string
"""Strings"""
'''Strings'''
data = "This is Payal. IOT : Internet Of Things"
print(data)
# find function returns -1 if string is not found
substr = input("Enter the substring to find in above line :")
if(data.find(substr) != -1):
	print("Substring found")
else:
	print("Substring not found")
# print all the data after substring
idx = data.find(substr)
if(idx != -1):
	print(data[idx:])
else:
	print("Substring not found")
