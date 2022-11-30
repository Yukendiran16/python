"""
Here basics of mathematical operations are performed
inputs will be passes to the respective methods
it will be performing respective operations using
these inputs and return result to user
"""


from constants import RESULT


# this method used to add two values from user
# and return the addition of two inputs
def add_values():
    """ This function returns the addition of two inputs"""
    print("Enter two values to addition")
    x = int(input("Enter first value : "))   # first input
    y = int(input("Enter second value : "))  # second input

    return RESULT, x + y


# this method used to subtract two values from user
# and return the subtraction of two inputs
def sub_values():
    """ This function returns the addition of two inputs"""
    print("Enter values to subtraction")
    x = int(input("Enter first value : "))   # first input
    y = int(input("Enter second value : "))  # second input

    return RESULT, x - y


# this method used to multiply two values from user
# and return the multiplication of two inputs
def mul_values():
    """ This function returns the addition of two inputs"""
    print("Enter values to multiplication")
    x = int(input("Enter first value : "))    # first input
    y = int(input("Enter second value : "))   # second input

    return RESULT, x * y


# this method used to  two values from user
# and return the division of two inputs
def div_values():
    """ This function returns the addition of two inputs"""
    print("Enter values to division")
    x = int(input("Enter dividend : "))   # dividend
    y = int(input("Enter divider : "))    # divider

    return RESULT, x / y
