import math
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print(self.x, self.y)

    def move(self,x,y):
        self.x=x
        self.y=y
    
    def dist(self,op):
        print(math.sqrt((self.x - op.x) ** 2 + (self.y - op.y) ** 2))
        
a=Point(1,4)
b=Point(7,9)
a.show()
a.move(4,5)
a.show()
a.dist(b)