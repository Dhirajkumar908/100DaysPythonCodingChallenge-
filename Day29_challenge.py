"""
👉 Day 29 Challenge
Write a subroutine that writes text in color. All it will do is print out the text in that color and turn the color back to normal when it's finished.

Control end and sep so there are not random symbols or spaces.

Check out this github resource for the color codes.
"""
def sup(color, word):
  if color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "green":
    print("\033[32m", word, sep="", end="")
  elif color == "blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")


print("Supre subroutine")
print("With my", end="")
sup("red", " new program")
sup("reset", " I can just call red ('and') ")
sup("red", "it will print in red")
sup("blue", "or enen blue")
