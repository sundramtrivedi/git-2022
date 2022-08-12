name = "siddhant"
for i in name[1:7]:
	print(i,end = "\t")
print("\n")
# variable.function()
x = name.upper()	# converts to upper case
print(x)
x = name.lower()	# converts to lower case
print(x)
print(name.isupper())		# return true if string is in upper case
print(name.islower())		# return true if string is in lower case
print(name.startswith("Si"))	# returns true if string start with given string
print(name.endswith("ant"))	# returns true if string end with given string
print(name.isdigit())		# returns true if string is digit "10"
print(name.isalpha())		# returns true if string is alphabet
