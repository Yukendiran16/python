# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
This is the program to create list.
list is one of the python datatype.
using this list perform all methods
and check the method how will be working
"""

# Create user defined list's
list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # list using numbers
list_str = ["hii", "hello", "i", "am", "here", "myself", "program"]  # list using string
list_bool = [True, False]  # list using boolean
list_mix = [1, "hii", True, 2, "myself", False]  # list using numbers, string, boolean

print(len(list_bool))  # length of the list_bool
print(type(list_bool))  # type of the list_bool

try:
    print(list_int)
    print(list_int[1])
    print(list_int[2:6])
    print(list_int[1:])
    print(list_int[:6])
    print(list_int[-1])
    print(list_int[-6:-2])
    print(list_int[:-1])
    print(list_int[-6:])
except IndexError:
    print("you entered wrong index number")

if "hello" in list_str:
    print("is present")
    print("\n")

set_int = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for i in set_int:
    print(set_int)
    print(i)
set_int.add("sss")
set_int.add("dss")
print(set_int)


