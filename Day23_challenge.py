"""
Day 23 Challenge
Create a subroutine with both a username and password.
Create a loop to prompt the user again and again until they put in the correct login information.
Replit Login System
What is your username?: david
What is your password? whatAmazingHairYouHave
Whoops! I don't recognize that username or password. Try again!
What is your username? david
What is your password? baldies4life
Welcome to Replit!
"""
def login():
    while True:
        username = input("Enter the Username:")
        password = input("Enter the password:")
        print("")
        if username == "admin" and password == "admin123":
            print("You have loged in successfully")
            break
        else:
            print("Invalid username or password try again\n")
            continue
    return username, password


login()