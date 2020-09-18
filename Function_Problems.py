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



# WRITE A FUNCTION TO CALCULATE AREA AND PERIMETER OF A RECTANGLE
#
# lETS START
#
'''
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