import re

from management.utils.logger_util import logger
from management.utils.employee_util import calculate_salary
from management.exception_handler.custom_exception import PatternError

role_list = ['Software Developer', 'Quality Analyst', 'Manager', 'Human Resource']


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
        self.__is_active = False
        logger.info("Employee object initialized")

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

    def set_is_active(self):
        """
        setter method of an employee role
        :return: nothing
        """
        self.__is_active = True

    def get_is_active(self):
        """
        getter method of an employee mobile
        :return: employee mobile
        """
        return self.__is_active
