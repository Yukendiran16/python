import itertools
from functools import reduce
import operator

dummy = [-1, 5, 10, 6, 3]
# Use reduce to calculate the sum of the list along with add operator function
print("The sum using add operator function is", reduce(operator.add, dummy))

# using concat operator function to join strings
print(reduce(operator.concat, ["Scaler ", "Academy"]))


# pre-defined function to calculate minimum
def mini(a, b):
    return a if a < b else b


# pre-defined function to calculate maximum
def maxi(a, b):
    return a if a > b else b


nums = [3, 5, 2, 4, 7, 1]

# passing both functions in to reduce along with nums as iterable
print('The minimum in the given list is', reduce(mini, nums))
print('The maximum in the given list is', reduce(maxi, nums))


# creating a function to check if both arguments are True or not
def is_true(a, b):
    return bool(a and b)


print(reduce(is_true, [1, 1, 1, 1, 1]))
print(reduce(is_true, [1, 1, 1, 1, 0]))

nums = [1, 2, 3, 4]

# printing the iterator
print(list(itertools.accumulate(nums)))

nums = [1, 3, 5, 7]

# using for loop to calculate the sum of a list
ans = 0
for i in nums:
    ans += i
print(ans)

# single line code using reduce
print(reduce(lambda x, y: x + y, nums))

# a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Use reduce function for flattening a 2D list
print(reduce(lambda x, y: x + y, matrix))

# using list comprehension
print([i for row in matrix for i in row])
