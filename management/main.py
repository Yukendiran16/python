from utils.logger_util import logger
from user.controllers.user_controller import user_action
from admin.controllers.employee_controller import admin_action

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