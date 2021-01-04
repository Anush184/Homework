class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 3.14 * self.radius ** 2

    def circle_length(self):
        return 6.28 * self.radius


c1 = Circle(7.3)
print("%.2f"% c1.circle_area())
print("%.2f"% c1.circle_length())
