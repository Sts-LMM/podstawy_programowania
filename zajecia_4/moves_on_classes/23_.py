import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius ** 2

    def compute_perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print("Area of the circle:", circle.compute_area())          # Output: ~78.54
print("Perimeter of the circle:", circle.compute_perimeter())  # Output: ~31.42
