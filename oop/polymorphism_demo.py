#
# 
import math  # Needed for math.pi in Circle calculations

# Base class
class Shape:
    def area(self):
        """
        This method should be overridden by all derived classes.
        If not, it raises an error indicating the method is not implemented.
        """
        raise NotImplementedError("Derived classes must override this method")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize the rectangle with length and width.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the base class method to calculate the area of a rectangle.
        Formula: length × width
        """
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize the circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the base class method to calculate the area of a circle.
        Formula: π × radius²
        Uses math.pi for π.
        """
        return math.pi * (self.radius ** 2)


