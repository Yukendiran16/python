import csv
from typing import Dict
from collections import OrderedDict

from management.admin.models.employee import Employee
from management.utils.logger_util import logger
from management.exception_handler.custom_exception import DataNotFoundException

employees = OrderedDict()


def create_employee(employee, employee_id: str = "I2I0", name: str = "name",
                    email: str = "abc@ideas2it.com",
                    role: str = "role", mobile: str = '0', salary: float = 0.0) -> None:
    """
    This method used to create new employee and save it to collection
    :param employee:
    :param employee_id:
    :param name:
    :param email:
    :param role:
    :param mobile:
    :param salary:
    :return: nothing
    """
    employee.set_employee_id(employee_id)
    employee.set_name(name)
    employee.set_email(email)
    employee.set_role(role)
    employee.set_mobile(mobile)
    employee.set_salary(salary)
    employees[employee_id] = employee
    logger.info("New employee object created id = " + employee_id)


def update_employee():
    """

    :return:
    """
    print("1. email\n"
          "2. role\n"
          "3. mobile")
    update = int(input("Choose one option : "))
    employee = get_employee()
    match update:
        case 1:
            employee.set_email(input("Enter mail id : "))
            return employee
        case 2:
            employee.set_role(input("Enter role : "))
            return employee
        case 3:
            employee.set_mobile(input("Enter mobile : "))
            return employee
        case _:
            print("wrong input")


def get_all() -> Dict:
    """

    :return:
    """
    if len(employees) == 0:
        logger.error(f"nothing to show because empty list")
        raise DataNotFoundException(f"nothing to show because empty list")
    return employees


def get_employee():
    """

    :return:
    """
    print("Search By ->\n"
          "1. Employee Id\n"
          "2. Name\n"
          "3. Mail")
    choice = 0
    try:
        choice = int(input("Enter one choice : "))
    except ValueError:
        logger.warning(f"Your choice is wrong : {choice}")
        print(f"Your choice is wrong : {choice}")
    match choice:
        case 1:
            employee_id = input("Enter employee Id : ")
            employee = employees.get(employee_id)
            if employee.get_employee_id() == employee_id:
                return employee
            else:
                logger.error(f"Couldn't find employee by id {employee_id}")
                raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")
        case 2:
            name = input("Enter name : ")
            for x, y in employees.items():
                if name is y.get_name():
                    return employees.get(x)
                else:
                    logger.error("Couldn't find employee by name at line 232")
                    raise DataNotFoundException("Couldn't find employee at line 208")
        case 3:
            email = input("Enter email Id : ")
            for x, y in employees.items():
                if email is y.get_email():
                    return employees.get(x)
                else:
                    logger.error("Couldn't find employee by mail at line 240")
                    raise DataNotFoundException("Couldn't find employee at line 215")


def create_csv(file_name='./employee.csv'):
    """
    This method used to create csv file for all employees
    :return: csv file with employee details
    """
    try:
        with open(file_name, 'w+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=(
                'employee_id', 'email', 'name', 'role', 'mobile', 'salary', ''))
            writer.writeheader()
            for employee in employees.values():
                print(employee.__dict__)
                writer.writerow(employee.__dict__)
    except (FileNotFoundError, FileExistsError):
        logger.error("Something went wrong to create file")
        print("Something went wrong to create file")