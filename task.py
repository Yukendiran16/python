employee_list = []
property_ = ['ids', 'name', 'age']
ids = [1, 2, 3, 4, 5]
name = ["a", "b", "c", "d", "e"]
age = [25, 22, 34, 45, 45]
for i in zip(ids, name, age):
    dict_sample = {}
    for j in zip(property_, i):
        dict_sample.__setitem__(j[0], j[1])
    employee_list.append(dict_sample)
print(employee_list)