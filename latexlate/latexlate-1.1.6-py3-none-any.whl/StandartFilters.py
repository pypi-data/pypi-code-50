import re



filters = dict()


def filter(key):
    def decorator(func):
        filters[key] = func
        return func

    return decorator

@filter('upper')
def to_upper_case(string):
    return string.upper()


@filter('prec')
def preccision(value, precision=4):
    def repr(m):
        return '\.10^{' + str(int(m.group(1))) + '}'

    return str(re.sub(r'E([-+]\d+)', repr, '{value:.{precision}G}'.format(value=value, precision=precision)))

