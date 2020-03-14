def _is_primitive(obj):
    return obj.__class__ in [str, float, int, bool]


def _is_list(obj):
    return obj.__class__ in [list]


def _is_json_object(obj):
    return obj.__class__ in [dict]


def _is_list_with_generic(type):
    return hasattr(type, '_name') and type._name == "List"


def _get_generic(signature):
    return signature.__args__[0]


def _deserialize_json_list_to(json_list, type):
    return [_marshal_dictionary_to_object(e, type) for e in json_list]


def _deserialize_json_object_to(json_obj, type):
    return _marshal_dictionary_to_object(json_obj, type)


def _marshal_dictionary_to_object(dictionary, object_type):
    resp_obj = object_type()
    for k, v in dictionary.items():
        if hasattr(resp_obj, k):
            if _is_primitive(v):
                setattr(resp_obj, k, v)
            elif _is_json_object(v):
                setattr(resp_obj, k, _marshal_dictionary_to_object(v, object_type.types[k]))
            elif _is_list(v):
                setattr(resp_obj, k, [_marshal_dictionary_to_object(e, _get_generic(object_type.types[k])) for e in v])
    return resp_obj
