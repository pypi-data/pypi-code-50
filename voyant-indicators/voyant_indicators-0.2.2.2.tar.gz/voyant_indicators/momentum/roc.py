import pandas as pd


def roc(df, n, price="close", col="roc"):
    """
    The Price Rate of Change (ROC) is a momentum-based technical indicator that measures the percentage change in price between the current price 
    and the price a certain number of periods ago. The ROC indicator is plotted against zero, 
    with the indicator moving upwards into positive territory if price changes are to the upside, 
    and moving into negative territory if price changes are to the downside.

    
    ROC=((close - close_n )/close_n ) * 100

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        col (string): the column name for the rate of change values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with roc of the asset calculated.

    Strategy: ROC smaller than 0 is typically a sell signal and ROC above 0 is typically a buy signal
    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < n:
        df[col] = None
        return df

    price_shift_n = df[price].shift(n)
    df[col] = ((df[price] - price_shift_n) / price_shift_n) * 100
    #df = df.dropna().reset_index(drop=True)

    return df
