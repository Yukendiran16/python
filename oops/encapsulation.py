class Employee:
    """This class used to create properties for Employee
    object and access the properties of Employee"""
    # constructor of the class it initialize the object
    def __init__(self, name, salary, project):
        # data members
        self.name = name         # public variable
        self.__salary = salary   # private variable declare by using __ prefix of the attribute
        self._project = project  # protected variable declare by using _ prefix of the attribute

    # method
    # to display employee's details
    def show(self):
        """Display the properties of Employee object"""
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.__salary)

    # method
    def work(self):
        """Display the work status of Employee object"""
        print(self.name, 'is working on', self._project)

    # getter method
    def get_salary(self):
        """This method used to get value of private variable salary"""
        return self.__salary

    # setter method
    def set_salary(self, salary):
        """This method used to set value of  private variable salary"""
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
print('Salary:', employee.__salary)

# Direct access protected data member
print('Project:', employee._project)
