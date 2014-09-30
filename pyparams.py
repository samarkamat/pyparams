import re       # used for split
modname = 'pyparams'
def super_split(string, delim):
    ret = [i.strip() for i in string.split(delim)]
    while ret.count(''):
        ret.remove('')
    return ret

def get_params(arglist):
    ret = dict()
    ret[''] = []
    is_key = False
    look_for_val = False
    key = ''
    for arg in arglist:
        arg = arg.strip()
        #print ("arg: ", arg)
        is_key = arg[0] == '-'
        if is_key:
            # check if full named or abbreviated
            #print ('\tkey')
            if arg[0:2] == '--':
                #print ("\t\tnamed key")
                # Named Key
                arg = arg[2:]
                argtoks = super_split(arg,'=')
                key = argtoks[0]
                if len(argtoks) == 2:
                    #print ('\t\twith val: ', argtoks[1])
                    val = argtoks[1]
                    if ',' in val:
                        val = super_split(val, ',')
                    ret[key] = val
                    key = ''
                elif len(argtoks) > 2:
                    print (modname, ":ERROR: Could not parse argument: ", arg)
                else:
                    ret[key] = True
            else:
                #print ('\t\tabbrev key')
                # Abbreviated Key
                arg = arg[1:]
                argtoks = arg.split('=')
                is_value_present = len(argtoks) == 2
                #if is_value_present: 
                    #print('\t\twith val: ', argtoks[1])
                for i in argtoks[0][0:-1]:
                    ret[i] = True
                last_abbrev_key = argtoks[0][-1]
                if not is_value_present:
                    ret[last_abbrev_key] = True
                else:
                    val = argtoks[1].strip()
                    if ',' in val:
                        valtoks = super_split(val, ',')
                        ret[last_abbrev_key] = valtoks
                    else:
                        ret[last_abbrev_key] = val
                        #print ('set key: ', key, ' to val: ', val)
        else:
            #print ('\tvalue, current key is ', key)
            # not key
            if arg[0] == '"' and arg[-1] == '"':
                arg = arg[1:-1]
            if ',' in arg:
                arg = super_split(arg, ',')
            if key == '':
                if isinstance(arg, list):
                    ret[''].extend(arg)
                else:
                    ret[''].append(arg)
            else:
                ret[key] = arg

            # reset the key to empty
            key = ''
    return ret

def get_params_strict (argstr, param_dict):
    return

def get_param_usage_string (param_dict):
    print ("would print param dict here:")
    print (param_dict)
    return