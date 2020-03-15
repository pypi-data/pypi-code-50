import pandas as pd


def willr(df,n, high="high", low="low", close="close", col="willr"):
    """
    The Williams %R is a momentum indicator, which gauges if a stock is overbought or oversold.

    willr = ((Highesst High - Close) / (Highest High - lowest Low)) * -100

    Williams %R is a momentum indicator that reflects the level of the
    close relative to the highest high for the look-back period. %R corrects for the
    inversion by multiplying the raw value by -100. As a result, the Fast Stochastic
    Oscillator and Williams %R produce the exact same lines, only the scaling is different.
    Williams %R oscillates from 0 to -100. Readings from 0 to -20 are considered overbought.
    Readings from -80 to -100 are considered oversold. Unsurprisingly, signals derived
    from the Stochastic Oscillator are also applicable to Williams %R.
    
    Strategy:
    The oscillator has a range of -100 to 0. Readings below -80 represent oversold territory and readings above -20 represent overbought.

    Now, this does not mean you should buy readings below -80 and sell readings above -20.

    During a strong uptrend, a stock can hover around -20. Conversely, in a strong downtrend, a stock can stay in the -80 territory.


    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        col (string): the column name for the willr values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with willr of the asset calculated.

    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < n:
        df[col] = None
        return df

    hh = df[high].rolling(window=n).max()
    ll = df[low].rolling(window=n).min()
    df[col] = -100 * (hh - df[close]) / (hh - ll)
    #df = df.dropna().reset_index(drop=True)

    return df
