import os, time

while True:
  f = open("high_score.txt", "a+")
  initail = input("Input your intials >  ")
  f.write(f"{initail}\n")
  score = input("Input your score >")
  f.write(f"{score}\n")
  print("Added to high score table.")
  again = input("Add another? y/n > ")
  f.close()
  if again == "y":
    continue
  else:
    break
  time.sleep(2)
  os.system("clear")
