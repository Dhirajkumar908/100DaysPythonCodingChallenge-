"""
Day 24 Challenge
Let's build an infinity dice!

Create subroutines that will roll a dice with any number of sides (essentially as big of a number as you like). Write one subroutine with one parameter that allows us to call a function (such as rollDice).
"""
import random

sides=int(input("How many sides :"))
playgame="yes"

def rollDice(sides):
  print("You rolled", random.randint(1,sides))
  
while playgame=="yes":
  rollDice(sides)
  playgame=input("roll again?:")
    