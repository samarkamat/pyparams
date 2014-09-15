#!/usr/bin/env python

import sys
import pyparams

def test_abbrev_flag():
    flagstr = 'a'
    key = flagstr[0]
    val = flagstr[1:]

    print ("key: '" + key + "'")
    print ("val: '" + val + "'")

def test_argv():
    print ("This is the name of the script: " + sys.argv[0])
    print ("Number of arguments: "+ str(len(sys.argv)))
    print ("Arguments, ignoring the script name: " + str(sys.argv[1:]))

def test_spliting_mixed():
    teststr = "--named_flag -f --named_value 5 -v 5"
    print (teststr.split('-')[1:])

def test_splitting_in_list():
    testlist = ["word", "two words", "comma,separated, words"]
    print (list (n.split(',') for n in testlist))

def test_keyval_single_item():
    singleitemlist = ['a']
    print ("singleitemlist: '" + ' '.join(singleitemlist[1:]) + "'")

def test_print_param_dict():
    pyparams.print_param_dict({'abba': 4, 'beatles' : 6})

def test_get_params():
    teststr = "--named_flag -f --named_value 5 -v 5"
    params = pyparams.get_params(teststr)
    print (params)


test_get_params()

