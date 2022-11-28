a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)
a.extend(b)
print(a)

sample_dict_x = {1: "name", 2: "age", 3: "place"}
sample_dict_y = {4: "DOB"}
print(sample_dict_x.keys())
print(sample_dict_y.values())
for i, j in sample_dict_y.items():
    sample_dict_x.__setitem__(i, j)
print(sample_dict_x)
print(sample_dict_x.get(2))
for i, j in sample_dict_x.items():
    if j == "age":
        print(sample_dict_x.get(i))
print({x: y for x, y in zip(a, b)})

x = "something is better than nothing"
counter_dict = {}
for i in x:
    if i != " ":
        if i in counter_dict:
            counter_dict[i] += 1
        else:
            counter_dict.__setitem__(i, 1)
print(counter_dict)


def generate_numbers():
    for number in range(100):
        yield number


# numbers = generate_numbers()
numbers = (1, 30, 49, 10, 30, 54, 60)
print(list(filter(lambda x: x % 10 == 0, numbers)))

sample_list = list(map(lambda x: x % 2 == 0, range(10)))
print("odd = ", sample_list.count(False))
print("even = ", sample_list.count(True))
