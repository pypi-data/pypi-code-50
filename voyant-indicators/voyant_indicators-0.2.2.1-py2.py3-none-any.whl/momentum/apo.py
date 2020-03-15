import pandas as pd
from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def apo(df, price, col, fast_period, slow_period, ma_type):
    """
    The Absolute Price Oscillator (APO) shows the difference between two moving
    averages. It is basically a MACD, but the Price Oscillator can use any time
    periods. A buy signal is generated when the Price Oscillator rises above
    zero, and a sell signal when the it falls below zero.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        fast_period (int): the time period of the fast moving average.
        slow_period (int): the time period of the slow moving average.
        ma_type (int): Moving average type.

    Returns:
        df (pd.DataFrame): Dataframe with apo of the asset calculated.

    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < slow_period:
        df[col] = None
        return df

    ma_types = {"sma":sma, "ema" : ema, "wma": wma, "dema": dema, "tem": tema}

    df = ma_types[ma_type](df, price, col + "_fast", fast_period)
    df = ma_types[ma_type](df, price, col + "_slow", slow_period)
    df[col] = df[col + "_fast"] - df[col + "_slow"]
    df = df.dropna().reset_index(drop=True)

    return df
