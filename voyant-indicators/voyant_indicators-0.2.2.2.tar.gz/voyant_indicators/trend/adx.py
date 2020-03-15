import pandas as pd
import numpy as np

def adx(df, high="high", low="low", close="close", col="adx", n=14):
    """Calculate the Average Directional Movement Index for given data.


    The Average Directional Index (ADX), Minus Directional Indicator (-DI) and Plus Directional Indicator (+DI) represent a group of directional movement indicators that form a trading system developed by Welles Wilder. 
    Positive and negative directional movement form the backbone of the Directional Movement System. 
    Wilder determined directional movement by comparing the difference between two consecutive lows with the difference between their respective highs.
    The Plus Directional Indicator (+DI) and Minus Directional Indicator (-DI) are derived from smoothed averages of these differences and 
    measure trend direction over time. These two indicators are often collectively referred to as the Directional Movement Indicator (DMI).
    The Average Directional Index (ADX) is in turn derived from the smoothed averages of the difference between +DI and -DI; 
    it measures the strength of the trend (regardless of direction) over time.
    Using these three indicators together, chartists can determine both the direction and strength of the trend.


    
    Args:
        df= dataframe
        high:  Column name for 'High' column.
        low: Column name for 'Low' column.
        close: Column name for 'Close' column.
        n(int): n period.
    Returns:
        pandas.Series: New feature generated.

    Strategy:
    Buy Signal:

    AND [Daily SMA(20,Daily Volume) > 100000] 
    AND [Daily SMA(60,Daily Close) > 10] 

    AND [Daily ADX Line(14) > 20] 
    AND [Daily Plus DI(14) crosses Daily Minus DI(14)] 
    AND [Daily Close > Daily SMA(50,Daily Close)]
    
    SELL Signal:

    AND [Daily SMA(20,Daily Volume) > 100000] 
    AND [Daily SMA(60,Daily Close) > 10] 

    AND [Daily ADX Line(14) > 20] 
    AND [Daily Minus DI(14) crosses Daily Plus DI(14)] 
    AND [Daily Close < Daily SMA(50,Daily Close)]


    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx
    
    """
    n = int(n)

    df = df.copy()

    cs = df[close].shift(1)

    tr = df[high].combine(cs, max) - df[low].combine(cs, min)
    trs = tr.rolling(n).sum()

    up = df[high] - df[high].shift(1)
    dn = df[low].shift(1) - df[low]

    pos = ((up > dn) & (up > 0)) * up
    neg = ((dn > up) & (dn > 0)) * dn

    dip = 100 * pos.rolling(n).sum() / trs
    din = 100 * neg.rolling(n).sum() / trs

    dx = 100 * np.abs((dip - din) / (dip + din))
    adx = dx.ewm(n).mean()

    df[col] = adx
    return df



