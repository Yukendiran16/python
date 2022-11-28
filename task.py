import re
import sys
from functools import reduce

# employee_list = []
# property_ = ['ids', 'name', 'age']
# ids = [1, 2, 3, 4, 5]
# name = ["a", "b", "c", "d", "e"]
# age = [25, 22, 34, 45, 45]
# for i in zip(ids, name, age):
#     dict_sample = {}
#     for j in zip(property_, i):
#         dict_sample.__setitem__(j[0], j[1])
#     employee_list.append(dict_sample)
# print(employee_list)
#
# employee_list = []
# property_ = ['ids', 'name', 'age']
# employees = [(1, "a", 25), (2, "b", 26), (3, "c", 27), (4, "d", 28), (5, "e", 29)]
# for employee in employees:
#     dict_sample = {}
#     for j in zip(property_, employee):
#         dict_sample.__setitem__(j[0], j[1])
#     employee_list.append(dict_sample)
# print(employee_list)
# *********************************************************************************************************************


# def add(a, b):
#     return a + b

#
# def sub(a=20, b=20):
#     return a - b
#
#
# def multiply(a):
#     result = 1
#     for i in a:
#         result *= i
#     return result
#
#
# def even(*number_list):
#     return list(x for x in number_list if x % 2 == 0)
#
#
# def math_equation(x, y, /, d, *, a, b):
#     return x + y - d * a / b
#
#
# def book_author(**library_dict):
#     return {x: y for x, y in library_dict.items()}
#
#
# def multi_arguments(a, b, *x):
#     return [a, b, [c for c in x]]
#
#
# def printing(*a):
#     return a
#
#
# print(list(zip(map(add, [1, 2, 3, 4, 5], (5, 4, 3, 2, 1)), filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))))
# print(list(zip(map(add, [1, 2, 3, 4, 5], (5, 4, 3, 2, 1)), range(1, 10))))
# print(list(map(multi_arguments, zip([1, 2, 3, 4, 5], (5, 4, 3, 2, 1)),
#                                     filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))))
# print(list(filter(printing, zip(zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]),
#                                     map(add, [1, 2, 3, 4, 5], (5, 4, 3, 2, 1))))))
# print(list(zip(map(add, [1, 2, 3, 4, 5], filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))))
# print(list(zip(filter(even, map(add, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))))
# print(reduce(add, range(100)))
# print(reduce(printing, range(10)))
# print(reduce(multi_arguments, range(10)))
# # print(list(zip(map(add, [1, 2, 3, 4, 5], (5, 4, 3, 2, 1)), reduce(add, range(50)))))
# # print(tuple(zip([1, 2, 3, 4, 5], (5, 4, 3, 2, 1), reduce(add, range(50)))))


# a = "do something-kasi"
# b = a.split(" ")
# c = ""
# for i in b:
#     if not(i.isalpha()) and not(i.isdigit()):
#         j = i.split("-")
#         for k in j:
#             if k == j[-1]:
#                 c += k[::-1]
#             else:
#                 c += k[::-1] + "-"
#     else:
#         c += i[::-1] + " "
# print(c)


brackets = [']', '[', ']', '{', '}', '{', '{', '}', '{', '{', '}', '(', '}', '{', ']', '{', '}', '(', ')', ')']
count = 0


def check_count(*args):
    global count
    for bracket in args:
        if brackets.count(bracket[0]) <= brackets.count(bracket[1]):
            count += brackets.count(bracket[0])
        else:
            count += brackets.count(bracket[1])


check_count(('{', '}'), ('[', ']'), ('(', ')'))

print(count)

counter_dict = {}
for i in brackets:
    if i in counter_dict:
        counter_dict[i] += 1
    else:
        counter_dict.__setitem__(i, 1)
print(counter_dict)


mix = "Al*97FY*Rd!vg$v"
last = ""
out = [x for x in mix]
for i, char in enumerate(out):
    if 48 <= ord(char) <= 57:
        out[i] = '0'
    elif 32 <= ord(char) <= 47:
        out[i] = '#'
    elif 65 <= ord(char) <= 90:
        out[i] = chr(ord(char) + 32)
    elif 97 <= ord(char) <= 122:
        out[i] = chr(ord(char) - 32)

for j in out:
    last += j
print(last)
