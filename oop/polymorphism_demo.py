import math

class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self):
        super().__init__()

    def area(self, length, width):
        return self.length * self.width
    
    def __str__(self):
        return super().__str__()
    
class Circle(Shape):

    def __init__(self):
        super().__init__()

    def area(self, radius):
        return math.pi * self.radius ** 2