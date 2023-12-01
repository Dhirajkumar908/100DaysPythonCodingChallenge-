"""
👉 Day 30 Challenge
Create a program that uses a loop that asks the user what they have thought of each of the 30 days of challenges so far.

For each day, prompt the user to answer a question and restate it in a full sentence that is center aligned underneath the heading.
"""

for i in range(1, 31):
  day = input(f"Day {i}:")
  print()
  mytext = f"you think Day {i} was "
  
  print(f"{mytext:^35}")
  
  print(f"{day:^35}")
