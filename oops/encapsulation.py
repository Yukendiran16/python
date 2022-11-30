class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.__salary = salary
        self._project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.__salary)

    # method
    def work(self):
        print(self.name, 'is working on', self._project)

    # getter method
    def get_salary(self):
        return self.__salary

    # setter method
    def set_salary(self, salary):
        self.__salary = salary


# creating object of a class
employee = Employee('Yuki K', 20000, 'SDE')

# calling public method of the class
employee.show()
employee.work()

# retrieving age using getter
print('Name:', employee.name, employee.get_salary())

# changing age using setter
employee.set_salary(25000)

# retrieving age using getter
print('Name:', employee.name, employee.get_salary())

# direct access to private member using name mangling
print('Salary:', employee._Employee__salary)

# Direct access protected data member
print('Project:', employee._project)
