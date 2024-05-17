# Path: hands-on-python/class_circle.py
# Create a class called Car that has attributes make, model, and year.
# Add methods start and stop that simulate starting and stopping the car, respectively.
# Add a method called key that returns a random boolean value (either True or False).

# import random module to generate random boolean value
import random

# Create a class called Car that has attributes make, model, and year.
class Car:
    # Add a method called key that returns a random boolean value (either True or False).
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.key = random.choice([True, False])

    # Add methods start and stop that simulate starting and stopping the car, respectively.
    def start(self):
        if self.key == True:
            return "Key detected, the car is starting."
        else:
            return "Key undetected, the car can't start"

    def stop(self):
        if self.key == True:
            return "Key detected, the car is stopping."
        else:
            return "Key undetected, the car can't stop."

# Create an instance of the Car class and call the start and stop methods.
car_instance = Car("Porshe", "Macan", 2021)
# print the car instance and call the start and stop methods
print(f"Welcome to: {car_instance.make} {car_instance.model} {car_instance.year}.")
print(car_instance.start())
print(car_instance.stop())


