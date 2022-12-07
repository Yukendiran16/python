from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, first_name='f_name', last_name='l_name'):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary=0):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary


class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, rate):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_salary(self):
        return self.worked_hours * self.rate


class Payroll:
    def __init__(self):
        self.employee_list = []

    def add(self, employee):
        self.employee_list.append(employee)

    def print(self):
        for e in self.employee_list:
            print(e.__dict__)
            print(f"{e.full_name} \t ${e.get_salary()}")


payroll = Payroll()

payroll.add(FullTimeEmployee('John', 'Doe', 6000))
payroll.add(FullTimeEmployee('Jane', 'Doe', 6500))
payroll.add(HourlyEmployee('Jenifer', 'Smith', 200, 50))
payroll.add(HourlyEmployee('David', 'Wilson', 150, 100))
payroll.add(HourlyEmployee('Kevin', 'Miller', 100, 150))

payroll.print()

from abc import ABC


class geometric(ABC):

    # abstract method
    @abstractmethod
    def volume(self):
        pass


class Rectangle(geometric):
    length = 4
    width = 6
    height = 6

    def volume(self):

        return self.length * self.width * self.height


class Sphere(geometric):
    radius = 8

    def volume(self):

        return 1.3 * 3.14 * self.radius * self.radius * self.radius


class Cube(geometric):
    Edge = 5

    def volume(self):

        return self.Edge * self.Edge * self.Edge


class triangle_3D:
    length = 5
    width = 4

    def volume(self):

        return 0.5 * self.length * self.width


rectangle = Rectangle()
sphere = Sphere()
cube = Cube()
triangle = triangle_3D()
print("Volume of a rectangle:", rectangle.volume())
print("Volume of a circle:", sphere.volume())
print("Volume of a square:", cube.volume())
print("Volume of a triangle:", triangle.volume())
