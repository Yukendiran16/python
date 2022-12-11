from collections import UserString
import re


class FunnyString(UserString):

    def __init__(self, sequence, seq):
        super().__init__(seq)
        self.data = re.sub(r'[^\w\s]', '', sequence)

    # def fun(self):
    #     funny = ""
    #     for idx in range(len(self.data)):
    #         if not idx % 2:
    #             funny += self.data[idx].upper()
    #         else:
    #             funny += self.data[idx].lower()
    #
    #     print(funny)


text = FunnyString('Hello! Welcome to My World!', 'a')
print(text)