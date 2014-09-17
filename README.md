# pyparams

Python3 module to parse CLI parameters. argparse seemed too heavy-duty for some simple tools I was writing, so this aims to be something (appropriately) simpler. Feedback welcome!

## Parameter Types Supported

- Single char parameters that are preceded by a single '-' (as flags or values)
  - '-v'; '-v 5'; '-v5'; '-v5, 6, 7';  '-v5,6,7'; '-v 5,6,7'; '-v=5'
- Named parameters that are preceded by '--' (as flags or values)
  - '--flag'; '--value 5'; '--value 5,6,7'

## Value Types Supported

- Flags
  - returned dictionary element will have a value of True (planning to specify False for strict parameters)
- String
- List of Strings

## Usage

```
import sys
import pyparams

paramstr = ' '.join(sys.argv[1:])
params = get_params(paramstr)
port = params['port']
```

There are two intended uses that both accept a string of all the parameters joined by whitespace:
- Loose Parameter Parser: returns a dictionary of key/value pairs of all parameters passed in
- Strict Parameter Parser: accepts a dictionary of recognized keys (and expected types), and returns a dict matching those keys, or will throw an exception if an invalid parameter is found
  - YET TO BE IMPLEMENTED

