from class_car import Car

def test_car_attributes():
    car = Car("Porsche", "Macan", 2021)
    assert car.make == "Porsche"
    assert car.model == "Macan"
    assert car.year == 2021

def test_car_start_with_key():
    car = Car("Porsche", "Macan", 2021)
    car.key = True
    assert car.start() == "Key detected, the car is starting."

def test_car_start_without_key():
    car = Car("Porsche", "Macan", 2021)
    car.key = False
    assert car.start() == "Key undetected, the car can't start."

def test_car_stop_with_key():
    car = Car("Porsche", "Macan", 2021)
    car.key = True
    assert car.stop() == "Key detected, the car is stopping."

def test_car_stop_without_key():
    car = Car("Porsche", "Macan", 2021)
    car.key = False
    assert car.stop() == "Key undetected, the car can't stop."

# Run the tests
test_car_attributes()
test_car_start_with_key()
test_car_start_without_key()
test_car_stop_with_key()
test_car_stop_without_key()
