import random
secret = random.randint(1, 100)
guess = int(input("Your guess: "))
while guess != secret:
    if guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Your guess: "))
print("Bravo! It was",secret)
