import pandas as pd
import numpy as np

def ichimoku_a(df, high="high", low="low", col="ichimoku_a", n1=9, n2=26):
    """Ichimoku Kinkō Hyō (Ichimoku)
    It identifies the trend and look for potential signals within that trend.
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ichimoku_cloud
    Args:
        df: dataframe
        high:  Column name for 'High' column.
        low: Column name for 'Low' column.
        col: Column name for result column.
        n1: fast n period
        n2:medium  n period.
        
    Returns:
        pandas.Series: New column generated.
    """

    df = df.copy()
    conv = 0.5 * (df[high].rolling(n1).max() + df[low].rolling(n1).min())
    base = 0.5 * (df[high].rolling(n2).max() + df[low].rolling(n2).min())

    spana = 0.5 * (conv + base)
    spana = spana.shift(n2)
    df[col] = spana
    return df


def ichimoku_b(df, high="high", low="low", col="ichimoku_b", n2=26, n3=52):
    """Ichimoku Kinkō Hyō (Ichimoku)
    It identifies the trend and look for potential signals within that trend.
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:ichimoku_cloud
    Args:
        df: dataframe
        high:  Column name for 'High' column.
        low: Column name for 'Low' column.
        col: Column name for result column.
        n2:medium  n period.
        n3: slow n period
    Returns:
        pandas.Series: New column generated.
    """

    df = df.copy()

    spanb = 0.5 * (df[high].rolling(n3).max() + df[low].rolling(n3).min())
    spanb = spanb.shift(n2)
    df[col] = spanb
    return df

def ichimoku_base(df,high="high",low="low",col="ichimoku_base",n2=26):
    """
    Kijun-sen (Base Line): (26-period high + 26-period low)/2))

    The default setting is 26 periods and can be adjusted. On a daily chart, this line is the midpoint of the 26-day high-low range, 
    which is almost one month).  

    Args:
        df: dataframe
        high:  Column name for 'High' column.
        low: Column name for 'Low' column.
        col: Column name for result column.
        n2(int): n period.
    Returns:
        pandas.Series: New column generated.

    """

    df = df.copy()
    high_prices = df[high].rolling(n2).max()
    low_prices = df[low].rolling(n2).min()
    df[col] = (high_prices + low_prices) / 2
    return df


