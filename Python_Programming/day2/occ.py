str ="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English."
print(str)
print("\n")
a = input("Enter the word :")
count = 0
words = str.split(" ")
for i in words:
	if(i == a):
		count = count + 1
print(count)
