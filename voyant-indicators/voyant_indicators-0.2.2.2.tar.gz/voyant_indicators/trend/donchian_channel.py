import pandas as pd
def donchian_channel(df, n, high="high", low="low", col="dc"):
    """Calculate donchian channel of given pandas data frame.
    :param df: pandas.DataFrame
    :param n:
    :return: pandas.DataFrame
    """
    i = 0
    dc_l = []
    while i < n - 1:
        dc_l.append(0)
        i += 1

    i = 0
    while i + n - 1 < df.index[-1]:
        dc = max(df[high].ix[i:i + n - 1]) - min(df[low].ix[i:i + n - 1])
        dc_l.append(dc)
        i += 1

    donchian_chan = pd.Series(dc_l, name=col)
    donchian_chan = donchian_chan.shift(n - 1)
    return df.join(donchian_chan)
