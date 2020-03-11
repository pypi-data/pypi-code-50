import numpy as np
import pandas as pd
def exp_filter(df,
               ctime=10,
               nan=-999999.0):
    """
    Calculates exponentially smoothed time series using an
    iterative algorithm
    Parameters
    ----------
    df : a pandas dataframe with a datetime index and a SM column
    ctime : int
        characteristic time used for calculating
        the weight
    nan : double
        nan values to exclude from calculation
    """

    in_data = df.values
    in_jd = df.index.to_julian_date()

    filtered = np.empty(len(in_data))
    gain = 1
    found_index = -1

    filtered.fill(np.nan)
    # find the first non nan value in the time series
    for i in range(in_jd.shape[0]):

        isnan = (in_data[i] == nan) or np.isnan(in_data[i])
        if not isnan:
            last_jd_var = in_jd[i]
            last_filtered_var = in_data[i]
            # set the first filtered value to the first found non nan value
            filtered[i] = in_data[i]
            found_index = i
            break

    if found_index > -1:

        for index in range(found_index + 1, in_jd.shape[0]):
            isnan = (in_data[index] == nan) or np.isnan(in_data[index])
            if not isnan:
                tdiff = in_jd[index] - last_jd_var
                ef = np.exp(-tdiff / ctime)
                gain = gain / (gain + ef)
                filtered[index] = last_filtered_var + gain * (in_data[index] - last_filtered_var)
                last_jd_var = in_jd[index]
                last_filtered_var = filtered[index]

    return pd.DataFrame(filtered, df.index)


if __name__ == '__main__':
		
	exp_filter(test, ctime=20)

	test = corrdfs['643']['tuwien']
	test1 = corrdfs['643']['dir_resam']

	plt.plot(exp_filter(test, ctime=20)[0] - test.ewm(com=19.5041665).mean()[~np.isnan(test)])


	plt.plot(exp_filter(test, ctime=10)[0] - test.ewm(span=20).mean()[~np.isnan(test)])

	plt.plot(exp_filter(test, ctime=20)[0])
	plt.plot(test.ewm(span=40).mean()[~np.isnan(test)], marker='.')

	plt.plot(exp_filter(test, ctime=20)[0] - test.ewm(com=1/(1+np.exp(-1/20))).mean()[~np.isnan(test)])
