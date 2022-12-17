import csv
import re
import logging
from collections import OrderedDict
from collections import defaultdict
from csv import DictWriter
from csv import writer
from datetime import datetime
from typing import Optional, Dict

from custom_exception import DataNotFoundException
from custom_exception import PatternError

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('mylog.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

role_list = ['Software Developer', 'Quality Analyst', 'Manager', 'Human Resource']
leave_types = ['Casual Leave']
employees = OrderedDict()
leave_record = {}
leaves = defaultdict()


def generate():
    """
    This method used to create a unique id for employee
    :return: generated id
    """
    for i in range(100000):
        result = "I2I" + str(i)
        yield result
        logger.info("New employee id generated")


def pf(function):
    def sub_pf(*args):
        logger.info("Inside PF calculation")
        salary = args[0] - args[0] * 15 / 100

        return function(salary)

    return sub_pf


def insurance(function):
    def sub_insurance(*args):
        logger.info("Inside Insurance calculation")
        salary = args[0] - args[0] * 5 / 100

        return function(salary)

    return sub_insurance


@pf
@insurance
def calculate_salary(*args):
    logger.info("salary calculated successfully")
    return args[0] + 1000


ids = generate()


class Employee:
    """
    This is an Employee class for create employee instance and access an employee
    then employee added into csv file
    """

    def __init__(self, employee_id: str = "I2I0", name: str = "name",
                 email: str = "abc@ideas2it.com",
                 role: str = "role", mobile: int = 0, salary: float = 0.0) -> None:
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.role = role
        self.mobile = mobile
        self.salary = salary
        logger.info("Employee object initialized")

    def create_employee(self, employee_id: str = "I2I0", name: str = "name",
                        email: str = "abc@ideas2it.com",
                        role: str = "role", mobile: str = '0', salary: float = 0.0) -> None:
        """
        This method used to create new employee and save it to collection
        :param employee_id:
        :param name:
        :param email:
        :param role:
        :param mobile:
        :param salary:
        :return: nothing
        """
        self.set_employee_id(employee_id)
        self.set_name(name)
        self.set_email(email)
        self.set_role(role)
        self.set_mobile(mobile)
        self.set_salary(salary)
        employees[employee_id] = self
        logger.info("New employee object created id = " + employee_id)

    def set_employee_id(self, employee_id):
        """
        setter method of an employee employee_id
        :param employee_id: employee employee_id
        :return: nothing
        """
        self.employee_id = employee_id
        return self.employee_id

    def get_employee_id(self):
        """
        getter method of an employee employee_id
        :return: employee employee_id
        """
        return self.employee_id

    def set_name(self, name):
        """
        setter method of an employee name
        :param name: employee name
        :return: nothing
        """
        self.name = name
        return self.name

    def get_name(self):
        """
        getter method of an employee name
        :return: employee name
        """
        return self.name

    def set_salary(self, salary):
        """
        setter method of an employee salary
        :param salary: employee salary
        :return: nothing
        """
        self.salary = round(calculate_salary(salary), 2)
        return self.salary

    def get_salary(self):
        """
        getter method of an employee salary
        :return: employee salary
        """
        return self.salary

    def set_email(self, email):
        """
        setter method of an employee email
        :param email: employee email
        :return: nothing
        """
        if re.match('[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+', email):
            self.email = email
        else:
            logger.error("wrong mail pattern at line 134")
            raise PatternError("wrong mail pattern at line 134")

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
            logger.error("wrong mobile pattern at line 169")
            raise PatternError("wrong mobile pattern at line 169")

    def get_mobile(self):
        """
        getter method of an employee mobile
        :return: employee mobile
        """
        return self.mobile

    @staticmethod
    def get_all() -> Dict:
        if len(employees) == 0:
            logger.error("no data found at line 181")
            raise DataNotFoundException("no data found at line 181")
        return employees

    @staticmethod
    def get_employee():
        print("Search By ->\n"
              "1. Employee Id\n"
              "2. Name\n"
              "3. Mail")
        choice = 0
        try:
            choice = int(input("Enter one choice : "))
        except ValueError:
            print(logger.warning(""))
            print("Your choice is wrong")
        match choice:
            case 1:
                employee = employees.get(input("Enter employee Id : "))
                if employee is not None:
                    return employee
                else:
                    logger.error("Couldn't find employee by id at line 224")
                    raise DataNotFoundException("Couldn't find employee at line 201")
            case 2:
                name = input("Enter name : ")
                for x, y in employees.items():
                    if name is y.name:
                        return employees.get(x)
                    else:
                        logger.error("Couldn't find employee by name at line 232")
                        raise DataNotFoundException("Couldn't find employee at line 208")
            case 3:
                name = input("Enter email Id : ")
                for x, y in employees.items():
                    if name is y.email:
                        return employees.get(x)
                    else:
                        logger.error("Couldn't find employee by mail at line 240")
                        raise DataNotFoundException("Couldn't find employee at line 215")

    @staticmethod
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


class LeaveRecord:
    """
    This the class for create leave record for employee
    """

    def __init__(self, employee_id: str = "I2I", from_date: datetime = 12 / 12 / 2001,
                 to_date: datetime = 12 / 12 / 2001,
                 leave_type: str = "", leave_purpose: str = "") -> None:
        self.employee_id = employee_id
        self.from_date = from_date
        self.to_date = to_date
        self.leave_type = leave_type
        self.leave_purpose = leave_purpose
        self.leave_avail = 12
        self.leave_taken = 0
        self.leave_dates = leaves

    def take_leave(self, employee_id: str = "I2I", from_date: datetime = 12 / 12 / 2001,
                   to_date: datetime = 12 / 12 / 2001,
                   leave_type: str = "", leave_purpose: str = "") -> None:
        """
        this the method to create leave record for an employee
        :param employee_id:
        :param from_date:
        :param to_date:
        :param leave_type:
        :param leave_purpose:
        :return: nothing
        """
        self.set_employee_id(employee_id)
        self.set_from_date(from_date)
        self.set_to_date(to_date)
        self.set_leave_type(leave_type)
        self.set_leave_purpose(leave_purpose)
        self.take_record()

    def set_employee_id(self, employee_id):
        """
        setter method of an employee employee_id
        :param employee_id: employee employee_id
        :return: nothing
        """
        self.employee_id = employee_id
        return self.employee_id

    def get_employee_id(self):
        """
        getter method of an employee employee_id
        :return: employee employee_id
        """
        return self.employee_id

    def set_from_date(self, from_date):
        """
        setter method of an employee from_date
        :param from_date: employee from_date
        :return: nothing
        """
        self.from_date = from_date
        return self.from_date

    def get_from_date(self):
        """
        getter method of an employee from_date
        :return: employee from_date
        """
        return self.from_date

    def set_to_date(self, to_date):
        """
        setter method of an employee to_date
        :param to_date: employee to_date
        :return: nothing
        """
        self.to_date = to_date
        return self.to_date

    def get_to_date(self):
        """
        getter method of an employee to_date
        :return: employee to_date
        """
        return self.to_date

    def set_leave_purpose(self, leave_purpose):
        """
        setter method of an employee leave_purpose
        :param leave_purpose: employee leave_purpose
        :return: nothing
        """
        self.leave_purpose = leave_purpose
        return self.leave_purpose

    def get_leave_purpose(self):
        """
        getter method of an employee leave_purpose
        :return: employee leave_purpose
        """
        return self.leave_purpose

    def set_leave_type(self, leave_type):
        """
        setter method of an employee leave_type
        :param leave_type: employee leave_type
        :return: nothing
        """
        self.leave_type = leave_type
        return self.leave_type

    def get_leave_type(self):
        """
        getter method of an employee leave_type
        :return: employee leave_type
        """
        return self.leave_type

    def take_record(self):
        for day in range(self.from_date.day, self.to_date.day):
            new_date = datetime.now().replace(day, self.from_date.month, self.from_date.year)
            leaves[self.employee_id] = new_date
        self.leave_dates = leaves
        self.leave_taken += len(leaves.get(self.employee_id))
        self.leave_avail -= len(leaves.get(self.employee_id))
        leave_record[self.employee_id] = self


def add_employee(run):
    name, role, mail, mobile, salary = 'a', 'a', 'a', 0, 0
    while run:
        name = input("Enter employee name : ")
        if not re.match("[A-Z]+", name):
            print("name must be in uppercase letters")
        else:
            break
    while run:
        role = input("Enter employee role : ")
        if role not in role_list:
            print("invalid role type")
        else:
            break
    while run:
        mail = input("Enter employee mail : ")
        if not re.match('[a-z_.+-]+@[a-z-]+\.[a-z-.]+', mail):
            print("invalid mail pattern")
        else:
            break
    while run:
        try:
            mobile = input("Enter employee mobile : ")
            if not re.match('(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}', mobile):
                print("mobile number contains min 10 numbers")
            else:
                break
        except ValueError:
            print("enter integer")
    while run:
        try:
            salary = int(input("Enter employee salary : "))
            if not re.match("[0-9]+", str(salary)):
                print("Salary must be integers")
            else:
                break
        except ValueError:
            print("enter integer")
    employee = Employee()
    employee.create_employee(next(ids), name, mail, role, mobile, salary)


def add_leave():
    leave = LeaveRecord()
    employee_id, from_date, to_date, leave_type, leave_purpose = 'a', '12/12/2001', '12/12/2001', 'a', 'a'
    run = True
    while run:
        employee_id = input("Enter employee id : ")
        if employee_id not in employees.keys():
            print("Enter valid id")
        else:
            break
    while run:
        try:
            from_date = datetime.strptime(input("Enter date for leave from :"),
                                          "%m/%d/%Y" or "%Y/%m/%d" or "%Y/%d/%m" or "%d/%m/%Y")
            break
        except ValueError:
            print("Please enter valid date")
    while run:
        try:
            to_date = datetime.strptime(input("Enter date for leave from :"),
                                        "%m/%d/%Y" or "%Y/%m/%d" or "%Y/%d/%m" or "%d/%m/%Y")
            break
        except ValueError:
            print("Please enter valid date")
    while run:
        leave_type = input("Enter leave type")
        if leave_type not in leave_types:
            print("Enter valid leave type")
        else:
            break
    leave_purpose = input("Tell reason for your leave")
    leave.take_leave(employee_id, from_date, to_date, leave_type, leave_purpose)


def view_leave_record():
    view_leave = input("Enter employee id : ")
    if view_leave in employees:
        return leave_record[view_leave]


def update_employee():
    print("1. email\n"
          "2. role\n"
          "3. mobile")
    update = int(input("Choose one option"))
    employee = Employee.get_employee()
    match update:
        case 1:
            employee.set_email(input("Enter mail id"))
            return employee
        case 2:
            employee.set_role(input("Enter role"))
            return employee
        case 3:
            employee.set_mobile(input("Enter mobile"))
            return employee
        case _:
            print("wrong input")


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
                add_employee(True)
                add_next = input("if you want to add enter yes/no")
                if add_next == "yes":
                    add_employee(True)
            case 2:
                print(Employee.get_employee().__dict__)
            case 3:
                print(update_employee().__dict__)
            case 4:
                if not employees.pop(input("Enter employee Id : ")):
                    logger.error("no data found")
                    raise DataNotFoundException("no data found")
            case 5:
                Employee.create_csv(input("Enter file Directory : "))
            case 6:
                employee_list = Employee.get_all().values()
                for value in employee_list:
                    print(value.__dict__)
            case 7:
                break
            case _:
                print("you entered wrong choice")


def user_action():
    is_continue = True
    while is_continue:
        print("1. Leave Record\n"
              "2. Add skills\n"
              "3.Exit")
        choice = 0
        try:
            choice = int(input("Enter choice  : "))
        except ValueError:
            logger.error("enter correct choice")
            print("enter correct choice")
        match choice:
            case 1:
                leave_action()
            case 2:
                add_skills()
            case 3:
                break
            case _:
                print("you entered wrong choice")


def leave_action():
    is_continue = True
    while is_continue:
        print("1. take leave\n"
              "2. view leave record\n"
              "3. Exit")
        choice = 0
        try:
            choice = int(input("Enter choice  : "))
        except ValueError:
            logger.error("enter correct choice")
            print("enter correct choice")
        match choice:
            case 1:
                add_leave()
            case 2:
                print(view_leave_record())
            case 3:
                break
            case _:
                print("you entered wrong choice")


if __name__ == '__main__':
    logger.info("Main method start")
    sign_in = 0
    run = True
    while run:
        try:
            print("1. Admin\n"
                  "2. User\n"
                  "3. exit")
            sign_in = int(input())
            if sign_in == 1:
                admin_action()
            elif sign_in == 2:
                user_action()
            elif sign_in == 3:
                break
            else:
                print("Wrong input")
        except Exception as e:
            logger.error(e)
            print(e)
            if sign_in == 1:
                admin_action()
            elif sign_in == 2:
                user_action()
        finally:
            print("Thank you")
