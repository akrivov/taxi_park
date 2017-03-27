from car import Car
from park import Park

while len(Park.car_list) < 5:
    car = Car()
    car.ride()
    car.get_info()

