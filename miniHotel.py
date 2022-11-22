dishes = {}
customer = []
food_list = {}


def generate():
    for i in range(100000):
        result = "I2I" + str(i)
        yield result


def add_dish():
    global food_list
    choice = input("If want to add yes/no")
    while choice == "yes":
        cuisine = input("Enter cuisine name")
        food_name = input("Enter fod name")
        amount = int(input("Enter amount"))
        dishes.__setitem__(cuisine, {food_name: amount})
    food_list = ({food: amount} for food, amount in (dish_list for dish_list in dishes.values()))


def view_dish():
    print({cuisine: dish for cuisine, dish in dishes.items()})
    print("1. Indian food")
    print("2. English food")
    print("3. Chinees food")
    view = int(input("Enter choice"))
    while view == 1 or 2 or 3:
        if view == 1:
            print({cuisine: dish for cuisine, dish in dishes.items()
                   if cuisine == "Indian"})
        elif view == 2:
            print({cuisine: dish for cuisine, dish in dishes.items()
                   if cuisine == "English"})
        elif view == 3:
            print({cuisine: dish for cuisine, dish in dishes.items()
                   if cuisine == "Chinees"})
        else:
            break


def bill_amount():
    print("Enter name of dishes had you eaten with count")
    bill = {}
    customer.append(ids.__next__())
    while True:
        next_item = input("next item yes/no")
        if next_item == "yes":
            name = input("Name")
            count = int(input("count"))
            bill.__setitem__(name, count)
        else:
            break
        for food_name in bill.keys():
            total = sum(
                amount for food_name, amount in filter(lambda food: food_name == food_list.get(food), food_list))
            print({ids.__next__(): total})


ids = generate()
isContinue = input("yes/no")
while isContinue == "yes":
    print("***********Welcome*********")
    print("1. Add dish")
    print("2. view dish")
    print("3. dish bill")
    print("*********Thank you*********")
    option = int(input())
    if option == 1:
        add_dish()
    elif option == 2:
        view_dish()
    elif option == 3:
        bill_amount()
    else:
        "thank you"
