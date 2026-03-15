import math

class Shape:
    def __init__(self, color="Transparent"):
        self.color = color

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius, color="Transparent"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color="Transparent"):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(5, "red")
rect = Rectangle(4, 6, "blue")

print(circle.area())
print(rect.area())
print(circle.color)
