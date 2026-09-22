import math

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

        
    def show(self):
        print("Coordinates:",  self.x, self.y)
    
    def move(self, new_x, new_y):
        self.x=new_x
        self.y=new_y
    
    def dist(self, other_point):
        distance=math.sqrt(
            (self.x - other_point.x)**2 
            + (self.y - other_point.y)**2
        )
        return distance
    
point_one=Point(0,0)
point_two=(3,4)

point_one.show()
print("distance ",point_one.dist(point_two))
point_one.move(5, 6)
point_one.show()

        


