class Array:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target

    def pair_of_elements(self):
        lst = []
        length = len(self.numbers)
        for i in range(length):
            for j in range(i + 1, length):
                if self.numbers[i] + self.numbers[j] == self.target:
                    lst.append((i + 1, j + 1))
        return lst


arr = Array([30, 20, 10, 40, 50, 20, 70], 50)
for el in arr.pair_of_elements():
    print(f"indices of two numbers, whose sum equals a {arr.target}: {el[0]}, {el[1]}")
