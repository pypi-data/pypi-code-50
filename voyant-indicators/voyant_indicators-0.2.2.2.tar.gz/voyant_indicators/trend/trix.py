
import pandas as pd

from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema

from voyant_indicators.momentum.roc import roc


def trix(df, n, price="close", col="trix"):
    """
    TRIX is a momentum oscillator that displays the percent rate of change of a
    triple exponentially smoothed moving average.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        trix (string): the column name for the rate of change of a triple exponential moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with the rate of change of a triple exponential moving average of the asset calculated.

    """

    df = ema(df, price, col + "_ema", n)
    df = ema(df[n - 1 :], col + "_ema", col + "_ema_2", n)
    df = ema(df[n - 1 :], col + "_ema_2", col + "_ema_3", n)
    df = roc(df, col + "_ema_3", col, 1)

    return df
