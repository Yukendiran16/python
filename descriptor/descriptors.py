class Descriptor(object):

    def __init__(self, name=''):
        self.name = name

    def __get__(self, obj, obj_type):
        return "{}".format(self.name)

    def __set__(self, obj, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name should be string")


class GFG(object):
    name = Descriptor()


g = GFG()
g.name = "descriptors"
print(g.name)
print("***************************************************************")


class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    @property
    def value(self):
        print('Getting value')
        return self._value

    # setting the values
    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value


# passing the value
x = Alphabet('Peter')
print(x.value)

x.value = 'Diesel'

del x.value
print("***************************************************************")


# Python program to explain property() function
# Alphabet class
class Alphabet:
    def __init__(self, value):
        self._value = value

    # getting the values
    def get_value(self):
        print('Getting value')
        return self._value

    # setting the values
    def set_value(self, value):
        print('Setting value to ' + value)
        self._value = value

    # deleting the values
    def del_value(self):
        print('Deleting value')
        del self._value

    value = property(get_value, set_value, del_value, )


# passing the value
x = Alphabet('Me Descriptors')
print(x.value)

x.value = 'desc'

del x.value
print("***************************************************************")


# descriptors.py
class Verbose_attribute:
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class Foo:
    attribute1 = Verbose_attribute()


my_foo_object = Foo()
x = my_foo_object.attribute1
# print(Verbose_attribute.__set__(Verbose_attribute, obj=3, value=5))
print(x)
print("***************************************************************")
# property_decorator.py


class Foo:
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)

print("***************************************************************")
# property_function.py


class Foo:
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)


my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
print("***************************************************************")


class ClassMethod(object):
    """Emulate PyClassMethod_Type() in Objects/func_object.c"""

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)

        def new_func(*args):
            return self.f(klass, *args)

        return new_func


print("***************************************************************")


class Vehicle(object):
    can_fly = False
    number_of_wheels = 0


class Car(Vehicle):
    number_of_wheels = 4

    def __init__(self, color):
        self.color = color


my_car = Car("red")
print(my_car.__dict__)
print(type(my_car).__dict__)
print(my_car.color)
print(my_car.number_of_wheels)
print(my_car.can_fly)
print(my_car.__dict__['color'])
print(type(my_car).__dict__['number_of_wheels'])
print(type(my_car).__base__.__dict__['can_fly'])
print("***************************************************************")


# descriptors2.py
class OneDigitNumericValue(object):
    def __init__(self):
        self.value = 0

    def __get__(self, obj, type=None) -> object:
        return self.value

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value


class Foo(object):
    number = OneDigitNumericValue()


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

print("***************************************************************")


# descriptors3.py
class OneDigitNumericValue(object):
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0

    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value[obj] = value


class Foo(object):
    number = OneDigitNumericValue()


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)
print("***************************************************************")


# descriptors4.py
class OneDigitNumericValue():
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value


class Foo():
    number = OneDigitNumericValue("number")


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)
print("***************************************************************")


# descriptors5.py
class OneDigitNumericValue():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value


class Foo():
    number = OneDigitNumericValue()


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)
print("***************************************************************")


# properties.py
class Values:
    def __init__(self):
        self._value1 = 0
        self._value2 = 0
        self._value3 = 0
        self._value4 = 0
        self._value5 = 0

    @property
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value if value % 2 == 0 else 0

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, value):
        self._value2 = value if value % 2 == 0 else 0

    @property
    def value3(self):
        return self._value3

    @value3.setter
    def value3(self, value):
        self._value3 = value if value % 2 == 0 else 0

    @property
    def value4(self):
        return self._value4

    @value4.setter
    def value4(self, value):
        self._value4 = value if value % 2 == 0 else 0

    @property
    def value5(self):
        return self._value5

    @value5.setter
    def value5(self, value):
        self._value5 = value if value % 2 == 0 else 0


my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
print("***************************************************************")


# properties2.py
class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()


my_values = Values()
my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
print("***************************************************************")


class Ten:
    def __get__(self, obj, obj_type=None):
        return 10


class A:
    """To use the descriptor, it must be stored as a class variable in another class"""
    x = 5  # Regular class attribute
    y = Ten()  # Descriptor instance


a = A()  # Make an instance of class A
print(a.x)  # Normal attribute lookup
print(a.y)  # Descriptor lookup
print("***************************************************************")

import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess:

    def __get__(self, obj, obj_type=None):
        value = obj._age
        logging.info('Accessing %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Updating %r to %r', 'age', value)
        obj._age = value


class Person:
    age = LoggedAgeAccess()  # Descriptor instance

    def __init__(self, name, age):
        self.name = name  # Regular instance attribute
        self.age = age  # Calls __set__()

    def birthday(self):
        self.age += 1  # Calls both __get__() and __set__()


mary = Person('Mary M', 30)  # The initial age update is logged
dave = Person('David D', 40)
print(mary.age)  # Access the data and log the lookup
print(dave.name)  # Regular attribute lookup isn't logged
print(dave.age)  # Only the managed attribute is logged
