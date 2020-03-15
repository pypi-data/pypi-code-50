import pandas as pd
from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def ppo(df, fast_period, slow_period, ma_type, price="close", col="ppo"):
    """
    The Percentage Price Oscillator (PPO) is a momentum oscillator that measures
    the difference between two moving averages as a percentage of the larger
    moving average.
    
        PPO = (MA_long - MA_Slow)/MA_Slow

    One advantage to the percentage price oscillator is that it's a dimensionless quantity, 
    a pure number that isn't fixed to a value such as the price of the underlying stock or other security. 
    Also, because the percentage price oscillator compares two exponential moving averages, 
    it lets the user compare movements through different time frames. 
    The price of the security itself becomes almost of secondary importance.
    
    For analysts who choose to use the percentage price oscillator, a value outside the range of -10% to +10% 
    is supposed to indicate a stock being oversold or overbought, respectively.


    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        col (string): the column name for the % price oscillator values.
        fast_period (int): the time period of the fast moving average.
        slow_period (int): the time period of the slow moving average.
        ma_type (int): Moving average type.

    Returns:
        df (pd.DataFrame): Dataframe with ppo of the asset calculated.

    """
    df = df.copy().reset_index(drop=True)
    if df.shape[0] < slow_period:
        df[col] = None
        return df

    ma_types = {"sma":sma, "ema" : ema, "wma": wma, "dema": dema, "tem": tema}

    df = ma_types[ma_type](df, price, col + "_fast", fast_period)
    df = ma_types[ma_type](df, price, col + "_slow", slow_period)
    df[col] = ((df[col + "_fast"] - df[col + "_slow"]) / df[col + "_slow"]) * 100
    df = df.dropna().reset_index(drop=True)

    return df
