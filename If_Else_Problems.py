# Problem 1
# Leap year
# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year
# but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

def leap_year(year):
    if year % 400 == 0 and year % 4 == 0 and year % 100 and year % 100 != 0:





        return "LEAP_YEAER"
    else:
        print("Not Leap Year")


year = int(input("Please enter a year "))
print(leap_year(year))

