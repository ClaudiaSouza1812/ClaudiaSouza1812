# Create a Circle class with an attribute radius. Implement methods to calculate and return
# the area and circumference of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


cir = Circle(7) # 153.86 43.96
print(cir.area()) # 153.86
print(cir.circumference()) # 43.96
