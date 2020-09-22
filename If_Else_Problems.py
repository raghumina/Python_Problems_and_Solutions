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


# Problem number 3
#
# A 4 digit number is entered through keyboard.
# Write a program to print a new number with digits reversed as of orignal one. E.g.-
# INPUT : 1234        OUTPUT : 4321
# INPUT : 5982        OUTPUT : 2895


rev = 0
num = int(input("Enter a number: "))
while num > 0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10
    print(rev)


# Problem 4

#  Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

num1 = int(input("Enter number 1 here: "))
num2 = int(input("Enter number 2 here: "))

product = num1 * num2
if product > 1000:
    print(num1 + num2)
else:
    print(product)

# Problem 5
#
#  Given a range of first 10 numbers,
#  Iterate from start number to the end number and print the sum of the current number and previous number
count = 0
print("Printing current and previous number sum in a given range(10)")
num = int(input())
for num in range(num):
    count = count + 1
    print(count, num+ count)
'''


# we can also do it with help of functions


def sumNum(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("Current Number", i, "Previous Number ", previousNum," Sum: ", sum)
        previousNum = i

print("Printing current and previous number sum in a given range(10)")
sumNum(10)