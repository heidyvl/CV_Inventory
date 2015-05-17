#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""


class Store(object):
    """Store operations"""

    def __init__(self):
        """Class constructor"""
        self.products = dict()

    def product_exist(self, code):
        """This function checks if the product exists
            in the inventory
            Args:
            code(str) = product code
            Returns:
            Bool: true if exists
                  false id not"""

        if code in self.products:
            return True
        else:
            return False

    def get_product(self, code):
        """This function gets the product code
            from the inventory
            Args:
            code(str) = product code
            Returns:
            dict: product info"""

        if self.product_exist(code):
            return self.products[code]

    def add_product(self, code, name, price, cant=1):
        """This funtion adds product to the store
            Args:
            code(str) = product code
            name(str) = product name
            price(float) = product price
            cant(int) = products in stock
            Returns:
            None"""
        self.products[code] = [price, name, cant]

    def update_product(self, code, cant):
        """This function updates quantity
            of existing product
            Args:
            code(str) = product code
            cant(int) = number products to be added
            Returns:
            None"""
        self.products[code] = [self.products[code][0], self.products[code][1],
                               int(cant) + self.products[code][2]]

    def delete_product(self, code, cant=1):
        """This function updates quantity
            of product sold in inventory
            Args:
            code(str) = product code
            cant(int) = number products sold
            Returns:
            Bool: True in products available in stock
            False if quantity to be sold is larger tahn
            product in stock"""

        if self.product_exist(code):
            if self.products[code][2] >= cant:
                self.products[code][2] = self.products[code][2] - cant
                return True
            else:
                print 'Sorry but there are only\
                        '+ str(self.products[code][2]) + ' in stock'
                return False

    def del_product(self, code):
        """This function deletes products from
            the inventory
            Args:
            code(str) = product code
            Returns: None"""
        if self.product_exist(code):
            del self.products[code]
        else:
            print 'A product with Code {0} does not exists.'.format(code)
            print 'Please enter a valid product code'

    def print_inventory(self):
        """Tis function shows the total inventory of products"""
        print 'Code \t Product \t Cant. \t Price'
        print '-------------------------------------------'
        for k, val in self.products.items():
            print '{0} \t {1} \t {2} \t ${3}'.format(k, val[1], val[2], val[0])
        print 'Press enter to go to the main menu'
