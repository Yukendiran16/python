import csv
import re
from collections import OrderedDict
from csv import DictWriter
from csv import writer
from typing import Optional, Dict

from custom_exception import DataNotFoundException


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
        salary = args[0] - args[0] * 15 / 100

        return function(salary)

    return sub_pf


def insurance(function):
    def sub_insurance(*args):
        salary = args[0] - args[0] * 5 / 100

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

    def __init__(self, employee_id: str = "I2I", name: str = "name", email: str = "abc@ideas2it.com",
                 role: str = "role", mobile: int = 0, salary: float = 0.0) -> None:
        super().__init__()
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.role = role
        self.mobile = mobile
        self.salary = salary

    def set_salary(self, salary):
        self.salary = round(calculate_salary(salary), 2)
        return self.salary

    def get_salary(self):
        return self.salary

    def set_email(self, email):
        """
        setter method of an employee email
        :param email: employee email
        :return: nothing
        """
        if re.match('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', email):
            self.email = email
        else:
            raise Exception("wrong mail pattern")

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
        if role in ['SDE', 'QA']:
            self.role = role
            return role

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
        if re.match('(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}', mobile):
            self.mobile = mobile
        else:
            raise Exception("wrong mobile pattern")

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
        employee = employees.get(input("Enter employee Id : "))
        if isinstance(employee, Employee):
            print(employee)
        else:
            raise DataNotFoundException("Couldn't find employee")

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


def add_employee(run):
    while run:
        employee_id = next(ids)
        name = input("Enter employee name : ")
        role = input("Enter employee role : ")
        mail = input("Enter employee mail : ")
        mobile = int(input("Enter employee mobile : "))
        salary = int(input("Enter employee salary : "))
        if not re.match("[A-Z][a-z]+", name):
            print("error in name")
        elif not re.match("[A-Z][a-z]+", role):
            print("error in name")
        elif not re.match("[\w.-]+@[\w.-]+\.\w+", email):
            print("error in name")
        elif not re.match("[6789][0-9]{9}", str(mobile)):
            print("error in name")
        elif not re.match("[0-9]+", str(salary)):
            print("error in name")
        else:
            employee = Employee(employee_id, name, role, mail, mobile, salary)
            employee.set_salary(employee.salary)
            employees[employee.employee_id] = employee
        run = False


def update_employee():
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


def action():
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
        choice = int(input("Enter choice  : "))
        employee_object = Employee()
        match choice:
            case 1:
                add_employee(True)
                add_next = input("if you want to enter yes/no")
                if add_next == "yes":
                    add_employee(True)
            case 2:
                employee_object.get_employee()
            case 3:
                update_employee()
            case 4:
                if not employees.pop(input("Enter employee Id : ")):
                    raise DataNotFoundException("no data found")
            case 5:
                employee_object.create_csv(input("Enter file Directory : "))
            case 6:
                employee_list = employee_object.get_all().values()
                if isinstance(employee_list, OrderedDict.Employee):
                    for value in employee_list:
                        print(value.__dict__)
                else:
                    raise DataNotFoundException("no data found")
            case 7:
                is_continue = False
            case _:
                print("you entered wrong choice")


if __name__ == '__main__':
    try:
        action()
    except Exception as e:
        print(e)
        action()
    finally:
        print("Thank you")
