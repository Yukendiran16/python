import csv
from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'employee_id, name, role, mobile',
                            rename=False, defaults=None, module=None)
file = csv.reader(open("employee.csv", "r"))
for i, emp in enumerate(map(EmployeeRecord._make, file)):
    if i != 0:
        print(emp)
        next(file)
    else:
        next(file)
