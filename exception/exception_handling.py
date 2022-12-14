from collections import OrderedDict
from csv import DictWriter
from csv import writer
from custom_exception import DataNotFoundException
from typing import Optional, Dict
import csv, re


def generate():
    """
    This method used to create a unique id for employee
    :return: generated id
    """
    for i in range(100000):
        result = "I2I" + str(i)
        yield result


def pf(function):

    def sub_pf(*args):
        salary = args[0] - args[0] * 15/100

        return function(salary)

    return sub_pf


def insurance(function):

    def sub_insurance(*args):
        salary = args[0] - args[0] * 5/100

        return function(salary)

    return sub_insurance


@pf
@insurance
def calculate_salary(*args):
    return args[0] + 1000


ids = generate()
employees = OrderedDict()


class Employee:
    """
    This is an Employee class for create employee instance and access an employee
    then employee added into csv file
    """

    def __init__(self,employee_id: str = "I2I", name: str = "name", email: str = "abc@ideas2it.com",
                 role: str = "role", mobile: int = 0, salary: float = 0.0) -> None:
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.role = role
        self.mobile = mobile
        self.salary = salary

    def set_salary(self, salary):
        self.salary = round(calculate_salary(salary), 2)

    def set_email(self, email):
        """
        setter method of an employee email
        :param email: employee email
        :return: nothing
        """
        self.email = email

    def get_email(self):
        """
        getter method of an employee email
        :return: employee email
        """
        return self.email

    def set_role(self, role):
        """
        setter method of an employee role
        :param role: employee role
        :return: nothing
        """
        self.role = role

    def get_role(self):
        """
        getter method of an employee role
        :return: employee role
        """
        return self.role

    def set_mobile(self, mobile):
        """
        setter method of an employee mobile
        :param mobile: employee mobile
        :return: nothing
        """
        self.mobile = mobile

    def get_mobile(self):
        """
        getter method of an employee mobile
        :return: employee mobile
        """
        return self.mobile

    @staticmethod
    def get_all() -> Dict:
        if len(employees) == 0:
            raise DataNotFoundException("no data found")
        return employees

    @staticmethod
    def get_employee():
        try:
            print(employees.get(input("Enter employee Id : ")).__dict__)
        except:
            raise DataNotFoundException("Couldn't find employee")
        else:
            print("employee found or empty dict found")

    @staticmethod
    def create_csv(file_name='./employee.csv'):
        """
        This method used to create csv file for all employees
        :return: csv file with employee details
        """
        try:
            with open(file_name, 'x+') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=(
                    'employee_id', 'email', 'name', 'role', 'mobile', 'salary', ''))
                writer.writeheader()
                for employee in employees.values():
                    writer.writerow(employee)
        except (FileNotFoundError, FileExistsError) as ex:
            print(ex)


def main():
    """
    performing operation for employee like adding new employee,
    get particular employee details, update details,
    delete an employee, get all employees
    :return: nothing
    """

    is_continue = True
    while is_continue:
        print("1. Add Employee\n"
              "2. Search Employee\n"
              "3. Update Employee\n"
              "4. Delete Employee\n"
              "5. Create csv file for employees\n"
              "6. Get all Employees\n"
              "7. Exit\n")
        try:
            choice = int(input("Enter choice  : "))
            employee_object = Employee()
            match choice:
                case 1:
                    while is_continue:
                        employee_id = next(ids)
                        name = input("Enter employee name : ")
                        role = input("Enter employee role : ")
                        mail = input("Enter employee mail : ")
                        mobile = int(input("Enter employee mobile : "))
                        salary = int(input("Enter employee salary : "))
                        if re.match("^[A-Z][a-z]$", name):
                            pass
                        else:
                            employee = Employee(employee_id, name, role, mail, mobile, salary)
                            employee.set_salary(employee.salary)
                            employees[employee.employee_id] = employee
                        add_next = input("if you want to enter yes/no")
                        if add_next == "no":
                            is_continue = False
                    is_continue = True
                case 2:
                    try:
                        employee_object.get_employee()
                    except DataNotFoundException as message:
                        print(message)
                case 3:
                    print("1. email\n"
                          "2. role\n"
                          "3. mobile")
                    update = int(input("Choose one option"))
                    employee = employee_object.get_employee()
                    match update:
                        case 1:
                            employee.set_email(input("Enter mail id"))
                        case 2:
                            employee.set_role(input("Enter role"))
                        case 3:
                            employee.set_mobile(int(input("Enter mobile")))
                        case _:
                            print("wrong input")
                case 4:
                    try:
                        print(employees.pop(input("Enter employee Id : ")))
                    except KeyError as ep:
                        print("Couldn't find employee", ep)
                    else:
                        print("employee found")
                case 5:
                    employee_object.create_csv(input("Enter file Directory : "))
                case 6:
                    try:
                        for value in employee_object.get_all().values():
                            print(value.__dict__)
                    except DataNotFoundException as msg:
                        print(msg)
                case 7:
                    is_continue = False
                case _:
                    print("you entered wrong choice")
        except (ValueError, TypeError) as exception:
            print("\nyou entered wrong input choice must be in numbers", exception)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        main()
    finally:
        print("Thank you")
