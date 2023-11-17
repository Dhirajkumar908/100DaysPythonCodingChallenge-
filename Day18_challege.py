"""Day 18 Challenge
We are going to build a "Guess the Number" guessing game.

You are going to use a while loop and some of the concepts from the past few days."""

import random

attempts = 0
randam_num = random.randrange(1, 100)

while True:
    num_guesses = int(input('Gess the number between 1 to 100:'))
    print("")
    attempts += 1
    if num_guesses > randam_num:
        print('You gessed too high\n')

    elif num_guesses < randam_num:
        print('You gesses too low\n')

    elif num_guesses == randam_num:
        print("You gessed the rihgt number", randam_num)
        print("Attempt #" + str(attempts))
        continue
    else:
        print('You gesses number is wrong')
        exit()
