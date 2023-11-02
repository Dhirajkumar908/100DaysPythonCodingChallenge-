#Day 6 Challenge: Make your own login program.
# Create a program where someone logins with their username and password correctly and then gets a lovely individual greeting.
#Write a specific personalized greeting for 3 different people.


# Add a password
"""
 Now that we have input for both a username and password, we need to change our if and elif statements just a bit so both the username and password must match for Mark and Suzanne to login.
"""
print("SECURE LOGIN")

username = input("Username >")
password = input("Passwords>")

if username == "mark" and password == "123":
    print("Welcome Mark!")
elif username == "tony" and password == "tony123":
    print("Hey there tony!")
else:
    print("Go away!")


"""
Try and fix this code which is full of errors.

First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.
"""




