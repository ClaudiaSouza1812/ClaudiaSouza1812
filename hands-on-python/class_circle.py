# Create a class called Circle that has attribute radius. Add methods area and circumference that calculate the area
# and circumference of the circle, respectively.

# Define a class called Circle with one attribute: radius.
class Circle:
    """
    A class to represent a circle.
    Attributes:
        radius (int): The radius of the circle.
    """
    def __init__(self, radius):
        self.radius = radius

    """
    Define the area method to calculate the area of the circle.
    Calculate the area of the circle using the formula: 3.14 * radius ** 2.
    Returns:
        int: The area of the circle.
    """
    def area(self):
        return 3.14 * self.radius ** 2

    """
    Define the circumference method to calculate the circumference of the circle.
    Calculate the circumference of the circle using the formula: 2 * 3.14 * radius.
    Returns:
        int: The circumference of the circle.
    """
    def circumference(self):
        return 2 * 3.14 * self.radius


# Define a main function
def main():

    # Define a variable to store the user input.
    user_radius = int()
    # Use a while loop to prompt the user to enter the radius of the circle.
    while user_radius == 0:
        try:
            user_radius = int(input("Enter the radius (integer) of the circle:"'\n'))
        # Handle the ValueError exception if the user enters a non-integer value.
        except ValueError:
            print("Please enter a valid integer number.")

    # Create an instance of the Circle class and input the radius of the circle as an argument.
    circ = Circle(user_radius)
    # Call the area and circumference methods of the circle instance and print the results.
    print(f"The area of a circle with radius '{circ.radius}' is: ", circ.area())
    print(f"The circumference of a circle with radius '{circ.radius}' is: ", circ.circumference())

# Call the main function.
main()
