import random
print("Number Guessing Game")
num = random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")

while chances < 5:
    guess=int(input("Enter your Guess :"))

    if guess == num :
        print("you won")
        break

    elif guess<num:
        print("too low, guess higher",guess)

    else:
        print("too high, guess low", guess)

    chances += 1

if not chances < 5:
    print("you lose! the numbert is", num)
