import pandas as pd


def mfi(df, n, high="high", low="low", close="close", volume="volume", col="mfi"):
    """
    The Money Flow Index (MFI) is an oscillator that uses both price and volume to measure buying and selling pressure.
    Money flow is positive when the typical price rises (buying pressure) and negative when the typical price declines (selling pressure). 
    A ratio of positive and negative money flow is then plugged into an RSI formula to create an oscillator that moves between zero and one hundred. 
    As a momentum oscillator tied to volume, MFI is best suited to identify reversals and price extremes with a variety of signals.
    
    Typical Price = (High + Low + Close)/3

    Raw Money Flow = Typical Price x Volume
    Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)

    Money Flow Index = 100 - 100/(1 + Money Flow Ratio)


    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name of the volume of the asset.
        mfi (string): the column name for the mfi values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with mfi of the asset calculated.

    Strategy:
     - Bullish
        AND [Daily SMA(20,Daily Volume) > 40000] 
        AND [Daily SMA(60,Daily Close) > 20] 
        AND [Daily MFI(14) < 10]

     - Bearish

        AND [Daily SMA(20,Daily Volume) > 100000] 
        AND [Daily SMA(60,Daily Close) > 20] 

        AND [Daily MFI(14) > 90]

    Citation: https://school.stockcharts.com/doku.php?id=technical_indicators:money_flow_index_mfi


    """

    df = df.copy().reset_index(drop=True)
    if df.shape[0] < n:
        df[col] = None
        return df


    typical_price = (df[high] + df[low] + df[close]) / 3
    money_flow = typical_price * df[volume]
    typical_price_diff = typical_price.diff()
    df.loc[typical_price_diff > 0, "positive_money_flow"] = 1
    df.loc[typical_price_diff <= 0, "negative_money_flow"] = -1
    df["positive_money_flow"] *= money_flow
    df["negative_money_flow"] *= money_flow
    df = df.fillna(0)
    n_pos_money_flow = (
        df.loc[1:, "positive_money_flow"].rolling(window=n).sum()
    )
    n_neg_money_flow = (
        df.loc[1:, "negative_money_flow"].rolling(window=n).sum()
    )
    mfi_ratio = n_pos_money_flow / -n_neg_money_flow
    df[col] = 100 - (100 / (1 + mfi_ratio))
    df.drop(
        ["positive_money_flow", "negative_money_flow"], axis=1, inplace=True
    )
    #df = df.dropna().reset_index(drop=True)

    return df
