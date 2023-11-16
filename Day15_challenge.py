"""
All About Loops
git
Day 15 Challenge
Write a program that loops. Inside the loop, ask the user what animal sound they want to hear.
"""

exit = "no"

while exit == "no":
    animal = input("what animal do you want?:")
    if animal == "Cow" or animal == "cow":
        print("A cow goes mooo....")
    elif animal == "Dog" or animal == "dog":
        print('A doc goes bhau bhau bhau')
    elif animal == "Cat" or animal == "cat":
        print("a cat say meow meow")
    else:
        print("You are not animal Lover")
    exit = input("You want to Exit?:")
