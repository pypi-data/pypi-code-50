import json

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
