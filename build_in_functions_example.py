list_x = ["eat", "sleep", "repeat"]
seq = [0, 1, 2, 3, 5, 8, 13]
players = ["KL Rahul", "Rohit", "Virat", "Surya", "Rishab", "Harthik", "Ashwin", "Jadeja", "Bhuvi", "Shami", "Arshdeep"]
runs_australia = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
runs_west_indies = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
runs_south_africa = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]
runs_sri_lanka = [28, 13, 50, 32, 53, 0, 0, 0, 0, 0, 0]


# Python program to illustrate
# enumerate function
def enumeration():
    print("\nEnumerate function used for count the iterable\n")
    print(list(enumerate(list_x)))
    print(list(enumerate(list_x, 100)))


def do_filter():
    print("\nFilter function used to filter datas in collection")
    # result contains odd numbers of the list
    print(list(filter(lambda x: x % 2 != 0, seq)))
    # result contains even numbers of the list
    print(list(map(lambda a: a * a, filter(lambda x: x % 2 == 0, seq))))


def do_zip():
    print("\nZip function used to map datas in collection")
    dict_x = dict(zip(players, runs_australia))
    print(dict_x)
    print(dict(filter(lambda player: player[1] >= 50, dict_x.items())))


def do_map():
    print("\nMap function used to map datas in collection")
    # Add two lists using map and lambda
    print(list(map(lambda player, x: {player: sum(x)}, players,
                   zip(runs_australia, runs_west_indies, runs_south_africa, runs_sri_lanka))))
    result = list(filter(lambda score: [y for x, y in score.items()] >= [50],
                         map(lambda player, x: {player: sum(x)}, players,
                             zip(runs_australia, runs_west_indies, runs_south_africa, runs_sri_lanka))))
    print(list(filter(lambda score: [y for x, y in score.items()] >= [50], result)))


print("1. Goto enumeration")
print("2. Goto filter")
print("3. Goto zip")
print("4. Goto map")
choice = int(input("Enter one choice"))
isContinue = True
while isContinue:
    match choice:
        case 1:
            enumeration()
        case 2:
            do_filter()
        case 3:
            do_zip()
        case 4:
            do_map()
        case _:
            print("wrong input")
            break
