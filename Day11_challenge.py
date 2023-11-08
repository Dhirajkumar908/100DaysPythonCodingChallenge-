# Day 11 Challenge
# How many seconds are in a year?
"""
Use the power of breaking a program down into its parts. We could Google this, but why not make a program for this instead.
"""
year = int(input('Enter the number of year :'))
leep_year = input('Is this a leap year? (yes/no):')
"""
60 seconds = 1 minute

60 minutes = 1 hour

24 hours = 1 day

31 days = 1 month

12 months = 1 year

365 days = 1 year

366 day = 1 leap year 
"""
if leep_year == 'yes':
    result = year * 366 * 24 * 60 * 60
    print(result)

elif leep_year == 'no':
    result = year * 365 * 24 * 60 * 60
    print(result)

else:
    print('invalid input')
