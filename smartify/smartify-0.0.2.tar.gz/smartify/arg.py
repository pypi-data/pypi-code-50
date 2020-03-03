import inspect


def get_arg_dict(func, *args, **kwargs):
    arg_dict = dict()
    parameters = inspect.signature(func).parameters
    for parameter in parameters:
        param = parameters[parameter]
        arg_dict[parameter] = param.default
    args_name = list(parameters.keys()) + list(kwargs.keys())
    arg_dict.update(dict(zip(args_name, args)))
    arg_dict.update(kwargs)
    return arg_dict
