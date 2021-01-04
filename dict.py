class Dictionary:

    def __init__(self, string, res_dict):
        self.string = string
        self.res_dict = res_dict

    def create_dict(self):
        for letter in self.string:
            if letter.isalpha():
                self.res_dict.setdefault(letter, self.string.count(letter))
        return self.res_dict

    def remove_duplicate_values(self):
        dic = {}
        value_list = list((self.create_dict().values()))
        for key, value in self.create_dict().items():
            if value_list.count(value) == 1:
                dic.setdefault(key, value)
        return dic

    def highest_three_values(self):
        lst = sorted(self.create_dict().values(), reverse=True)
        return lst[0], lst[1], lst[2]

    def highest_three_values2(self):
        curr_lst = list(set(list(self.create_dict().values())))
        curr_lst.sort(reverse=True)
        if len(curr_lst) > 3:
            return curr_lst[0], curr_lst[1], curr_lst[2]
        else:
            return "The dictionary haven't three highest values"


d = Dictionary("potatoes!", {})
print(f"Dictionary from string '{d.string}': ", d.create_dict())
print("Dictionary after removing duplicate values: ", d.remove_duplicate_values())
print("Highest three values in dictionary: ", d.highest_three_values())
