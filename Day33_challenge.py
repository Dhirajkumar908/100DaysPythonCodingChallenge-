Todo = []


def add(item):
  Todo.append(item)
  print(item, "has been added to the list")
  print(" ")


def remove(item):
  Todo.remove(item)
  print(item, "has been removed from the list")
  print(" ")


def Displaylist():
  print(Todo)
  print(" ")


while True:
  print("1. Add to list")
  print("2. Remove from list")
  print("3. Display list")
  print("4. Quit")
  print(" ")
  choice = input("Enter your choice: ")
  print(" ")
  if choice == "1":
    item = input("Enter the Item to add: ")
    add(item)
    print(" ")
  elif choice == "2":
    item = input("Enter the Item to remove: ")
    remove(item)
    print(" ")
  elif choice == "3":
    Displaylist()
    print(" ")
  elif choice == "4":
    break

  else:
    print("Invalid choice")
    print(" ")
