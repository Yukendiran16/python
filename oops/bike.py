class Bike(object):
    """This class is used to create properties of bike and access the properties"""
    # class variable
    bike_show = "bike on the road vibes are good"

    # object initialization
    # parameterized constructor
    def __init__(self, name, model, price, fuel_type, horse_power, engin, fuel_capacity):
        # self keyword used to access the instance variable and instance method of the object.
        # data members (instance variables)
        self.name = name
        self.model = model
        self.price = price
        self.fuel_type = fuel_type
        self.horse_power = horse_power
        self.engin = engin
        self.fuel_capacity = fuel_capacity

    # instance method
    def get(self):
        """This method is instance method of the class it return all property of the class."""
        return " name : " + self.name + "\n model : " + self.model \
               + "\n price : " + str(self.price) + "\n fuelType : " + self.fuel_type \
               + "\n horsePower : " + self.horse_power + "\n engin : " + self.engin \
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


# TypeError: Bike.__init__() missing 6 required positional arguments
# new = Bike('name')
# create a new object for class bike
bike = Bike('MT15', 'YAMAHA', 150000, 'petrol', '150CC', 'tata-182', '10L')
print(bike.get())    # get all property of the bike
Bike.main(" 'bike on the road vibes are good'")   # call the class method using class name
bike.privacy()
