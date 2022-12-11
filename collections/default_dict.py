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
