import pandas as pd
import numpy as np


def vortex_pos(df, high="high", low="low", close="close", col="vortex_pos", n=14):
    """Vortex Indicator (VI)
    It consists of two oscillators that capture positive and negative trend
    movement. A bullish signal triggers when the positive trend indicator
    crosses above the negative trend indicator or a key level.
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:vortex_indicator
    Args:
        high(pandas.Series): dataset 'High' column.
        low(pandas.Series): dataset 'Low' column.
        close(pandas.Series): dataset 'Close' column.
        n(int): n period.
        fillna(bool): if True, fill nan values.
    Returns:
        pandas.Series: New feature generated.
    """
    tr = df[high].combine(df[close].shift(1), max) - df[low].combine(df[close].shift(1), min)
    trn = tr.rolling(n).sum()

    vmp = np.abs(df[high] - df[low].shift(1))
    vmm = np.abs(df[low] - df[high].shift(1))

    vip = vmp.rolling(n).sum() / trn

    df[col] = vip
    return df


def vortex_neg(df, high="high", low="low", close="close", col="vortex_neg", n=14):

    """Vortex Indicator (VI)
    It consists of two oscillators that capture positive and negative trend
    movement. A bearish signal triggers when the negative trend indicator
    crosses above the positive trend indicator or a key level.
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:vortex_indicator
    Args:
        high(pandas.Series): dataset 'High' column.
        low(pandas.Series): dataset 'Low' column.
        close(pandas.Series): dataset 'Close' column.
        n(int): n period.
        fillna(bool): if True, fill nan values.
    Returns:
        pandas.Series: New feature generated.
    """

    df = df.copy()
    tr = df[high].combine(df[close].shift(1), max) - df[low].combine(df[close].shift(1), min)
    trn = tr.rolling(n).sum()

    vmp = np.abs(df[high] - df[low].shift(1))
    vmm = np.abs(df[low] - df[high].shift(1))

    vin = vmm.rolling(n).sum() / trn

    df[col] = vin
    return df