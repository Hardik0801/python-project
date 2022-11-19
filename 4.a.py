#Smallcase and Uppercase in list
output = []
user = str(input("Enter any string: "))
store_upper = ''
store_lower = ''
for ele in user:
    if ele == ele.upper():
        store_upper += ele
    elif ele == ele.lower():
        store_lower += ele
    else:
        pass
output.append(store_lower)
output.append(store_upper)
print(output)
