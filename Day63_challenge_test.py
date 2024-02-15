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


f = open("inventory.txt", "w")
f.write(str(items_list))
f.close()
