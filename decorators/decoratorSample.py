# def design(function):
#
#     def create_design(*args, **kwargs):
#         print("***************************************")
#         print("function name : ", function.__name__)
#         print("***************************************")
#         print(function.__code__.co_freevars)
#         function(*args, **kwargs)
#     return create_design
#
#
# def my_decorator(function):
#
#     def expression_caller(*args, **kwargs):
#         print("***************************************")
#         print("function name : ", function.__name__)
#         print("***************************************")
#         print(function.__doc__)
#         function(*args, **kwargs)
#         print("Evaluation success")
#     return expression_caller
#
#
# @design
# @my_decorator
# def evaluate(*args, **kwargs):
#     """It evaluates the expression and returns the result"""
#     for i in args:
#         print("Result is : ", eval(i))
#     for i, j in kwargs.items():
#         print("Result is : ", eval(j))
#
#
# evaluate("2+3-54+43*4/3", "3+4-45*45/2", exp1="12+34-32*4+34/4")


def add_s_gst(function):
    print("Coming to calculate S_GST")

    def add_tax(*args, **kwargs):
        for amount in args:
            print("S_GST for your bill: ", amount * 0.2)
            print("State government GST added.")
            amount += amount * 0.2
            return function(amount)
        for amount in kwargs.values():
            print("S_GST for your bill: ", amount * 0.2)
            print("State government GST added.")
            amount += amount * 0.2
            return function(amount)

    return add_tax


def add_c_gst(function):
    print("Coming to calculate C_GST")

    def add_tax(*args, **kwargs):
        for amount in args:
            print("C_GST for your bill: ", amount * 0.3)
            print("Central government GST added.")
            amount += amount * 0.3
            return function(amount)
        for amount in kwargs.values():
            print("C_GST for your bill: ", amount * 0.3)
            print("Central government GST added.")
            amount += amount * 0.3
            return function(amount)

    return add_tax


@add_c_gst
@add_s_gst
def calculate_bill_amount(*args, **kwargs):
    """It calculates the total bill with all tax to be added"""
    print("Calculate bill")
    for amount in args:
        return "Bill amount is : ", amount
    for name, amount in kwargs.items():
        print("Bill name : ", name, "\nBill amount is : ", amount)


print(calculate_bill_amount(1000))
