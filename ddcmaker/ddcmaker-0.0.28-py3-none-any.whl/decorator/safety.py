from inspect import signature
from functools import wraps


def parameter_checking(*type_args, **type_kwargs):
    def decorate(func):
        sig = signature(func)
        bound_types = sig.bind_partial(*type_args, **type_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument [{}] must be {}'.format(name, bound_types[name]))
                    if value < 0:
                        raise ArithmeticError("Argument [{}] must be positive integer!".format(name))
            return func(*args, **kwargs)

        return wrapper

    return decorate


def upper_limit_check(attr_min, attr_max):
    def check(func):
        def make_decorater(*args, **kwargs):
            func_args = list(args)
            func_args.extend(kwargs.values())
            for arg in func_args:
                if attr_max < arg or arg < attr_min:
                    raise Exception("参数不满足指定范围，预期min:{}，max:{}，实际{}".format(attr_min, attr_max, arg))
            return func(*args, **kwargs)
        return make_decorater
    return check


def args_check(attr_type=(int,), attr_min=1, attr_max=30):
    def check(func):
        def decorater(*args, **kwargs):
            # args_num = len(args) + len(kwargs)
            # if args_num != attr_num:
            #     raise Exception("参数数量不对，预期{}，实际{}".format(attr_num, args_num))
            func_args = list(args)
            func_args.extend(kwargs.values())
            for arg in func_args:
                if not isinstance(arg, attr_type):
                    raise Exception("参数类型不对，预期{}，实际{}".format(attr_type, type(arg)))
            if len(func_args) != 0:
                if attr_max < func_args[0]:
                    raise Exception("参数{}超出上限:{}".format(func_args[0], attr_max,))
                if func_args[0] < attr_min:
                    raise Exception("参数{}超出下限:{}".format(func_args[0], attr_min, ))
            return func(*args, **kwargs)
        return decorater
    return check


# @args_check(attr_max=30)
# def add(a=1):
#     try:
#         c = a + 10
#     except:
#         c = 123
#     print(c)









