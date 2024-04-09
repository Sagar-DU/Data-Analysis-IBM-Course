# Importing the library
import matplotlib.pyplot as plt
# %matplotlib inline #this one needed in Jupeter notebook

# Creating a class Circle
class Circle(object):
    # Constructor
    def __init__(self, radius = 3, color = "blue"):
        self.radius = radius
        self.color = color

    # Method
    def add_radius (self, r):
        self.radius = self.radius + r
        return self.radius
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius = self.radius, fc = self.color))
        plt.axis("scaled")
        plt.show()

# Creating an object RedCircle
RedCircle = Circle(10, "red")

# Find out hte methods can be used on the object RedCircle
print(dir(RedCircle))

# Print the object attribute radius
print(RedCircle.radius)

# Print the object attribute color
print(RedCircle.color)

# Setting the object attribute radius
RedCircle.radius = 1

# Print the object attribute radius
print(RedCircle.radius)

# Print the object attribute color
print(RedCircle.color)

# Drawing Circle
# RedCircle.drawCircle()

# Using method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Creating a blue circle with a given radius
BlueCircle = Circle(radius=100)

# Print the object attribute radius
print(BlueCircle.radius)

# Print the object attribute color
print(BlueCircle.color)

# Drawing Circle
# BlueCircle.drawCircle()

# Creating a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        
# Creating a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attributes
print("Height of the rectangle", SkinnyBlueRectangle.height)
print("Width of the rectangle", SkinnyBlueRectangle.width)
print("Color of the rectangle", SkinnyBlueRectangle.color)

# Drawing the Rectangle
# SkinnyBlueRectangle.drawRectangle()

# Create a new object rectangle
FatYellowRectangle = Rectangle(20, 5, 'yellow')

# Printing the object attributes
print("Height of the new Ractangle",FatYellowRectangle.height)
print("Width of the new Ractangle",FatYellowRectangle.width)
print("Color of the new Ractangle",FatYellowRectangle.color)

# Drawing the new Rectangle
# FatYellowRectangle.drawRectangle()

# Excercise
# Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage.
class Vehicle:
    def __init__(self, maxSpeed, milage, color):
        self.maxSpeed = maxSpeed
        self.milage = milage

# Task-2. Update the class with the default color for all vehicles," white".
class Vehicle:
    color = "white"
    def __init__(self, maxSpeed, milage):
        self.maxSpeed = maxSpeed
        self.milage = milage

# Task-3. Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.
class Vehicle:
    color = "white"
    def __init__(self, maxSpeed, milage):
        self.maxSpeed = maxSpeed
        self.milage = milage
    
    # Method
    def assign_seatting_capacity (self, seating_capacity):
        self.seating_capacity = seating_capacity

# Task-4. Create a method to display all the properties of an object of the class.
class Vehicle:
    color = "white"
    def __init__(self, maxSpeed, milage):
        self.maxSpeed = maxSpeed
        self.milage = milage
    
    # Method
    def assign_seatting_capacity (self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    # Method
    def display_properties (self):
        print ("Properties of the Vehicle:")
        print ("Color", self.color)
        print ("Max Speed", self.maxSpeed)
        print ("Milage", self.milage)
        print ("Seating Capacity", self.seating_capacity)

# Task-5. Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, and another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.
car1 = Vehicle(200, 20)
car1.assign_seatting_capacity(5)
print (car1.display_properties())

car2 = Vehicle (180, 25)
car2.assign_seatting_capacity(4)
print (car2.display_properties())

# Completed