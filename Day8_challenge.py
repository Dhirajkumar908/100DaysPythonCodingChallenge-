# Day 8 Challenge
"""
Today's focus is using all the skills you have learned so far:

input and output
concatenation
if statements
nested if statements
Build a custom affirmations generator to give the user a customized affirmation each day of the week.

Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.
"""
name = input("What is your name: ")
day = input("what is the day to day: ")
work = input("What is your working hours: ")
work_loacation = input("is your work from office or Home: ")

if work_loacation == "office":
    print("hello", name, "your are working from", work_loacation)
    if day == "monday":
        print("It's litel sad for you Today is", day, "and you have go office")
    elif day == "tuesday":
        print("Don't worry you have to", work, "but you have to go you office")
    elif day == "wednesday":
        print("hello", name, "you work hard at your", work, "and your",
              work_loacation, "good to work")
    elif day == "thursday":
        print("its nice")
    elif day == "friday":
        print("It's litel sad for to day is", day, "and you have go office")
    elif day == "saturday":
        print(day, "is holly day")
    elif day == "sunday":
        print("To day is", day, "mean funday")
    else:
        print("as your working profection you need to no the curent day")

elif work_loacation == "home":
    print("hello", name, "your are working from", work)
    if day == "monday":
        print("Congratulation you are very lucy for to day is", day,
              "and you are doing your work from", work_loacation)
    elif day == "tuesday":
        print("Yahh! to day is", day,
              "but don't worry you don't have go office")
    elif day == "wednesday":
        print(day, "is meddle day of working day")
    elif day == "thursday":
        print("Nice", work_loacation, "Second last day of this week")
    elif day == "friday":
        print("Great!", day,
              "is last day of this week finish your work and go to home")
    elif day == "saturday":
        print(day, "is holly day")
    elif day == "sunday":
        print("To day is", day, "mean funday")
    else:
        print("as your working profection you need to no the curent day")
