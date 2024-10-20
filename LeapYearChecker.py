## Assignment 1 - Part Two
## Leap Year Checker

## Your Code goes here. 
year = int(input("Please enter a year: "))
if year < 1582:
    print("Year must be greater than 1582 - the first year of the Gregorian calendar.")
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
