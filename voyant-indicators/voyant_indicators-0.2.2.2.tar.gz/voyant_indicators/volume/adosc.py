

import pandas as pd
from voyant_indicators.volume.ad import ad
from voyant_indicators.trend.ema import ema


def adosc(df, fast_period, slow_period, high="high", low="low", close="close", volume="volume", col="adsoc"):
    """
    Developed by Marc Chaikin, the Chaikin Oscillator measures the momentum of the Accumulation Distribution Line using the MACD formula. 
    (This makes it an indicator of an indicator.) The Chaikin Oscillator is the difference between the 3-day and 10-day EMAs 
    of the Accumulation Distribution Line. Like other momentum indicators, this indicator is designed to anticipate directional changes 
    in the Accumulation Distribution Line by measuring the momentum behind the movements. A momentum change is the first step to a trend change.
    Anticipating trend changes in the Accumulation Distribution Line can help chartists anticipate trend changes in the underlying security. 
    The Chaikin Oscillator generates signals with crosses above/below the zero line or with bullish/bearish divergences.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name for the volume of the asset.
        adosc (string): the column name for the adosc values.
        fast_period (int): the time period of the fast exponential moving average.
        slow_period (int): the time period of the slow exponential moving average.

    Returns:
        df (pd.DataFrame): Dataframe with adosc of the asset calculated.

    Sample Strategy:
    
    Bullish:

        AND [Daily SMA(60,Daily Volume) > 100000] 
        AND [Daily SMA(60,Daily Close) > 10] 

        AND [Daily Chaikin Osc(3,10) crosses 1000] 
        AND [Daily RSI(14,Daily Close) crosses 55]

    Bearish:

        AND [Daily SMA(60,Daily Volume) > 100000] 
        AND [Daily SMA(60,Daily Close) > 10] 

        AND [-1000 crosses Daily Chaikin Osc(3,10)] 
        AND [45 crosses Daily RSI(14,Daily Close)]

    Citation: https://school.stockcharts.com/doku.php?id=technical_indicators:chaikin_oscillator


    """

    df = ad(df, high, low, close, volume, col + "_ad")
    df = ema(df, col + "_ad", col + "_ad_fast", fast_period)
    df = ema(df, col + "_ad", col + "_ad_slow", slow_period)
    df[col] = df[col + "_ad_fast"] - df[col + "_ad_slow"]

    if df.shape[0] > slow_period:
        df = df.dropna().reset_index(drop=True)

    df.drop(
        [col + "_ad", col + "_ad_fast", col + "_ad_slow"],
        axis=1,
        inplace=True,
    )

    return df
