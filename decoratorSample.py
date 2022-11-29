def design(function):
    def create_design(*args, **kargs):
        print("***************************************")
        print("function name : ", function.__name__)
        print("***************************************")
        print(function.__code__.co_freevars)
        function(*args, **kargs)
    return create_design


def my_decorator(function):

    def expression_caller(*args, **kargs):
        print("***************************************")
        print("function name : ", function.__name__)
        print("***************************************")
        print(function.__doc__)
        function(*args, **kargs)
        print("Evaluation success")
    return expression_caller


@design
@my_decorator
def evaluate(*args, **kwargs):
    """It evaluates the expression and returns the result"""
    for i in args:
        print("Result is : ", eval(i))
    for i, j in kwargs.items():
        print("Result is : ", eval(j))


evaluate("2+3-54+43*4/3", "3+4-45*45/2", exp1="12+34-32*4+34/4")



