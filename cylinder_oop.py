'''
To calculate volume and surface area of cylinder
'''
#Defining class cylinder 
class Cylinder():

#class object attribute
    pi = 3.14    

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
    #volume
    def volume(self):
        return self.pi * (self.radius ** 2) * self.height
    #Surface area
    def surface_area(self):
        return self.pi * 2 * self.radius * self.height


radius = int(input("Enter the radius of cylinder\n"))
height = int(input("Enter the height of cylinder\n"))
mycylinder = Cylinder(height, radius)
volume = mycylinder.volume()
area = mycylinder.surface_area()
print (f" The area and volume of the cylinder are {area} and {volume}")
