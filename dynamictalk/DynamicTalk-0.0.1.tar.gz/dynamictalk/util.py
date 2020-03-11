from datetime import datetime
import copy


def memoize_ignore_self(func):

    def new_cache() -> (dict, datetime.date):
        return dict(), datetime.utcnow().date()
    
    cache, cache_date = new_cache()

    def memoized_func(*args):
        nonlocal cache
        nonlocal cache_date
        if cache_date < datetime.utcnow().date():
            cache, cache_date = new_cache()
        if args[1] in cache:
            return copy.deepcopy(cache[args[1]])
        result = func(*args)
        cache[args[1]] = copy.deepcopy(result)
        return result

    return memoized_func


def capitalize_first_letter(string: str) -> str:
    list_string = list(string)
    list_string[0] = list_string[0].upper()
    return ''.join(list_string)