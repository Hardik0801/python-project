user = int(input("Enter a number: "))
facto = user - 1
original = user
while facto >= 1:
    user = user*facto
    facto = facto - 1
print("Therefore",original,"! is",user)

