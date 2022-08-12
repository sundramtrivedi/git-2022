lst = "aabbaa"
l = lambda i : i[::-1] == lst
print(l(lst))	

lst = "aabb"
l = lambda i : i[::-1] == lst
print(l(lst))
