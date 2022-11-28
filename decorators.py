# # from decorator import decorator
#
# print("\n**************************************************")
# """Functions are first-class objects in Python. As a result,
# they have all of the attributes of an object, and we may handle them
# as such by assigning them to variables and passing them as
# arguments to other functions as arguments."""
#
#
# # assigning function to a variable
# def site():
#     """This the sample program for creating a function and assign
#     to a variable then access the function when calling the variable"""
#     print("My Decorator")
#
#
# website = site
# print(f"{site = }")
# print(f"{website = }")
# site()
# website()
# print("**************************************************")
#
#
# # passing functions as arguments.
# # one function return another function
# def sqrt(num):
#     """It will be return addition of 100 and value from square function returns."""
#     return 100 + square(num)
#
#
# def square(num):
#     """It will be return square root of the input"""
#     return num ** 2
#
#
# def math(function):
#     """It will be return addition of 100 + value from which function is called."""
#     print(100 + function(10))
#
#
# math(sqrt)
# math(square)
# print(square(10))
# print("**************************************************")
#
#
# # function within another function is called nested functions
# def math():
#     """It returns output from inner function sqr()"""
#
#     def sqr(num):
#         return num ** 2
#
#     print(sqr(2))
#
#
# math()
# print("**************************************************")
#
#
# # Closure Functions are nested functions that can access non-local variables.
# # non-local variable and closure function in Python
# def math(num):
#     """It returns output from inner function sqr()"""
#
#     def sqr():
#         """It will be returns some outputs"""
#         return num ** 2
#
#     print(sqr())
#
#
# math(4)
# print("**************************************************")
#
#
# def my_decor(func):
#     """It returns what is obtained from inner function of my_wrap"""
#
#     def my_wrap():
#         """It will be returns some outputs"""
#         print("Decorator Function")
#         return func()
#
#     return my_wrap
#
#
# def my_function():
#     """It will be returns some outputs"""
#     print("Main Function")
#
#
# my_function = my_decor(my_function)
# my_function()
# print("**************************************************")
#
#
# def my_decor(func):
#     """It returns what is obtained from inner function of my_wrap"""
#
#     def my_wrap(str1, str2):
#         """It will be returns some outputs"""
#         print("Decorator Function")
#         return func(str1, str2)
#
#     return my_wrap
#
#
# def my_function(str1, str2):
#     """It will be returns some outputs"""
#     print("Main Function")
#     print(str1 + " are " + str2)
#
#
# my_function = my_decor(my_function)
# my_function("Mangoes", "Sweet")
# print("**************************************************")
#
#
# # we can apply several decorators to a single function.
# # The decorators, on the other hand, will be used in the sequence that we’ve designated.
# # This is called chaining decorators.
# def my_decor(func):
#     """It returns what is obtained from inner function of my_wrap"""
#
#     def my_wrap(*args, **kwargs):
#         """It will be returns some outputs"""
#         print("Decorator Function")
#         return func(*args, **kwargs)
#
#     return my_wrap
#
#
# def my_function(str1, str2):
#     """It will be returns some outputs"""
#     print("Main Function")
#     print(str1 + " are " + str2)
#
#
# my_function = my_decor(my_function)
#
# my_function("Mangoes", "Delicious")
# print("**************************************************")
#
#
# # we can apply several decorators to a single function.
# # The decorators, on the other hand, will be used in the sequence that we’ve designated.
# # This is called chaining decorators.
# def my_decor(func):
#     """It returns what is obtained from inner function of my_wrap"""
#
#     def my_wrap(*args, **kwargs):
#         """It will be returns some outputs"""
#         print("Decorator Function 1")
#         return func(*args, **kwargs)     # It will be pass to next order of function
#
#     return my_wrap
#
#
# def my_another_decor(func):
#     """It returns what is obtained from inner function of my_wrap"""
#
#     def my_wrap(*args, **kwargs):
#         """It will be returns some outputs"""
#         print("Decorator Function 2")
#         return func(*args, **kwargs)   # It returns main function
#
#     return my_wrap
#
#
# # Instead of assigning the decorator to a variable, we can simply use the @ sign.
# # This is the most common method of implementing decorators.
# @my_decor          # This function is executed first
# @my_another_decor  # This function is executed next
# def my_function(str1, str2):
#     """It will be returns some outputs"""
#     print("Main Function")
#     print(str1 + " are " + str2)
#
#
# my_function("Mangoes", "Delicious")
# print("**************************************************")
#
#
# from functools import wraps
#
#
# def decorator(function):
#     @wraps(function)
#     def wrapper(num1, num2):
#         print("##", function.__name__, "of", num1, "and", num2, "##")
#         function(num1, num2)
#     return wrapper
#
#
# @decorator
# def sum(a, b):
#     print(a + b)
#
#
# @decorator
# def difference(a, b):
#     print(a - b)
#
#
# @decorator
# def product(a, b):
#     print(a * b)
#
#
# sum(1, 2)
# difference(2, 1)
# product(2, 2)
#

import requests
from functools import wraps
from flask import Flask, request, abort
import functools

app = Flask(__name__)


def validate_json(*expected_args):  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:  # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)

        return wrapper_validate_json

    return decorator_validate_json


@app.route("/grade", methods=["POST"])
@validate_json("student_id")
def update_grade():
    json_data = request.get_json()
    # Update database.
    return "success!"


class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return


@LimitQuery
def get_coin_price(limit):
    """View the Bitcoin Price Index (BPI)"""

    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))


def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'

    return wrapper


@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


print(net_price(1000, 12))
help(net_price)
print(net_price.__name__)


# def accepts(*types):
#     def check_accepts(f):
#         assert len(types) == f.func_code.co_argcount
#
#         def new_f(*args, **kwds):
#             for (a, t) in zip(args, types):
#                 assert isinstance(a, t), \
#                     "arg %r does not match %s" % (a, t)
#             return f(*args, **kwds)
#
#         new_f.func_name = f.func_name
#         return new_f
#
#     return check_accepts
#
#
# def returns(rtype):
#     def check_returns(f):
#         def new_f(*args, **kwds):
#             result = f(*args, **kwds)
#             assert isinstance(result, rtype), \
#                 "return value %r does not match %s" % (result, rtype)
#             return result
#
#         new_f.func_name = f.func_name
#         return new_f
#
#     return check_returns
#
#
# @accepts(int, (int, float))
# @returns((int, float))
# def func(arg1, arg2):
#     return arg1 * arg2
