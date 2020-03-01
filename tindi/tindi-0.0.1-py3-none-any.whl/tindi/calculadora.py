#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""
Calculadora: Padres >> Hijos
"""

__author__ = "Marcelo Nuñez"
__copyright__ = "Copyright 2020, Tindi"
__credits__ = "PalCole"

__licence__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Marcelo Nuñez"
__email__ = "real.nugatti@gmail.com"
__status__ = "Developer"




import math

class Calculadora():
    def __init__(self):
        self.value_one = 0
        self.value_two = 0
        self.value_three = 0

    def suma(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two
        """Esto se encarga de sumar"""
        result = self.value_one + self.value_two
        print(f"La suma es: {result}")

    def resta(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two
        """Esto se encarga de restar"""
        result = self.value_one - self.value_two
        print(f"La resta es: {result}")

    def multiplica(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two
        """Esto se encarga de multiplicar"""
        result = self.value_one * self.value_two
        print(f"La multiplicación es: {result}")

    def divide(self, value_one, value_two):
        self.value_one = value_one
        self.value_two = value_two
        """Esto se encarga de dividir"""
        result = self.value_one * self.value_two
        print(f"La división es: {result}")

    def raiz_cuadrada(self, value_three):
        self.value_three = value_three
        """Esto se encarga de sacar raiz cuadrada"""
        result = math.sqrt(self.value_three)
        print(f"La raiz cuadrada es: {result}")


#End of the program, thanks ;).
