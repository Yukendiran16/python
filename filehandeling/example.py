import os
from pathlib import Path
from datetime import datetime

# file_sample1 = open('C:/Users/lenovo/Documents/day5.txt', 'r')    # read mode
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='r' encoding='cp1252'>
# print(file_sample1)
# file_sample3 = open('C:/Users/lenovo/Documents/day5.txt', 'w')    # write mode
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='w' encoding='cp1252'>
# print(file_sample3)
# file_sample4 = open('C:/Users/lenovo/Documents/days.txt', 'x')
# # crate mode the file is already exists error thrown
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='x' encoding='cp1252'>
# print(file_sample4)
# file_sample5 = open('C:/Users/lenovo/Documents/day5.txt', 'a')    # append mode
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='a' encoding='cp1252'>
# print(file_sample5)
# file_sample6 = open('C:/Users/lenovo/Documents/day5.txt', 't')
# # Must have exactly one of create/read/write/append mode and at most one plus
# print(file_sample6)
# file_sample7 = open('C:/Users/lenovo/Documents/day5.txt', '+')
# # Must have exactly one of create/read/write/append mode and at most one plus
# print(file_sample7)
# file_sample8 = open('C:/Users/lenovo/Documents/day5.txt', 'b')
# # Must have exactly one of create/read/write/append mode and at most one plus
# print(file_sample8)
# file_sample61 = open('C:/Users/lenovo/Documents/day5.txt', 'rt')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='rt' encoding='cp1252'>
# print(file_sample61)
# file_sample71 = open('C:/Users/lenovo/Documents/day5.txt', 'w+')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='w+' encoding='cp1252'>
# print(file_sample71)
# file_sample81 = open('C:/Users/lenovo/Documents/day5.txt', 'rb')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='rb' encoding='cp1252'>
# print(file_sample81)
# file_sample9 = open('C:/Users/lenovo/Documents/day5.txt', 'r+')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='r+' encoding='cp1252'>
# print(file_sample9)
# file_sample10 = open('C:/Users/lenovo/Documents/day5.txt', 'a+')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='a+' encoding='cp1252'>
# print(file_sample10)
# # file_sample11 = open('C:/Users/lenovo/Documents/day5.txt', 'x+')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='x+' encoding='cp1252'>
# print(file_sample11)
# file_sample12 = open('C:/Users/lenovo/Documents/day5.txt', 'wt')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='wt' encoding='cp1252'>
# print(file_sample12)
# file_sample13 = open('C:/Users/lenovo/Documents/day5.txt', 'wb')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='wb' encoding='cp1252'>
# print(file_sample13)
# file_sample14 = open('C:/Users/lenovo/Documents/day5.txt', 'ab')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='ab' encoding='cp1252'>
# print(file_sample14)
# file_sample15 = open('C:/Users/lenovo/Documents/day5.txt', 'at')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='at' encoding='cp1252'>
# print(file_sample15)
# # file_sample16 = open('C:/Users/lenovo/Documents/day5.txt', 'xb')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='xb' encoding='cp1252'>
# print(file_sample16)
# # file_sample17 = open('C:/Users/lenovo/Documents/day5.txt', 'xt')
# # returns <_io.TextIOWrapper name='C:/Users/lenovo/Documents/day5.txt' mode='xt' encoding='cp1252'>
# print(file_sample17)


"""Use the read() method on the file object and print the result."""
# f = open("C:/Users/lenovo/Documents/day5.txt")
# print(f.read(), end="")          # read line by line to end of the line, line by line output
#
# f = open("C:/Users/lenovo/Documents/day5.txt")
# print(f.read(324))               # read char by count line by line output
#
# f = open("C:/Users/lenovo/Documents/day5.txt")
# print(f.readline(), end="")      # read single line
#
# f = open("C:/Users/lenovo/Documents/day5.txt")
# for line in f:
#     print(line, end="")          # read line by line to end of the line, line by line output
#
# f = open("C:/Users/lenovo/Documents/day5.txt")
# print(f.readlines(), end="")     # read line by line in one line of output
#
# f = open("C:/Users/lenovo/Documents/day5.txt")
# print(f.readlines(150))          # read char by count but single line of output
#
# with open("C:/Users/lenovo/Documents/day5.txt") as f:
#     file_contents = f.read()    # read line by line using with
#     print(file_contents)
#     # Additional code here

# remove the file from your directory
# os.remove("C:/Users/lenovo/Documents/days.txt")

# with open('C:/Users/lenovo/Documents/days.txt', 'w') as f:
#     data = 'some data to be written to the file'
#     f.write(data)    # io.UnsupportedOperation: not writable

