import os

file_path = r'E:\demos\files\sales_2.txt'
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print("The system cannot find the file specified")


file_path = r'E:\demos\files\sales_21.txt'
try:
    os.remove(file_path)
except:
    print("The system cannot find the file specified")
    # your code
