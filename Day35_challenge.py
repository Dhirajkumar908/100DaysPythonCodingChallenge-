import os, time

todo = []


def viewTask():
  print()
  if len(todo) <= 0:
    print("No tasks in the list")
  else:
    for task in range(len(todo)):
      print(f"{task}: {todo[task]}")


def addTask():
  print()
  task = input("Enter the task: ")
  if task not in todo:
    todo.append(task)
  else:
    print("Task alredy exists in Your TODO list")


def removeTask():
  print()
  task = input("Enter the task to remove: ")
  status = input(f"Do you really want to remove {task}:Yes/No:")
  if status == "Yes":
    if task in todo:
      todo.remove(task)
      print(f"{task} removed from the list")
  else:
    print('You task is still in Your ToDo list')


def restToDo():
  todo.clear()



while True:
  print()
  menu = input(
    "1. Add Task\n2. view task\n3. Remove Task\n4. Reset Todo List\n")
  if menu == '1':
    addTask()
  elif menu == '2':
    viewTask()
  elif menu == '3':
    removeTask()
  elif menu == '4':
    restToDo()

