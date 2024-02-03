'''
👉 Day 53 Challenge
Your video game inventory system should:

Have a menu that allows the user to:
Add
View
Remove
Adding an item saves it to a file using captalize mode. Duplicates are allowed.
Removing an item deletes it from the file.
View is trickier. It should output the name of the item and tell you how many of those items you have.
Use auto-save and auto-load with try... except.
'''

import time, os

items_list = []

try:
  f = open("inventory.txt", "r")
  items_list = eval(f.read())
  f.close()
except:
  print("Error: No existing inventory list, using a blank list")


def add():
  time.sleep(1)
  os.system("clear")
  item = input("Input the item to add: >  ").capitalize()
  items_list.append(item)
  print("Added")


def view():
  time.sleep(2)
  os.system("clear")
  item = input("Input the item to view: > ").capitalize()
  if item in items_list:
    count = items_list.count(item)
    print(f"You have {count} {item}")
  else:
    print("You don't have that item")


def remove():
  time.sleep(1)
  os.system("clear")
  item = input("inter the item to remove: > ").capitalize()
  if item in items_list:
    items_list.remove(item)
    print("Removed")


while True:
  time.sleep(1)
  os.system("clear")
  menu = input("1: Add\n2: View\n3: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    remove()
  else:
    print("Invalid input")

  f = open("inventory.txt", "w")
  f.write(str(items_list))
  f.close()