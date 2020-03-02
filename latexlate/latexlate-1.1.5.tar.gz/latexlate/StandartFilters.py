import re
from sympy import latex

filters = dict()


def filter(key):
    def decorator(func):
        filters[key] = func
        return func

    return decorator

@filter('latex')
def my_latex(sym):
    _default_settings = {'order': None,
 'mode': 'plain',
 'itex': False,
 'fold_frac_powers': False,
 'fold_func_brackets': False,
 'fold_short_frac': None,
 'long_frac_ratio': 2,
 'mul_symbol': None,
 'inv_trig_style': 'abbreviated',
 'mat_str': None,
 'mat_delim': '[',
 'symbol_names': {}}
    return latex(sym, **_default_settings)

@filter('upper')
def to_upper_case(string):
    return string.upper()


@filter('prec')
def preccision(value, precision=4):
    def repr(m):
        return '\.10^{' + str(int(m.group(1))) + '}'

    return str(re.sub(r'E([-+]\d+)', repr, '{value:.{precision}G}'.format(value=value, precision=precision)))

