import pandas as pd

from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def ao(df, high, low, col, ma_type, fast_period=5, slow_period=34):
    """Awesome Oscillator
    From: https://www.tradingview.com/wiki/Awesome_Oscillator_(AO)
    The Awesome Oscillator is an indicator used to measure market momentum. AO calculates the difference of a 
    34 Period and 5 Period Simple Moving Averages. The Simple Moving Averages that are used are not calculated 
    using closing price but rather each bar's midpoints. AO is generally used to affirm trends or to anticipate 
    possible reversals. 
    
    From: https://www.ifcm.co.uk/ntx-indicators/awesome-oscillator
    Awesome Oscillator is a 34-period simple moving average, plotted through the central points of the bars (H+L)/2, 
    and subtracted from the 5-period simple moving average, graphed across the central points of the bars (H+L)/2.
    MEDIAN PRICE = (HIGH+LOW)/2
    AO = SMA(MEDIAN PRICE, 5)-SMA(MEDIAN PRICE, 34)
    where
    SMA — Simple Moving Average.
    
    Args:
        high(pandas.Series): dataset 'High' column.
        low(pandas.Series): dataset 'Low' column.
        s(int): short period
        l(int): long period
        
    Returns:
        pandas.Series: New feature generated.
    """

    df = df.copy()

    df["mp"] = 0.5 * (df[high] + df[low])

    ma_types = {"sma":sma, "ema" : ema, "wma": wma, "dema": dema, "tem": tema}


    df = ma_types[ma_type](df, "mp", col + "_fast", fast_period)
    df = ma_types[ma_type](df, "mp", col + "_slow", slow_period)


    ao = df[col+"_fast"] - df[col+"_slow"]
    df[col] = ao
    

    return df
