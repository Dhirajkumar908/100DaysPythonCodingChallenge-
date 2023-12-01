"""
Day 31 Challenge
Create a classic user interface using string manipulation.

Create these two user interfaces (below) using everything you know about extensions to print statements and f-strings.

The second one is a bit more tricky as it involves alignment.

There are no input statements. This is all about using print and variables in interesting ways. However, you may want to create a subroutine to make the color changing easier (like you did on Day 29).
"""
def color(color):
  if color == "red":
    return ("\033[31m")
  elif color == "white":
    return ("\33[0m")
  elif color == "blue":
    return ("\033[34m")
  elif color == "yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")


title = f"{color('red')} ={color('white')}={color('blue')}={color('yellow')} Music app {color('blue')}={color('white')}={color('red')}="

print(f"{title:^35}")
print(f"\t{color('white')} Radio Gaga")
print(f"\t{color('yellow')} Queen")

prev = "prev"
next = "next"
pause = "pause"
print(f"{color('white')} {prev:^35}")
print(f"{color('green')}{next:^35}")
print(f"{color('purple')}{pause:^35}")

print()
print()

text = "WELCOME TO"
print(f"{color('white')} {text:^35}")
text = "__ARMBOOK__"
print(f"{color('blue')}{text:^35}")
text = "Definitely not a rip off"
print(f"{color('yellow')}{text:>35}")
text = "a certain other social"
print(f"{color('yellow')}{text:>35}")
text = "networking site"
print(f"{color('yellow')}{text:>35}")
text = "Honest."
print(f"{color('red')}{text:^35}")
text = "Username: "
username = input(f"{color('white')}{text:^35}")
text = "Password: "
username = input(f"{color('white')}{text:^35}")
