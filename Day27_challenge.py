import os, time, random

print("Welcome")


def character():
  character_name = input("Enter the character name: ")
  character_type = input("Enter the character Type: ")
  print("Character name:", character_name)
  print("Character type:", character_type)


def character_health():
  health1 = random.randint(1, 7)
  health2 = random.randint(1, 13)
  health = ((health1 * health2) / 2) + 12
  return health


def character_strength():
  strength1 = random.randint(1, 7)
  strength2 = random.randint(1, 12)
  strength = ((strength1 * strength2) / 2) + 12
  return strength


while True:
  menu = int(input("Enter 1 to create a character, 2 to quit: "))
  if menu == 1:
    character()
    print("Character Health:", character_health())
    print("Character strength:", character_strength())
    time.sleep(2)
    os.system('clear')

  elif menu == 2:
    print("Thank you for playing")
    break
  else:
    print("Invalid choice")
