# Python Problems and Solutions
# Python function Problms and solutions


# Problem 1
# 1. Write a Python function to find the Max of three numbers
'''
def max(a, b, c):
   # PYTHON FUNCTION TO FIND THE MAX OF THREE NUMBERS
   # In this we are supposing that three numbers are different not equal of each other  # put a docstring here
    if a > b and a > c:
        print("A is Max")
    elif b > a and b > c:
        print("b is Max")
    else:
        print("C is max")


#a = int(input("Enter number a: "))
#b = int(input("Enter number b: "))
#c = int(input("Enter number c: "))


# max_of_number = max(a,b,c)
# print("The maximum number between three numbers is",max_of_number)  # correct
# print("The max number between three numbers is: ", max(a, b, c))

# another way of solving this problem is

def max_of_two_number(a, b):
     Function to find max number among two- # put a docstring here
    if a > b:
        return a
    return b


def max_of_three_numbers(a, b, c):
    To find max among three       # put a docstring here
    the numbers should not be equal
    return max_of_two_number(a, max_of_two_number(b, c))


#a = int(input("Enter number a: "))
#b = int(input("Enter number c: "))
#c = int(input("Enter number c: "))

#print(max_of_three_numbers(a, b, c))


# Problem 2
#
# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_of_list(list):
    total = 0
    for x in list:
        total += x
    return total
print(sum_of_list((8, 2, 3, 0, 7)))


# Problem 3
#
# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

def multiplication_of_list(list1):
    total = 0
    for x in list1:
        total *= x
    return total

print(multiplication_of_list((8, 2, 3, -1, 7)))


# Problem 4
# WRITE A FUNCTION TO CALCULATE AREA AND PERIMETER OF A RECTANGLE
#
# lETS START
#

def rectangle_area(length,width):
    area = length * width
    return area
def rectangel_parameter(length,width):
    parameter = 2 * length + 2 * width
    return parameter

length = int(input("Enter length of the rectangle: "))
width = int(input("Enter width of the rectangle: "))
print("The area of rectangle is:",rectangle_area(length,width))
print("The parameter of rectange: ",rectangel_parameter(length,width))

# Problem 5
#
# Write a function to calculate area and circumference of a circle.
# lets start
import math
def circle_area(radius):
    area = 2 * math.pi * radius
    return area
def circle_circumfrence(radius):
    circumfrence = 2 * math.pi * radius ** 2
    return circumfrence
radius = float(input("Enter radius here: "))
print("The area of circle is: ",round(circle_area(radius)))     # i used round() function to round off the answer
print("The circumgrence is : ",round(circle_circumfrence(radius)))
'''


#
# Problem 6
#
# Write a function to calculate power of a number raised to other. E.g.- ab.

def power_number(num, power):
    power_of_number = num ** power
    return power_of_number

num = int(input("Enter the number here: "))
power = int(input("Enter the power of number here: "))
print("THE",num,"the POWER",power,"is",power_number(num, power))
