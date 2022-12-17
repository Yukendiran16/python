import unittest
from exception_handling import Employee
from exception_handling import employees
from exception_handling import calculate_salary
from custom_exception import PatternError


class Test(unittest.TestCase):
    employee = Employee()

    def test_0_set_salary(self):
        self.assertLessEqual(10000000, self.employee.set_salary(1234567890))
        self.assertGreaterEqual(10000000, self.employee.set_salary(123456))

    def test_1_get_salary(self):
        self.assertIsNotNone(self.employee.get_salary())
        print(self.employee.salary)

    def test_2_set_email(self):
        self.assertRaises(PatternError, self.employee.set_email('jhgfrty7wygs'))
        self.assertEqual('yuki@ideas2it.com', self.employee.set_email('yuki@ideas2it.com'))

    def test_3_get_email(self):
        self.assertIsNotNone(self.employee.get_email())
        print(self.employee.email)

    def test_4_set_role(self):
        self.assertEqual('SDE', self.employee.set_role('SDE'))
        self.assertNotEqual('SDE', self.employee.set_role('seke'))

    def test_5_get_role(self):
        self.assertIsNotNone(self.employee.get_role())
        print(self.employee.role)

    def test_6_set_mobile(self):
        self.assertRaises(PatternError, self.employee.set_mobile('4323456'))
        self.assertEqual('+919876543210', self.employee.set_mobile('+919876543210'))

    def test_7_get_mobile(self):
        self.assertIsNotNone(self.employee.get_mobile())
        print(self.employee.mobile)

    def test_8___init__(self):
        emp = Employee('yuki', 'yuki@ideas2it.com', 4567, '9876543210', 234567.00)
        self.assertIs(emp, employees.get("I2I1"))
        self.assertNotEqual(emp, employees.get("I2I0"))

    def test_9_calculate_salary(self):
        self.assertEqual(9075.0, calculate_salary(10000))
        self.assertNotEqual(10000, calculate_salary(10000))


if __name__ == '__main__':
    unittest.main()
