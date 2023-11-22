"""
👉 Day 22 Challenge
Copy and paste your code from Day 18.

We are going to make a change to this project:

Make the number generator completely random between 1 and 1,000,000. Now, the game will always have the user guess a random number each time (now the user can't cheat...)

Totally Random One-Million-to-One
What is your guess?: 500000
Too low
What is your guess?: 750000
Too high
What is your guess?: 600000
Too low
What is your guess?: 650000
Correct!
It took you 4 guesses to get the number correct.
Click 'run' to try again with a different number.
"""
import random

attempts = 0
randam_num = random.randrange(1, 1000000)

while True:
    num_guesses = int(input('Gess the number between 1 to 100:>'))
    print("")
    attempts += 1
    if num_guesses > randam_num:
        print('You gessed too high\n')

    elif num_guesses < randam_num:
        print('You gesses too low\n')

    elif num_guesses == randam_num:
        print("You gessed the rihgt number", randam_num)
        print("Attempt #" + str(attempts))
        print("")
        continue
    else:
        print('You gesses number is wrong')
        exit()





