#(i)
print("Odd or Even")
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.\n")
else:
    print("This is an even number.\n")

#(ii)
print("Prime or Composite")
a= int(input("Enter a number:"))
b=2
c=True
if b < a:
    while (b < a):
        if a%b==0:
            c=False
            break
        b+=1
    if c:
        print(a,'is prime')
    else:
        print(a,'composite')
print("All Done")


