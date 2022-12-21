from collections import UserString as US


# Here, we will create a Mutable String
class User_string(US):

    # Function to append to string
    def append(self, s):
        self.data += s

        # Function to remove from string

    def remove(self, s):
        self.data = self.data.replace(s, "")

    # Driver's code


s_1 = User_string("python")
print(s_1.count('p'))
print("The Original String: ", s_1.data)

# Here, we will Append to string
s_1.append(" programming")
print("String After Appending: ", s_1.data)

# Here, we will Remove from string
s_1.remove(" ")
print("String after Removing: ", s_1.data)

