#!/usr/bin/env python

import sys
import pyparams
import unittest

class ParamsTest (unittest.TestCase):
    def setUp(self):
        #self.test_str = "--named_flag -f --named_value=5 -v5 --named_list 5,6,7 -l5,6,7"
        #self.expected_params = {'named_value': '5', 'l': ['5', '6', '7'], 
        #    'named_list': ['5', '6', '7'], 'named_flag': True, 
        #    'f': True, 'v': '5'}
        self.test_argv = ['--named_flag', '--named_value', '5', '--named_list', '4,5,6', 
            '-f', '-wv=5',  '--quote_val', '"This is a quoted value"', 
            'anon_val', '"anonymous quoted val"',
            '--named_val_with_equal=5', '--named_list_with_equal=8,9,0']
        self.expected_params = {'named_flag': True, 'named_value': '5', 
            'named_list': ['4','5','6'], 
            'f': True, 'v': '5', 'quote_val': 'This is a quoted value', 
            '': ['anon_val', 'anonymous quoted val'], 'named_val_with_equal': '5',
            'named_list_with_equal': ['8','9','0'], 'w': True}


#    def test_param_str(self):
#        test_params = pyparams.get_params_from_str(self.test_str)
#       self.assertTrue(test_params == self.expected_params)
#
    def test_param_list(self):
        test_params = pyparams.get_params_from_list(self.test_argv)
        #print (test_params)
        self.assertEqual(test_params, self.expected_params)


if __name__ == '__main__':
    unittest.main()
