from management.utils.logger_util import logger


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
