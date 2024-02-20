import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return super().__str__() + f",{self.radius}"

    def area(self):
        return math.pi * self.radius * self.radius


class Square(Shape):
    def __init__(self, x, y, base):
        super().__init__(x, y)
        self.base = base

    def __str__(self):
        return super().__str__() + f",{self.base}"

    def area(self):
        return self.base * self.base


c = Circle(10, 20, 15)
print(c)
print(f"{c.area():5.2f}")
s = Square(5, 5, 20)
print(s)
print(s.area())
