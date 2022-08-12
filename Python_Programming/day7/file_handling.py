# File handling
fd = open("data.txt","r+")
print(fd.read())
fd.seek(0,2)	# offset should be end and current location because python can not identify the how many chars in regular file
fd.seek(0,0)
fd.close()

with open("data.txt","r+") as fd:
	# fd can be accessed only inside this block
	print(fd.read())	# use decode function to convert bytes data to string
	fd.write("some data")	# use .encode function to convert to bytes formate
	# when control goes out of this block file automatically close
# print(fd.write("Data"))
# 
print(fd)
