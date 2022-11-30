def add(a, b):
    return a + b


def sub(a=20, b=20):
    return a - b


def multiply(a):
    result = 1
    for i in a:
        result *= i
    return result


def even(*number_list):
    return list(x for x in number_list if x % 2 == 0)


def math_equation(x, y, /, d, *, a, b):
    return x + y - d * a / b


def book_author(**library_dict):
    return {x: y for x, y in library_dict.items()}


def multi_arguments(a, b, *x):
    return [a, b, [c for c in x]]


print(add(a=10, b=20))
print(add(10, 20))
print(sub())
print(sub(20, 10))
print(multiply([1, 2, 3, 4]))
print(even(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(math_equation(x=5, y=5, a=5, b=5))
# print(math_equation(5, 5, 5, 5, 5))
print(math_equation(5, 5, d=5, a=5, b=5))
# print(book_author(8, b=2, c=3, d=4))
print(book_author(a=1, b=2, c=3, d=4))
print(multi_arguments(1, (2, 3, 4, 5), 6, 7, 8, 9, 0))
