terms = 10
t_1= 0  
t_2 = 1  
count = 0  
print ("The fibonacci sequence of the numbers is:")  
while count < terms:  
    print(t_1)  
    t = t_1 + t_2  
    t_1 = t_2  
    t_2 = t  
    count += 1