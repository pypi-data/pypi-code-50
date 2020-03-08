import datacode as dc
import numpy as np
from sympy import Symbol


def log_name_func(name: str, *args, **kwargs) -> str:
    return f'Ln({name})'


def log_symbol_func(sym: Symbol, *args, **kwargs) -> Symbol:
    sym_str = str(sym)
    new_sym_str = r'\text{Ln}(' + sym_str + ')'
    sym = Symbol(new_sym_str)
    return sym


def log_data_func(col: dc.Column, variable: dc.Variable, source: dc.DataSource, shift: float = 0) -> dc.DataSource:
    source.df[variable.name] = np.log(source.df[variable.name] + shift)

    return source


log_transform = dc.Transform(
    'log',
    name_func=log_name_func,
    data_func=log_data_func,
    symbol_func=log_symbol_func,
    data_func_target='source'
)