# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
This is the program to create tuple.
tuple is one of the python datatype.
using this tuple perform all methods
and check the method how will be working
"""

# Create user defined tuple's
tuple_int = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tuple using numbers
tuple_str = ("hii", "hello", "i", "am", "here", "myself", "program")  # tuple using string
tuple_bool = (True, False)  # tuple using boolean
tuple_mix = (1, "hii", True, 2, "myself", False)  # tuple using numbers, string, boolean

print(len(tuple_bool))  # length of the tuple_bool
print(type(tuple_bool))  # type of the tuple_bool

try:
    print(tuple_int)
    print(tuple_int[1])
    print(tuple_int[2:6])
    print(tuple_int[1:])
    print(tuple_int[:6])
    print(tuple_int[-1])
    print(tuple_int[-6:-2])
    print(tuple_int[:-1])
    print(tuple_int[-6:])
except IndexError:
    print("you entered wrong index number")
print(tuple_str)

if "hello" in tuple_str:
    print("is present")
    print("\n")

# TypeError: 'tuple' object does not support item assignment
# if you modify the tuple returns above error
# using try except you handle it.
# try:
#     tuple_str[-1] = "python"
#     print(tuple_str)
# except TypeError:
#     print("\n exception occurs you try to modify tuple, but it is not possible\n")
try:
    tuple_str_dup = list(tuple_str)
    tuple_str_dup[-1] = "python"
    # tuple_str_dup[-10] = "python"
    tuple_str = tuple(tuple_str_dup)
    print(tuple_str)
except IndexError:
    print("you entered wrong index number")
    print("\n")

# NameError: name 'tuple_str_' is not defined.
tuple_str_dup = list(tuple_str)
tuple_str_dup.append("welcome")
tuple_str = tuple(tuple_str_dup)
print(tuple_str)
print("\n")
# try:
#     print(tuple_str_)
#     del (tuple_str_)
# except NameError:
#     print("\n you entered wrong name it doesn't initialize \n")

tuple_srt_add = ("to", "my", "world")
tuple_str += tuple_srt_add
print(tuple_str)
print("\n")

# returns ValueError: list.remove(x): x not in list
# if you push to remove value is not present in tuple
# using try with except you handle the ValueError
# tuple_str_dup = list(tuple_str)
# tuple_str_dup.remove("abc")
# tuple_str = tuple(tuple_str_dup)
# print(tuple_str)
# raise ValueError("\n exception occurs you try to remove value is not present in the tuple\n")

tuple_str_dup = list(tuple_str)
try:
    tuple_str_dup.remove("abc")
    tuple_str = tuple(tuple_str_dup)
    print(tuple_str)
except ValueError:
    print("\nexception occurs you try to remove value is not present in the tuple\n")

tuple_str_dup = list(tuple_str)
tuple_str_dup.remove("hello")
tuple_str = tuple(tuple_str_dup)
print(tuple_str)
print("\n")

# tuple unpacking
# (a, b, c, *d, *e) = tuple_str    # SyntaxError: multiple starred expressions in assignment
(a, b, c, d, *e) = tuple_str
print(a, b, c, d)
print(e)  # returns list all values in tuple expect a, b, c, d
print("\n")

# iterating through tuple using for loop
for mix in tuple_mix:
    print(mix)
print("\n")

# iterating through index of tuple using for
for mix in range(len(tuple_mix)):
    print(tuple_mix[mix])
print("\n")

for mix in range(0, len(tuple_mix)):
    print(mix)
    print(tuple_mix[mix])
print("\n")

# iterating through tuple using while loop
mix_itr = 0
while mix_itr < len(tuple_mix):
    print(mix_itr)
    print(tuple_mix[mix_itr])
    mix_itr += 1
print("\n")

# tuple joins
join_tuple = (tuple_str + tuple_int) * 2
print(join_tuple)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
