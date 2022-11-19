#1 Occurences 
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
# the_list = eval(input("Enter a list: "))
# count = int(input("Enter the number to be counted: "))
# print(countX(the_list,count))

#2 Concatenate lists
list_1 = eval(input("Enter a list: "))
list_2 = eval(input("Enter the list to be concatenate: "))
list_1.extend(list_2)
print(list_1,"\n")

#3 Common element
r1_list = [12,43,12,98]
r2_list = [1,23,65,88,100]
def common_data(x,y):
   common=0
   for value in x:
      if value in y:
         common=1
   if(not common):
      return ("The lists have no common elements")
   else:
        return ("The lists have common elements")

print(common_data(r1_list,r2_list))