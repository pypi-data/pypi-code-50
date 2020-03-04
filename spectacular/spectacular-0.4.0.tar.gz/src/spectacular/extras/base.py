def type_checker(registry, name):
    def decorator(fn):
        registry[name] = fn
        return fn

    return decorator


TYPE_CHECKERS = {}
