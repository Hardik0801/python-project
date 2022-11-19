number = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}

user = str(input("Enter a number: "))
store = ' '
for ele in user:
    store = store + ' ' + number[ele]
print(store.strip())
