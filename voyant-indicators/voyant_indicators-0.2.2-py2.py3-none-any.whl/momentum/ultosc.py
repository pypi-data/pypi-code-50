import pandas as pd


from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema
from voyant_indicators.util.trange import trange


def ultosc(df,high="high",low="low", close="close", col="ultosc", time_period_1=7, time_period_2=14,time_period_3=28):
    """
    The Ultimate Oscillator (ULTOSC) by Larry Williams is a momentum oscillator
    that incorporates three different time periods to improve the overbought and
    oversold signals.
    
    There are three steps to calculating the Ultimate Oscillator. This example uses 7, 14, 28 parameters:

    1. Before calculating the Ultimate Oscillator, two variable need to be defined; Buying Pressure and True Range.

    Buying Pressure (BP) = Close - Minimum (Lowest between Current Low or Previous Close)
    True Range (TR) = Maximum (Highest between Current High or Previous Close) - Minimum (Lowest between Current Low or Previous Close)

    2. The Ultimate Oscillator then uses these figures over three time periods:

    Average7 = (7 Period BP Sum) / (7 Period TR Sum)
    Average14 = (14 Period BP Sum) / (14 Period TR Sum)
    Average28 = (28 Period BP Sum) / (28 Period TR Sum)

    3. The final Ultimate Oscillator calculations can now be made:

    UO = 100 x [(4 x Average7)+(2 x Average14)+Average28]/(4+2+1)

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        ultosc (string): the column name for the ultimate oscillator values.
        time_period_1 (int): The first time period for the indicator. By default, 7.
        time_period_2 (int): The second time period for the indicator. By default, 14.
        time_period_3 (int): The third time period for the indicator. By default, 28.

    Returns:
        df (pd.DataFrame): Dataframe with ultimate oscillator of the asset calculated.

    Strategy:
        Bullish UO Divergence

        Bullish Divergence forms meaning price forms a lower low while UO makes a higher low.
        The low of the Divergence should be below 30.
        UO breaks above the high of the Divergence.


        Bearish UO Divergence

        Bearish Divergence forms meaning price forms a higher high while UO makes a lower high.
        The high of the Divergence should be above 70.
        UO falls below the low of the Divergence.

    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < time_period_3:
        df[col] = None
        return df


    df[col + "previous_close"] = df[close].shift(1)
    df = trange(df, high, low, close, col + "_true_range")
    df = df.dropna().reset_index(drop=True)
    df[col + "_true_low"] = df[[low, col + "previous_close"]].min(axis=1)
    df[col + "_close-tl"] = df[close] - df[col + "_true_low"]
    df = sma(df, col + "_close-tl", col + "_a1", time_period_1)
    df = sma(df, col + "_true_range", col + "_b1", time_period_1)
    df = sma(df, col + "_close-tl", col + "_a2", time_period_2)
    df = sma(df, col + "_true_range", col + "_b2", time_period_2)
    df = sma(df, col + "_close-tl", col + "_a3", time_period_3)
    df = sma(df, col + "_true_range", col + "_b3", time_period_3)
    a1_b1 = df[col + "_a1"] / df[col + "_b1"]
    a2_b2 = df[col + "_a2"] / df[col + "_b2"]
    a3_b3 = df[col + "_a3"] / df[col + "_b3"]
    df[col] = 100 * ((4 * a1_b1) + (2 * a2_b2) + a3_b3) / 7.0
    df.drop(
        [
            col + "_true_range",
            col + "previous_close",
            col + "_true_low",
            col + "_close-tl",
            col + "_a1",
            col + "_b1",
            col + "_a2",
            col + "_b2",
            col + "_a3",
            col + "_b3",
        ],
        axis=1,
        inplace=True,
    )
    #df = df.dropna().reset_index(drop=True)
    return df
