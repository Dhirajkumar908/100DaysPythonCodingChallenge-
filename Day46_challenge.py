beast = {}


def prettyPrint():
  print()
  for key, value in beast.items():
    print(key, end=":")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end=" | ")
    print()


while True:
  print()
  name = input("Input the beast name >  ")
  element = input("Input the beast element  >")
  move = input("Input the beast special move >")
  hp = input("Input the beast starting HP >")
  Mp = input(" Input the beast starting MP >")

  beast[name] = {"element": element, "move": move, "hp": hp, "Mp": Mp}
  prettyPrint()