from collections import namedtuple


def custom_divmod(x, y):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(x, y))


result = custom_divmod(12, 5)
print(result)

# Use a list of strings as field names
Point = namedtuple("Point", ["x", "y"])
point = Point(2, 4)
print(point)

# Access the coordinates
print(point.x)
print(point.y)
print(point[0])

# Use a generator expression as field names
Point = namedtuple("Point", (field for field in "xy"))
print(Point(2, 4))

# Use a string with comma-separated field names
Point = namedtuple("Point", "x, y")
print(Point(2, 4))

# Use a string with space-separated field names
Point = namedtuple("Point", "x y")
print(Point(2, 4))


# Define default values for fields
Person = namedtuple("Person", "name job", defaults=["Python Developer"])
person = Person("Jane")
print(person)
# Create a dictionary from a named tuple
person._asdict()

# Replace the value of a field
person = person._replace(job="Web Developer")
print(person)


class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()

    @property
    def hy_pot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hy_pot=%6.3f' % (self.x, self.y, self.hy_pot)


for p in Point(3, 4), Point(14, 5 / 7):
    print(p)
