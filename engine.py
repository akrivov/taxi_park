# -*- coding: utf-8 -*-
from park import Park
from constants import Constants

class Engine(object):
    def __init__(self):
        Park.car_list.append(self)
        self.vin = len(Park.car_list)
        if self.vin % 3 == 0:
            self.engine_type = Constants.Disel
        else:
            self.engine_type = Constants.Petrol
        self.mileage = 0
        self.fuel = 0
        self.fuel_price = self.engine_type.FUEL_PRICE
        self.consumption = self.engine_type.CONSUMPTION
        self.total_refuel = 0
        self.total_fuel_expenses = 0
