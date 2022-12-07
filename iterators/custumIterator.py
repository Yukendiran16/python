class TopValues:
    def __init__(self):
        self.N = '*'

    def __iter__(self):
        return self

    def __next__(self):
        VALUE = self.N
        self.N += '*'
        return VALUE


custom_numbers = TopValues()
for i, j in enumerate(custom_numbers):
    if i <= 10:
        print(j)



