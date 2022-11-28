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
