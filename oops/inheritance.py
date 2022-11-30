class Vehicle:
    @staticmethod
    def vehicle_info():
        print("Inside Vehicle class")


# Car can inherit properties of Vehicle
class Car(Vehicle):
    @staticmethod
    def car_info():
        print("Inside Car class")


# Truck can inherit properties of Vehicle
class Truck(Vehicle):
    @staticmethod
    def truck_info():
        print("Inside Truck class")


# Sports Car can inherit properties of Vehicle and Car
class SportsCar(Car, Vehicle):
    @staticmethod
    def sports_car_info():
        print("Inside SportsCar class")


# create object
s_car = SportsCar()
truck = Truck()

s_car.vehicle_info()
s_car.car_info()
truck.truck_info()
s_car.sports_car_info()
