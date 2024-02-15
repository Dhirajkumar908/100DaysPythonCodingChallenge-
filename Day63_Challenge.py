import time, os
import Day63_challenge_test as test

while True:
  time.sleep(1)
  os.system("clear")
  menu = input("1: Add\n2: View\n3: Remove\n> ")
  if menu == "1":
    test.add()
  elif menu == "2":
    test.view()
  elif menu == "3":
    test.remove()
  else:
    print("Invalid input")

