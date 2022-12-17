from abc import ABC, abstractmethod


def calculate_price(price):
    return price + price * 2.5 + 1000


class Vehicle(ABC):
    """This class used to create properties for Vehicle
    object and access the properties of Vehicle"""

    @staticmethod
    @abstractmethod
    def privacy():
        pass


class Bike(Vehicle):
    """This class is used to create properties of bike and access the properties"""

    # class variable
    bike_show = "bike on the road vibes are good"

    # instance method
    def __init__(self, name='name', model='model', price=0, fuel_type='fuel', horse_power='0cc',
                 fuel_capacity='0l', brand_name='brand', seat_count=0, max_speed=0, bike_type='bike'):
        super(Bike, self).__init__()
        self.name = name
        self.model = model
        self._price = self.__calculate_price(price)
        self.fuel_type = fuel_type
        self.horse_power = horse_power
        self.fuel_capacity = fuel_capacity
        self.brand_name = brand_name
        self._seat_count = seat_count
        self.__max_speed = max_speed
        self.bike_type = bike_type
        bikes.append(self)

    # getter method
    def get_price(self):
        """getting price of the vehicle using getter method"""
        return self._price

    # setter method
    def set_price(self, price):
        """set price of the vehicle using setter method"""
        self._price = calculate_price(price)

    # getter method
    def get_max_speed(self):
        """getting max speed of the vehicle using getter method"""
        return self.__max_speed

    # setter method
    def set_max_speed(self, max_speed):
        """set max speed of the vehicle using setter method"""
        self.__max_speed = max_speed

    @staticmethod
    def __calculate_price(price):
        """Calculate price of the vehicle with tax"""
        return price + price * 2.7 + 1000

    @staticmethod
    def privacy():
        """This is the static method it doesn't have self or cls arguments."""
        print("\n This our privacy policy document read carefully.")

    @classmethod
    def main(cls):
        """this is class method, and it used for access class variables."""
        cls.bike_show = "welcome my ride"

    def __repr__(self):
        """This method is instance method of the class it return all property of the class."""
        return ("\n name : {name} \n model : {model} \n price : {price} \n "
                + "fuelType : {fuel} \n horsePower : {hp} \n fuel_capacity : {fc}") \
            .format(name=self.name, model=self.model, price=str(self._price),
                    fuel=self.fuel_type, hp=self.horse_power, fc=self.fuel_capacity)

    def __del__(self):
        print("\nInside Destructor Method. \n Object destroyed.")


bikes = []
honda = Bike('splendor', 'honda', 80000, 'petrol', '125CC', '10l', 'splendor125', 3, 100, 'normal')
hero = Bike('splendor', 'honda', 80000, 'petrol', '125CC', '11l', 'splendor125', 3, 120, 'normal')
print(honda)
print(hero)

