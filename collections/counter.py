from collections import Counter


def count_sequence(word):
    """
    This function count the sequence of characters
    :param word: String
    :return: dictionary {char: count}
    """
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter


def count_sequence_with_counter(word):
    """
    This function count the sequence of characters
    :param word: String
    :return: dictionary {char: count}
    """
    return Counter(word).most_common(3)


def counter_operations():
    letters = Counter("mississippi")
    print("Before changes : ", letters)

    # Update the counts of m and i
    letters.update(m=3, i=4)
    print("\'m\' and \'i\' count increased by 3 and 4", letters)

    # Add a new key-count pair
    letters.update({"a": 2})
    print("\'a\' letter count increased by 2", letters)

    # Update with another counter
    letters.update(Counter(["s", "s", "p"]))
    print("added characters :", letters.elements())


def counter_with_math():
    inventory = Counter(dogs=23, cats=14, pythons=7)
    print("before changes :                             ", inventory)

    adopted = Counter(dogs=2, cats=5, pythons=1)
    inventory.subtract(adopted)
    print("After subtracted dogs=2, cats=5, pythons=1   ", inventory)

    new_pets = {"dogs": 4, "cats": 1}
    inventory.update(new_pets)
    print("After added dogs: 4, cats: 1                 ", inventory)

    inventory = inventory - Counter(dogs=2, cats=3, pythons=1)
    print("After subtracted dogs=2, cats=3, pythons=1   ", inventory)

    new_pets = {"dogs": 4, "pythons": 2}
    inventory += new_pets
    print("After added dogs: 4, cats: 2                 ", inventory)


print(count_sequence("ehfertuiopocjhdlefhr"))
print(count_sequence_with_counter("ehfertuiopocjhdlefhr"))
counter_operations()
counter_with_math()
