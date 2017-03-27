# -*- coding: utf-8 -*-
from engine import Engine
from constants import engine_properties
from park import Park


class Car(object):
    def __init__(self):
        Park.car_list.append(self)
        self.serial_number = len(Park.car_list)
        if self.serial_number % 3 == 0:
            type = 'disel'
        else:
            type = 'petrol'
        Car.get_car(self, type)
        if self.serial_number % 5 == 0:
            self.tank_volume = 75


    def get_car(self, type):
        """creates car with engine"""
        engine = Engine(type)
        self.route = engine.route
        self.engine_type = engine.type
        self.tank_volume = engine.tank_volume
        self.fuel = engine.fuel
        self.expenses = engine.expenses
        self.cost = engine.cost
        self.fuel_price = engine.fuel_price
        self.consumption = engine.consumption
        self.mileage = engine.mileage
        self.tank_volume =engine.tank_volume
        self.total_fuel_expenses = engine.total_fuel_expenses
        self.total_refuel = engine.total_refuel


    def calc_residual_value(self, type):
        """Calculates residual price of the car"""
        residual_value = self.cost - (self.mileage / 1000 * engine_properties.get(type).get('FALLING_PRICE'))
        return residual_value


    def get_info(self):
        """Print info"""
        print('serial nimber: %r' % self.serial_number)
        print('engine_type : %r' % self.engine_type)
        print('mileage : %r' % self.mileage)
        print('residual_price : %r' % self.calc_residual_value(self.engine_type))
        print('tank_volume : %r' % self.tank_volume)
        print('expenses : %r' % self.expenses)
        print('refuel : %r' % self.total_refuel)
        print('total_fuel_expenses : %r' % self.total_fuel_expenses)
        print ('')

    def expend_fuel(self):
        """Calculates fuel"""
        self.fuel =  self.fuel - self.consumption / 100.0
        return self.fuel


    def increases_consumption(self):
        """Calculates consumption for old cars"""
        self.consumption += self.consumption * 0.01


    def refuel(self):
        """Refueling car when fuel is less than one liter """
        need_fuel = self.tank_volume - self.fuel
        need_money = need_fuel * self.fuel_price
        self.expenses = self.expenses + need_money
        self.fuel = self.tank_volume
        self.total_fuel_expenses += need_money
        self .total_refuel += 1
        return self.expenses


    def overhaul(self, type):
        self.expenses += engine_properties.get(type).get('OVERHAUL_PRICE')


    def ride(self):
        """Starts the route"""
        while self.mileage < self.route:
            if self.fuel <= 1:
                self.refuel()
            self.mileage += 1
            self.expend_fuel()
            if self.mileage % 1000 == 0:
                self.increases_consumption()
            if self.mileage % (engine_properties.get(self.engine_type).get('OVERHAUL_PRICE')) == 0:
                self.overhaul(self.engine_type)
