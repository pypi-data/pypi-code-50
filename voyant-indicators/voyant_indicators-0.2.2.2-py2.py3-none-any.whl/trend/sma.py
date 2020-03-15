
import pandas as pd


def sma(df, price, col, n):
    """
    Simple Moving Average (SMA) is an arithmetic moving average calculated by
    adding recent closing prices then dividing that by the number of time periods
    in the calculation average.

    SMA = (P_1 + ... + P_n) / n

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        col (string): the column name for the n-day moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day moving average of the asset calculated.

    Example Strategy:
    Bullish

    AND [Daily SMA(20,Daily Volume) > 40000] 
    AND [Daily SMA(60,Daily Close) > 20] 

    AND [Daily SMA(150,Daily Close) > 5 days ago Daily SMA(150,Daily Close)] 
    AND [Daily EMA(5,Daily Close) > Daily EMA(35,Daily Close)] 
    AND [Yesterday's Daily EMA(5,Daily Close) < Yesterday's Daily EMA(35,Daily Close)] 
    AND [Daily Volume > Daily SMA(200,Daily Volume)]

    Bearish:

    AND [Daily SMA(20,Daily Volume) > 40000] 
    AND [Daily SMA(60,Daily Close) > 20] 

    AND [Daily SMA(150,Daily Close) < 5 days ago Daily SMA(150,Daily Close)] 
    AND [Daily EMA(5,Daily Close) < Daily EMA(35,Daily Close)] 
    AND [Yesterday's Daily EMA(5,Daily Close) > Yesterday's Daily EMA(35,Daily Close)] 
    AND [Daily Volume > Daily SMA(200,Daily Volume)]

    Citation: https://school.stockcharts.com/doku.php?id=technical_indicators:moving_averages

    """
    df = df.copy()

    if df.shape[0] < n:
        df[col] = None
    
    else:
        df[col] = df[price].rolling(window=n).mean()

    return df
