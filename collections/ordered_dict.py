from collections import OrderedDict

life_stages = OrderedDict()

life_stages["childhood"] = "0-9"
life_stages["adolescence"] = "9-18"
life_stages["adulthood"] = "18-65"
life_stages["old"] = "+65"

for stage, years in life_stages.items():
    print(stage, "->", years)


letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)
# OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])

# Move b to the right end
letters.move_to_end("b")
print(letters)
# OrderedDict([('d', 4), ('a', 1), ('c', 3), ('b', 2)])

# Move b to the left end
letters.move_to_end("b", last=False)
print(letters)
# OrderedDict([('b', 2), ('d', 4), ('a', 1), ('c', 3)])

# Sort letters by key
for key in sorted(letters):
    letters.move_to_end(key)


print(letters)
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])


# Regular dictionaries compare the content only
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)
letters_0 |= letters_1
print(letters_0)
print(letters_0 == letters_1)

# Ordered dictionaries compare content and order
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)

letters_2 = OrderedDict(a=1, b=2, c=3, d=4)
print(letters_0 == letters_2)