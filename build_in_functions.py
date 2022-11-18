# importing numpy module
# it is equivalent to "import numpy as np"
np = __import__('numpy', globals(), locals(), [], 0)  # __import__()

# array from numpy
a = np.array([1, 2, 3])

# prints the type
print(type(a))

print("*****************************************************")
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]  # zip()
roll_no = [4, 1, 3, 2]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))

print("*****************************************************")
names = ['Mukesh', 'Roni', 'Chari']  # zip()
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
print("*****************************************************")
stocks = ['reliance', 'infosys', 'tcs']  # zip()
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks,
                               prices in zip(stocks, prices)}
print(new_dict)
print("*****************************************************")
# Python code to demonstrate the working of                 # unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]  # zip()
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)
print("*****************************************************")
# Python code to demonstrate the application of                    # zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))

print("*****************************************************")


# Python program to illustrate                               # vars()
# working of vars() method in Python

class Geeks:

    def __init__(self, name1="Arun", num2=46, name3="Rishab"):
        self.name1 = name1
        self.num2 = num2
        self.name3 = name3


GeeksforGeeks = Geeks()
print(vars(GeeksforGeeks))

print("*****************************************************")


# Python program to illustrating                            # vars()
# the use of vars() and locals
# when no argument is passed and
# how vars() act as locals().
class Geeks(object):
    def __init__(self):
        self.num1 = 20
        self.num2 = "this is returned"

    def __repr__(self):
        return "Geeks() is returned"

    def loc(self):
        ans = 21
        return locals()

    # Works same as locals()
    def code(self):
        ans = 10
        return vars()

    def prog(self):
        ans = "this is not printed"
        return vars(self)


if __name__ == "__main__":
    obj = Geeks()
    print(obj.loc())
    print(obj.code())
    print(obj.prog())
print("*****************************************************")
a = ("Geeks", "for", "Geeks")
b = ["Geeks", "for", "Geeks"]  # type()
c = {"Geeks": 1, "for": 2, "Geeks": 3}
d = "Hello World"
e = 10.23
f = 11.22

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print("*****************************************************")

# when parameter is not passed
tuple1 = tuple()  # tuple()
print("empty tuple:", tuple1)

# when an iterable(e.g., list) is passed
list1 = [1, 2, 3, 4]
tuple2 = tuple(list1)
print("list to tuple:", tuple2)

# when an iterable(e.g., dictionary) is passed
dict = {1: 'one', 2: 'two'}
tuple3 = tuple(dict)
print("dict to tuple:", tuple3)

# when an iterable(e.g., string) is passed
string = "geeksforgeeks";
tuple4 = tuple(string)
print("str to tuple:", tuple4)

print("*****************************************************")


class Emp():
    def __init__(self, id, name, Add):  # super()
        self.id = id
        self.name = name
        self.Add = Add


# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails


Emp_1 = Freelance(103, "Suraj kr gupta", "Noida", "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

print("*****************************************************")


class demoClass:  # staticMethod()

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(a, b):
        return a + b

    def diff(self):
        return self.a - self.b


# convert the add to a static method
demoClass.add = staticmethod(demoClass.add)

# we can access the method without creating
# the instance of class
print(demoClass.add(1, 2))

# if we want to use properties of a class
# then we need to create a object
Object = demoClass(1, 2)
print(Object.diff())

print("*****************************************************")

# Python code to demonstrate the working of                  # sum()

numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# start parameter is not provided
Sum = sum(numbers)
print(Sum)

# start = 10
Sum = sum(numbers, 10)
print(Sum)

print("*****************************************************")
# Python program to demonstrate                           # str()
# strings

# Empty string
s = str()
print(s)

# String with values
s = str("GFG")
print(s)

print("*****************************************************")

# sorted()
# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))

# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))

# String-sorted based on ASCII translations
x = "python"
print(sorted(x))

# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))

# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))

# Frozen Set
x = frozenset(('q', 'w', 'e', 'r', 't', 'y'))
print(sorted(x))
print("*****************************************************")

# Python3 code to demonstrate
# Reverse Sort a String
# using join() + sorted() + reverse

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))

# using join() + sorted() + reverse
# Sorting a string
res = ''.join(sorted(test_string, reverse=True))

# print result
print("String after reverse sorting : " + str(res))

print("*****************************************************")


