def run_kalman_filter(split):
	split = int(len(df) * .4)
	pvalue_matrix,pairs = find_cointegrated_pairs(df[:split])
	pvalue_matrix_df = pd.DataFrame(pvalue_matrix)
	print(pairs)
	return pairs


def KalmanFilterAverage(x):
	# Construct a Kalman filter
	kf = KalmanFilter(transition_matrices = [1], observation_matrices = [1], initial_state_mean = 0, initial_state_covariance = 1, observation_covariance=1, transition_covariance=.01)

	# Use the observed values of the price to get a rolling mean
	state_means, _ = kf.filter(x.values)
	state_means = pd.Series(state_means.flatten(), index=x.index)
	return state_means

# Kalman filter regression
def KalmanFilterRegression(x,y):
	delta = 1e-3
	trans_cov = delta / (1 - delta) * np.eye(2) # How much random walk wiggles
	obs_mat = np.expand_dims(np.vstack([[x], [np.ones(len(x))]]).T, axis=1)

	kf = KalmanFilter(n_dim_obs=1, n_dim_state=2, # y is 1-dimensional, (alpha, beta) is 2-dimensional
						initial_state_mean=[0,0],
						initial_state_covariance=np.ones((2, 2)),transition_matrices=np.eye(2),
						observation_matrices=obs_mat, observation_covariance=2, transition_covariance=trans_cov)
	
	# Use the observations y to get running estimates and errors for the state parameters
	state_means, state_covs = kf.filter(y.values)
	return state_means

def half_life(spread):
	spread_lag = spread.shift(1)
	spread_lag.iloc[0] = spread_lag.iloc[1]
	spread_ret = spread - spread_lag
	spread_ret.iloc[0] = spread_ret.iloc[1]
	spread_lag2 = sm.add_constant(spread_lag)
	model = sm.OLS(spread_ret,spread_lag2)
	res = model.fit()
	halflife = int(round(-np.log(2) / res.params[1],0))
	
	if halflife <= 0:
		halflife = 1

	return halflife


def get_zScores(df,s1,s2):
	x = df[s1]
	y = df[s2]

	df1 = pd.DataFrame({s2:y,s1:x})
	df1.index = pd.to_datetime(df1.index)

	#run regression (including Kalman Filter) to find hedge ratio and then create spread series
	state_means = KalmanFilterRegression(KalmanFilterAverage(x),KalmanFilterAverage(y))
	df1['hr'] = - state_means[:,0]
	df1['spread'] = df1[s2] + (df1[s1] * df1.hr)
	halflife = half_life(df1['spread']) #Calculate Half Life


	#calculate z-score with window = half life period
	meanSpread = df1.spread.rolling(window=halflife).mean()
	stdSpread = df1.spread.rolling(window=halflife).std()
	df1['zScore'] = (df1.spread-meanSpread)/stdSpread

	return df1
	