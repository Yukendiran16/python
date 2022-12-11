from collections import OrderedDict
import csv
from csv import DictWriter
from csv import writer


def generate():
    for i in range(100000):
        result = "I2I" + str(i)
        yield result


ids = generate()

employees = OrderedDict()


class Employee:

    def __init__(self, name="name", role="role", mobile=0):
        employee_dict = {}
        self.employee_id = next(ids)
        self.name = name
        self.role = role
        self.mobile = mobile
        employee_dict["employee_id"] = self.employee_id
        employee_dict["name"] = name
        employee_dict["role"] = role
        employee_dict["mobile"] = mobile
        employees[self.employee_id] = employee_dict

    @staticmethod
    def create_csv():
        with open('F:/py/employee.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=('employee_id', 'name', 'role', 'mobile'))
            writer.writeheader()
            for employee in employees.values():
                print(employee)
                writer.writerow(employee)


Employee("yuki", "SDE", 9087654321)
Employee("mahi", "SDE", 9087654321)
Employee("maddy", "SDE", 9087654321)
Employee("diya", "SDE", 9087654321)
Employee("dhoni", "SDE", 9087654321)
Employee.create_csv()
