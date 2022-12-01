from abc import ABC, abstractmethod


class Vehicle(ABC):
    """This class used to create properties for Vehicle
    object and access the properties of Vehicle"""
    # constructor of the class it initialize the object
    def __init__(self, name, model, price, fuel_type, horse_power,
                 fuel_capacity,  brand_name, seat_count, max_speed):
        # self keyword used to access the instance variable and instance method of the object.
        # data members (instance variables)
        self.name = name
        self.model = model
        self.price = price
        self.fuel_type = fuel_type
        self.horse_power = horse_power
        self.fuel_capacity = fuel_capacity
        self.brand_name = brand_name
        self.seat_count = seat_count
        self.max_speed = max_speed

    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power\
               + "\n fuel_capacity : " + self.fuel_capacity

    @staticmethod
    @abstractmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")


# Car can inherit properties of Vehicle
class Car(Vehicle):
    """This class used to create properties for Car
        object and access the properties of Car
        It also has a properties of Vehicle"""

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, gear_type, car_type):
        super(Car, self).__init__(name, model, price, fuel_type, horse_power,
                                  fuel_capacity,  brand_name, seat_count, max_speed)
        self.gear_type = gear_type
        self.car_type = car_type

    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power\
               + "\n fuel_capacity : " + self.fuel_capacity

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")


# Truck can inherit properties of Vehicle
class Truck(Vehicle):
    """This class used to create properties for Truck
        object and access the properties of Truck
        It also have a properties of Vehicle"""

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, truck_type, max_load):
        super(Truck, self).__init__(name, model, price, fuel_type, horse_power,
                                    fuel_capacity,  brand_name, seat_count, max_speed)
        self.truck_type = truck_type
        self.max_load = max_load

    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power\
               + "\n fuel_capacity : " + self.fuel_capacity

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")


class TowTruck(Truck):
    """This class used to create properties for TowTruck
        object and access the properties of TowTruck
        It also have a properties of Truck"""

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, organisation, max_tow_load):
        super(TowTruck, self).__init__(truck_type, max_load)
        super(Truck, self).__init__(name, model, price, fuel_type, horse_power,
                                    fuel_capacity,  brand_name, seat_count, max_speed)
        self.organisation = organisation
        self.max_tow_load = max_tow_load

    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power\
               + "\n fuel_capacity : " + self.fuel_capacity

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")


# Sports Car can inherit properties of Vehicle and Car
class SportsCar(Car, Truck):
    """This class used to create properties for SportsCar
        object and access the properties of SportsCar 
        It also have a properties of Car and Truck"""

    def __init__(self, name, model, price, fuel_type, horse_power,
                 fuel_capacity,  brand_name, seat_count, max_speed):
        super(SportsCar, self).__init__(gear_type, car_type)
        super(Truck, self).__init__(name, model, price, fuel_type, horse_power,
                                    fuel_capacity, brand_name, seat_count, max_speed)

    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power\
               + "\n fuel_capacity : " + self.fuel_capacity

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")


class Bike(Vehicle):
    """This class is used to create properties of bike and access the properties"""
    # class variable
    bike_show = "bike on the road vibes are good"

    # constructor of the class it initialize the object
    # instance method
    def __init__(self, name, model, price, fuel_type, horse_power,
                 fuel_capacity,  brand_name, seat_count, max_speed, bike_type):
        super().__init__(name, model, price, fuel_type, horse_power,
                         fuel_capacity,  brand_name, seat_count, max_speed)
        self.bike_type = bike_type

    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power\
               + "\n fuel_capacity : " + self.fuel_capacity

    # static method
    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")

    # class method
    @classmethod
    def main(cls, bike_show):
        """this is class method, and it used for access class variables."""
        cls.bike_show = bike_show
        print(cls.bike_show)
    
    def __del__(self):
        pass


honda = Bike('splendor', 'honda', 80000, 'petrol', '125CC', '10l', 'splendor125', 3, 100, 'normal')
hero = Bike('splendor', 'honda', 80000, 'petrol', '125CC', '10l', 'splendor125', 3, 100, 'normal')
honda.privacy()
print(honda.get())
print(hero.get())
print(honda.__dict__)

