class Hotel:
    def __init__(self, hotel_name: str, place: str, rooms_mid: dict,
                 mid_room_price: int, rooms_lux: dict, lux_room_price: int):
        self._hotel_name = hotel_name
        self._place = place
        self._rooms_mid = rooms_mid
        self._mid_room_price = mid_room_price
        self._rooms_lux = rooms_lux
        self._lux_room_price = lux_room_price

    def hotel_presentation(self):
        print(f"""Hotel
name - {self._hotel_name}
place - {self._place}
rooms middle: {self._rooms_mid}
rooms lux: {self._rooms_lux}
room price - {self._mid_room_price}(mid) and {self._lux_room_price}(lux)""")

    def _available_room_check(self, room_type: dict):
        for value in room_type.values():
            if value == "free":
                return True
        return False

    def booking_mid_room(self):
        if self._available_room_check(self._rooms_mid):
            for key, value in self._rooms_mid.items():
                if value == "free":
                    self._rooms_mid[key] = "busy"
                    print(f"Thank you! Just now you book {key} middle room.")
                    break
        else:
            print("Sorry, we don't have a free room in middle rooms.")

    def booking_lux_room(self):
        if self._available_room_check(self._rooms_lux):
            for key, value in self._rooms_lux.items():
                if value == "free":
                    self._rooms_lux[key] = "busy"
                    print(f"Thank you! Just now you book {key} lux room.")
                    break
        else:
            print("Sorry, we don't have a free room in lux rooms.")

    def discount_mid_room_price(self, percent):

        return self._mid_room_price - (self._mid_room_price * percent) / 100

    def discount_lux_room_price(self, percent):

        return self._lux_room_price - (self._lux_room_price * percent) / 100


class Taxi:
    def __init__(self, car_name, car_types, price_for_tour):
        self._car_name = car_name
        self._car_types = car_types
        self._price_for_tour = price_for_tour

    def taxi_presentation(self):
        print(f"""name - {self._car_name}
type of cars - {self._car_types}
price for trip - {self._price_for_tour}""")

    def discount(self, percent):
        return self._price_for_tour - (self._price_for_tour * percent) / 100


class Tour(Hotel, Taxi):
    def __init__(self, name, hotel_name, place, rooms_mid,
                 mid_room_price, rooms_lux, lux_room_price, car_name, car_types, price_for_tour,
                 percent=0):
        self.name = name
        self.percent = percent
        Hotel.__init__(self, hotel_name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
        Taxi.__init__(self, car_name, car_types, price_for_tour)

    def price_lux(self):
        return self._lux_room_price + self._price_for_tour

    def price_mid(self):
        return self._mid_room_price + self._price_for_tour

    def presentation(self):
        print(f"""TOUR
name - {self.name}
price lux room - {self.price_lux() - (self.price_lux() * self.percent) / 100}  
price middle room - {self.price_mid() - (self.price_mid() * self.percent) / 100}
including
Taxi""")
        self.taxi_presentation()

        self.hotel_presentation()

    def presentation2(self):
        print(f"""Hello!
We offer {self.name}. 
We have two options: {self.price_lux() - (self.price_lux() * self.percent)
                      / 100} and {self.price_mid() - (self.price_mid() * 
                                                      self.percent) / 100} 
Includes transport with '{self._car_name}' company, which provides '{self._car_types}' cars,
price for it is {self._price_for_tour}. We will stay at '{self._hotel_name}' hotel, 
which offers two types of rooms:
middle-{self.discount_mid_room_price(self.percent)} and lux-{self.discount_lux_room_price(self.percent)}""")


tour1 = Tour("GEGHARD tour", "Lerane", "Geghard",
             {"room1": "busy", "room2": "busy", "room3": "busy"}, 20000,
             {"room1": "busy", "room2": "free", "room3": "free", "room4": "free"}, 45000,
             "Ride_over", "BMW", 10000, 15)
tour1.presentation()
