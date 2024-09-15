# Assignment 1: Define a class named Book that represents a book in a library.
# Attributes :
# title (string): The title of the book.
# author (string): The author of the book.
# year (integer): The year the book was published.
# available (boolean): A status indicating whether the book is available or checked out.
# Methods:
# display_details() that prints the book’s details (title, author, and year).
# borrow_book() that sets the availability to False and prints a message saying the book has been borrowed.
# return_book() that sets the availability to True and prints a message saying the book has been returned.
# Tasks:
# Create at least two objects of the Book class with different attributes
# Display the details of each book using the display_details method.
# Use the borrow_book method on one of the objects and check its availability status.
# Use the return_book method to change the status back to available.


# class Book:
#     no_of_copies_available = 0
#
#     def __init__(self, title, author, year, price):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.__price = price
#         Book.no_of_copies_available += 1
#
#     def display_details(self):
#         print(f"Title: {self.title} \nAuthor: {self.author} \nYear: {self.year} \nPrice : {self.__price}")
#
#     def borrow_book(self):
#         Book.no_of_copies_available -= 1
#         print(f"The book ({self.title}) has been Borrowed!!")
#
#     def return_book(self):
#         Book.no_of_copies_available += 1
#         print(f"The book ({self.title}) has been Returned")
#
#     @classmethod
#     def total_no_of_copies(cls):
#         print(f"Total number of books: {cls.no_of_copies_available}")
#
#     @staticmethod
#     def stat():
#         print("Books are man's best friend")
#
#
# if __name__ == "__main__":
#     book1 = Book("Mahabharat", "Vedavyasa", 400, 1000)
#     book1.__price = 300  # private variable can not be changed
#     book1.display_details()
#     print()
#     book2 = Book("Ramayana", "Valmiki", 500, 200)
#     book2.display_details()
#     print()
#     Book.total_no_of_copies()
#     book1.borrow_book()
#     Book.total_no_of_copies()
#     book1.return_book()
#     Book.total_no_of_copies()
#     Book.stat()

# Assignment 2: Add constructor method to Book example

# Assignment 3: Add a class method to Book example to update class variable ‘number_of_copies_available’

# Assignment : Bank Interest calculator. Calculate SI for senior citizens and regular citizens
# Classname : bank_interest_calculator
# Class variables:
# _ _interest_rate = 8.6
# _ _interest_rate_SeniorCitizen = 8.4
# Instance Variables:
# p_amount
# Duration
# seniorCitizen - flag
# Method:
# simple_interest_calculator(seniorCitizen)
# Formulae:
# Simple Interest = P X R X T / 100
# Equated Monthly Installment = P * r * (1 + r) ^ n / ((1 + r) ^ n - 1)

# class InterestCalculator:
#
#     def __init__(self, principal, time, is_senior=False):
#         self.principal = principal
#         self.time = time
#         self.is_senior = is_senior
#         self.__rate_regular = 8.6
#         self.__rate_senior = 8.4
#
#     def calculate_si(self):
#         if self.is_senior:
#             rate = self.__rate_senior
#         else:
#             rate = self.__rate_regular
#
#         si = (self.principal * rate * self.time) / 100
#         return si
#
#
# # Example usage
# if __name__ == "__main__":
#     principal = float(input("Enter the principal amount: "))
#     time = float(input("Enter the time period in years: "))
#     is_senior = input("Is the person a senior citizen? (yes/no): ").strip().lower() == 'yes'
#
#     calculator = InterestCalculator(principal, time, is_senior)
#     si = calculator.calculate_si()
#
#     if is_senior:
#         print(f"Simple Interest for senior citizen: {si}")
#     else:
#         print(f"Simple Interest for regular citizen: {si}")

# Create a class shape
# Write a function print_shape_area(shape) that takes an instance of Shape (or any subclass of Shape) and prints the area of the shape.
# Create sub classes Circle and Rectangle inherited from shape
# Implement print_shape_area(shape) in these classes appropriately
#
# Create instances of Circle and Rectangle.
#
# Call the print_shape_area function with these instances to demonstrate polymorphism.
#
# Use super method to call method from parent class
#
# Note: Use polymorphism to ensure that print_shape_area () works with any subclass of Shape.

