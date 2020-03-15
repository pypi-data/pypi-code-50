import pandas as pd

from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema

def stochf(df, fast_k_n, fast_d_n, high="high", low="low", close="close", fast_d_ma_type=0,col="stochf"):
    """
    The Stochastic Oscillator is another well-known momentum indicator used in
    technical analysis. The idea behind this indicator is that the closing
    prices should predominantly close in the same direction as the prevailing
    trend.

    In an upward trend the price should be closing near the highs of the trading
    range and in a downward trend the price should be closing near the lows of
    the trading range. When this occurs it signals continued momentum and
    strength in the direction of the prevailing trend.

    Fast Stochastic Oscillator:
        Fast %K = %K basic calculation
        Fast %D = n period moving average of Fast %K

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        fast_k_n (int): the time period of the fast k moving average.
        fast_d_n (int): the time period of the fast d moving average.
        fast_d_ma_type (int): Moving average type for the slow d moving average.

    Returns:
        df (pd.DataFrame): Dataframe with fast %k and fast %d of the asset calculated.

    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < n:
        df[col] = None
        return df


    ma_types = {"sma": sma, "ema": ema, "wma": wma, "dema": dema, "tema": tema}

    hh = df[high].rolling(window=fast_k_n).max()
    ll = df[low].rolling(window=fast_k_n).min()
    df["fast_%k"] = (df[close] - ll) / (hh - ll) * 100
    df = ma_types[fast_d_ma_type](
        df[fast_k_n - 1 :], "fast_%k", "fast_%d", fast_d_n
    )

    df[col] = 0

    #df = df.dropna().reset_index(drop=True)

    return df
