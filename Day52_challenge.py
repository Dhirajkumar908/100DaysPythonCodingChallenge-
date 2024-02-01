import os, time

order_list = []
'''
Day 52 Challenge
There's no place like Rome...Or Napoli, Milan, possibly even New York if you must.

Just not the dodgy 2am 'round bread with suspicious toppings' merchants that I definitely do not visit on my way home from a night out.

That's right, you're opening a pizza shop! Try not to get anchovy on your keyboard. Man that stuff never washes out.

Regardless, your program today must:

Prompt the user to input the quantity and size of pizzas.

Multiply the two inputs together to calculate the cost of the pizzas.

Store that in a 2D list with the user's name.

Use try.... except for two reasons:

Include auto-save and auto-load. Use it with the auto-load.
When casting the quantity of pizzas to an integer. Avoid the user crashing the program by typing 'three' instead of '3'. Or any other non-integer input. If they do, then prompt them to try again.
'''
try:
  f = open("pizza.txt", "r")
  order_list = eval(f.read())
  f.close()
except:
  print("Error: Unable to load")


def viewPizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Tatal"
  print(f"{h1:^10}{h2:^15}{h3:^10}{h4:^10}{h5:^10}")
  for row in order_list:
    print(f"{row[0]:^10}{row[1]:^15}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  time.sleep(5)


def addPizza():
  cost = 0
  name = input("Enter the name: ")
  topping = input("Enter the topping: ")
  size = input("Size of pizza(s/m/l): ").lower()
  while True:
    try:
      quantity = int(input("Enter the quantity of pizza: "))
      break
    except:
      print("Error: Quantity must be a number")
  if size == "s":
    cost = 50
  elif size == "m":
    cost = 100
  else:
    cost = 150
  total = cost * quantity
  order = [name, quantity, size, topping, total]
  order_list.append(order)
  print("Order added")


while True:
  time.sleep(1)
  os.system("clear")

  print("Rominos Pizza")
  print()
  menu = input("1:add Pizza, 2:view pizza: ")
  if menu == "1":
    addPizza()
  elif menu == "2":
    viewPizza()
  else:
    print("invaild input")

  f = open("pizza.txt", "w")
  f.write(str(order_list))
  f.close()

  time.sleep(2)
  os.system("clear")
