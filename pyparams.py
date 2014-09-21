import re
def get_params_from_list(arglist):
    return get_params_from_str(' '.join(arglist))

def get_params_from_str(argstr):
    if '-' not in argstr:
        return argstr.split()
    args = argstr.split('-')[1:];
    is_full_name = False
    ret = dict()
    for arg in args:
        if not arg: is_full_name = True; continue
        key=''
        val=''
        if is_full_name:
            parts = re.split('=| ', arg.strip(), 1)
            key = parts[0]
            val = ' '.join(parts[1:])
            is_full_name = False
        else:
            key=arg[0].strip()
            val=arg[1:].strip()
        if not val:
            val = True
        elif ',' in val:
            val = [i.strip() for i in val.split(',')]
        ret[key] = val
    return ret

def get_params_strict (argstr, param_dict):
    print_param_dict(param_dict)
    return

def get_param_usage_string (param_dict):
    print ("would print param dict here:")
    print (param_dict)