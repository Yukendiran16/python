def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(f'Factorial of 10 = {factorial(10)}')
# factorial(5)
# = 5 * factorial(4)
# = 5 * 4 * factorial(3)
# = 5 * 4 * 3 * factorial(2)
# = 5 * 4 * 3 * 2 * factorial(1)
# = 5 * 4 * 3 * 2 * 1
# = 120
print(f'Factorial of 5 = {factorial(5)}')


def fibonacci(n):
    """ Returns Fibonacci Number at nth position using recursion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=" ")


# Recursive Python function to solve the tower of hanoi

def tower_of_hanoi(n, source, destination, auxiliary):
    print(n)
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')