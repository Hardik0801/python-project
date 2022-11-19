import random
random_number = random.randint(1,101)
user = int(input("Guess a number between 1 to 100: "))
if random_number == user:
    print("You guessed it right")
else:
    print(f"You guessed it wrong.The number was {random_number}")