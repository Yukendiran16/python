list_a = ['abcd', 'efgh', 'ijkl']
for i in list_a:
    if 'ijkl' is i:
        print(i)


def sample(a, b, c):
    print(a + b + c)


sample(12, 23, 34)
sample(c=34, b=23, a=12)

sample_map = list(filter(lambda x: x, list_a))

a = b = []
b = [1, 2, 3]
import time

c = [1, [3, [5, 4, 5, [7, 7]]]]
c[1][1][1] = 20
print(c)
c = [[2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20]]
c[1][2] = 19
print(c)
from datetime import date


class School:

    def __init__(self, name: str = "", type: str = "", place: str = "", started_on: date = 12 / 12 / 2022):
        pass

    @staticmethod
    def address():
        return "India"


class Class(School):

    def __init__(self, name, type, place, started_on,
                 class_name, section, no_of_students, no_of_teachers):
        super().__init__(name, type, place, started_on)
        pass

    @staticmethod
    def address():
        return "India"


class PlayGround(School):

    def __init__(self, name, type, place, started_on, size, ground_type):
        super().__init__(name, type, place, started_on)
        pass


class Student(Class):

    def __init__(self, name, type, place, started_on, class_name, section, no_of_students,
                 no_of_teachers, st_name, age, rank, gender):
        super().__init__(name, type, place, started_on, class_name, section, no_of_students,
                         no_of_teachers)

    @staticmethod
    def address():
        print(Class.address() + "-600028")


Student.address()


class IncorrectTypeException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def function_timer(func):
    def calculate_time(n):
        start = time.time()
        func(n)
        print("Time taken : ", round((time.time() - start), 5))

    return calculate_time


@function_timer
def sample_func(n):
    print(type(n))
    if type(n) is not int:
        raise IncorrectTypeException("You entered wrong input please enter numbers")
    else:
        for i in range(n):
            print(i*i*i*i*i)


try:
    sample_func(100)
except IncorrectTypeException as e:
    print(e)


from collections import OrderedDict

sample_ordered_dict = OrderedDict()

sample_ordered_dict['name'] = 'yuki'
sample_ordered_dict['age'] = 21
sample_ordered_dict['role'] = "dev"

sample_ordered_dict = OrderedDict([('name', 'yuki')])
print(type(sample_ordered_dict))

print(sample_ordered_dict)
