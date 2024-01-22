import time, os
todos = []


def add():
  time.sleep(2)
  os.system("clear")
  task = input("What is the task?: ")
  due = input("whene is it due by?: ")
  priority = input("What is the priority?: ")
  todo = [task, due, priority]

  todos.append(todo)
  print("Thanks, this task has been added.")



def view():
  time.sleep(2)
  os.system("clear")
  menu = input("MENU:\n View All:\t 1\n View Priority:\t 2 \n")
  if menu == "1":
    for todo in todos:
      for task in todo:
        print(task, end=" | ")
      print()
    print()
  elif menu == "2":
    priority = input("What priority : high, medium or low?")
    print()
    for todo in todos:
      if priority in todo:
        for task in todo:
          print(task, end=" | ")
        print()
      print()
  else:
    print("Invalid Input")


def edut():
  find=input("Name of todo to edit >")
  found=False
  for todo in todos:
    if find in todo:
      found=True
  if not found:
    print("Couldn't find that")
    return

  for todo in todos:
    if find in todo:
      todos.remove(todo)

  task = input("Name > ")  
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  todo = [task, date, priority]
  todos.append(todo)
  print("Added")



def remove():
  time.sleep(2)
  os.system("clear")
  task = input("Which task do you want to remove?:")
  for todo in todos:
    if task in todo:
      todos.remove(todo)
      print("Thanks, this task has been removed.")


while True:
  print("🌟Life Organizer🌟")
  menu = input("Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > ").strip().capitalize()
  print()
  if menu == "Add":
    add()
  elif menu == "View":
    view()
  elif menu == "Remove":
    remove()
  elif menu=="Edit":
    edut()

  time.sleep(2)
  os.system("clear")
