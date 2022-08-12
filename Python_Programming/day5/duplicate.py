st = input("Enter the string :")
lst = st.split()
print("lst :",lst)
newstr=[]
for i in lst:
	if (lst.count(i) < 2):
		newstr.append(i)
print("new string :",newstr)
