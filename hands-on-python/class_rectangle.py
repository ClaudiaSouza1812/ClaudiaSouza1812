# Create a class called Rectangle that has attributes width and height.
# Add methods area and perimeter that calculate the area and perimeter of the rectangle, respectively.

# Define a class called Rectangle with two attributes: width and height.
class Rectangle:
    """
    A class to represent a rectangle.
    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    # Define the __init__ method to initialize the width and height attributes.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Define the area method to calculate the area of the rectangle.
    def area(self):
        """
        Calculate the area of the rectangle using the formula: width * height.
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    # Define the perimeter method to calculate the perimeter of the rectangle.
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle using the formula: 2 * width + 2 * height.
        Returns:
            int: The perimeter of the rectangle.
        """
        return self.width * 2 + self.height * 2

# Define a main function
def main():

    # Define variables to store the user input.
    user_base = int()
    user_height = int()
    # Use a while loop to prompt the user to enter the width and height of the rectangle.
    while user_base == 0 or user_height == 0:
        try:
            # Prompt the user to enter the width and height of the rectangle.
            user_base = int(input("Enter the base of the rectangle: "))
            user_height = int(input("Enter the height of the rectangle: "))
        # Handle the ValueError exception if the user enters a non-integer value.
        except ValueError:
            # Print an error message and call the main function again.
            print("Please enter a valid integer number.")


    # Create an instance of the Rectangle class and input the width and height of the rectangle as arguments.
    rect = Rectangle(user_base, user_height)
    # Call the area and perimeter methods of the rectangle instance and print the results.
    print(f"The area of the rectangle with base '{rect.width}' and height '{rect.height}' is: ", rect.area())
    print(f"The perimeter of the rectangle with base '{rect.width}' and height '{rect.height}' is: ", rect.perimeter())
    exit()

# Call the main function.
main()


