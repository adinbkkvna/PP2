class Shape:
    def area(self):
        print("area", 0)

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    
    def area(self):
        print("Rectangle area", self.length*self.width)

rectangle=Rectangle(5,6)
rectangle.area()
        