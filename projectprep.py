#!/usr/bin/env python3

# GAME WORK:
# 5 guesses at guessing a number between 1 and 100
# if you get it wrong, it will tell you if the answer is higher or lower than your guess
# after 5 guesses and you are still wrong, it prints the correct answer
# if you get it right, it finishes early

import random

max_guesses = 5
guess_count = 0
number = random.randint(1, 100)

while True:
    
    if guess_count == max_guesses:
        print(f"You've run out of guesses! The correct answer was {number}.")
        break
    try:
        guess = input("Choose a number between 1 and 100!\n>")

        # force the guess into being an integer
        guess = int(guess)

    except:
        # aka CATCH
        # this is what occurs if an error happens
        print("That's not a number")
        continue

    guess_count += 1

    if guess == number:
        print("CORRECT!")

    elif guess < number:
        print("Too low!")

    else:
        print("Too high!")




