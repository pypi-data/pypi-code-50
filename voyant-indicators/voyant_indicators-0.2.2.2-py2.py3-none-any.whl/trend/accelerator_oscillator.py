from indicators.momentum.ao import ao
import pandas as pd
from voyant_indicators.overlapping_studies.sma import sma
from voyant_indicators.overlapping_studies.ema import ema
from voyant_indicators.overlapping_studies.wma import wma
from voyant_indicators.overlapping_studies.dema import dema
from voyant_indicators.overlapping_studies.tema import tema


def accelerator_oscillator(df,ma_type, high="high", low="low", col="ao", n =5):
   
    ma_types = {"sma":sma, "ema" : ema, "wma": wma, "dema": dema, "tema": tema}

    # Data frame for storing temporary data
    df_tmp = pd.DataFrame()
    df_tmp[high] = df[high]
    df_tmp[low] = =df[low]

        # Calculate Awesome Oscillator
    df_tmp = ao(df_tmp, high, low, col, ma_type, 'ao')

        # Calculate SMA for Awesome Oscillator
    df_tmp = calculate_sma(df_tmp, 'ao' , 'sma_ao', n)

        # Calculate Accelerator Oscillator
    df_tmp[column_name] = df_tmp['ao'] - df_tmp['sma_ao']
    df_tmp = df_tmp[[column_name]]
    df = df.merge(df_tmp, left_index=True, right_index=True)

    return df
