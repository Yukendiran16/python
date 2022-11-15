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


def indexing():
    print("Tuple of numbers")
    print(tuple_int)
    print("\n Positive indexing")
    print("Value at index 1")
    print(tuple_int[1])
    print("values from index 2 to 6")
    print(tuple_int[2:6])
    print("values from index 1 to end of the tuple")
    print(tuple_int[1:])
    print("values from index 6 to stating of the tuple in reverse")
    print(tuple_int[:6])
    print("\n Negative indexing")
    print("Value at index 1")
    print(tuple_int[-1])
    print("values from index -6 to -2")
    print(tuple_int[-6:-2])
    print("values from index -1 to stating of the tuple in reverse")
    print(tuple_int[:-1])
    print("values from index -6 to end of the tuple")
    print(tuple_int[-6:])


# TypeError: 'tuple' object does not support item assignment
# if you modify the tuple returns above error
# using try except you handle it.
# tuple_str[-1] = "python"
# print(tuple_str)

tuple_srt_add = ("to", "my", "world")
tuple_str += tuple_srt_add
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

new_tuple = tuple.__add__(tuple_str, tuple_int)
# new_tuple = tuple.__class_getitem__(tuple_str)
print(new_tuple)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
