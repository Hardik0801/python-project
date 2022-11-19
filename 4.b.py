lst = eval(input("Enter a valid of list of numbers: "))

#1 Largest value
store_largest = 0
for ele in lst:
    if ele > store_largest:
        store_largest = ele
print(store_largest)

#2 Remove duplicates
no_duplicates = set(lst)
convert = list(no_duplicates)
print("List after removing duplicate elements: ", convert)

#3 Copy of the list
copied_list = lst.copy()
print(copied_list)

# 4Get the desired values
value_from_lst = int(input("Enter any value to be printed: "))
placed_at = lst.index(value_from_lst)
get_value = lst[placed_at]
print(get_value)