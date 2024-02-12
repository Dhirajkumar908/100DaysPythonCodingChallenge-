'''
Today's challenge is an events countdown timer.

Your program should:

Austomatically work out today's date.
Prompt the user to input the name and date of their event (year, month and day).
Work out the number of days until the event and output it.
If the event is happening today, insert some party emojis.
If the event was in the past, sad face emojis and tell the user how many days ago it was.
'''
import datetime

today = datetime.date.today()

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
eventday = datetime.date(year, month, day)

daylef = eventday - today

if eventday > today:
  dayleft = eventday - today
  print(f"Coming soon:{daylef} left")
elif eventday < today:
  daypast = today - eventday
  print(f"Your event is {daypast} before! Hope you enjoyed it ")
else:
  print("🎉🎉Nan's 100th birthday is today! 🎉🎉")
