import sys

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(sys.getsizeof(var for var in input_list if var % 2 == 0))
print(sys.getsizeof(set(var for var in input_list if var % 2 == 0)))

tuple_x = (10, 6, 45, 89, 90, 1, 225, 76, 44, 356, 356, 24, 676, 68, 2435, 676, 24)
x = (i for i in tuple_x if i % 5 == 0)
print(list(x))
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
print([[sum(x * y for x, y in zip(X, Y)) for Y in zip(*matrix_y)] for X in matrix_x])


def add(a, b):
    yield a + b


def generator_thr_iter():
    yield 'xyz', 444, 440.4
    yield list(add(3, 4))
    yield list(add(10, 10))


for i in generator_thr_iter():
    print(i)


def num_generator(n):
    num = 1
    while True:
        yield num
        if num == n:
            return
        else:
            num += 1

    for i in num_generator(20):
        print(i * i)
