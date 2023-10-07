from abc import ABC, abstractmethod

# Define an abstract class for geometric shapes
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Create concrete subclasses of Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create instances of concrete subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculate and print the area of shapes
print(f"Area of the circle: {circle.area()}")
print(f"Area of the rectangle: {rectangle.area()}")
