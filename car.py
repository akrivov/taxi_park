# -*- coding: utf-8 -*-
from engine import Engine
from constants import Constants
import random


class Car(object):
    def __init__(self):
        self.engine = Engine()
        self.cost = Constants.Common.COST
        self.expenses = 0
        # self.route = random.randint(55000, 286000)
        self.route = 150
        if not self.engine.vin % 5:
            self.tank_volume = Constants.Common.TANK_VOLUME_INCREASED
        else:
            self.tank_volume = Constants.Common.TANK_VOLUME


    def calc_residual_value(self):
        """Calculates residual price of the car"""
        residual_value = self.cost - (self.engine.mileage / 1000 * self.engine.engine_type.FALLING_PRICE)
        return residual_value


    def get_info(self):
        """Print info"""
        print('serial nimber: %r' % self.engine.vin)
        print('engine_type : %r' % self.engine.engine_type.NAME)
        print('mileage : %r' % self.engine.mileage)
        print('residual_price : %r' % self.calc_residual_value())
        print('tank_volume : %r' % self.engine.engine_type.NAME)
        print('expenses : %r' % self.expenses)
        print('refuel : %r' % self.engine.total_refuel)
        print('total_fuel_expenses : %r' % self.engine.total_fuel_expenses)
        print ('')


    def expend_fuel(self):
        """Calculates fuel"""
        self.engine.fuel = self.engine.fuel - self.engine.engine_type.CONSUMPTION / 100.0
        return self.engine.fuel


    def increases_consumption(self):
        """Calculates consumption for old cars"""
        self.engine.engine_type.CONSUMPTION *= Constants.Common.CONSUMPTION


    def refuel(self):
        """Refueling car when fuel is less than one liter """
        need_fuel = self.tank_volume - self.engine.fuel
        need_money = need_fuel * self.engine.engine_type.FUEL_PRICE
        self.engine.expenses = self.expenses + need_money
        self.engine.fuel = self.tank_volume
        self.engine.total_fuel_expenses += need_money
        self.engine.total_refuel += 1


    def overhaul(self):
        """Calculates overhaul price"""
        self.expenses += self.engine.engine_type.OVERHAUL_PRICE


    def ride(self):
        """Starts the route"""
        while self.engine.mileage < self.route:
            if self.engine.fuel <= 1:
                self.refuel()
            self.engine.mileage += 1
            self.expend_fuel()
            if not self.engine.mileage % 1000:
                self.increases_consumption()
            if not self.engine.mileage % self.engine.engine_type.OVERHAUL:
                self.overhaul()
