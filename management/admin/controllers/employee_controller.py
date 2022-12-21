import re

from management.admin.models.employee import Employee
from management.utils.logger_util import logger
from management.admin.service.employee_service import get_all, get_employee, create_csv
from management.exception_handler.custom_exception import DataNotFoundException
from management.admin.service.employee_service import employees
from management.admin.service.employee_service import update_employee
from management.admin.service.employee_service import create_employee
from management.utils.employee_util import generate


role_list = ['Software Developer', 'Quality Analyst', 'Manager', 'Human Resource']
ids = generate()


def admin_action():
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
        choice = 0
        try:
            choice = int(input("Enter choice  : "))
        except ValueError:
            logger.error("enter correct choice")
            print("enter correct choice")
        match choice:
            case 1:
                add_employee()
                add_next = input("if you want to add enter yes/no : ")
                if add_next == "yes":
                    add_employee()
            case 2:
                print(get_employee().__dict__)
            case 3:
                print(update_employee().__dict__)
            case 4:
                employee_id = input("Enter employee Id : ")
                employee = employees.get(employee_id)
                if employee is None:
                    logger.error(f"Couldn't find employee by id {employee_id}")
                    raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")
                else:
                    employee.set_is_active()
            case 5:
                create_csv(input("Enter file Directory : "))
            case 6:
                employee_list = get_all().values()
                for value in employee_list:
                    if value.get_is_active is False:
                        print(value.__dict__)
            case 7:
                break
            case _:
                print("you entered wrong choice")


def add_employee():
    """

    :return:
    """
    name, role, mail, mobile, salary = 'a', 'a', 'a', 0, 0
    isContinue = True
    while isContinue:
        name = input("Enter employee name : ")
        if not re.match("[A-Z]+", name):
            print("name must be in uppercase letters")
        else:
            break
    while isContinue:
        for i, j in enumerate(role_list, 1):
            print(i, j)
        role = input("Choose employee role : ")
        if role.isdigit() and int(role) <= len(role_list):
            role = role_list[int(role) - 1]
            break
        else:
            print("You entered wrong input")
    while isContinue:
        mail = input("Enter employee mail : ")
        if not re.match('[a-z_.+-]+@[a-z-]+\.[a-z-.]+', mail):
            print("invalid mail pattern")
        else:
            break
    while isContinue:
        try:
            mobile = input("Enter employee mobile : ")
            if not re.match('(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}', mobile):
                print("mobile number contains min 10 numbers")
            else:
                break
        except ValueError:
            print("enter integer")
    while isContinue:
        try:
            salary = int(input("Enter employee salary : "))
            if not re.match("[0-9]+", str(salary)):
                print("Salary must be integers")
            else:
                break
        except ValueError:
            print("enter integer")
    employee = Employee()
    create_employee(employee, next(ids), name, mail, role, mobile, salary)
