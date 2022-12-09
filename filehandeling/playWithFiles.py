import os
from pathlib import Path
from datetime import datetime


def file_list_way_one(base_path):
    print("\n all folders and files in specified directory\n")
    print(" " + str(os.listdir(base_path)))


def file_list_way_two(base_path):
    # list of folders and files in the specified directory
    print("\n list of folders and files in specified directory\n")
    for i in os.listdir(base_path):
        print(" " + i)


def file_list_way_three(base_path):
    with os.scandir(base_path) as entries:
        print("\n file list object" + str(entries) + "\n")
        for entry in entries:
            print(" " + entry.name)


def file_list_way_four(base_path):
    path = Path(base_path)
    for count, entry in enumerate(path.iterdir(), 1):
        print(" " + entry.name, count)


def file_list_way_five(base_path):
    for count, entry in enumerate(os.listdir(base_path), 1):
        if os.path.isfile(os.path.join(base_path, entry)):
            print(" " + entry, count)


def file_list_way_six(base_path):
    with os.scandir(base_path) as entries:
        for entry in entries:
            if entry.is_file():
                print(entry.name)


def file_list_way_seven(base_path):
    files_in_base_path = base_path.iterdir()
    for item in files_in_base_path:
        if item.is_file():
            print(item.name)


def file_list_way_eight(base_path):
    for entry in os.listdir(base_path):
        if os.path.isdir(os.path.join(base_path, entry)):
            print(entry)


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formatted_date = d.strftime('%d %b %Y')
    return formatted_date


def time_stamp():
    with os.scandir(base_path) as dir_contents:
        for entry in dir_contents:
            if entry.is_dir():
                info = entry.stat()
                print(f'{entry.name}\t {convert_date(info.st_mtime)}')


file_list_way_one(r"C:/Users/lenovo/Documents/")
file_list_way_two(r"C:/Users/lenovo/Documents/")
file_list_way_three(r"C:/Users/lenovo/Documents/")
file_list_way_four(r"C:/Users/lenovo/Documents/")
file_list_way_five(r"C:/Users/lenovo/Documents/")
file_list_way_six(r"C:/Users/lenovo/Documents/")
file_list_way_seven(r"C:/Users/lenovo/Documents/")
file_list_way_eight(r"C:/Users/lenovo/Documents/")
time_stamp()


