import random
n = random.randint(0,9)

chances = 0
print("Guess a number between 0-9? ")

while chances < 5:
    guess = int(input("Enter your Guess"))
    if guess == n:
        
        print("Congratulations YOU WON!!!")
        break

    elif guess < n:
        print("Guess a higher number ")

    else:
        print("Your guess was too high")
        
    chances += 1

if not chances < 5:
    print("You loose The number is", n )
