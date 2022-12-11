import csv
import re
from csv import writer

logs = open("F:/py/log.txt")     # this is the log file


def get_warning():
    """
    This is the method used to get warning from log file and
    put them into a csv file in the format of TimeStamp,
    Application Name, Status, Description, Code.
    :return: csv file
    """
    with open('F:/py/warning.csv', "r+") as warning:
        file = csv.writer(warning)
        header = ("Timestamp", "Application Name", "Status", "Description", "Code")
        file.writerow(header)
        for log in logs:
            if "Warning" in log:
                warn = re.split(',|: |    ', log)
                warning_log = (warn[0], warn[5], "Warning", warn[7].replace("\n", ""), "code")
                file.writerow(warning_log)
        read_file = csv.reader(warning)
        for i in read_file:
            print(i)


def get_failure():
    """
    This is the method used to get failures from log file and
    put them into a csv file in the format of TimeStamp,
    Application Name, Status, Description, Code.
    :return: csv file
    """
    with open('F:/py/failed.csv', "r+") as failed:
        file = csv.writer(failed)
        header = ("Timestamp", "Application Name", "Status", "Description", "Code")
        file.writerow(header)
        for log in logs:
            if "Failed" in log:
                fail = re.split(',|    ', log)
                failed_log = (fail[0], fail[5], "Failed", fail[6].replace("\n", ""), "code")
                file.writerow(failed_log)
        read_file = csv.reader(failed)
        for i in read_file:
            print(i)


print("1. warning logs")
print("2. failed logs")
choice = int(input("Enter choice"))
match choice:
    case 1:
        get_warning()
    case 2:
        get_failure()
    case _:
        print("bye.....")