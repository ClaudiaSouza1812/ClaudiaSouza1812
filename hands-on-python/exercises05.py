
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        return f'{self.name} is {self.age} years old.'

p1 = MyClass("John", 36)
print(p1.name, p1.age)  # John 36
print(p1.myFunc())  # John is 36 years old.


class MyClass:
    def __init__(self):
        self.__my_var = 42

obj = MyClass()
print(obj.__my_var)  # AttributeError: 'MyClass' object has
print(obj._MyClass__my_var)  # 42


class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_object_1 = ExampleClass() # 1
example_object_2 = ExampleClass(2) # 2
example_object_2.set_second(3) # 3
example_object_3 = ExampleClass(4) # 4
example_object_3.__third = 5 # 5

print(example_object_1.__dict__)  # {'_ExampleClass__first': 1}


class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

example_object1 = ExampleClass() # 1
example_object2 = ExampleClass(2) # 2
example_object3 = ExampleClass(4) # 3

print(example_object1.__dict__, example_object1._ExampleClass__counter)  # {'_ExampleClass__first': 1} 3
print(example_object2.__dict__, example_object2._ExampleClass__counter)  # {'_ExampleClass__first': 2} 3
print(example_object3.__dict__, example_object3._ExampleClass__counter)  # {'_ExampleClass__first': 4} 3


class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)  # {'__module__': '__main__', 'varia': 1, '__init__': <function ExampleClass.__init__ at 0x7f8e3c3f3d30>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
example_object1 = ExampleClass(2)

print()
print(ExampleClass.__dict__)  # {'__module__': '__main__', 'varia': 2, '__init__': <function ExampleClass.__init__ at 0x7f8e3c3f3d30>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}
print()
print(example_object1.__dict__)  # {}

class ExampleClass:
    varia = 1
    def __init__(self, val, num):
        self.varia = val
        self.num = num

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1) # 1
example_object.a # 1
example_object.b # AttributeError: 'ExampleClass' object has no attribute 'b'
example_object = ExampleClass(2) # 2
print(example_object.__dict__)  # {'b': 1}


class Super:
    supVar = 1

class Sub(Super):
    subVar = 2

obj = Sub()
print(obj.subVar)  # 2
print(obj.supVar)  # 1

obj = Super()
print(obj.subVar)  # AttributeError: 'Super' object has no attribute 'subVar'


class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()
print(obj.supVar)  # 11
print(obj.subVar)  # 12


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname. self.graduationyear)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
x.printname()  # Mike Olsen 2019


class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

for cl1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cl2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cl1, cl2), end="\t")
    print()


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cl in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cl), end="\t")
    print()



class level1:
    var = 100
    def fun(self):
        return 101

class level2(level1):
    var = 200
    def fun(self):
        return 201

class level3(level2):
    pass

obj = level3() # 1
print(obj.var) # 200

print(obj.fun()) # 201


class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

obj = Sub() # 1
print(obj.var) # L


class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
one.doanything() # do_it from One
two = Two()
two.doanything() # do_it from Two


class SampleClass:
    def __init__(self, val):
        self.val = val

obj1 = SampleClass(0)
obj2 = SampleClass(2)

print(obj1 is obj2)  # False

obj3 = obj1
print(obj1 is obj3)  # True

obj3.val += 1
print(obj3.val)  # 1


from dataclasses import dataclass

@dataclass
class Person():
    name: str = "John"
    age: int = 30
    height: float = 1.80
    email: str = "joe@test.com"

    def myFunc(self):
        return f"Person(name='{self.name}', age={self.age}, height={self.height}, email='{self.email}')"

p1 = Person() # 1
print(p1.myFunc()) # Person(name='John', age=30, height=1.8, email='joe@test.com')


class Employee(Person):
    salary: float
    department: str

print(Employee(salary=1000, department="IT").myFunc()) # Person(name='John', age=30, height=1.8,
