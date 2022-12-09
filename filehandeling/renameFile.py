import os
from datetime import datetime
import glob


def rename_file(old, new):
    """
    This method used to rename the file name without
    changing file and file directory
    :var old file name, new file name
    :return if the file is exists throw a message else nothing to pass

    """

    directory = r"C:/Users/lenovo/Documents/"

    if os.path.isfile(directory + new):
        print("The file already exists")
    else:
        # Rename the file
        os.rename(directory + old, directory + new)


def change_folder_and_rename_file(old, new):
    """
    This method used to rename the file name without
    changing file and also change file directory
    :var old folder name, new folder name
    :return if the file is exists throw a message else nothing to pass

    """

    directory = r"C:/Users/lenovo/"

    if os.path.isfile(directory + new):
        print("The file already exists")
    else:
        # Rename the file
        os.rename(directory + old, directory + new)


def rename_multiple_files(old, new):
    """
    This method used to rename the multiple files name without
    changing file and also change file directory
    :var folder name, new file name
    :return if the file is exists throw a message else nothing to pass

    """

    folder = r"C:/Users/lenovo/Documents/" + old + "/"
    # count increase by 1 in each iteration
    # iterate all files from a directory
    for value, file_name in enumerate(os.listdir(folder)):
        # Construct old file name
        source = folder + file_name

        # Adding the count to the new file name and extension
        destination = folder + new + "day" + str(value) + ".txt"

        # Renaming the file
        os.rename(source, destination)
    print('All Files Renamed')
    print('New Names are')
    # verify the result
    res = os.listdir(folder)
    print(res)


print("1. rename file")
print("2. Change folder")
print("3. Change folder and change name")
print("4. rename multiple files on time")
choice = int(input("Enter one choice"))
match choice:
    case 1:
        old_name = input("Enter your old file name : ")
        new_name = input("Enter your new file name : ")
        rename_file(old_name, new_name)
    case 2:
        old_name = input("Enter your file name with old folder name : ")
        new_name = input("Enter your file name with new folder name : ")
        change_folder_and_rename_file(old_name, new_name)
    case 3:
        old_name = input("Enter your old file name with old folder name : ")
        new_name = input("Enter your new file name with new folder name : ")
        change_folder_and_rename_file(old_name, new_name)
    case 4:
        old_name = input("Enter your folder name : ")
        new_name = input("Enter your new file name : ")
        rename_multiple_files(old_name, new_name)
    case _:
        print("you entered incorrect choice")


