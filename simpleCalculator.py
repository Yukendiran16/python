"""
In this class I implement to python coding
standards like I used pep8Standards
I wish to create simple calculator using pep8
and I create some other examples
"""

from calculate import add_values
from calculate import sub_values
from calculate import mul_values
from calculate import div_values
from constants import WRONG_INPUT
# from calculate import *


# method for choose operation like,
# addition, subtraction, multiplication, division
def calculator(choice):
    """ this function handle the mathematical operations"""
    if 1 == choice:
        result = add_values()
        print(result[0], result[1])
    elif 2 == choice:
        print(sub_values())
    elif 3 == choice:
        print(mul_values())
    elif 4 == choice:
        print(div_values())
    else:
        print(WRONG_INPUT, choice)


def add_matrix():
    matrix_X = [1, 2, 3,
                4, 5, 6,
                7, 8, 9]
    matrix_Y = [
        9, 8, 7,
        6, 5, 4,
        3, 2, 1]

    result_matrix = []
    for i in range(0, len(matrix_X)):
        result_matrix.append(matrix_X[i] + matrix_Y[i])

    return result_matrix


# This is the controller of the calculator
print("\n\n Hi welcome I am calculator for your calculations")
print(" Can I help ?")
print(" 1. addition \n 2. subtraction \n 3. multiplication \n 4. division ")
print("Press one option for what do you now")
print(add_matrix())
option = int(input())  # input for choose what kind of operation will be performed
calculator(option)

# def add_values(value_list):
#     result = 0
#
#         result = result+i
#     return result
#
#
# def div_values(value_list):
#     result = 0
#
#         result = result-i
#     return result
#
#
# def mul_values(value_list):
#     result = 0
#
#         result = result*i
#     return result
#
#
# def sub_values(value_list):
#     result = 0
#
#         result = result/i
#     return result
#
#
# def calculate(choice):
#     value_list = []
#     match choice:
#         case 1:
#             print("Enter values to addition")
#             for i in range(100):
#                 add_value = int(input())
#                 if add_value != 0:
#                     value_list.append(add_value)
#                 else:
#                     break
#             result = add_values(value_list)
#             print(result)
#
#         case 2:
#             print("Enter values to subtraction")
#             for i in range(100):
#                 sub_value = int(input())
#                 if sub_value != 0:
#                     value_list.append(sub_value)
#                 else:
#                     break
#             result = sub_values(value_list)
#             print(result)
#
#         case 3:
#             print("Enter values to multiplication")
#             for i in range(100):
#                 mul_value = int(input())
#                 if mul_value != 0:
#                     value_list.append(mul_value)
#                 else:
#                     break
#             result = mul_values(value_list)
#             print(result)
#
#         case 4:
#             print("Enter values to division")
#             for i in range(100):
#                 div_value = int(input())
#                 if div_value != 0:
#                     value_list.append(div_value)
#                 else:
#                     break
#             result = div_values(value_list)
#             print(result)
