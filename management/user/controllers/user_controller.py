from management.admin.service.employee_service import employees
from management.exception_handler.custom_exception import DataNotFoundException
from management.user.models.skill import Skill
from management.user.service.user_service import view_leave_record, get_skills, add_skills, add_leave
from management.utils.logger_util import logger


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
        skill = Skill()
        match choice:
            case 1:
                employee_id = input("Enter Your employee id : ")
                if employee_id not in employees:
                    logger.error("employee Id not found")
                    raise DataNotFoundException("employee Id not found")
                technology = input("Enter skill to be add : ")
                version = input("Enter version of the technology : ")
                experience = input("Enter experience in month in technology : ")
                add_skills(skill, employee_id, technology, version, experience)
            case 2:
                for s in get_skills():
                    print(s.__dict__)
            case 3:
                break
            case _:
                print("you entered wrong choice")