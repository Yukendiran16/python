# Python code to demonstrate dictionary
# creation using list comprehension
myDict = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print(myDict)

# Python code to demonstrate dictionary
# comprehension
# Lists to represent keys and values
keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]
# but this line shows dict comprehension here
myDict = {k: v for (k, v) in zip(keys, values)}
# myDict = dict(zip(keys, values))
print(myDict)

# Python code to demonstrate dictionary
# comprehension using if.
new_dict = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print(new_dict)

# names of cricket players list
players = ["K L Rahul", "Rohit", "Virat", "Surya", "Rishab", "Harthik", "Ashwin", "Jadeja", "Bhuvi", "Shami",
           "Arshdeep"]
# runs with individual players vs west indies
runs_wi = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
# runs with individual players vs south africa
runs_sa = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
# runs with individual players vs sri lanka
runs_sl = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
print({player: runs for player, runs in zip(players, runs_wi)})
print({player: runs for player, runs in zip((player for player in players),
                                            (y + z + w for y, z, w in zip(runs_sa, runs_wi, runs_sl)))})
print([y + z + w for y, z, w in zip(runs_sa, runs_wi, runs_sl)])
print({1: "hii", True: "hello"})

for i in zip(runs_sa, runs_wi, runs_sl):
    print(i)

multiples = {key1: {key2: key1 ** key2 for key2 in range(1, 10)} for key1 in range(1, 10)}
for i in multiples:
    print("key = " + str(i) + " " + str(multiples.get(i)))

