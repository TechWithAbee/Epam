# Develop a class Field with "full encapsulation" whose attributes are accessed, and data changes are implemented through method calls.

# In OOP, it is generally accepted to start the names of the methods for extracting data with the word "get" and the names of the methods in which fields are equated to a certain value - "set".

# In this task, you must implement get_value and set_value methods for the Field class (__value property).

class Field:
    __value = None
    def __init__(self):
        self.__value = None
    
    def get_value(self, ):
        return self.__value
    
    def set_value(self, value):
        self.__value = value


# Create a class SchoolMember that represents any person in school. Classes Teacher and Student are inherited from SchoolMember.

# Classes should have the same interface as the public show () method. Teacher accepts name (str), age (int), and salary (int). Student accepts name (str), age (int), and grades. Move the same logic of initialization to the class SchoolMember.

# Method show() returns a string (see string patterns in the Example).

# All attributes that were accepted should be public.

# Example
# >>> teacher = Teacher("Mr.Snape", 40, 3000)
# >>> teacher.name
# "Mr.Snape"

# >>> persons = [teacher, Student("Harry", 16, 75)]

# >>> for person in persons:
#        print(person.show())

# "Name: Mr.Snape, Age: 40, Salary: 3000"
# "Name: Harry, Age: 16, Grades: 75"

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name}, Age: {self.age}"
    
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class Student(SchoolMember):
    def __init__(self, name, age, grades):
        super().__init__(name, age)
        self.grades = grades

    def show(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"
    
# Usage
# teacher = Teacher("Mr.Snape", 40, 3000)
# teacher.name

# persons = [teacher, Student("Harry", 16, 75)]

# for person in persons:
#        print(person.show())


print('-------------------------')


# Implement a Counter class that optionally accepts the start value and the counter stop value. If the start value is not specified, the counter should begin with 0. If the stop value is not specified, it should be counting up infinitely. If the counter reaches the stop value, print "Maximal value is reached."

# Implement the two methods: "increment" and "get"

# Example:

# >>> c = Counter(start=42)
# >>> c.increment()
# >>> c.get()
# 43

# >>> c = Counter()
# >>> c.increment()
# >>> c.get()
# 1
# >>> c.increment()
# >>> c.get()
# 2

# >>> c = Counter(start=42, stop=43)
# >>> c.increment()
# >>> c.get()
# 43
# >>> c.increment()
# The maximal value is reached.
# >>> c.get()
# 43


class Counter:
    def __init__(self, start=0, stop=None):
        self.start = start
        self.stop = stop
        self.current = start
    
    def increment(self):
        if self.stop is not None and self.current == self.stop:
            print("The maximal value is reached.")
        else:
            self.current += 1
    
    def get(self):
        return self.current
    
# Usage
# c = Counter(start=42, stop=44)
# c.increment()
# print(c.get())
# c.increment()
# print(c.get())
# c.increment()
# print(c.get())

print('-------------------------')

# Implement a custom dictionary that will memorize the five latest changed keys. Each changed key has to be added in the end of the history data structure.

# Using the method "get_history" returns these keys.

# Example:

# >>> d = HistoryDict({"foo": 42})
# >>> d.set_value("bar", 43)
# >>> d.get_history()

# ["bar"]
# >>> d.set_value("foo", 44)
# >>> d.get_history()
# ["bar", "foo"]

    
from collections import deque

class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data
        self.history = deque(maxlen=5)
    
    def set_value(self, key, value):
        self.data[key] = value
        self.history.append(key)

    def get_history(self):
        return list(self.history)

# Usage
d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())
d.set_value("foo0", 44)
print(d.get_history())
d.set_value("foo1", 44)
print(d.get_history())
d.set_value("foo2", 44)
print(d.get_history())
d.set_value("foo3", 44)
print(d.get_history())
d.set_value("foo4", 44)
print(d.get_history())

print('-------------------------')

# You need to create an abstract class Vehicle. Classes Car, Motorcycle, Truck, and Bus are inherited from Vehicle and already implemented.

# Class Vehicle accepts the following parameters:

# brand_name -> str (e.g. Honda)
# year_of_issue -> int (e.g. 2020)
# base_price -> int (e.g. 1_000_000)
# mileage -> int (e.g. 10_000)
# The following methods should be implemented:

# vehicle_type - returns str - a type of the vehicle in the following pattern brand_name + name of the class. For example: Toyota Car, Suzuki Motorcycle;
# is_motorcycle returning a boolean value depends on the number of wheels (2 wheels -> motorcycle, so the method should return True);
# purchase_price - returns the price of the vehicle: (base_price - 0.1 * mileage). If the resulting price is less than 100_000, the method should return 100_000.
# Put the following decorators where necessary and if it is necessary:

# abstractmethod, classmethod, staticmethod, property, and other decorators.

# Example
# >>> vehicles = (
#     Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
#     Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
#     Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
#     Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
# )

# >>> for vehicle in vehicles:
#         print(
#             f"Vehicle type={vehicle.vehicle_type()}\n"
#             f"Is motorcycle={vehicle.is_motorcycle()}\n"
#             f"Purchase price={vehicle.purchase_price}\n"
#         )


# Vehicle type=Toyota Car
# Is motorcycle=False
# Purchase price=985000.0

# Vehicle type=Suzuki Motorcycle
# Is motorcycle=True
# Purchase price=796500.0

# Vehicle type=Scania Truck
# Is motorcycle=False
# Purchase price=14915000.0

# Vehicle type=MAN Bus
# Is motorcycle=False
# Purchase price=9905000.0


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand_name: str, year_of_issue: int, base_price: int, mileage: int):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @property
    @abstractmethod
    def wheels_num(self) -> int:
        """Abstract method to be implemented in child classes to return the number of wheels."""
        pass

    def vehicle_type(self) -> str:
        return f"{self.brand_name} {self.__class__.__name__}"
    
    def is_motorcycle(self) -> bool:
        return self.wheels_num == 2

    @property
    def purchase_price(self) -> float:
        price = self.base_price - 0.1 * self.mileage
        return max(price, 100_000)

# Don't change class implementation
class Car(Vehicle):
    @property
    def wheels_num(self) -> int:
        return 4

# Don't change class implementation
class Motorcycle(Vehicle):
    @property
    def wheels_num(self) -> int:
        return 2

# Don't change class implementation
class Truck(Vehicle):
    @property
    def wheels_num(self) -> int:
        return 10

# Don't change class implementation
class Bus(Vehicle):
    @property
    def wheels_num(self) -> int:
        return 6

# Example usage
vehicles = (
    Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000),
    Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000),
    Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000),
    Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000)
)

for vehicle in vehicles:
    print(
        f"Vehicle type={vehicle.vehicle_type()}\n"
        f"Is motorcycle={vehicle.is_motorcycle()}\n"
        f"Purchase price={vehicle.purchase_price}\n"
    )


print('-------------------------')

def exception():
    try:
        a = int(input("Enter a positive integer: "))
        if a <= 0:
            raise ValueError("That is not a positive number!")
    except ValueError as ve:
        print(ve)

exception()
