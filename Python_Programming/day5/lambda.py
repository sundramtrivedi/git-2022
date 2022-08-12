# def add(a,b)
#	return a + b
# only one expression
# any number of argument
print("-"*80)
print("e.g : 1")
add = lambda a,b : a + b
c = add(10,20)
print("add(a,b) :",add(10,20))

print("-"*80)
print("e.g : 2")
sub = lambda a,b : a - b
d = sub(10,20)
print("sub(a,b) :",sub(10,20))

print("-"*80)
print("e.g : 3")
add = lambda c,d : c + d
print("add(c,d) :",add(c,d))

print("-"*80)
print("e.g : 4")
lst = ["10","20","30,20",["Sid","Anubhav"],("Tushar","Vivek"),{"name" : "Siddhant"}]
print("List :",lst)

print("-"*80)
print("e.g : 5")
get_value = lambda i : lst[i][0]
print("get_value(1) :",get_value(1))	# 2
get_value = lambda i,j : lst[i][j]
print("get_value(2,4) :",get_value(2,4))	# 0

print("-"*80)
print("e.g : 6")
lst = ["Payal","Vishwajeet","Trivediji","Ganesh","Triedi"]
print(lst)

print("-"*80)
print("e.g : 7")
# lst.sort(reverse = 0)
lst.sort(key = lambda i : i[0])
print(lst)

print("-"*80)
print("e.g : 8")
lst.sort(key = lambda i : i[2:])
print(lst)

print("-"*80)
print("e.g : 9")
lst.sort(key = lambda i : i[2:].upper() )
print(lst)

print("-"*80)
print("e.g : 10")
lst = [{"prn" : "1" , "name" : "Snehal" },{ "prn" : "2" , "name" : "Priyanka" },{ "prn" : "3" , "name" : "Shital" },{ "prn" : "4" , "name" : "Sweety"}]
print(lst)
"""
print("-"*80)
print("e.g : 11")
lst.sort(key = lambda i : i["prn"])
print(lst)

print("-"*80)
print("e.g : 12")
lst.sort(key = lambda i : i["name"])
print(lst)
"""
print("-"*80)
print("e.g : 13")
sorted(lst,key = lambda i : i["prn"])	# have to comment upper side (e.g : 11 and e.g : 12)
print(lst)

print("-"*80)
print("e.g : 14")
lst = [10,20,30,40,50,60,70]
# for i in lst:
# 	l.append(i*i)
l = map(lambda i : i*i , lst)	
"""
or we can use
def sqr(i):
	return i*i
l = map(sqr , lst)

"""
print(list(l))

print("-"*80)
print("e.g : 15")
lst = ["Tushar","Siddhant","Siddhesh","Kiran","Aditya","Varma"]
print(lst)

print("-"*80)
print("e.g : 16")
l = list(map(lambda i : i[-2:] , lst))
print(l)

print("-"*80)
print("e.g : 17")
lst = [{"prn" : 1 , "name" : "Snehal" },{ "prn" : 2 , "name" : "Priyanka" },{ "prn" : 3 , "name" : "Shital" },{ "prn" : 4 , "name" : "Sweety"}]
print(lst)

print("-"*80)
print("e.g : 18")
l = list(map(lambda i : tuple([i["prn"]+1 ,i["name"][::-1][0].lower()]), lst))
print(l)

print("-"*80)
print("e.g : 19")
l = list(map(lambda i : {"prn" : str(i["prn"])[0] , "nick_name" : i["name"][:4]},lst))
print(l)

print("-"*80)
print("e.g : 20")
l = list(map(lambda i : str(i["prn"]) == 10 ,lst))
print(l)

print("-"*80)
print("e.g : 21")
lst = [101,202,303,404,505,606,707]
print(lst)

print("-"*80)
print("e.g : 22")
l = list(filter(lambda a : a % 2 == 0 , lst))
print(l)

print("-"*80)
print("e.g : 23")
lst = ["Tushar" , "Siddhesh" , "Kiran" , "Aditya" , "Siddhant"]
print(lst)

print("-"*80)
print("e.g : 24")
l = list(filter(lambda i : i[-2] == "s" , lst))
print(l)

print("-"*80)
print("e.g : 25")
lst = [{"prn" : 1 , "name" : "Snehal" },{ "prn" : 2 , "name" : "Priyanka" },{ "prn" : 3 , "name" : "Shital" },{ "prn" : 4 , "name" : "Sweety"}]
print(lst)

print("-"*80)
print("e.g : 26")
l = list(filter(lambda i : lambda a : str(a["prn"]).isdigit() , lst))
print(l)

print("-"*80)
