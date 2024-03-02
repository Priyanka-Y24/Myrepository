import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return math.pi*2*(self.radius)

c = Circle(5)
print("The Area of Circle is: ", round(c.area(),2))
print("Perimeter of the Circle: ",round(c.perimeter(),2))
    
        
