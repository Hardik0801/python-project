user_1 = str(input("What's your martual status: ")).capitalize()
if user_1 == "Married":
    print("Your eligible for Insurance.")
elif user_1 == "Unmarried":
    user_2 = str(input("What's your sex: ")).capitalize
    user_3 = int(input("Enter your age: "))
    if user_1 == "Unmarried" and user_2 == "Male" and user_3 > 30:
        print("Your eligible for Insurance.")
    elif user_1 == "Unmarried" and user_2 == "Female" and user_3 > 25:
        print("Your eligible for Insurance.")
    else:
        print("Your not eligible for insurance")