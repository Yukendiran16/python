import sys

# numbers list 1 to 20 for iterate using comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(sys.getsizeof(var for var in input_list if var % 2 == 0))          # 208
print(sys.getsizeof(set(var for var in input_list if var % 2 == 0)))     # 702

tuple_x = (10, 6, 45, 89, 90, 1, 225, 76, 44, 356, 356, 24, 676, 68, 2435, 676, 24)
x = (i for i in tuple_x if i % 5 == 0)
print(sys.getsizeof(tuple_x))
print(sys.getsizeof(list(x)))
print(sys.getsizeof(x))

y = tuple(i for i in tuple_x if i % 5 == 0)
print(y)
print(sys.getsizeof(y))

matrix_x = [[3, 1, 2],
            [5, 4, 6],
            {9, 7, 8},
            (3, 6, 9)]
print(sys.getsizeof(matrix_x))
matrix_y = [[3, 1, 2],
            [5, 4, 6],
            (9, 7, 8)]
for i in ((sum(x * y for x, y in zip(X, Y)) for Y in zip(*matrix_y)) for X in matrix_x):
    print(list(i))


def add(a, b):
    yield a + b


def generator_thr_iter():
    yield 'xyz', 444, 440.4
    yield list(add(3, 4))
    yield list(add(10, 10))


generate = generator_thr_iter()
print(generate.__next__(), "\n", generate.__next__(), "\n", generate.__next__())

