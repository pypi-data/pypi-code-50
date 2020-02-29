import json

__version__ = '0.0.2'

def hello():
    """Says hello from Simon Fong"""
    msg = "Hello from Simon Fong!"
    print(msg)

def dumps(obj):
    obj_str = json.dumps(
        obj,
        indent=4,
        sort_keys=True
    )

    return obj_str

def j_print(obj):
    obj_str = dumps(obj)
    print(obj_str)
