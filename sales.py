#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


class Sales(object):
    """Manages sales"""

    def __init__(self):
        self.products = dict()

    def add_sale(self, code, price, name, cant):
        """This function adds sales to the daily sale list
         Args:
             code(string): product code
             price(string): product price
             name(string): product name
             price(float): product price

        Returns: None
        """
        if code in self.products:
            if (self.products[code][1]
                    == name and self.products[code][0] == price):
                self.products[code][2] = self.products[code][2] + cant
        else:
            self.products[code] = [price, name, cant]

    def print_sales(self):
        """This function prints the sales for the day
        Args:
             None

        Returns: None
        """
        total = 0
        print'Code\tProduct\t\tCant\tPrice\tTotal'
        print '----------------------------------------------'
        for key, value in self.products.iteritems():
            total += value[2]*value[0]
            print'{0} \t{1} \t{2} \t${3} \
                \t${4}'.format(key, value[1], value[2],
                               value[0], value[2]*value[0])
        print '----------------------------------------------'
        print 'Total \t* \t* \t* \t* \t${0}'.format(total)
        print 'Press enter to go to the main menu'
