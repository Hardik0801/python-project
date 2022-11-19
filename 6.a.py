#(i)
a= ("FyBscDS" , "18", "Sies")
(Course, Age, College) = a
print("Course:",Course)
print("Age:",Age)
print("Colege:",College)

#(ii)
store = ''
for ele in a:
    store += ele
print(store)

#(iii)
b = (12,34,54,11,87,59)
store_smallest = b[0]
for ele in b:
    if ele < store_smallest:
        store_smallest = ele
    else:
        pass
print(store_smallest)

#(iv)
print(b)
user = int(input("Enter the number to be removed: "))
ab = list(b)
ab.remove(user)
print(tuple(ab))