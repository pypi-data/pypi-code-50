def de_marker(df,high="high", low="low", col="demarker", period=14):
        """
        DeMarker (DeM)
        --------------
            https://www.metatrader4.com/en/trading-platform/help/analytics/tech_indicators/demarker
            >>> Indicators.de_marker(period=14, column_name='dem')
            :param int period: Period, default: 14
            :param str column_name: Column name, default: dem
            :return: None
        """
    df_tmp = df[[high, low]]

    df_tmp = df_tmp.assign(
        hdif=(df_tmp[high] > df_tmp[high].shift(1)).astype(int))
    df_tmp = df_tmp.assign(hsub=df_tmp[high] - df_tmp[high].shift(1))
    df_tmp = df_tmp.assign(demax=np.where(df_tmp.hdif == 0, 0, df_tmp.hsub))

    df_tmp = df_tmp.assign(ldif=(df_tmp[low] < df_tmp[low].shift(1)).astype(int))
    df_tmp = df_tmp.assign(lsub=df_tmp[low].shift(1) - df_tmp[low])
    df_tmp = df_tmp.assign(demin=np.where(df_tmp.ldif == 0, 0, df_tmp.lsub))

    df_tmp['sma_demax'] = df_tmp['demax'].rolling(window=period).mean()
    df_tmp['sma_demin'] = df_tmp['demin'].rolling(window=period).mean()

    df_tmp = df_tmp.assign(dem=df_tmp.sma_demax / (df_tmp.sma_demax + df_tmp.sma_demin))

    df_tmp = df_tmp[['dem']]
    df_tmp = df_tmp.rename(columns={'dem': col})

    df = df.merge(df_tmp, left_index=True, right_index=True)

    return df