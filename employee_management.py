import csv
import re
from collections import OrderedDict
from collections import defaultdict
from csv import DictWriter
from csv import writer
from datetime import date
from datetime import datetime
from typing import Optional, Dict

from custom_exception import DataNotFoundException
from custom_exception import PatternError
from log import logger


role_list = ['Software Developer', 'Quality Analyst', 'Manager', 'Human Resource']
leave_types = ['Casual Leave']
employees = OrderedDict()
leave_record = {}
leaves = defaultdict(list)
skills = defaultdict(list)


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
    """

    :param function:
    :return:
    """
    def sub_pf(*args):
        """

        :param args:
        :return:
        """
        logger.info("Inside PF calculation")
        salary = args[0] - args[0] * 15 / 100

        return function(salary)

    return sub_pf


def insurance(function):
    """

    :param function:
    :return:
    """
    def sub_insurance(*args):
        """

        :param args:
        :return:
        """
        logger.info("Inside Insurance calculation")
        salary = args[0] - args[0] * 5 / 100

        return function(salary)

    return sub_insurance


@pf
@insurance
def calculate_salary(*args):
    """

    :param args:
    :return:
    """
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
        self.__employee_id = employee_id
        self.__name = name
        self.__email = email
        self.__role = role
        self.__mobile = mobile
        self.__salary = salary
        self.is_active = False
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
        self.__employee_id = employee_id
        return self.__employee_id

    def get_employee_id(self):
        """
        getter method of an employee employee_id
        :return: employee employee_id
        """
        return self.__employee_id

    def set_name(self, name):
        """
        setter method of an employee name
        :param name: employee name
        :return: nothing
        """
        self.__name = name
        return self.__name

    def get_name(self):
        """
        getter method of an employee name
        :return: employee name
        """
        return self.__name

    def set_salary(self, salary):
        """
        setter method of an employee salary
        :param salary: employee salary
        :return: nothing
        """
        self.__salary = round(calculate_salary(salary), 2)
        return self.__salary

    def get_salary(self):
        """
        getter method of an employee salary
        :return: employee salary
        """
        return self.__salary

    def set_email(self, email):
        """
        setter method of an employee email
        :param email: employee email
        :return: nothing
        """
        if re.match('[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+', email):
            self.__email = email
        else:
            logger.error(f"mail pattern couldn't match for this {email}")
            raise PatternError(f"mail pattern couldn't match for this {email}")

    def get_email(self):
        """
        getter method of an employee email
        :return: employee email
        """
        return self.__email

    def set_role(self, role):
        """
        setter method of an employee role
        :param role: employee role
        :return: nothing
        """
        if role in role_list:
            self.__role = role
            return role

    def get_role(self):
        """
        getter method of an employee role
        :return: employee role
        """
        return self.__role

    def set_mobile(self, mobile):
        """
        setter method of an employee mobile
        :param mobile: employee mobile
        :return: nothing
        """
        if re.match('(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}', mobile):
            self.__mobile = mobile
        else:
            logger.error(f"mobile pattern couldn't match for this {mobile}")
            raise PatternError(f"mobile pattern couldn't match for this {mobile}")

    def get_mobile(self):
        """
        getter method of an employee mobile
        :return: employee mobile
        """
        return self.__mobile

    @staticmethod
    def get_all() -> Dict:
        """

        :return:
        """
        if len(employees) == 0:
            logger.error(f"nothing to show because empty list")
            raise DataNotFoundException(f"nothing to show because empty list")
        return employees

    @staticmethod
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
                if employee is not None and employee.is_active is False:
                    return employee
                else:
                    logger.error(f"Couldn't find employee by id {employee_id}")
                    raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")
            case 2:
                name = input("Enter name : ")
                for x, y in employees.items():
                    if name == y.name and y.is_active is False:
                        return employees.get(x)
                    else:
                        logger.error("Couldn't find employee by name at line 232")
                        raise DataNotFoundException("Couldn't find employee at line 208")
            case 3:
                email = input("Enter email Id : ")
                for x, y in employees.items():
                    if email == y.email and y.is_active is False:
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

    def __init__(self, employee_id: str = "I2I") -> None:
        self.__employee_id = employee_id
        self.leave_avail = 12
        self.leave_taken = 0
        self.leave_dates = leaves

    def take_leave(self, employee_id: str = "I2I", from_date: date = 12 / 12 / 2001,
                   to_date: date = 12 / 12 / 2001,
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
        self.take_record(from_date, to_date, leave_type, leave_purpose)

    def set_employee_id(self, employee_id):
        """
        setter method of an employee employee_id
        :param employee_id: employee employee_id
        :return: nothing
        """
        self.__employee_id = employee_id
        return self.__employee_id

    def get_employee_id(self):
        """
        getter method of an employee employee_id
        :return: employee employee_id
        """
        return self.__employee_id

    def take_record(self, from_date, to_date, leave_type, leave_purpose):
        """

        :param from_date:
        :param to_date:
        :param leave_type:
        :param leave_purpose:
        :return:
        """
        for day in range(from_date.day, to_date.day):
            new_date = datetime.now().replace(day=day, month=from_date.month, year=from_date.year)
            leaves[self.employee_id].append({new_date: {'leave type': leave_type, 'leave_purpose': leave_purpose}})
        self.leave_dates = leaves[self.employee_id]
        self.leave_taken += len(leaves.get(self.employee_id))
        self.leave_avail -= len(leaves.get(self.employee_id))
        leave_record[self.employee_id] = self


class Skills:
    """

    """
    def __init__(self, technology: str = "", version: str = "", experience: str = ""):
        self.technology = technology
        self.version = version
        self.experience = experience

    def add_skills(self, employee_id, technology, version, experience):
        """

        :param employee_id:
        :param technology:
        :param version:
        :param experience:
        :return:
        """

        self.technology = technology
        self.version = version
        self.experience = experience
        skills[employee_id].append(self)

    @staticmethod
    def get_skills():
        employee_id = input("Enter your employee Id :")
        if employee_id in skills:
            if skills.get(employee_id) is None:
                raise DataNotFoundException("nothing to show")
            else:
                return skills.get(employee_id)
        else:
            raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")


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
    employee.create_employee(next(ids), name, mail, role, mobile, salary)


def add_leave():
    """

    :return:
    """
    leave = LeaveRecord()
    employee_id, from_date, to_date, leave_type, leave_purpose = 'a', '12/12/2001', '12/12/2001', 'a', 'a'
    isContinue = True
    while isContinue:
        employee_id = input("Enter employee id : ")
        if employee_id not in employees.keys():
            logger.error(f"Couldn't find employee by id {employee_id}")
            raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")
        else:
            break
    while isContinue:
        try:
            from_date = datetime.strptime(input("Enter date for leave from :"),
                                          "%m/%d/%Y" or "%Y/%m/%d" or "%Y/%d/%m" or "%d/%m/%Y").date()
            break
        except ValueError:
            logger.warning("Please enter valid date")
            print("Please enter valid date")
    while isContinue:
        try:
            to_date = datetime.strptime(input("Enter date for to from :"),
                                        "%m/%d/%Y" or "%Y/%m/%d" or "%Y/%d/%m" or "%d/%m/%Y").date()
            break
        except ValueError:
            logger.warning("Please enter valid date")
            print("Please enter valid date")
    while isContinue:
        leave_type = input("Enter leave type : ")
        if leave_type not in leave_types:
            print("Enter valid leave type")
        else:
            break
    leave_purpose = input("Tell reason for your leave : ")
    leave.take_leave(employee_id, from_date, to_date, leave_type, leave_purpose)


def view_leave_record():
    """

    :return:
    """
    view_leave = input("Enter employee id : ")
    if view_leave in employees:
        return leave_record.get(view_leave)


def update_employee():
    """

    :return:
    """
    print("1. email\n"
          "2. role\n"
          "3. mobile")
    update = int(input("Choose one option : "))
    employee = Employee.get_employee()
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
                print(Employee.get_employee().__dict__)
            case 3:
                print(update_employee().__dict__)
            case 4:
                employee_id = input("Enter employee Id : ")
                employee = employees.get(employee_id)
                if employee is None:
                    logger.error(f"Couldn't find employee by id {employee_id}")
                    raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")
                else:
                    employee.is_active = True
            case 5:
                Employee.create_csv(input("Enter file Directory : "))
            case 6:
                employee_list = Employee.get_all().values()
                for value in employee_list:
                    if value.is_active is False:
                        print(value.__dict__)
            case 7:
                break
            case _:
                print("you entered wrong choice")


def user_action():
    """

    :return:
    """
    is_continue = True
    while is_continue:
        print("1. Leave Record\n"
              "2. Skill \n"
              "3. Exit")
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
                skill_action()
            case 3:
                break
            case _:
                print("you entered wrong choice")


def leave_action():
    """

    :return:
    """
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
                print(view_leave_record().__dict__)
            case 3:
                break
            case _:
                print("you entered wrong choice")


def skill_action():
    """

    :return:
    """
    is_continue = True
    while is_continue:
        print("1. add skill\n"
              "2. view skills\n"
              "3. Exit")
        choice = 0
        try:
            choice = int(input("Enter choice  : "))
        except ValueError:
            logger.error("enter correct choice")
            print("enter correct choice")
        match choice:
            case 1:
                skill = Skills()
                employee_id = input("Enter Your employee id : ")
                if employee_id not in employees:
                    logger.error("employee Id not found")
                    raise DataNotFoundException("employee Id not found")
                technology = input("Enter skill to be add : ")
                version = input("Enter version of the technology : ")
                experience = input("Enter experience in month in technology : ")
                skill.add_skills(employee_id, technology, version, experience)
            case 2:
                for s in Skills.get_skills():
                    print(s.__dict__)
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
