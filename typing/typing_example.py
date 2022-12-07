from typing import Dict
from typing import NewType
from typing import Any
import re


def print_list(a: list) -> None:
    print(a)


print_list([1, 2, 3])
print_list(1)

# Create a new user type called 'StudentID'
StudentID = NewType('StudentID', int)


def get_student_name(stud_id: StudentID) -> str:
    return str(input(f'Enter username for ID #{stud_id}:\n'))


stud_a = get_student_name(StudentID(100))
print(stud_a)

# This is incorrect!!
stud_b = get_student_name(-1)
print(stud_b)

# Create an alias called 'ContactDict'
ContactDict = Dict[str, str]


def check_if_valid(contacts: ContactDict) -> bool:
    for name, email in contacts.items():
        # Check if name and email are strings
        if (not isinstance(name, str)) or (not isinstance(email, str)):
            return False
        # Check for email xxx@yyy.zzz
        if not re.match(r"[a-zA-Z0-9\._\+-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$", email):
            return False
    return True


print(check_if_valid({'vijay': 'vijay@sample.com'}))
print(check_if_valid({'vijay': 'vijay@sample.com', 123: 'wrong@name.com'}))
