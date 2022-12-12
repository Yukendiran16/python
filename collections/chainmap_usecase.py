from collections import OrderedDict
import csv
from csv import DictWriter
from csv import writer
from collections import ChainMap


class CompanyChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


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
        with open('employee.csv', 'r+') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=('employee_id', 'name', 'role', 'mobile', ""))
            writer.writeheader()
            for employee in employees.values():
                writer.writerow(employee)


Employee("yuki", "SDE", 9087654321)
Employee("mahi", "SDE", 9087654321)
Employee("maddy", "SDE", 9087654321)
Employee("diya", "SDE", 9087654321)
Employee("dhoni", "SDE", 9087654321)
Employee.create_csv()

empty_list = []
for employee in employees.values():
    empty_list.append(employee)
chain_map = CompanyChainMap(empty_list)
print(chain_map.maps)
