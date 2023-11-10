"""
Day 13 Challenge
Grade Generator
This project is going to take some time (and some hard thinking)
but will be brilliant once you have it working!

You are going to ask the user to type in the name of a test, maximum score they could receive,
and how many points they received. For example, your test could be called "Python Skills" 
and the maximum score is 50 points and the user receives 30 points out of 50 possible points.
"""

test = input("Type your test name?: ")
Max_points = int(input("Type the maximum points: "))
receive_points = float(input("Enter the received points: "))

percentage = round(receive_points / Max_points * 100, 2)
print("--------------------------")
if percentage >= 90 and percentage <= Max_points:
    print(f"Test Name: {test}, Received:- {percentage}% - Grade: A+ ")
elif percentage >= 80 and percentage < 90:
    print(f"Test Name: {test}, Received:- {percentage}% - Grade: A ")
elif percentage >= 70 and percentage < 80:
    print(f"Test Name: {test}, Received:- {percentage}% - Grade: B ")
elif percentage >= 60 and percentage < 70:
    print(f"Test Name: {test}, Received:- {percentage}% - Grade: C ")
elif percentage >= 50 and percentage < 60:
    print(f"Test Name: {test}, Received:- {percentage}% - Grade: D ")

elif percentage >= 0 and percentage < 50:
    print(f"Test Name: {test}, Received:- {percentage}% - Grade: u ")

else:
    print("Pease enter the valice points")