# def print_shape_area(obj):
#     print(f"Area : {obj.area()}")
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#
# c1 = Circle(radius=5)
# r1 = Rectangle(length=5, width=2)
# print_shape_area(c1)
# print_shape_area(r1)

# Assignment 3: Use abstract classes to manage a vehicle system and enforce method implementation across various vehicle types.
# Tasks:
# Create an abstract class Vehicle with the following abstract methods:
# start(): To start the vehicle.
# stop(): To stop the vehicle.
# Implement three subclasses: Car, Bike, and Bus, each with custom implementations for start() and stop().
# Create a Garage class that can add vehicles and call their start() and stop() methods.
# Demonstrate adding different vehicle types to the garage and operating them.

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        pass


# class Car(Vehicle):
#     def start(self):
#         print("Car engine is starting...")
#
#     def stop(self):
#         print("Car engine is terminating...")
#
#
# class Bike(Vehicle):
#     def start(self):
#         print("Bike engine is starting...")
#
#     def stop(self):
#         print("Bike engine is terminating...")
#
#
# class Bus(Vehicle):
#     def start(self):
#         print("Bus engine is starting...")
#
#     def stop(self):
#         print("Bus engine is terminating...")
#
#
# class Garage:
#     def __init__(self):
#         self.vehicles = []
#
#     def add_vehicle(self, *vehicles):
#         for vehicle in vehicles:
#             self.vehicles.append(vehicle)
#
#     def operate_vehicles(self):
#         for vehicle in self.vehicles:
#             vehicle.start()
#             vehicle.stop()
#             print()
#
#
# garage = Garage()
#
# car1 = Car()
# bike1 = Bike()
# bus1 = Bus()
#
# garage.add_vehicle(car1, bike1, bus1)
#
# garage.operate_vehicles()

# car1 = Car()
# car1.start()
# car1.stop()
# print()
#
# bike1 = Bike()
# bike1.start()
# bike1.stop()
# print()
#
# bus1 = Bus()
# bus1.start()
# bus1.stop()
# car1 = Car()
# bike1 = Bike()
# bus1 = Bus()
#
# g1 = Garage()
# g1.operate_vehicle(car1)
# g1.operate_vehicle(bike1)
# g1.operate_vehicle(bus1)


# Assignment 4: Smart Home Devices Management
#  Base abstract class: SmartDevice
# Class variables: _name (string), _status
# Abstract methods: turn_on(), turn_off()
# Non-abstract method : device_info()
# Subclass SmartLight: Inherit from the SmartDevice class.
# Implement turn_on() and turn_off() method to set _status to 'on' and return "Smart light is now on.".
#  Add a method set_brightness(level) that accepts a brightness level (integer from 0 to 100) and returns a string, e.g., "Brightness set to 70%.".
# Use the super() function to initialize the inherited protected instance variables in the constructor.

# from abc import ABC, abstractmethod
#
#
# class SmartDevice(ABC):
#     _name = ""
#     _status = "off"
#
#     def __init__(self, name: str):
#         self._name = name
#
#     @abstractmethod
#     def turn_on(self):
#         pass
#
#     @abstractmethod
#     def turn_off(self):
#         pass
#
#     @abstractmethod
#     def device_info(self):
#         pass
#
#
# class SmartLight(SmartDevice):
#     def __init__(self, name: str):
#         super().__init__(name)
#         self._brightness = 0
#
#     def turn_on(self):
#         self._status = "on"
#         print(f"Smart light '{self._name}' is now on.")
#
#     def turn_off(self):
#         self._status = "off"
#         print(f"Smart light '{self._name}' is now off.")
#
#     def set_brightness(self, level):
#         if 0 <= level <= 100:
#             self._brightness = level
#             return f"Brightness set to {level}%."
#
#     def device_info(self):
#         return f"Smart Light '{self._name}': Status is {self._status}."
#
#
# if __name__ == "__main__":
#     living_room_light = SmartLight(name="Living Room Light")
#
#     living_room_light.turn_on()
#     print(living_room_light.device_info())
#
#     print(living_room_light.set_brightness(70))
#     print(living_room_light.device_info())
#
#     living_room_light.turn_off()
#     print(living_room_light.device_info())

