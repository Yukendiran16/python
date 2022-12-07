import os
from datetime import datetime
import glob

old_name = r"E:\demos\files\reports\details.txt"
new_name = r"E:\demos\files\reports\new_details.txt"

if os.path.isfile(new_name):
    print("The file already exists")
else:
    # Rename the file
    os.rename(old_name, new_name)


old_name = r"E:\demos\files\reports\details.txt"
new_name = r"E:\demos\files\reports\new_details.txt"

# enclosing inside try-except
try:
    os.rename(old_name, new_name)
except FileExistsError:
    print("File already Exists")
    print("Removing existing file")
    # skip the below code
    # if you don't' want to forcefully rename
    os.remove(new_name)
    # rename it
    os.rename(old_name, new_name)
    print('Done renaming a file')


folder = r'E:\demos\files\reports\\'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder + "sales_" + str(count) + ".txt"

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)


files_to_rename = ['sales_1.txt', 'sales_4.txt']
folder = r"E:\demos\files\reports\\"

# Iterate through the folder
for file in os.listdir(folder):
    # Checking if the file is present in the list
    if file in files_to_rename:
        # construct current name using file name and path
        old_name = os.path.join(folder, file)
        # get file name without extension
        only_name = os.path.splitext(file)[0]

        # Adding the new name with extension
        new_base = only_name + '_new' + '.txt'
        # construct full file path
        new_name = os.path.join(folder, new_base)

        # Renaming the file
        os.rename(old_name, new_name)

# verify the result
res = os.listdir(folder)
print(res)

# adding date-time to the file name
current_timestamp = datetime.today().strftime('%d-%b-%Y')
old_name = r"E:\demos\files\reports\sales.txt"
new_name = r"E:\demos\files\reports\sales" + current_timestamp + ".txt"
os.rename(old_name, new_name)


path = r"E:\demos\files\reports\\"
# search text files starting with the word "sales"
pattern = path + "sales" + "*.txt"

# List of the files that match the pattern
result = glob.glob(pattern)

# Iterating the list with the count
count = 1
for file_name in result:
    old_name = file_name
    new_name = path + 'revenue_' + str(count) + ".txt"
    os.rename(old_name, new_name)
    count = count + 1

# printing all revenue txt files
res = glob.glob(path + "revenue" + "*.txt")
for name in res:
    print(name)

folder = "/Users/sample/eclipse-workspace/Sample/Files/Images/"
for count, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename
    newname = folder + "Emp_" + str(count + 1) + ".jpg"
    os.rename(oldname, newname)

# printing the changed names
print(glob.glob(folder + "*.*"))


# Old and new folder locations
old_folder = r"E:\demos\files\reports\\"
new_folder = r"E:\demos\files\new_reports\\"

# Old and new file names
old_name = old_folder + "expense.txt"
new_name = new_folder + "expense.txt"

# Moving the file to the another location

os.rename(old_name, new_name)


folder = "/Users/sample/eclipse-workspace/Sample/Files/Images/"
for count, filename in enumerate(os.listdir(folder)):
    oldname = folder + filename
    newname = folder + "Emp_" + str(count + 1) + ".jpg"
    os.rename(oldname, newname)

# printing the changed names
print(glob.glob(folder + "*.*"))
