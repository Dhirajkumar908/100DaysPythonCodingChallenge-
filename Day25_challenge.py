"""
👉 Day 25 Challenge
Let's extend Day 24's project and create a health stats generator for a character in a video game.

Create a subroutine that rolls a dice of any size and returns that number.
Then, create a second subroutine that rolls one six-sided dice and one eight-sided dice.
Multiply the number from the six-sided dice and eight-sided dice together and return that subroutine as a character's health stats for a video game.
Print out the character's health stats.
Add a loop to give the user the option to generate health stats for another character.

"""
import random

sides = int(input("How many sides :"))
playgame = "yes"


def rollDice(sides):
  number = random.randint(1, sides)
  return number


def charhealth():
  six_side_dice_Number = random.randint(1, 7)
  eight_side_dice_Number = random.randint(1, 7)
  character_health = six_side_dice_Number * eight_side_dice_Number
  return character_health


while playgame == "yes":
  print(rollDice(sides))
  name = input("Name your warrior:")
  print("There health is:", charhealth())
  playgame = input("roll again?:")
