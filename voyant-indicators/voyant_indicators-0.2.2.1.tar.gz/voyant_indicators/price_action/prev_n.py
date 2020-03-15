def prev_n(df,col,n):

	df = df.copy()

	if df.shape[0] <=n:
		print("in if")
		df[col] = None
		return df

	df = df.iloc[-(n+1):-1]
	df = df[['datetime',col]]
	return df