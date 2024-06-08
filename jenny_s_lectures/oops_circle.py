class Circle:
    pi=3.14
    def __init__(self,radius):
        self.rad=radius
    def circumference(self):
        return 2 * self.pi * self.rad
    def get_area(self):
        return self.pi*self.rad**2

circle_1=Circle(8)
# print('circumference for circle 1 is',circle_1.circumference())
# print('area of circle 1 is',circle_1.get_area())
circle_2=Circle(4)
# print('circumference for circle 2 is',circle_2.circumference())
# print('area of circle 2 is',circle_2.get_area())

class Square:
    def __init__(self,side):
        self.s=side
    def area(self):
        return self.s**2

square_1=Square(4)
print('Area of square 1 is',square_1.area())
square_2=Square(8)
print('Area of square 2 is',square_2.area())

