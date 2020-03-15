import numpy as np
import pandas as pd

from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def cci(df, n, high="high", low="low", close="close", col="cci", c=0.015):
    """
    The CCI is designed to detect beginning and ending market trends. The range
    of 100 to -100 is the normal trading range. CCI values outside of this range
    indicate overbought or oversold conditions. You can also look for price divergence
    in the CCI. If the price is making new highs, and the CCI is not, then a price
    correction is likely.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        col (string): the column name for the cci values.
        n (int): the total number of periods.
        c (float): scaling factor to provide more readable numbers, usually 0.015.

    Returns:
        df (pd.DataFrame): Dataframe with commodity channel index calculated.

    """


    df = df.copy()

    if df.shape[0] < n:
        df[col] = None


    df[col + "_tp"] = (df[high] + df[low] + df[close]) / 3.0
    df = sma(df, col + "_tp", col + "_atp", n)
    mdev = (
        df[col + "_tp"]
        .rolling(n)
        .apply(lambda x: np.fabs(x - x.mean()).mean(), raw=True)
    )
    df[col] = (df[col + "_tp"] - df[col + "_atp"]) / (c * mdev)
    df.drop([col + "_tp", col + "_atp"], axis=1, inplace=True)
    #df = df.dropna().reset_index(drop=True)

    return df
