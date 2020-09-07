#!/usr/bin/env python3

import unittest
from g_python.TimeOutDecider import *

# Class to test the json argument
class JsonTests(unittest.TestCase):

    def test_json_handler(self):
        self.assertIsNotNone(json_handler('C:\\Users\\gerar\\source\\repos\\master\\g_python\\python_tdd\\users.json') is not None)

# Class to test parsing dict to compare with app user input
class InputTest(unittest.TestCase):

    def test_input(self):
        self.assertIsNotNone(input(['Robert Webb', 'Gavin Coulson', 'Alan Allen'] ) is not None)
        
if __name__ == '__main__':
    unittest.main()