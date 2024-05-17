# Create a class called Rectangle that has attributes width and height.
# Add methods str and repr that return a string representation of the rectangle object.

# Define a class called Rectangle with two attributes: width and height.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Define the str method to return a string representation of the rectangle object, that is more readable for the user.
    def __str__(self):
        return f"Rectangle: width = {self.width}, height = {self.height}"

    # Define the repr method to return a string representation of the rectangle object, that is more technical and unambiguous for the developer.
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

# Create an instance of the Rectangle class and call the str and repr methods.
rect = Rectangle(7, 12)
# print the result of calling the str and repr methods
print(str(rect))
print(repr(rect))
