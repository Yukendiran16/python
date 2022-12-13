from collections import deque

weather_deque = deque(maxlen=2)
IS_CONTINUE = True


class Weather:
    def __init__(self, _date="DD/MM/YYYY", day="day", city="chennai", max_temp="0C", min_temp="0C"):
        self.date = _date
        self.day = day
        self.city = city
        self.max_temp = max_temp
        self.min_temp = min_temp
        weather_deque.append(self)


is_continue = IS_CONTINUE
while is_continue:
    Weather(input("Enter date of weather report :  "),
            input("Enter day of weather report :  "),
            input("Enter city of weather report :  "),
            input("Enter maximum temperature of weather report :  "),
            input("Enter minimum temperature of weather report :  ")
            )
    value = input("If you continue enter 1 else enter 0  ")
    if value == "0":
        is_continue = False


print(weather_deque.pop().__dict__)
print(weather_deque.popleft().__dict__)

