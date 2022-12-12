from collections import defaultdict

departments = [('Sales', 'John Doe'),
               ('Sales', 'Martin Smith'),
               ('Accounting', 'Jane Doe'),
               ('Marketing', 'Elizabeth Smith'),
               ('Marketing', 'Elizabeth Smith'),
               ('Marketing', 'Adam Doe'),
               ('Marketing', 'Adam Doe'),
               ('Marketing', 'Adam Doe')
               ]

departments_default_dict = defaultdict(set)
for department, employee in departments:
    departments_default_dict[department].add(employee)

print(departments_default_dict)

incomes = [('Books', 1250.00),
           ('Books', 1300.00),
           ('Books', 1420.00),
           ('Tutorials', 560.00),
           ('Tutorials', 630.00),
           ('Tutorials', 750.00),
           ('Courses', 2500.00),
           ('Courses', 2430.00),
           ('Courses', 2750.00)
           ]

profit = defaultdict(float)
for product, income in incomes:
    profit[product] += income

print(profit)

for product, income in profit.items():
    print(f'Total income for {product}: ${income:,.2f}')

dep = [('Sales', 'John Doe'),
       ('Sales', 'Martin Smith'),
       ('Accounting', 'Jane Doe'),
       ('Marketing', 'Elizabeth Smith'),
       ('Marketing', 'Adam Doe')]
dd = defaultdict(int)
for department, _ in dep:
    dd[department] += 1
print(dd)
