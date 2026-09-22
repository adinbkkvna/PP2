class Shape:
    def area(self):
        print("area",0)

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        print("Square area", self.length**2 )

square=Square(5)
square.area()