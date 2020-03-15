

import pandas as pd
from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def upper_bbands(df, ma_type, n, price="close", col="bbands", n_bdev=2):
    """
    Bollinger Bands are volatility bands placed above and below a moving average.
    Volatility is based on the standard deviation, which changes as volatility
    increases and decreases. The bands automatically widen when volatility
    increases and narrow when volatility decreases.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the desired price type of the asset.
        bbands (string): the column name for the bbands values.
        n_bdev_up (int): the standard deviation multiplier of the upper band.
        n_bdev_dn (int): the standard deviation multiplier of the lower band.
        ma_type (int): moving average type of the time series.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with average true range of the asset calculated.

    """

    ma_types = {"sma": sma, "ema": ema, "wma": wma, "dema": dema, "tema": tema}

    n_days_std = df[price].rolling(window=n).std(ddof=0)
    df = ma_types[ma_type](df, price, col + "_middle_band", n)
    df[col + "_upper_band"] = df[col + "_middle_band"] + (
        n_days_std * n_bdev_up
    )

    df = df.dropna().reset_index(drop=True)

    return df




def lower_bbands(df, price="close", col="bbands", n_bdev=2, ma_type, n):
    """
    Bollinger Bands are volatility bands placed above and below a moving average.
    Volatility is based on the standard deviation, which changes as volatility
    increases and decreases. The bands automatically widen when volatility
    increases and narrow when volatility decreases.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the desired price type of the asset.
        bbands (string): the column name for the bbands values.
        n_bdev_up (int): the standard deviation multiplier of the upper band.
        n_bdev_dn (int): the standard deviation multiplier of the lower band.
        ma_type (int): moving average type of the time series.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with average true range of the asset calculated.

    """

    ma_types = {"sma": sma, "ema": ema, "wma": wma, "dema": dema, "tema": tema}

    n_days_std = df[price].rolling(window=n).std(ddof=0)
    df = ma_types[ma_type](df, price, col + "_middle_band", n)
    
    df[col + "_lower_band"] = df[col + "_middle_band"] - (
        n_days_std * n_bdev_dn
    )
    df = df.dropna().reset_index(drop=True)


    return df