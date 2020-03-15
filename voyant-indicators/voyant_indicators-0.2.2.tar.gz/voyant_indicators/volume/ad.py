
import pandas as pd


def ad(df, high, low, close, volume, col):
    """
    Accumulation/distribution is a cumulative indicator that uses volume and price to assess whether a stock is being accumulated or distributed. 
    The accumulation/distribution measure seeks to identify divergences between the stock price and volume flow. 
    This provides insight into how strong a trend is. If the price is rising but the indicator is falling this 
    indicates that buying or accumulation volume may not be enough to support the price rise and a price decline could be forthcoming.
    The CLV is based on the movement of the issue within a single bar and can be +1, -1 or zero.
    
    A/D=Previous A/D+Current Money Flow Value
    CMFV = ((Close - Low) - (high - close)//(high - Low)) * Volume

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name for the volume of the asset.
        col (string): the column name for the ad values.

    Returns:
        df (pd.DataFrame): Dataframe with ad of the asset calculated.

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
	
	Citation: https://school.stockcharts.com/doku.php?id=technical_indicators:accumulation_distribution_line
    """

    money_flow_multiplier = (
        (df[close] - df[low]) - (df[high] - df[close])
    ) / (df[high] - df[low])
    df[col + "_money_flow_volume"] = money_flow_multiplier * df[volume]
    prev_ad = df.loc[0, col + "_money_flow_volume"]
    df.loc[0, col] = prev_ad
    ads = [0.0]
    for row in df.loc[1:, [col + "_money_flow_volume"]].itertuples(index=False):
        ads.append(prev_ad + row[0])
        prev_ad = ads[-1]
    df = df.fillna(0)
    df[col] += ads
    df.drop([col + "_money_flow_volume"], axis=1, inplace=True)

    return df
