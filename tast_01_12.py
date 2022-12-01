n = int(input("enter an input"))
for i in range(n):
    if i != n - 1:
        print(" " * i + str(n - i) + (" " * (2 * (n - 1 - i) - 1) + str(n - i)))
    else:
        print(" " * i + str(n - i))
for i in range(1, n):
    print(" " * (n - i - 1) + str(i + 1) + (" " * (2 * i - 1) + str(i + 1)))
