# -*- coding: utf-8 -*-

class Constant(object):
    pass

class Petrol(Constant):
    TYPE = 'petrol'
    FUEL_PRICE = 2.4
    PETROL_92_PRICE = 2.2
    CONSUMPTION = 8
    OVERHAUL = 100000
    OVERHAUL_PRICE = 500
    FALLING_PRICE = 9.5

petrol = Petrol()

class Disel(Constant):
    TYPE = 'disel'
    FUEL_PRICE = 1.8
    CONSUMPTION = 6
    OVERHAUL = 150000
    OVERHAUL_PRICE = 700
    FALLING_PRICE = 10.5

disel = Disel()
