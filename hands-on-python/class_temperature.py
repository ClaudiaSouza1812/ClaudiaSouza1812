# Create a class called Temperature that has attribute celsius (a temperature in degrees Celsius).
# Add methods to_fahrenheit and to_kelvin that convert the temperature to degrees Fahrenheit and Kelvin, respectively.

# Create a class called Temperature that has attribute celsius (a temperature in degrees Celsius).
class Temperature:
    def __init__(self, Celsius):
        self.Celsius = Celsius
    # Add method to_fahrenheit that convert the temperature to degrees Fahrenheit
    def to_fahrenheit(self):
        return (self.Celsius * 9/5) + 32
    # Add method to_kelvin that convert the temperature to degrees Kelvin
    def to_kelvin(self):
        return self.Celsius + 273.15

# Create an instance of the Temperature class with a temperature as argument
celsius = Temperature(19)
# print the temperature in Celsius, Fahrenheit and Kelvin
print(f"The temperature now is: {celsius.Celsius}° Celsius, {celsius.to_fahrenheit()}° Fahrenheit and {celsius.to_kelvin()} Kelvin.")
