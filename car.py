# -*- coding: utf-8 -*-
from engine import Engine
from constants import petrol, disel
from park import Park

class Car(object):
    def __init__(self, engine = Engine()):
        Park.car_list.append(self)
        self.serial_number = len(Park.car_list)
        if self.serial_number % 3 == 0:
            type = 'disel'
            Car.get_car(self, type)
        else:
            type = 'petrol'
            Car.get_car(self, type)


    def get_car(self, type):
        self.tank_volume = 60
        self.fuel = 0
        self.expenses = 0
        self.cost = 10000
        self.engine_type = eval(type).TYPE
        self.fuel_price = eval(type).FUEL_PRICE
        self.consumption = eval(type).CONSUMPTION
        self.mileage = 0


    def calc_residual_value(self, type):
        residual_value = self.cost - (self.mileage / 1000 * eval(type).FALLING_PRICE)
        return residual_value

    def get_info(self):
        print('serial nimber: %r' % self.serial_number)
        print('mileage : %r' % self.mileage)
        print('residual_value : %r' % self.calc_residual_value(self.engine_type))

    def expend_fuel(self,):
        self.fuel =  self.fuel - self.consumption / 100.0
        return self.fuel

    def refuel(self):
        need_fuel = self. tank_volume - self.fuel
        need_money = need_fuel * self.fuel_price
        self.expenses = self.expenses + need_money
        self.fuel = self.tank_volume
        return self.expenses



    def go(self, route):
        while self.mileage < route:
            if self.fuel <= 1:
                self.refuel()
            self.mileage = self.mileage + 1
            self.expend_fuel()




wv = Car()

wv.go(750)
wv.get_info()

dd = Car()
dd.get_info()

ss = Car()
ss.go(23234)
ss.get_info()
