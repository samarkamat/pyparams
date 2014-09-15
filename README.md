pyparams
========

python module to manage CLI parameters

Parameter Types Supported
=========================

- Single char parameters that are preceded by a single '-' (as flags or values)
  - '-v'; '-v 5'; '-v5'; '-v5, 6, 7';  '-v5,6,7'; '-v 5,6,7'
- Named parameters that are preceded by '--' (as flags or values)
  - '--flag'; '--value 5'; '--value 5,6,7'

Value Types Supported
=====================
- Flags
  - returned dictionary element will have a value of True (planning to specify False for strict parameters)
- String
- List of Strings

Usage
=====
There are two intended uses that both accept a string of all the parameters joined by whitespace:
- Loose Parameter Parser: returns a dictionary of key/value pairs of all parameters passed in
- Strict Parameter Parser: accepts a dictionary of recognized keys (and expected types), and returns a dict matching those keys, or will throw an exception if an invalid parameter is found
  - YET TO BE IMPLEMENTED

