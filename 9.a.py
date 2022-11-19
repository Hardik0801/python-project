r_list = ['a', 0, 2]
for data in r_list:
    try:
        print("The entry is", data,)
        a = 1/int(data)
        break
    except ValueError:
        print("Its a value error.\n")
    except ZeroDivisionError:
        print("Its a Zero division error.\n")
print("The reciprocal of", data, "is", a)