user = int(input ("How many terms the user wants to print? "))
u_1 = 0
u_2 = 1
count = 0
if user <= 0:
    print ("Please enter a positive integer, the given number is not valid")
elif user == 1:
    print ("The Fibonacci sequence of the numbers up to", user, ": ")
    print(u_1)
else:
    print ("The fibonacci sequence of the numbers is:")
    while count < user:
        print(u_1)
        u = u_1 + u_2
        u_1 = u_2
        u_2 = u
        count += 1