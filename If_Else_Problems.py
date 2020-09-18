# Problem 1
# Leap year
# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year
# but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
'''
def leap_year(year):
    if year % 400 == 0:
        return "LeaP yEAR"
    elif year % 100 == 0:
        return "NoT LEAP yEAR "
    elif year % 4 == 0:
        return "LeaP yEAR"
    else:
        print("Not Leap Year")


year = int(input("Please enter a year "))
print(leap_year(year))
'''
# Problem 2
# Ask user to enter age, sex ( M or F ), marital status ( Y or N )
# and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.

# if employee is a male and age is in between 20 to 40 then he may work in anywhere

# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

# And any other input of age should print "ERROR".

def designation(gender,age):
    if gender == "M" and age >= 40:
        return "Urban areas"
    elif gender == "M" and age in range(19,39):
        return "Work anywhere"
    elif gender == "F":
        return "Urban areas only"

gender = input("Enter your gender here 'M' or 'F' only: ")
age = int(input("Enter your age here: "))
print(designation(gender.upper(),age))