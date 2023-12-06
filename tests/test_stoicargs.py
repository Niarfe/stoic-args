import sys
import os

print("syspath", sys.path)
print(os.getcwd())
sys.path.append(os.getcwd())
print("syspath", sys.path)
print(os.getcwd())

from stoicargs.parser import parse

def test_kwargs():
    cline = "one=1 name=marion"
    kwargs, _ = parse(cline)
    print("kwargs", kwargs)
    assert len(kwargs) == 2, f"Expected a dictionary of 2 items, but got {len(kwargs)}, {kwargs}"
    assert isinstance(kwargs, dict), f"Expected kwargs to be a dict, but got {type(kwargs)}"
#
#    assert kwargs["one"] == 1, f"Expected kwargs 'one' to be int 1 but got {kwargs['one']}"
#    assert isinstance(kwargs["one"], int), f"Expected kwags 'one' to be converted to int, but got {type(kwargs['one'])}"
#
#    assert kwargs["name"] == 'marion', f"Expected kwargs 'name' to be 'marion' but got {kwargs['name']}"
#    assert isinstance(kwargs["name"], str), f"Expected kwags 'one' to be a str, but got {type(kwargs['marion'])}"
#
