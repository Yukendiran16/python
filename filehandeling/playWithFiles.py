import os
from pathlib import Path
from datetime import datetime


# print("\n all folders and files in specified directory\n")
# print(" " + str(os.listdir("C:/Users/lenovo/Documents/")))    # list of folders and files in the specified directory
# print("\n list of folders and files in specified directory\n")
# for i in os.listdir("C:/Users/lenovo/Documents/"):
#     print(" " + i)
#
# with os.scandir('C:/Users/lenovo/Documents/') as entries:
#     print("\n file list object" + str(entries) + "\n")
#     for entry in entries:
#         print(" " + entry.name)

# entries = Path('C:/Users/lenovo/Documents/')
# for count, entry in enumerate(entries.iterdir(), 1):
#     print(" " + entry.name, count)
#
# # List all files in a directory using os.listdir
base_path = 'C:/Users/lenovo/Documents/'


# for count, entry in enumerate(os.listdir(base_path), 1):
#     if os.path.isfile(os.path.join(base_path, entry)):
#         print(" " + entry, count)
#
# with os.scandir(base_path) as entries:
#     for entry in entries:
#         if entry.is_file():
#             print(entry.name)
#
# files_in_base_path = basepath.iterdir()
# for item in files_in_base_path:
#     if item.is_file():
#         print(item.name)

# for entry in os.listdir(base_path):
#     if os.path.isdir(os.path.join(base_path, entry)):
#         print(entry)

# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formatted_date = d.strftime('%d %b %Y')
#     return formatted_date
#
#
# with os.scandir(base_path) as dir_contents:
#     for entry in dir_contents:
#         if entry.is_dir():
#             info = entry.stat()
#             print(f'{entry.name}\t {convert_date(info.st_mtime)}')
#