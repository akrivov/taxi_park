# -*- coding: utf-8 -*-
from constants import engine_properties
import random


class Engine(object):

    def __init__(self, type):
        self.route = random.randint(55000, 286000)
        self.type = type
        self.mileage = 0
        self.tank_volume = 60
        self.fuel = 0
        self.expenses = 0
        self.cost = 10000
        self.fuel_price = engine_properties.get(type).get('FUEL_PRICE')
        self.consumption = engine_properties.get(type).get('CONSUMPTION')
        self.total_refuel = 0
        self.total_fuel_expenses = 0
