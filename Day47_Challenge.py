
import os, time, random

trumps = {}
trumps["David"] = {
  "Intelligence": 178,
  "Speed": 4,
  "Guile": 80,
  "Baldness Level": 99
}
trumps["Mr Spock"] = {
  "Intelligence": 200,
  "Speed": 50,
  "Guile": 50,
  "Baldness": 0
}
trumps["Moica"] = {
  "Intelligence": 150,
  "Speed": 50,
  "Guile": 50,
  "Baldness": 50
}
trumps["Professor X"] = {
  "Intelligence": 250,
  "Speed": 1,
  "Guile": 200,
  "Baldness": 101
}
while True:
  print()
  print("Top Trumps")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Pick Your character\n>")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)
  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")
  answer = input(">")

  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp} : {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")
    time.sleep(1)
    os.sytem("clear")
