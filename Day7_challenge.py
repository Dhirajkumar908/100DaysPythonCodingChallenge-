# Day 7 Challenge
"""
Fake Fan Question Generator
Wanna find out if someone else is a true superfan of the same show, movie or interest as you? Create a program that asks what someone is interested in and includes nested if statements to ask annoying follow-up questions to see if someone is the real deal!

Make sure you include multiple if/elif statements and nested if statements too!

"""
print("""
Chose your favorite movies from "marvel","SpiderMan","Hulk","BatMan","IranMan"
  """)
movies = input("Which is you favorite movies:")
if movies == "marvel":
    print("Okey!, Then let's check this movies is realy favorite or Not")
    hero = input("Who is your favorite hero:")
    if hero == "IronMan":
        print("Okey!, Your favorite hero is IronMan")
    elif hero == "hulk":
        print("Okey!, Your favorite hero is Hulk")
    elif hero == "spiderman":
        print("Okey!, Your favorite hero is Spiderman")
    else:
        print("he is the very good actor of marvel serise")
elif movies == "spiderman":
    actor_name = input("What is the real name of spiderman movies")
    print(actor_name, "is very good actoer of spiderman movies")
else:
    print("ok")

# order = input("What would you like to order: pizza or hamburger? ")
# if order == "hamburger":
#     print("Thank you.")
#     cheese = input("Do you want cheese?")
#     if cheese == "yes":
#         print("You got it.")
#     else:
#         print("No cheese it is.")
# elif order == "pizza":
#     print("Pizza coming up.")
#     toppings = input("Do you want pepperoni on that?")
#     if toppings == "yes":
#         print("We will add pepperoni.")
# else:
#     print("Your pizza will not have pepperoni.")

# tvShow = input("What is your favourite tv show? ")
# if tvShow == "peppa pig":
#   print("Ugh, why?")
#   faveCharacter = input("Who is your favourite character? ")
#   if faveCharacter == "daddy pig":
#     print("Right answer")
#   else:
#     print("Nah, Daddy Pig's the greatest")
# elif tvShow == "paw patrol":
#   print("Aww, sad times")
# else:
#   print("Yeah, that's cool and all…")

# tvShow = input("What is your favorite tv show")
# if tvShow == "peppa pig":
#     print("Ugh, Why?")
#     favCharecter = input("Who is your favorite charecter")
#     if favCharecter == "daddy pig":
#         print("Right anwser")
#     else:
#         print("Nah, Daddy pig's the greatest")
# elif tvShow == "Big boos":
#     print("Aww!, Very bad choise")
# else:
#     print("Yeah, That's cool and all...!")

