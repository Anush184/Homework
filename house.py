class House:
    def __init__(self, name, house_type, *args):
        self.house_address = name
        self.house_type = house_type
        self.rooms = args

    def __str__(self):
        return f"""<{self.house_address}> {self.house_type} has a {len(self.rooms)} rooms:
{self.rooms}"""

    def __eq__(self, other):
        return isinstance(other, House) and self.house_address == other.house_address and \
            set(self.rooms) == set(other.rooms)


class HouseHeatingSystem(House):
    def __init__(self, name, house_type, goal_temp, *args, **kwargs):
        House. __init__(self, name, house_type, *args)
        self.goal_temp = goal_temp
        self.room_temps = kwargs

    def checking_temps(self, satisfied_temp=range(15, 27)):
        norm, low, high = 0, 0, 0
        for value in self.room_temps.values():
            if value in satisfied_temp:
                norm += 1
            elif value < satisfied_temp[0]:
                low += 1
            elif value > satisfied_temp[-1]:
                high += 1
        return norm, low, high

    def satisfied_temps(self):
        if self.checking_temps() == (len(self.rooms), 0, 0) and self.goal_temp < 40:
            return f"The {self.house_type} does not need heating, " \
                   f"all your rooms have satisfactory temperatures!"
        elif self.checking_temps() == (len(self.rooms), 0, 0) and self.goal_temp >= 40:
            return f"All rooms of your {self.house_type} have satisfactory temperatures." \
                   f"You don't need to change the goal temperature."
        elif self.checking_temps()[1] > len(self.rooms) / 2 and self.goal_temp < 60:
            return "You must to raise the goal temperature."
        elif self.checking_temps()[1] > len(self.rooms) / 2 and self.goal_temp >= 60:
            return f"Your {self.house_type} have a problem with a heating system."
        elif self.checking_temps()[2] > len(self.rooms) / 2 and self.goal_temp >= 50:
            return f"You must to lowered the goal temperature."
        elif self.checking_temps()[2] > len(self.rooms) / 2 and self.goal_temp <= 50:
            return f"Your {self.house_type} don't need heating." \
                       f"Turn of the heating system immediately"
        elif self.checking_temps()[0] > len(self.rooms) / 2:
            return f"Your {self.house_type} have a heating problem with some rooms."

        else:
            return f"Your {self.house_type} have a problem with a heating system."

    def normal_temp_house(self):
        return self.satisfied_temps() == f"The {self.house_type} does not need heating, " \
                   f"all your rooms have satisfactory temperatures!" or \
                   self.satisfied_temps() == f"All rooms of your {self.house_type} have satisfactory temperatures." \
                   f"You don't need to change the goal temperature."

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return int(self.normal_temp_house()) + other
        elif isinstance(other, HouseHeatingSystem):
            return int(self.normal_temp_house()) + int(other.normal_temp_house())

    def presentation(self):
        return f"""{self.__str__()}
Current goal temperature: {self.goal_temp}ºC
The rooms current temperatures:
{self.room_temps}
The result of checking satisfaction of rooms temperature:
count of rooms with normal temps: {self.checking_temps()[0]}
count of rooms with low temps: {self.checking_temps()[1]}
count of rooms with high temps: {self.checking_temps()[2]}
{self.satisfied_temps()}
"""


house1 = HouseHeatingSystem("Aghayan 60", "house", 60, "kitchen1", "kitchen2", "bathroom1", "bathroom2",
                            "guest_room1", "guest_room2", "bedroom1", "bedroom2", "bedroom3", "bedroom4", "sport_room",
                            kitchen1=10, kitchen2=9, bathroom1=15, bathroom2=14, guest_room1=18, guest_room2=19,
                            bedroom1=14, bedroom2=16, bedroom3=11, bedroom4=13, sport_room=10)

house2 = HouseHeatingSystem("Baghramyan 21", "apartment", 45, "kitchen", "bathroom",
                            "guest_room", "bedroom", kitchen=24, bathroom=19, guest_room=20, bedroom=22)

house3 = HouseHeatingSystem("Papazyan 35", "office", 50, "kitchen", "bathroom",
                            "guest_room", "bedroom", kitchen=25, bathroom=10, guest_room=20, bedroom=22)

house4 = HouseHeatingSystem("Sevak 14", "house", 50, "kitchen", "bathroom",
                            "guest_room", "bedroom1", "bedroom2", kitchen=19, bathroom=21, guest_room=18,
                            bedroom1=22, bedroom2=17)


def count_of_norm_temp_houses(*args):
    res = 0
    for i in range(0, len(args) - 1, 2):
        count = args[i] + args[i + 1]
        res += count
    return res


print(house1.presentation())
print("Number of houses with normal temperature:", count_of_norm_temp_houses(house1, house2, house3, house4))
