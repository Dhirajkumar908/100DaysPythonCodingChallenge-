#Day 5 Challenge
#"Which character are you?" Generator
#Ask your users a series of questions that identify if they're one of the characters in the world you have created.

#Add multiple if statements to check the result of each question.
#Make sure to have a final print if they haven't selected any of the characters so far.

#marvel movie Charecter creator
character = input("Do you like hanging around?:")
if character == 'no':
    print("Then you're not Spider-man")
else:
    print("You are spider man")

character = input("Do you have a gravelly voice?")
if character == 'no':
    print("Aww, then you're not Korg")
else:
    print("You are Korg")

character = input("Do you often feel Marvelous")
if character == 'yes':
    print("Aha! You're Captain Marvel! Hi!")
else:
    print("You're Captain america")
