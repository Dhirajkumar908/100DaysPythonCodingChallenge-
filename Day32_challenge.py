"""
 Day 32 Challenge
Create a list that stores greetings in different languages. Start with the language you speak.
Then, go on the internet to find other greetings in other languages. Here is a list of greetings to get you started.
Import random library. Generate a random number between 0 and maximum number of items in your list.
At random, when the user clicks run, print one of the greetings.
Use an f-string.

"""

import random

lang = [
  'hindi',
  'English',
  'urdu',
  'punjabi',
  'bengali',
  'gujarati',
  'marathi',
  'tamil',
]

num = random.randint(0, len(lang))
print(lang[num])
