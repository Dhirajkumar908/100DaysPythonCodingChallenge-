# Day 50! Boy, you are smashing this 100 days! 🎊 To celebrate, here's a project for you.

# Your idea storage system should:

# Prompt the user to add an idea, or load a random one.
# Choosing 'Add an idea' results in:
# A prompt for the user to input their idea.
# Add the idea to a text file called 'my.ideas'.
# Add the idea in append mode, with every new idea on a brand new line.
# Choosing 'Load random' results in:
# Load the list of ideas.
# Choose one at random.
# Display it on screen for a few seconds.
# Return to the menu.

import time, os, random


def add_idea():
  idea = input("What is your idea?: ")
  idea_file = open("ideaFile.txt", "a+")
  idea_file.write(f"{idea}\n")
  idea_file.close()
  print("Your idea has been added sucessfully!")


def show_idea():
  idea_file = open("ideaFile.txt", "r")
  ideas = idea_file.read().split("\n")
  idea_file.close()
  idea = random.choice(ideas)
  print()
  print(idea)
  print()


while True:
  print("Idea Stotrage Center")
  print()
  menu = input(
    "Enter 1 to add an idea, 2 to show a random idea, or 3 to exit: ")
  if menu == "1":
    add_idea()
  elif menu == "2":
    show_idea()

  elif menu == "3":
    break
  else:
    print("Invalid input")
  time.sleep(2)
  os.system("clear")
