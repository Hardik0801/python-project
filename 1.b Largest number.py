user_1 = float(input("Enter first number: "))
user_2 = float(input("Enter second number: "))
user_3 = float(input("Enter third number: "))
if user_1 > user_2 and user_1 > user_3:
    print(f"{(user_1)} is the largest number.")
elif user_2 > user_1 and user_2 > user_3:
    print(f"{(user_2)} is the largest number.")
elif user_3 > user_1 and user_3 > user_2:
    print(f"{(user_3)} is the largest number.")