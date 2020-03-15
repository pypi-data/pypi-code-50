
import pandas as pd

from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def trima(df, price,n, col="trima"):
    """
    The Triangular Moving Average (TRIMA) is similar to other moving averages in
    that it shows the average (or mean) price over a specified number of data
    points (usually a number of price bars). However, the triangular moving average
    differs in that it is double smoothed—which also means averaged twice.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        trima (string): the column name for the n-day double exponential moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with triangular moving average of the asset calculated.

    """

    first_period_sma = None
    second_period_sma = None
    if n % 2 == 0:
        first_period_sma = int((n / 2) + 1)
        second_period_sma = int(n / 2)
    else:
        first_period_sma = int((n + 1) / 2)
        second_period_sma = int((n + 1) / 2)
    df = sma(df, price, col + "_sma", first_period_sma)
    df = sma(
        df[first_period_sma - 1 :], col + "_sma", col, second_period_sma
    )
    df = df.dropna().reset_index(drop=True)
    df.drop([col + "_sma"], axis=1, inplace=True)

    return df
