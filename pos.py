#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

import store
import sales


class POS(object):
    """Class Point of Sale(POS)"""

    def __init__(self, name):
        self.name = name
        self.store = store.Store()
        self.sales = sales.Sales()

    def print_menu(self, option):

        """This function creates the system's menu
         Args:
             option(string): a value selecting one of the options of the menu
             Returns: None

        Examples:
           product = [('0001', 'Valnel', 5, '$32'),
           ('0002', 'Special 11', '$30'), ('0003', 'Deep Cleanser', '$22.75')]
           printMenu('1')
           'Enter Product Code'
           printMenu('2')
           'Code 	 Product 	 Cant. 	 Price
            -------------------------------------------
            0001 	 Valnel      	 5 	 $32
            0002 	 Special 11 	 1 	 $30
            0003 	 Deep Cleanser 	 1 	 $22.75


        """

        option_dict = {1: 'Sell Product', 2: 'View Inventory', 3: 'View \
                       Daily Sales', 4: 'Add New Product', 0: 'Exit', 5: '\
                       Update Existing Product', 6: 'Delete existing product'}
        print 'Please choose an option:'
        for key, value in option_dict.iteritems():
            print (key, value)
        if option == '0':
            exit()
        if option == '1':
            self.sell_product()
        if option == '2':
            self.store.print_inventory()
        if option == '3':
            self.sales.print_sales()
        if option == '4':
            self.add_product()
        if option == '5':
            self.update_product()
        if option == '6':
            self.del_product()

    def sell_product(self):
        """This function sells products
         Args:
           None
         Returns: None
        """

        option = 'y'
        while option == 'y':
            print 'Enter product code'
            code = raw_input()
            product = self.store.get_product(code)
            exists = self.store.product_exist(code)
            if product is not None and exists is True:
                print 'Product \t Price'
                print '{0} \t {1}'.format(product[1], product[0])
                print 'Please enter quantity'
                cant = int(raw_input())

                if self.store.delete_product(code, cant):
                    self.sales.add_sale(code, product[0], product[1], cant)
                    cost = cant*product[0]
                    print 'That will be ${0}.'.format(round(cost, 3))
                    print 'Please enter the cash'
                    cash = float(raw_input())
                    change = cash - cost
                    if change >= 0:
                        print 'Your change is ${0}'.format(round(change, 3))
                    else:
                        print'Please enter a valid ammount'
            else:
                print 'Wrong product code'

            print 'Do you want to sell another product? (y/n)'
            option = raw_input()

    def add_product(self):
        """This function adds products to the list fof products
         Args:
           None
         Returns: None
        """
        print 'Enter product code'
        code = raw_input()
        if self.store.product_exist(code):
            print 'A product with Code {0} already exists.'.format(code)
            print 'Please enter a new product code'
            self.add_product()
        else:
            print 'Enter product name'
            name = raw_input()
            print 'Enter product price'
            price = raw_input()
            print 'Enter product quantity'
            cant = raw_input()
            self.store.add_product(code, name, price, cant)
            print 'Your product with code ' + code + ' has been \
                   added to the inventory'
            print 'Press 2 to view your inventory or press enter to go \
                   to the main menu'

    def update_product(self):
        """This function updates quantity of products
         Args:
           None
         Returns: None

        """
        print 'Enter product code'
        code = raw_input()
        if not self.store.product_exist(code):
            print 'A product with Code {0} does not exists.'.format(code)
            print 'Please enter a valid product code'
            self.update_product()
        else:
            print 'Enter product quantity'
            cant = raw_input()
            self.store.update_product(code, cant)
            print 'Your product with code ' + code + ' has been updated'
            print 'Press 2 to view your inventory or press enter \
                   to go to the main menu'

    def del_product(self):
        """This function deletes products from the inventory
         Args:
           None
         Returns: None

        """
        print 'Enter product code'
        code = raw_input()
        print 'Your product with code ' + code + ' has been deleted'
        print 'Press 2 to view your inventory or press enter to \
               go to the main menu'
        self.store.del_product(code)
