class Vehicle:
    # Constructor of Vehicle
    def __init__(self, engine):
        print('Inside Vehicle Constructor')
        self.engine = engine


class Car(Vehicle):
    # Constructor of Car
    def __init__(self, engine, speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.speed = speed

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


class Electric_Car(Car):
    # Constructor of Electric Car
    def __init__(self, engine, speed, km_range):
        super().__init__(engine, speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')

    # destructor it calls automatically when reference
    # count id zero once it called all connection in closed
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')


# Object of electric car
ev = Electric_Car('1500cc', 240, 750)
print(f'Engine={ev.engine}, Max Speed={ev.speed}, Km range={ev.km_range}')
# del ev
ev.max_speed()
ev.change_gear()
car = Car('Car x1', 'Red')
# calls methods from Car class
car.max_speed()
car.change_gear()

