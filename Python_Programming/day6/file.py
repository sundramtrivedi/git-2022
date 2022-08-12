# File Handling
'''
operation :
Open -> open()
Read -> file_object.read()
Write -> file_object.write()
Seek : moving the cursor -> file_object.seek()
'''
# mode :
'''
r , w , a
r+ , w+ , a+
rb , wb , ab
rb+ , wb+ , ab+
'''

fd = open("data.txt","r+")
# print(fd.read())	# reading whole at a time
# fd.write("I am Writing from Function")
# fd.write(str(["Data,[874]"]))
# print(fd.readline())
# print(fd.readline())
for i in fd:
	print(f"Lines : {i}")

print("-"*80)

# seek
# 0 -> start point
# 1 -> current location
# 2 -> End location

fd.seek(0,0)	# (offset , seek_reference)
fd.writelines("I am again from Function")
print(fd.tell())	# cursor location
fd.write("XYZ")
fd.seek(0,2)
fd.seek(5,0)
fd.write("S")

