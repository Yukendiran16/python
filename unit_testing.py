import unittest
from exception_handling import Employee
from exception_handling import generate


class Test(unittest.TestCase):
    employee = Employee()

    # def test_0_set_employee_id(self):
    #     employee_id = generate
    #     self.assertIn("I2I", employee_id)
    #     self.employee.employee_id = employee_id
    #
    # def test_1_get_employee_id(self):
    #     self.assertIsNotNone(self.employee.get_employee_id)
    #     return self.employee_id

    # def test_set_name(self, name):
    #     self.name = name
    #
    # def test_get_name(self):
    #     return self.name

    def test_0_set_salary(self):
        salary = int(input("Enter employee salary : "))
        self.assertGreaterEqual(10000000, self.employee.set_salary(salary))

    def test_1_get_salary(self):
        self.assertIsNotNone(self.employee.get_salary())
        print(self.employee.salary)

    def test_2_set_email(self):
        email = input("Enter mail id : ")
        self.assertRaises(Exception, self.employee.set_email(email))

    def test_3_get_email(self):
        self.assertIsNotNone(self.employee.get_email())
        print(self.employee.email)

    def test_4_set_role(self):
        role = input("Enter Role : ")
        self.assertEqual(role, self.employee.set_role(role))

    def test_5_get_role(self):
        self.assertIsNotNone(self.employee.get_role())
        print(self.employee.role)

    def test_set_mobile(self):
        mobile = input("Enter mail id : ")
        self.assertRaises(Exception, self.employee.set_mobile(mobile))

    def test_get_mobile(self):
        self.assertIsNotNone(self.employee.get_mobile())
        print(self.employee.mobile)


if __name__ == '__main__':
    unittest.main()
