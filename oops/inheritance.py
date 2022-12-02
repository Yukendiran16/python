from abc import ABC, abstractmethod


def calculate_price(price):
    return price + price * 2.5 + 1000


class Vehicle(ABC):
    """This class used to create properties for Vehicle
    object and access the properties of Vehicle"""

    # constructor of the class it initialize the object
    def __init__(self, name, model, price, fuel_type, horse_power,
                 fuel_capacity, brand_name, seat_count, max_speed, ):
        # self keyword used to access the instance variable and instance method of the object.
        # data members (instance variables)
        self.name = name
        self.model = model
        self.price = calculate_price(price)
        self.fuel_type = fuel_type
        self.horse_power = horse_power
        self.fuel_capacity = fuel_capacity
        self.brand_name = brand_name
        self._seat_count = seat_count
        self.__max_speed = max_speed

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc} \n") \
            .format(name=self.name, model=self.model, price=str(self.price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def get_properties(self):
        print(self.__dict__)

    @staticmethod
    @abstractmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")

    def __del__(self):
        print(" Inside Destructor Method. \n Object destroyed.")

    @staticmethod
    def calculate_price(price):
        return price + price * 2.5 + 1000


# Car can inherit properties of Vehicle
class Car(Vehicle):
    """This class used to create properties for Car
        object and access the properties of Car
        It also has a properties of Vehicle"""

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, gear_type, car_type):
        super().__init__(name, model, price, fuel_type, horse_power,
                         fuel_capacity, brand_name, seat_count, max_speed)
        self.gear_type = gear_type
        self.car_type = car_type

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc} \n") \
            .format(name=self.name, model=self.model, price=str(self.price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def get_properties(self):
        print(self.__dict__)

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")

    def __del__(self):
        print(" Inside Destructor Method. \n Object destroyed.")


# Truck can inherit properties of Vehicle
class Truck(Vehicle):
    """This class used to create properties for Truck
        object and access the properties of Truck
        It also have a properties of Vehicle"""

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, truck_type, max_load):
        super().__init__(name, model, price, fuel_type, horse_power,
                         fuel_capacity, brand_name, seat_count, max_speed)
        self.truck_type = truck_type
        self.max_load = max_load

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc} \n") \
            .format(name=self.name, model=self.model, price=str(self.price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def get_properties(self):
        print(self.__dict__)

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")

    def __del__(self):
        print(" Inside Destructor Method. \n Object destroyed.")


class TowTruck(Truck):
    """This class used to create properties for TowTruck
        object and access the properties of TowTruck
        It also have a properties of Truck"""

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, organisation, max_tow_load):
        super().__init__(name, model, price, fuel_type, horse_power, fuel_capacity,
                         brand_name, seat_count, max_speed, truck_type, max_load)
        self.organisation = organisation
        self.max_tow_load = max_tow_load

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc} \n") \
            .format(name=self.name, model=self.model, price=str(self.price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def get_properties(self):
        print(self.__dict__)

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")

    def __del__(self):
        print(" Inside Destructor Method. \n Object destroyed.")


# Sports Car can inherit properties of Vehicle and Car
class SportsCar(Car, Truck):
    """This class used to create properties for SportsCar
        object and access the properties of SportsCar 
        It also have a properties of Car and Truck"""
    sports_cars = []

    def __init__(self, name, model, price, fuel_type, horse_power, fuel_capacity,
                 brand_name, seat_count, max_speed, gear_type, car_type, truck_type, max_load):
        super(Car, self).__init__(name, model, price, fuel_type, horse_power,
                                  fuel_capacity, brand_name, seat_count, max_speed, gear_type, car_type)
        super(Truck, self).__init__(name, model, price, fuel_type, horse_power,
                                    fuel_capacity, brand_name, truck_type)
        self.sports_cars.append(self)

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc} \n") \
            .format(name=self.name, model=self.model, price=str(self.price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def get_properties(self):
        print(self.__dict__)

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print(" This our privacy policy document read carefully.")

    def __del__(self):
        print("  Inside Destructor Method. \n Object destroyed.")


class Bike(Vehicle):
    """This class is used to create properties of bike and access the properties"""
    # class variable
    bike_show = "bike on the road vibes are good"
    bikes = []

    # instance method
    def __init__(self, name, model, price, fuel_type, horse_power,
                 fuel_capacity, brand_name, seat_count, max_speed, bike_type):
        super().__init__(name, model, price, fuel_type, horse_power,
                         fuel_capacity, brand_name, seat_count, max_speed)
        self.bike_type = bike_type
        self.bikes.append(self)

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc} \n") \
            .format(name=self.name, model=self.model, price=str(self.price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def get_properties(self):
        print(id(self.bike_show))
        self.bike_show = "welcome my ride"
        print(self.bike_show)
        print(id(self.bike_show))
        print(self.__dict__)

    # static method
    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print("\n This our privacy policy document read carefully.\n")

    # class method
    @classmethod
    def main(cls):
        """this is class method, and it used for access class variables."""
        print(id(cls.bike_show))
        cls.bike_show = "welcome my ride"
        print(Bike.bike_show)
        print(id(cls.bike_show))

    def __del__(self):
        print(" Inside Destructor Method. \n Object destroyed.")


honda = Bike('splendor', 'honda', 80000, 'petrol', '125CC', '10l', 'splendor125', 3, 100, 'normal')
hero = Bike('splendor', 'honda', 80000, 'petrol', '125CC', '11l', 'splendor125', 3, 120, 'normal')
honda.privacy()
honda.get_properties()
hero.privacy()
hero.get_properties()
print(Bike.bikes[0])
print(Bike.bikes[1])
Bike.main()
calculate_price(100)
SportsCar(input('Enter a bike name :'),
          input('Enter a bike model :'),
          int(input('Enter a bike price :')),
          input('Enter a bike fuel type :'),
          input('Enter a bike power :'),
          input('Enter a bike fuel capacity :'),
          input('Enter a bike brand name :'),
          int(input('Enter a bike seat :')),
          int(input('Enter a bike max speed :')),
          input('Enter a bike bike type :'),
          input('Enter a bike bike type :'),
          input('Enter a bike bike type :'),
          input('Enter a bike bike type :'))
print(SportsCar.sports_cars[0])
