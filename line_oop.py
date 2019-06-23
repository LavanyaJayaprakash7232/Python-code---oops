'''
To calculate the slope of a line and distance between two coordinates on the line
'''

#defining class line
class Line():
   
    def __init__(self, co1, co2):
        self.co1 = co1
        self.co2 = co2
    #slope
    def slope(self):
        x1, y1 = self.co1
        x2, y2 = self.co2
        return (y2 - y1)/(x2 - x1)
    #distance
    def distance(self):
        x1, y1 = self.co1
        x2, y2 = self.co2
        return ((x2 - x1)**2 + (y2 -y1)**2)**(1/2)
    
#User input of coordinates in the form of tuples
co1 = tuple(int(a) for a in input("Enter the coordinate point 1\n").split())
co2 = tuple(int(b) for b in input("Enter the coordinate point 2\n").split())
myline = Line(co1, co2)
slope = myline.slope()
distance = myline.distance()
print(f"The slope is {slope} and the distance is {distance}")
