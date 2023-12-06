"""
stoicargs - the simplest argparse for when just need the basics for prototyping etc.

Simply pass sys.argv to stoicargs and it will return a dictionary with the kwargs
    and a lit of flags.

Any kwargs required arguments should be passed in the 'required' list

example: call your script as
<myscript>  widgets=20

means you'll see  { 'widgets': '20' }  echoed when you load.

The flags are for args passed in without a '=', so "<myscript> debug"  means you can then do something like 

if 'debug' in flags:
   do-something
"""
import sys

def digitize(arg):
    return int(arg) if arg.isdigit() else arg

def parse(sys_argv, required=[], echo=True):
    kwargs = { arg.split('=')[0]:digitize(arg.split('=')[1]) for arg in sys.argv[1:] if '=' in arg }
    flags = [f for f in sys.argv[1:] if '=' not in f ]
    missing = set(required).difference(set(kwargs.keys())) if required else []
    
    assert not missing, "parameter(s) are missing: {}".format(missing)
    assert kwargs or flags, "Pass in key=val, (no spaces), or simply key1 key1 combinations"
    
    if echo:
        print(kwargs, flags)

    return flags, kwargs
