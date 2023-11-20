"""
👉 Day 20 Challenge
List Generator
Ask the user to list a starting number, ending number, and increment to use. Display an answer based on the users' answers (use the
"""

start_num = int(input("Enter the Starting number:>"))
ending_num = int(input("Enter the Ending number:>"))
IncreseBy = int(input("Enter the IncreseBy number:>"))

for i in range(start_num, ending_num, IncreseBy):
    print(i)