array = [12,34,65,87,90]

#Append
array.append(0)
print(f"Appended Array:-{array}")

#Insert
array.insert(3,5)
print(f"Inserted Array:-{array}")
 
#Extend
array_1 = [1,43,65] 
array.extend(array_1)
print(f"Extended Array:-{array}")

#Remove
array.remove(12)
print(f"Removed Array:-{array}\n")

#Pop
popped = array.pop()
print(f"Popped Array:-{array}")
print(f"Popped value is{popped}\n")

#Index
index_value = array.index(0)
print(f"Index value is{popped}\n")

#Reverse
array.reverse()
print(f"Reversed Array:-{array}")

#Count
count_value = array.count(43)
print(f"Count of the Array:-{count_value}\n")