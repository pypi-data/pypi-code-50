import pandas as pd
from voyant_indicators.momentum.rsi import rsi

from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema

def stoch(df, n,ma_type,ma_n, high="high" ,low="low", price="close",col="stoch"):
    """
    The Stochastic Oscillator is another well-known momentum indicator used in
    technical analysis. The idea behind this indicator is that the closing
    prices should predominantly close in the same direction as the prevailing
    trend.

    In an upward trend the price should be closing near the highs of the trading
    range and in a downward trend the price should be closing near the lows of
    the trading range. When this occurs it signals continued momentum and
    strength in the direction of the prevailing trend.

    StochRSI = (RSI - Lowest Low RSI) / (Highest High RSI - Lowest Low RSI)

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the price  of the asset.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period low price  of the asset.
        col (string): the column name for the result
        n: Time period to consider

    Returns:
        df (pd.DataFrame): Dataframe with slow %k and slow %d of the asset calculated.

    Strategy:
        Bullish:
        - AND [Daily SMA(20,Daily Volume) > 40000] 
          AND [Daily SMA(60,Daily Close) > 10] 

          AND [Daily SMA(10,Daily Close) > Daily SMA(60,Daily Close)] 
          AND [Daily Stoch RSI(14) < 0.1] 
          AND [Daily Close < Daily SMA(10,Daily Close)]
        
        Bearish:
        - AND [Daily SMA(20,Daily Volume) > 40000] 
          AND [Daily SMA(60,Daily Close) > 10] 

          AND [Daily SMA(10,Daily Close) < Daily SMA(60,Daily Close)] 
          AND [Daily Stoch RSI(14) > 0.9] 
          AND [Daily Close > Daily SMA(10,Daily Close)]

    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < n:
        df[col] = None
        return df

    df = rsi(df,price,"rsi",n)
    hh = df[high].rolling(window=n).max()
    ll = df[low].rolling(window= n).min()
    df[col] = (df["rsi"] - ll) / (hh - ll)

    if ma_type == -1:
        return df
    else:
        ma_types = {"sma": sma, "ema": ema, "wma": wma, "dema": dema, "tema": tema}
        df.rename(columns = {col:col+"_prev"}, inplace = True) 

        df = ma_types[ma_type]( df, col+"_prev", col, ma_n)
    
    
    #df = df.dropna().reset_index(drop=True)

    return df
