"""
Someone is wrong on the Internet!
Today, we're going to fix the major malfunction with social media - other people and their stupid opinions- and create a Twitter for one!

I know you like to hear the sound of your own voice!

Your program should.

Display a menu - Add or View tweets.

'Add' should:

Get the tweet input.
Store it to the database with the current timestamp as the key value.
'View' should:

Show the tweets in reverse chronological order.
Show 10 tweets at a time.
Prompt the user to show another 10 tweets (yes or no).
A 'no' choice goes back to the menu.
"""
from replit import db
import os, time, datetime

def add():
  tweets = input("Enter your tweet: ")
  date = datetime.date.today()
  key = f"mes{date}"
  db[key] = tweets

def view():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    if counter % 10 == 0:
      carryOn = input("next 10?:")
      if carryOn.lower() == "no":
        break

while True:
  menu = input("1. Add\2. view")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  else:
    print("Invalid input")
  time.sleep(2)
  os.system("clear")
