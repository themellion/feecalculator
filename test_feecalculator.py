#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:51:41 2019

@author: konstantinos.falangi
"""

import unittest
from feecalculator import feecalculator

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        loan_application = feecalculator(24, 2750)
        self.assertEqual(loan_application, 115)

unittest.main()