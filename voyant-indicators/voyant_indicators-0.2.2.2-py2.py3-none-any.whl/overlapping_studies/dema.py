import pandas as pd
from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma


def dema(df, price, col, n):
    """
    Double Exponential Moving Average (DEMA) attempts to offer a smoothed average
    with less lag than a straight exponential moving average.

    The DEMA equation doubles the EMA, but then cancels out the lag by subtracting
    the square of the EMA.

    DEMA = 2 * EMA(p, n) - EMA(EMA(p, n), n)

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        dema (string): the column name for the n-day double exponential moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day double exponential moving average of the asset calculated.


    """


    df = df.copy().reset_index(drop=True)

    if df.shape[0] < n:
        df[col] = None
        return df

    df = ema(df, price, col + "_ema", n)
    df = ema(df[n - 1 :], col + "_ema", col + "_ema_2", n)
    df[col] = 2 * df[col + "_ema"] - df[col + "_ema_2"]

    print(df)
    #df = df.dropna().reset_index(drop=True)
    df.drop([col + "_ema", col + "_ema_2"], axis=1, inplace=True)

    return df
