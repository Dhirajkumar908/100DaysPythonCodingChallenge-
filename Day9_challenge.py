#  Day 9 Challenge
# Generation Generator

# What generation are you a part of?

# Use this list to guide you.

"""
Generation Name	Starting Birth Year	Ending Birth Year
Traditionalists	1925	1946
Baby Boomers	1947	1964
Generation X	1965	1981
Millenials	    1982	1995
Generation Z	1996	2015
"""

print("What generation are you a part of?")

DOB = int(input("Enter you date of birth:"))

if DOB > 1925 and DOB <= 1946:
    print("You are Traditionalists")
elif DOB > 1047 and DOB <= 1964:
    print("you are a Boby Boomers")

elif DOB > 1965 and DOB <= 1981:
    print("You are generation X")
elif DOB > 1982 and DOB <= 1995:
    print("You are a millenials")
elif DOB > 1996 and DOB <= 2015:
    print("You are a generation Z")
else:
    print("You are a new born baby")
