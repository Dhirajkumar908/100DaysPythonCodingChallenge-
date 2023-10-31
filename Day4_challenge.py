#Day 4 Challenge
#Ask your users to list a bunch of information about them: things they like, things they hate, names of family and friends... it's up to you how many and what kinds of things you pick. Keep it wacky!
# Now construct your story - it can be about anything you want, but must use the variables you've created in step 1.
#Make sure to only work one paragraph at a time. Otherwise things could get a bit messy.

print(
    "Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!"
)
name = input("What is your name?")
enemy_name = input("What is your worst enemy’s name?")
superpower = input("What is your superpower?")
add = input("Where do you live?")
favorite_food = input("What is your favorite food?")
print("Hello", name, "! Your ability to ", superpower,
      "will make sure you never have to look at ", enemy_name,
      "again. Go eat ", favorite_food, " as you walk down the streets of", add,
      " and use", superpower, "for good and not evil!'")
