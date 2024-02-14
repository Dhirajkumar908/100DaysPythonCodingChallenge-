"""Look out, Big Brother! Today is a project day and you are going to build your own private diary to keep your innermost thoughts secret from the world.
Your diary should:
Set an access password.
Prompt the user to type in a password.
If they don't get the password right, exit the program.
If they get it right, they enter the main menu, which gives 'Add' or 'View' diary entries.
Choosing 'add' should:
Prompt the user to type the entry and store it in the database with the timestamp as the key.
Choosing 'view' should:
Show the user the previous (most recent) entry.
They can then choose to see the next previous entry working backwards until they get to the end. Or exit back to the menu.
🥳 Extra points for adding a feature which allows the user to view an entry from an exact date."""

from replit import db
import datetime, time, os

def cls():
  time.sleep(2)
  os.system("clear")

def add():
  cls()
  timestamp = datetime.datetime.now()
  db[timestamp] = input("Input your diary entry > ")

def view():
  cls()
  keys = db.keys()
  for key in keys:
    print(f"{key}:{db[key]}")
    opt = input("Next or exit?")
    if (opt.lower()[0] == "e"):
      break

def user():
  cls()
  username = input("Username: ")
  password = input("Password: ")
  db[username] = password

while True:
  cls()
  menu = input("1:login\n2:signup\n")
  if menu == "2":
    user()
  elif menu == "1":
    user_id = input("Enter user id:")
    password = input("Enter password:")
    if user_id in db.keys():
      if db[user_id] == password:
        print("Login successful")
        while True:
          cls()
          menu = input("1:View dairy>\n2:add in dairy> ")
          if menu == "1":
            add()
          elif menu == "2":
            view()
          else:
            print("Invalid input")

      else:
        print("Incorrect password")
