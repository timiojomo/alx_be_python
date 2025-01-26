import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def area(self, length, width):
        return length * width
    
class Circle(Shape):
    def area(self, radius):
        return math.pi * radius ** 2