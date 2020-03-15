
import pandas as pd


def obv(df, price="close", volume="volume", col="obv"):
    """
    On Balance Volume (OBV) measures buying and selling pressure as a cumulative indicator, adding volume on up days and subtracting it on down days
    The On Balance Volume (OBV) line is simply a running total of positive and negative volume. 
    A period's volume is positive when the close is above the prior close and is negative when the close is below the prior close.
    
    The On Balance Volume (OBV) is a cumulative total of the up and down volume.
    When the close is higher than the previous close, the volume is added to
    the running total, and when the close is lower than the previous close,
    the volume is subtracted from the running total.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        volume (string): the column name of the volume of the asset.
        obv (string): the column name for the on balance volume values.

    Returns:
        df (pd.DataFrame): Dataframe with obv of the asset calculated.

    Sample Strategy:
    Bullish:
        AND [Daily SMA(60,Daily Volume) > 100000] 
        AND [Daily SMA(60,Daily Close) > 10] 

        AND [Daily Close < Daily SMA(65,Daily Close)] 
        AND [Daily AccDist > Daily AccDist Signal (65)] 
        AND [Daily OBV > Daily OBV Signal(65)] 
        AND [Daily Close < Daily SMA(20,Daily Close)] 
        AND [Daily AccDist > Daily AccDist Signal (20)] 
        AND [Daily OBV > Daily OBV Signal(20)]

    Bearish:

        AND [Daily SMA(60,Daily Volume) > 100000] 
        AND [Daily SMA(60,Daily Close) > 10] 

        AND [Daily Close > Daily SMA(65,Daily Close)] 
        AND [Daily AccDist < Daily AccDist Signal (65)] 
        AND [Daily OBV < Daily OBV Signal(65)] 
        AND [Daily Close > Daily SMA(20,Daily Close)] 
        AND [Daily AccDist < Daily AccDist Signal (20)] 
        AND [Daily OBV < Daily OBV Signal(20)]
    
    Citation: https://school.stockcharts.com/doku.php?id=technical_indicators:on_balance_volume_obv


    """

    df["diff"] = df[price].diff()
    df = df.fillna(1)
    df.loc[df["diff"] > 0, col + "_sign"] = 1
    df.loc[df["diff"] < 0, col + "_sign"] = -1
    df.loc[df["diff"] == 0, col + "_sign"] = 0
    volume_sign = df[volume] * df[col + "_sign"]
    df[col] = volume_sign.cumsum()
    df.drop(["diff", col + "_sign"], axis=1, inplace=True)

    return df
