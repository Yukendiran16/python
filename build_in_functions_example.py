# Python program to illustrate
# enumerate function
print("\nEnumerate function used for count the iterable\n")
list_x = ["eat", "sleep", "repeat"]
print(list(enumerate(list_x)))
tuple_x = ("eat", "sleep", "repeat")
print(list(enumerate(tuple_x, 100)))

print("\nFilter function used to filter datas in collection")
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]
# result contains odd numbers of the list
print(list(filter(lambda x: x % 2 != 0, seq)))
# result contains even numbers of the list
print(list(filter(lambda x: x % 2 == 0, seq)))

print("\nZip function used to map datas in collection")
players = ["K L Rahul", "Rohit", "Virat", "Surya", "Rishab", "Harthik", "Ashwin", "Jadeja", "Bhuvi", "Shami",
           "Arshdeep"]
runs_aus = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
dict_x = dict(zip(players, runs_aus))
print(dict_x)
print(dict(filter(lambda player: player[1] >= 50, dict_x.items())))

print("\nMap function used to map datas in collection")
# Add two lists using map and lambda
runs_wi = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
runs_sa = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
runs_sl = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
result = map(lambda player, x, y, z, w: {player: x + y + z + w}, players, runs_aus, runs_wi, runs_sa, runs_sl)
print(list(result))

