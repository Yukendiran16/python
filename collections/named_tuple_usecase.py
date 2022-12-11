import csv
from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'employee_id, name, role, mobile')
file = csv.reader(open("F:/py/employee.csv", "r"))
for emp in map(EmployeeRecord._make, file):
    print(emp)
