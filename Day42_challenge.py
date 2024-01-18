beast = {
  "name": None,
  "type": None,
  "special_move": None,
  "HP": None,
  "MP": None
}

for name, value in beast.items():
  beast[name] = input(f"{name}:\t").strip().capitalize()


def mokebeast():
  print(
    f"Your beast is called {beast['name']}. It is an {beast['type']} beast with a special move of {beast['special_move']} "
  )


# for name, value in beast.items():
if beast['type'] == "Earth":
  print("\033[32m", end="")
  mokebeast()

elif beast['type'] == "Air":
  print("\033[37m", end="")
  mokebeast()

elif beast['type'] == "Fire":
  print("\033[31m", end="")
  mokebeast()

elif beast['type'] == "Water":
  print("\033[34m", end="")
  mokebeast()
else:
  print("\033[33m", end="")
  mokebeast()
