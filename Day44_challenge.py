
#bingo game
import random, time, os

bingo = []


def ran():
  number = random.randint(1, 90)
  return number


def prettyPrint():
  for row in bingo:
    for item in row:
      print(item, end="\t|\t")
    print()


def createCard():
  global bingo
  numbers = [] 
  for i in range(8):
    num = ran()
    while num in numbers:
      num = ran()
    numbers.append(ran())
  numbers.sort()
  
  bingo = [[numbers[0], numbers[1],numbers[2]], [numbers[3], "BINGO", numbers[4]],[numbers[5], numbers[6], numbers[7]]]
createCard()
while True:
  prettyPrint()
  num =int(input("Next Number:"))
  for row in range(3):
    for item in range(3):
      if bingo[row][item]==num:
        bingo[row][item]="X"
  exes=0

  for row in bingo:
    for item in row:
        if item=="X":
          exes+=1
  if exes==8:
    print("You have Won")
    break
  time.sleep(1)
  os.system("clear")


# listOfShame = []

# while True:
#   menu = input("Add or Remove?")

#   if (menu.strip().lower()[0] == "a"):

#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")

#     row = [name, age, pref]

#     listOfShame.append(row)

#   else:
#     name = input("What is the name of the record to delete?")
#     for row in listOfShame:
#       if name in row:
#         listOfShame.remove(row)

#   print(listOfShame)

# infolist = []

# def info():
#   for row in infolist:
#     print(row)

# while True:
#   add_remove = input("You want add/remove?: ").strip().lower()
#   if add_remove == 'add':
#     name = input("Name: ").strip().capitalize()
#     age = input("age: ").strip().capitalize()
#     row = [name, age]
#     infolist.append(row)
#   elif add_remove == 'remove':
#     name = input("name of the record to delete: ").strip().capitalize()
#     for row in infolist:
#       if name in row:
#         infolist.remove(row)

#   info()
