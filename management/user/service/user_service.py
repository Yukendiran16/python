from collections import defaultdict
from datetime import date
from datetime import datetime

from management.exception_handler.custom_exception import DataNotFoundException
from management.admin.service.employee_service import employees
from management.user.models.leave import LeaveRecord
from management.utils.logger_util import logger

leave_record = {}
leaves = defaultdict(list)
skills = defaultdict(list)
leave_types = ['Casual Leave']


def add_skills(skill, employee_id, technology, version, experience):
    """

    :param skill:
    :param employee_id:
    :param technology:
    :param version:
    :param experience:
    :return:
    """

    skill.technology = technology
    skill.version = version
    skill.experience = experience
    skills[employee_id].append(skill)


def view_leave_record():
    """

    :return:
    """
    view_leave = input("Enter employee id : ")
    if view_leave in employees:
        return leave_record.get(view_leave)


def get_skills():
    employee_id = input("Enter your employee Id :")
    if employee_id in skills:
        if skills.get(employee_id) is None:
            raise DataNotFoundException("nothing to show")
        else:
            return skills.get(employee_id)
    else:
        raise DataNotFoundException(f"Couldn't find employee by id {employee_id}")


def take_record(leave, from_date, to_date, leave_type, leave_purpose):
    """

    :param leave:
    :param from_date:
    :param to_date:
    :param leave_type:
    :param leave_purpose:
    :return:
    """
    for day in range(from_date.day, to_date.day):
        new_date = datetime.now().replace(day=day, month=from_date.month, year=from_date.year)
        leaves[leave.employee_id].append({new_date: {'leave type': leave_type, 'leave_purpose': leave_purpose}})
    leave.leave_dates = leaves[leave.employee_id]
    leave.leave_taken += len(leaves.get(leave.employee_id))
    leave.leave_avail -= len(leaves.get(leave.employee_id))
    leave_record[leave.employee_id] = leave


def take_leave(leave, employee_id: str = "I2I", from_date: date = 12 / 12 / 2001,
               to_date: date = 12 / 12 / 2001,
               leave_type: str = "", leave_purpose: str = "") -> None:
    """
    this the method to create leave record for an employee
    :param leave:
    :param employee_id:
    :param from_date:
    :param to_date:
    :param leave_type:
    :param leave_purpose:
    :return: nothing
    """
    leave.employee_id = employee_id
    take_record(leave, from_date, to_date, leave_type, leave_purpose)


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
    take_leave(leave, employee_id, from_date, to_date, leave_type, leave_purpose)
