tags = {'Django', 'Pandas', 'Numpy'}
print({tag.lower() for tag in tags if tag != 'Numpy'})
print(set(map(lambda tag: tag.lower(), tags)))

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print({element ** 2 for element in mySet})
print({element for element in mySet if element % 2 == 0})
