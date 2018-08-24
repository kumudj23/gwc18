from random import *

#Generates a random integer.

aRandomNumber = randint(1, 20)

# For Testing: print(aRandomNumber)

for i in range(3):

    guess = input("Guess a number between 1 and 20 (inclusive): ")

    if not guess.isnumeric(): # checks if a string is only digits 0 to 9

        print("That's not a positive whole number, try again!")
        continue

    elif guess.isnumeric():

        guess = int(guess) # converts a string to an integer

        if guess > 20:

            print("That is not in range, try again!")
            continue

    if guess > aRandomNumber:

        print("The number is lower")
        continue

    elif guess == aRandomNumber:

        print("You got it!")
        break

    elif guess < aRandomNumber:

        print("The number is higher")
        continue

print("Game over!")
