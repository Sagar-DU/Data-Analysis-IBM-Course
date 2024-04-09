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
BlueCircle.drawCircle()