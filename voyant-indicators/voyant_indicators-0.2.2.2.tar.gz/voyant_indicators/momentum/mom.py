import pandas as pd


def mom(df, n, price="close", col="mom"):
    """
    The Momentum indicator is a speed of movement indicator designed to identify the speed (or strength) of price movement. 
    The momentum indicator compares the most recent closing price to a previous closing price (can be the closing price of any time frame). 
    Common ways to use Momentum Indicator:
    Buy strategy: 14 MOM crosses above 0
    Sell strategy: 14 MOM crosses below 0.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        col (string): the column name for the rate of change values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with mom of the asset calculated.

    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < n:
        df[col] = None
        return df

    df[col] = df[price] - df[price].shift(n)
    #df = df.dropna().reset_index(drop=True)

    return df
