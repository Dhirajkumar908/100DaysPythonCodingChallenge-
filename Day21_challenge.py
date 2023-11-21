"""
Day 21 Challenge
Test your family and friends on their multiplication knowledge (or just be really mean to people you know and ask them to work out their multiplication tables for 5,474,000,000....)

Prompt the user by asking for a multiplication table for the number of their choice.
Generate the multiplication table for 1 to 10 times that number and ask each math fact as a question (psst...that's a hint).
If the user gets the math correct, award them a point. If they get it wrong, do not give them any points.
At the end of the 10 rounds, show the user their score out of 10 for how many math facts they got correct.
Why not give users an emoji if they get all 10 math facts correct?
Math Game!
"""

fact_family = int(input("Name of the multiplies:"))

count = 0
for i in range(1, 11):
    correct_ans = fact_family * i
    print(fact_family, "x", i)
    ans = int(input("enter the correct ans:>"))
    if correct_ans == ans:
        count += 1
        print("correct")
    else:
        print("wrong")
        print("correct ans:", correct_ans)
if count == 10:
    print("WOw! A perfect scoure")
else:
    print("You got", count, "out of 10")
