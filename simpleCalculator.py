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
# from calculate import *


# method for choose operation like,
# addition, subtraction, multiplication, division
def calculator(choice):
    match choice:
        case 1:
            print("Enter two values to addition")
            value1 = int(input("Enter first value : "))
            value2 = int(input("Enter second value : "))
            print("your result is :" + str(add_values(value1, value2)))

        case 2:
            print("Enter values to subtraction")
            value1 = int(input("Enter first value : "))
            value2 = int(input("Enter second value : "))
            print("your result is :" + str(sub_values(value1, value2)))

        case 3:
            print("Enter values to multiplication")
            value1 = int(input("Enter first value : "))
            value2 = int(input("Enter second value : "))
            print("your result is :" + str(mul_values(value1, value2)))

        case 4:
            print("Enter values to division")
            value1 = int(input("Enter first value : "))
            value2 = int(input("Enter second value : "))
            print("your result is :" + str(div_values(value1, value2)))


# This is the controller of the calculator
print("\n\n Hi welcome I am calculator for your calculations")
print(" Can I help ?")
print(" 1. addition \n 2. subtraction \n 3. multiplication \n 4. division ")
print("Press one option for what do you now")
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