# Sort a list of integers based on
# their remainder on dividing from 7
def func(x):
    return x % 7


L = [15, 3, 11, 7]

print("Normal sort :", sorted(L))
print("Sorted with key:", sorted(L, key=func))

L = ["cccc", "b", "dd", "aaa"]

print("Normal sort :", sorted(L))
print("Sort with len :", sorted(L, key=len))

print("*****************************************************")
# import the module
import functools

# initializing string
test_string = "geekforgeeks"

# printing original string
print("The original string : " + str(test_string))

# using sorted() + reduce() + lambda
# Reverse Sort a String
res = functools.reduce(lambda x, y: x + y,
                       sorted(test_string,
                              reverse=True))
# print result
print("String after reverse sorting : " + str(res))

print("*****************************************************")

# list -ve index slicing
l = ['a', 'b', 'c', 'd', 'e', 'f']  # slice()
slice_obj = slice(-2, -6, -1)
print("list slicing:", l[slice_obj])

# string -ve index slicing
s = "geeks"
slice_obj = slice(-1)
print("string slicing:", s[slice_obj])

# tuple -ve index slicing
t = (1, 3, 5, 7, 9)
slice_obj = slice(-1, -3, -1)
print("tuple slicing:", t[slice_obj])

print("*****************************************************")


# setattr()
class Dict2Class(object):
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


# Driver Code
if __name__ == "__main__":
    # Creating the dictionary
    my_dict = {"Name": "Geeks",
               "Rank": "1223",
               "Subject": "Python"}

    result = Dict2Class(my_dict)

    # printing the result
    print("After Converting Dictionary to Class : ")
    print(result.Name, result.Rank, result.Subject)
    print(type(result))
print("*****************************************************")


# setattr()
class Gfg:
    name = None
    descr = None


# initializing object
gfg = Gfg()

print("Before using setattr:\n"
      f"\tname: {gfg.name}\n"
      f"\tdescr: {gfg.descr}")

# setting value using setattr
setattr(gfg, "name", "GeeksForGeeks")
setattr(gfg, "descr", "CS Portal")

print("After using setattr:\n"
      f"\tname: {gfg.name}\n"
      f"\tdescr: {gfg.descr}")

# creating new attribute using setattr
setattr(gfg, 'value', 5)
print(f"\nNew attribute created, gfg.value: {gfg.value}")

print("*****************************************************")

# Python3 code to demonstrate the
# working of set() on list and tuple

# initializing list
lis1 = [3, 4, 1, 4, 5]

# initializing tuple
tup1 = (3, 4, 1, 4, 5)

# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
print("The tuple before conversion is : " + str(tup1))

# Iterables after conversion are
# notice distinct and elements
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))

# Python3 code to demonstrate the
# working of set() on dictionary

# initializing list
dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}

# Printing dictionary before conversion
# internally sorted
print("Dictionary before conversion is : " + str(dic1))

# Dictionary after conversion are
# notice lost keys
print("Dictionary after conversion is : " + str(set(dic1)))

print("*****************************************************")

# round()
print(round(12.1))
print(round(12.9))
print(round(12 / 11, 3))
print("*****************************************************")
# Python code to demonstrate working of
# reversed()

# For tuple
seqTuple = ('g', 'e', 'e', 'k', 's')
print(list(reversed(seqTuple)))

# For range
seqRange = range(1, 5)
print(list(reversed(seqRange)))

print("*****************************************************")


# reversed()
class gfg:
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Function to reverse the list
    def __reversed__(self):
        return reversed(self.vowels)


# Main Function
if __name__ == '__main__':
    obj = gfg()
    print(list(reversed(obj)))

print("*****************************************************")
# repr() representation
num = {1, 2, 3, 4, 5}

# printable representation of the set
printable_num = repr(num)
print(printable_num)
print("*****************************************************")
# incremented by -2
for i in range(25, 2, -2):
    print(i, end=" ")
print()

ele = range(10)[0]
print("First element:", ele)

ele = range(10)[-1]
print("\nLast element:", ele)

ele = range(10)[4]
print("\nFifth element:", ele)

from itertools import chain

# Using chain method
print("Concatenating the result")
res = chain(range(5), range(10, 20, 2))

for i in res:
    print(i, end=" ")

print("\n*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
print("*****************************************************")
