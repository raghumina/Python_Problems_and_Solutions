# Python Problems and Solutions
# Python function Problms and solutions


# Problem 1
# 1. Write a Python function to find the Max of three numbers

def max(a, b, c):
    '''PYTHON FUNCTION TO FIND THE MAX OF THREE NUMBERS
    In this we are supposing that three numbers are different not equal of each other '''
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
    ''' Function to find max number among two-'''
    if a > b:
        return a
    return b


def max_of_three_numbers(a, b, c):
    '''To find max among three
    the numbers should not be equal'''
    return max_of_two_number(a, max_of_two_number(b, c))


a = int(input("Enter number a: "))
b = int(input("Enter number c: "))
c = int(input("Enter number c: "))

print(max_of_three_numbers(a, b, c))
