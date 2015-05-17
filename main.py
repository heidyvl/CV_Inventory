#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A docstring."""

import pos

POS = pos.POS('My Store')
POS.store.add_product('0001', 'Valnel', 32.95, 5)
POS.store.add_product('0002', 'Deep Cleanser', 28.50)
POS.store.add_product('0003', 'Valora I', 22.75)

OPTION = None
while OPTION != 0:
    POS.print_menu(OPTION)
    OPTION = raw_input()
