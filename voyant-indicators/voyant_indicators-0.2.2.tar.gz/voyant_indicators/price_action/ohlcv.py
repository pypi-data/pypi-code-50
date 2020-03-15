def ohlcv(df,col,n):

	df = df.copy()
	df = df[['datetime',col]]

	return df.tail(n)