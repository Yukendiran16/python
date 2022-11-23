dishes = {}
customer = []
food_list = {}
isContinue = True


def generate():
    for i in range(100000):
        result = "I2I" + str(i)
        yield result


def add_dish():
    global food_list
    while isContinue:
        choice = input("If want to add yes/no")
        if choice == "yes":
            cuisine = input("Enter cuisine name")
            food_name = input("Enter fod name")
            amount = int(input("Enter amount"))
            dishes.__setitem__(cuisine, {food_name: amount})
            food_list = (dish_list for dish_list in dishes.values())
            print(list(food_list))
        else:
            break


def view_dish():
    print({cuisine: dish for cuisine, dish in dishes.items()})
    print("1. Indian food")
    print("2. English food")
    print("3. Chinees food")
    print("4. Exit")
    while isContinue:
        view = int(input("Enter choice"))
        if view == 1:
            print({cuisine: dish for cuisine, dish in dishes.items()
                   if cuisine == "Indian"})
        elif view == 2:
            print({cuisine: dish for cuisine, dish in dishes.items()
                   if cuisine == "English"})
        elif view == 3:
            print({cuisine: dish for cuisine, dish in dishes.items()
                   if cuisine == "Chinees"})
        elif view == 4:
            break
        else:
            print("Wrong input")


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
            total = sum(amount for food_name, amount in
                        filter(lambda food: food_name == food_list.get(food), food_list))
            print({ids.__next__(): total})


ids = generate()
while isContinue:
    print("***********Welcome*********")
    print("1. Add dish")
    print("2. view dish")
    print("3. dish bill")
    print("4. Exit")
    print("*********Thank you*********")
    option = int(input("Enter one choice"))
    if option == 1:
        add_dish()
    elif option == 2:
        view_dish()
    elif option == 3:
        bill_amount()
    elif option == 4:
        print("thank you")
        break
    else:
        print("Wrong input")
