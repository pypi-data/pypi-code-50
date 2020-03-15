import pandas as pd

def fi(df,close="close", volume="volume", col="fi", n=2):
    """Force Index (FI)
    It illustrates how strong the actual buying or selling pressure is. High
    positive values mean there is a strong rising trend, and low values signify
    a strong downward trend.
    http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:force_index
    Args:
        close(pandas.Series): dataset 'Close' column.
        volume(pandas.Series): dataset 'Volume' column.
        n(int): n period.
        fillna(bool): if True, fill nan values.
    Returns:
        pandas.Series: New feature generated.
    """
    df = df.copy()

    fi = df[close].diff(n) * df[volume].diff(n)
    
    df[col] = fi
    return df
