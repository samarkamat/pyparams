# pyparams

Python3 module to parse CLI parameters. argparse seemed too heavy-duty for some simple tools I was writing, so this aims to be something (appropriately) simpler. Feedback welcome!

## Parameter Types Supported

- Single char parameters that are preceded by a single '-' (as flags or values)
  - '-f'
  - '-v=5'
- Named parameters that are preceded by '--' (as flags or values)
  - '--flag'
  - '--value=5'
- Anonymous values are parameters that have no keys (think `cp file1 file2`). In the returned map, these values are appended to a list with a key of '' like `{'': ['file1', 'file2']}`

## Value Types Supported

- Flags
  - returned dictionary element will have a value of True (planning to specify False for strict parameters)
- String
- List of Strings, comma separated
  - cannot have spaces between the values or commas (5,6,7,yabba,dabba,doo)

NOTE: Strings or lists can follow full named keys with a space or a '='. They can follow abbeviated keys without space necessary. For example:
`-v4 -fw 5 -x=6 --named_val 7 --named_val2=abba`
would yield:
`{'v': '4', 'f': True, 'w': '5', 'x': '6', 'named_val': '7', '--named_val2': 'abba' }`

## Usage

```
import sys
import pyparams

params = get_params(sys.argv[1:])
port = params['port']
host = params['host']
verbose = params['v'] or params['verbose']
```

There are two intended uses that both accept a string of all the parameters joined by whitespace:
- Loose Parameter Parser: returns a dictionary of key/value pairs of all parameters passed in
- Strict Parameter Parser: accepts a dictionary of recognized keys (and expected types), and returns a dict matching those keys, or will throw an exception if an invalid parameter is found
  - YET TO BE IMPLEMENTED

