from collections import defaultdict

# favorites = {"pet": "dog", "color": "blue", "language": "Python"}
# print(favorites["fruit"])

favorites = {"pet": "dog", "color": "blue", "language": "Python"}
favorites.setdefault("fruit", "apple")
print(favorites)
# {'pet': 'dog', 'color': 'blue', 'language': 'Python', 'fruit': 'apple'}

favorites.setdefault("pet", "cat")
print(favorites)
# {'pet': 'dog', 'color': 'blue', 'language': 'Python', 'fruit': 'apple'}

favorites = {"pet": "dog", "color": "blue", "language": "Python"}
favorites.get("fruit", "apple")
print(favorites)
# {'pet': 'dog', 'color': 'blue', 'language': 'Python'}

counter = defaultdict(int)
print(counter)
print(counter["dogs"])
print(counter)

counter["dogs"] += 1
counter["dogs"] += 1
counter["dogs"] += 1
counter["cats"] += 1
counter["cats"] += 1
print(counter)

pets = [
    ("dog", "Affenpinscher"),
    ("dog", "Terrier"),
    ("dog", "Boxer"),
    ("cat", "Abyssinian"),
    ("cat", "Birman"),
]
group_pets = defaultdict(list)
for pet, breed in pets:
    group_pets[pet].append(breed)
for pet, breeds in group_pets.items():
    print(pet, "->", breeds)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))
print(dict(s))
