from collections import UserList


class MyUser(UserList):

    def pop(self, s=None):
        print("couldn't delete an item in the list")

    def append(self, item: tuple) -> None:
        print("couldn't append item into list because it size is fixed")


my_user = MyUser([('Sales', 'John Doe'),
                  ('Sales', 'Martin Smith'),
                  ('Accounting', 'Jane Doe'),
                  ('Marketing', 'Elizabeth Smith'),
                  ('Marketing', 'Elizabeth Smith'),
                  ('Marketing', 'Adam Doe'),
                  ('Marketing', 'Adam Doe'),
                  ('Marketing', 'Adam Doe')
                  ])
my_user.pop()
my_user.append(("wer", "wee"))
print(my_user)
