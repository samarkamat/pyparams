#!/usr/bin/env python

import sys
import pyparams
import unittest

class ParamsTest (unittest.TestCase):
    def test_full(self):
        test_str = "--named_flag -f --named_value=5 -v5 --named_list 5,6,7 -l5,6,7"
        expected_params = {'named_value': '5', 'l': ['5', '6', '7'], 'named_list': ['5', '6', '7'], 'named_flag': True, 'f': True, 'v': '5'}
        test_params = pyparams.get_params_from_str(test_str)
        self.assertTrue(test_params == expected_params)

if __name__ == '__main__':
    unittest.main()