def adx_pos(df, high, low, close,col,n=14):
    """Calculate the Average Directional Movement Index for given data.


    The Average Directional Index (ADX), Minus Directional Indicator (-DI) and Plus Directional Indicator (+DI) represent a group of directional movement indicators that form a trading system developed by Welles Wilder. 
    Positive and negative directional movement form the backbone of the Directional Movement System. 
    Wilder determined directional movement by comparing the difference between two consecutive lows with the difference between their respective highs.
    The Plus Directional Indicator (+DI) and Minus Directional Indicator (-DI) are derived from smoothed averages of these differences and 
    measure trend direction over time. These two indicators are often collectively referred to as the Directional Movement Indicator (DMI).
    The Average Directional Index (ADX) is in turn derived from the smoothed averages of the difference between +DI and -DI; 
    it measures the strength of the trend (regardless of direction) over time.
    Using these three indicators together, chartists can determine both the direction and strength of the trend.


    
    Args:
        df= dataframe
        high:  Column name for 'High' column.
        low: Column name for 'Low' column.
        close: Column name for 'Close' column.
        n(int): n period.
    Returns:
        pandas.Series: New feature generated.

    Strategy:
    Buy Signal:

    AND [Daily SMA(20,Daily Volume) > 100000] 
    AND [Daily SMA(60,Daily Close) > 10] 

    AND [Daily ADX Line(14) > 20] 
    AND [Daily Plus DI(14) crosses Daily Minus DI(14)] 
    AND [Daily Close > Daily SMA(50,Daily Close)]
    
    SELL Signal:

    AND [Daily SMA(20,Daily Volume) > 100000] 
    AND [Daily SMA(60,Daily Close) > 10] 

    AND [Daily ADX Line(14) > 20] 
    AND [Daily Minus DI(14) crosses Daily Plus DI(14)] 
    AND [Daily Close < Daily SMA(50,Daily Close)]


    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx
    
    """

    n = int(n)

    df = df.copy()

    cs = df[close].shift(1)

    tr = df[high].combine(cs, max) - df[low].combine(cs, min)
    trs = tr.rolling(n).sum()

    up = df[high] - df[high].shift(1)
    dn = df[low].shift(1) - df[low]

    pos = ((up > dn) & (up > 0)) * up
    neg = ((dn > up) & (dn > 0)) * dn

    dip = 100 * pos.rolling(n).sum() / trs
    din = 100 * neg.rolling(n).sum() / trs

    dx = 100 * np.abs((dip - din) / (dip + din))
    adx = dx.ewm(n).mean()

    df['adx_pos'] = dip

    return df



def adx_neg(df, high, low, close, col, n=14):
    """Calculate the Average Directional Movement Index for given data.


    The Average Directional Index (ADX), Minus Directional Indicator (-DI) and Plus Directional Indicator (+DI) represent a group of directional movement indicators that form a trading system developed by Welles Wilder. 
    Positive and negative directional movement form the backbone of the Directional Movement System. 
    Wilder determined directional movement by comparing the difference between two consecutive lows with the difference between their respective highs.
    The Plus Directional Indicator (+DI) and Minus Directional Indicator (-DI) are derived from smoothed averages of these differences and 
    measure trend direction over time. These two indicators are often collectively referred to as the Directional Movement Indicator (DMI).
    The Average Directional Index (ADX) is in turn derived from the smoothed averages of the difference between +DI and -DI; 
    it measures the strength of the trend (regardless of direction) over time.
    Using these three indicators together, chartists can determine both the direction and strength of the trend.


    
    Args:
        df= dataframe
        high:  Column name for 'High' column.
        low: Column name for 'Low' column.
        close: Column name for 'Close' column.
        n(int): n period.
    Returns:
        pandas.Series: New feature generated.

    Strategy:
    Buy Signal:

    AND [Daily SMA(20,Daily Volume) > 100000] 
    AND [Daily SMA(60,Daily Close) > 10] 

    AND [Daily ADX Line(14) > 20] 
    AND [Daily Plus DI(14) crosses Daily Minus DI(14)] 
    AND [Daily Close > Daily SMA(50,Daily Close)]
    
    SELL Signal:

    AND [Daily SMA(20,Daily Volume) > 100000] 
    AND [Daily SMA(60,Daily Close) > 10] 

    AND [Daily ADX Line(14) > 20] 
    AND [Daily Minus DI(14) crosses Daily Plus DI(14)] 
    AND [Daily Close < Daily SMA(50,Daily Close)]


    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:average_directional_index_adx
    
    """

    n = int(n)

    df = df.copy()

    cs = df[close].shift(1)

    tr = df[high].combine(cs, max) - df[low].combine(cs, min)
    trs = tr.rolling(n).sum()

    up = df[high] - df[high].shift(1)
    dn = df[low].shift(1) - df[low]

    pos = ((up > dn) & (up > 0)) * up
    neg = ((dn > up) & (dn > 0)) * dn

    dip = 100 * pos.rolling(n).sum() / trs
    din = 100 * neg.rolling(n).sum() / trs

    dx = 100 * np.abs((dip - din) / (dip + din))
    adx = dx.ewm(n).mean()

    df['adx_neg'] = din

    return df