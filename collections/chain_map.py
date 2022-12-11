from collections import ChainMap

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
print(alpha_nums.maps)

dad = {"name": "John", "age": 35}
mom = {"name": "Jane", "age": 31}
family = ChainMap(mom, dad)
print(family)

son = {"name": "Mike", "age": 0}
family = family.new_child(son)

for person in family.maps:
    print(person)

print(family.parents)

numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
print(alpha_nums)

# Add a new key-value pair
alpha_nums["c"] = "C"
print(alpha_nums)

# Pop a key that exists in the first dictionary
alpha_nums.pop("two")
print(alpha_nums)

# Clear the dictionary
alpha_nums.clear()
print(alpha_nums)


class DeepChainMap(ChainMap):
    'Variant of ChainMap that allows direct updates to inner scopes'

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)


d = DeepChainMap({'zebra': 'black'}, {'elephant': 'blue'}, {'lion': 'yellow'})
d['lion'] = 'orange'  # update an existing key two levels down
d['snake'] = 'red'  # new keys get added to the topmost dict
del d['elephant']  # remove an existing key one level down
print(d)  # display result
