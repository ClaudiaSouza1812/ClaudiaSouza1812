# Create a Car class with attributes make, model, and year. Implement a method display_info that prints information about the car,
# such as "Make: Toyota, Model: Camry, Year: 2022."

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
            print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

vehicle = Car("Toyota", "Camry", 2022)
vehicle.display_info() 
