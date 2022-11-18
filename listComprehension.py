import random

list_x = [1, 2, 3, 4, 5, 6, 9]
print([x for x in list_x])

list_y = [12, 34, 43, 55, 76, 43, 78]
print([int(x / 2) for x in list_y if x % 2 == 0 if x % 3 == 0])

matrix_x = [[3, 1, 2],
            [5, 4, 6],
            {9, 7, 8}]
matrix_y = [[3, 1, 2],
            [5, 4, 6],
            (9, 7, 8)]
print([[sum(x * y for x, y in zip(X, Y)) for Y in zip(*matrix_y)] for X in matrix_x])
# for X in matrix_x:
#     for Y in zip(*matrix_y):
#         for x, y in zip(X, Y):
#             print(x, y) xx

# Nested list comprehension
matrix = [[j for j in range(10)] for i in range(3)]
print(matrix)

print([x if x != 4 else "Some value" for x in list_x])
