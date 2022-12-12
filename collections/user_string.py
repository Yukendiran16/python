from collections import UserString
import re


class FunnyString(UserString):

    def __init__(self, seq):
        super().__init__(seq)
        self.data = seq

    # def fun(self):
    #     funny = ""
    #     for idx in range(len(self.data)):
    #         if not idx % 2:
    #             funny += self.data[idx].upper()
    #         else:
    #             funny += self.data[idx].lower()
    #
    #     print(funny)


text = FunnyString('Hello! Welcome to My World!')
print(text)
