'''Checking for a Leap Year , 2024 → Yes
Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400'''

year = int(input("Please enter the year : "))
if (year % 400==0) and (year % 100==0):
    print(f"{year} is a leap year")
elif (year%4==0) and (year%100!=0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")