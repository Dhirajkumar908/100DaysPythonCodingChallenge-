import os, time

listOfEmail = []


def prettyPrint():
  os.system("clear")
  print("listofEmail")
  print()
  for index in range(len(listOfEmail)):
    print(f"{index}: {listOfEmail[index]}")

  time.sleep(1)


def spammer():

  for index in range(len(listOfEmail)):
    if len(listOfEmail) < 10:
      print(
        f"Dear {listOfEmail[index]}It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.Love and hugs,Ian Spammington III"
      )
      print()

  time.sleep(5)


while True:
  print("SPAMMER Inc.")
  menu = input(
    "1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu == "2":
    email = input("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spammer()
  time.sleep(1)
  os.system("clear")

# import os, time

# listofEmail = []

# def prettyPrint():
#   os.system("clear")
#   print(listofEmail)
#   print()
#   for index in range(len(listofEmail)):
#     print(f"{index}: {listofEmail[index]}")
#   time.sleep(3)

# while True:
#   print("SPAMMER Indiageter")
#   menu = input("1. add email\n2. remove email\n3.show email\4.get spamming\n")
#   if menu == '1':
#     email = input("email > ")
#     listofEmail.append(email)
#   elif menu == '2':
#     email = input("email > ")
#     if email in listofEmail:
#       listofEmail.remove(email)
#   elif menu == '3':
#     prettyPrint()
#   time.sleep(3)
#   os.system('clear')



# import os, time

# listOfFood = []
# def prettyPrint():
#   os.system("clear")
#   print("listofFood")
#   print()
#   counter = 1
#   for order in listOfFood:
#     print(f"{counter}: {order}")
#     counter + 1
#   time.sleep(1)

# while True:
#   print("Yummy Food Restaurant")
#   menu = input(
#     "1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
#   if menu == "1":
#     order = input("order > ")
#     listOfFood.append(order)
#   elif menu == "2":
#     order = input("delete order> ")
#     if order in listOfFood:
#       listOfFood.remove(order)
#   elif menu == "3":
#     prettyPrint()
#   time.sleep(1)
#   os.system("clear")