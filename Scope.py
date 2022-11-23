# Built-in Scope
from math import pi


def scope():
    global name  # global key word is uds to declare a variable is global scope
    number = 10
    print(number)
    print(name)
    name = "maddy"  # if you want to change a value of a global variable in local
    # you must be declared a variable at in local global using global keyword
    print(name)


name = "yuke"
print(name)
scope()
print(name)


# print(number)   # if you change try to change a value of local variable in global it returns an error


def func_outer():
    x = "local"
    """local Variable is the variable that is defined in the function."""

    def func_inner():
        """Nonlocal Variable is the variable that is defined in the nested function."""
        nonlocal x  # To create a nonlocal variable nonlocal keyword is used.
        x = "nonlocal"
        print("inner:", x)

    func_inner()
    print("outer:", x)


func_outer()


# pi = 'Not defined in global pi'
def func_outer():
    """
    If a Variable is not defined in local, Enclosed or global scope, then python looks for it in the built-in scope.
    Hence, the name which is already present in the built-in scope should not be used as an identifier.
    """
    # pi = 'Not defined in outer pi'
    def inner():
        # pi = 'not defined in inner pi'
        print(pi)

    inner()


func_outer()
