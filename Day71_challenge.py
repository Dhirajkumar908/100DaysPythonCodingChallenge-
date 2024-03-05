from replit import db
import random


def adduser():
  user = input("Enter your username: ")
  password = input("Enter your password: ")
  salt = random.randint(1000, 9999)
  newpassword = f"{password}{salt}"
  newpassword = hash(newpassword)
  db[user] = {"password": newpassword, "salt": salt}
  print("User added")


def login():
  user = input("Enter your username: ")
  password = input("Enter your password: ")
  salt = db[user]["salt"]
  newpassword = f"{password}{salt}"
  newpassword = hash(newpassword)
  if newpassword == db[user]["password"]:
    print("Login successful")
  else:
    print("Invalid password")


while True:
  menu = input("Add User 1\nLogin 2\n> ")
  if menu == "1":
    adduser()
  elif menu == "2":
    login()
  else:
    print("invalide input")
