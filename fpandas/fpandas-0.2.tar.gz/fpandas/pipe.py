#!/usr/bin/env python
from typing import Optional, Callable, Sequence
from functools import reduce
import pandas as pd  # type: ignore
from .exceptions import DataFramePipeFailure


def pipe(
    functions: Sequence[Callable[[pd.DataFrame], Optional[pd.DataFrame]]],
    dataframe: pd.DataFrame
) -> pd.DataFrame:
    def f_after_g(
        f: Callable[[pd.DataFrame], pd.DataFrame],
        g: Callable[[pd.DataFrame], pd.DataFrame]
    ) -> Callable[[pd.DataFrame], pd.DataFrame]:
        def maybe_df(df: Optional[pd.DataFrame]) -> Optional[pd.DataFrame]:
            df = g(df)
            if df is not None:
                df = f(df)
                return df
            return None

        return maybe_df

    return reduce(f_after_g, functions)(dataframe)

class SafePiper:
    func: Optional[Callable[[pd.DataFrame], pd.DataFrame]] = None
    def __init__(self, kind: str = 'print'):
        if kind not in ('print', 'raise'):
            print(ValueError(f'please supply print or raise to {self.__class__}'))
        self.kind = kind

    def __call__(self, *arguments: Optional[pd.DataFrame]) -> pd.DataFrame:
        if not self.func:
            self.func = arguments[0]
            return self
        try:
            return self.func(*arguments)
        except Exception as exc:
            failure = DataFramePipeFailure(
                    f'Pipe failed at function {self.func.__name__} because {exc.__repr__()}: {exc}'
                )
            if self.kind == 'print':
                print(failure)
                return None
            if self.kind == 'raise':
                raise failure
