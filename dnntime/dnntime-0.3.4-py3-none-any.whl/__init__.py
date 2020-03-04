####################################################################################
####                     Deep Time Series Pre-Alpha  0.3.0                      ####
####                           Python 3 Version                                 ####
####                    Conceived and Developed by Kevin Chen                   ####
####                        All Rights Reserved                                 ####
####################################################################################

from IPython.display import display, HTML
import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
sns.set(style="white", color_codes=True)
import copy
import ipdb
from collections import defaultdict
import operator
import logging
import time
import art
import os
from statsmodels.tsa.stattools import adfuller
import tensorflow as tf

logger = logging.getLogger("dnntime")
logging.basicConfig(level=logging.INFO)

#######################################
# Version
from .__version__ import __version__
# Models
from .models import build_rnn_model, build_lstm_model, build_gru_model, build_convlstm_model
# Utils
from .utils import colorful, load_ts_data, clean_ts_data, convert_timeseries_dataframe_to_supervised, \
                   time_series_plot, print_static_rmse, print_dynamic_rmse
from .utils.classes import timesteps, interval_to_freq, interval_to_timesteps
from .utils.eda import ts_plot, test_stationarity, ets_decomposition_plot, \
                       acf_pacf_plot
from .utils.etl import log_power_transform, decompose, normalize, split_data


def make_ts_magic(data, ts_column, sep=',', target=None, univarate=True,
                  time_interval='', forecast_period='', auto_clean=False, epochs=10,
                  batch_size=256, score_type='rmse', conf_int=0.95, model_type='all', verbose=0):
    """
    ####################################################################################
    ####                          Auto Time Series                                  ####
    ####                           Python 3 Version                                 ####
    ####                    Authored and Developed by Kevin Chen                    ####
    ####                    Original Credit to Ram Seshadri                         ####
    ####                        All Rights Reserved                                 ####
    ####################################################################################
    ##################################################################################################
    DEEP_TIMESERIES IS A COMPLEX MODEL BUILDING UTILITY FOR TIME SERIES DATA. SINCE IT AUTOMATES MANY
    TASKS INVOLVED IN A COMPLEX ENDEAVOR, IT ASSUMES MANY INTELLIGENT DEFAULTS. BUT YOU CAN CHANGE THEM.
    Auto_Timeseries will rapidly build predictive models based on Statsmodels ARIMA, Seasonal ARIMA
    and Scikit-Learn ML. It will automatically select the BEST model which gives best score specified.
    It will return the best model and a dataframe containing predictions for forecast_period (default=2).
    #####################################################################################################
    INPUT:
    #####################################################################################################
    trainfile: name of the file along with its data path or a dataframe. It accepts both.
    ts_column: name of the datetime column in your dataset (it could be name or number)
    target: name of the column you are trying to predict. Target could also be the only column in your data
    score_type: 'rmse' is the default. You can choose among "mae", "mse" and "rmse".
    forecast_period: default is 2. How many periods out do you want to forecast? It should be an integer
    time_interval: default is "Month". What is the time period in your data set. Options are: "days",
    model_type: default is "stats". Choice is between "stats", "prophet" and "ml". "All" will build all.
        - stats will build statsmodels based ARIMA< SARIMAX and VAR models
        - ml will build a machine learning model using Random Forests provided explanatory vars are given
        - prophet will build a model using FB Prophet -> this means you must have FB Prophet installed
        - all will build all the above models which may take a long time for large data sets.
    We recommend that you choose a small sample from your data set bedfore attempting to run entire data.
    #####################################################################################################
    and the evaluation metric so it can select the best model. Currently only 2 are supported: RMSE and
    Normalized RMSE (ratio of RMSE to the standard deviation of actuals). Other eval metrics will be soon.
    the target variable you are trying to predict (if there is more than one variable in your data set),
    and the time interval that is in the data. If your data is in a different time interval than given,
    Auto_Timeseries will automatically resample your data to the given time interval and learn to make
    predictions. Notice that except for filename and ts_column which are required, all others are optional.
    Note that optionally you can give a separator for the data in your file. Default is comman (",").
    "time_interval" options are: 'Days', 'Weeks', 'Months', 'Qtr', 'Year', 'Minutes', 'Hours', 'Seconds'.
    Optionally, you can give seasonal_period as any integer that measures the seasonality in the data.
    If not, seasonal_period is assumed automatically as follows: Months = 12, Days = 30, Weeks = 52,
    Qtr = 4, Year = 1, Hours = 24, Minutes = 60 and Seconds = 60.
    If you want to give your own order, please input it as non_seasonal_pdq and seasonal_PDQ in the input
    as tuples. For example, seasonal_PDQ = (2,1,2) and non_seasonal_pdq = (0,0,3). It will accept only tuples.
    The defaul is None and Auto_Timeseries will automatically search for the best p,d,q (for Non Seasonal)
    and P, D, Q (for Seasonal) orders by searching for all parameters from 0 to 12 for each value of
    p,d,q and 0-3 for each P, Q and 0-1 for D.
    #####################################################################################################
    """

    start_time = time.time()

    ### Introductory texts:
    art.tprint("Make   deep\ntime-series\nmagic!!")
    print("-------------------------------------------------------------------")
    print("-------------------------------------------------------------------\n")
    print("SUMMARY STEPS:")
    print("    STEP 1) Extract Data from Source")
    print("    STEP 2) Preprocessing I (Cleaning)")
    print("    STEP 3) EDA I (General)")
    print("    STEP 4) EDA II (Time-Series Stats)")
    print("    STEP 5) Preprocessing II (Transformations)")
    print("    STEP 6) Preprocessing III (Make Supervised)")
    print("    STEP 7) Model Search (DNNs)")
    print("    STEP 8) Model Results Output")

    ##### Best hyper-parameters in statsmodels chosen using the best aic, bic or whatever. Select here.
    stats_scoring = 'aic'
    seed = 99

    ########################### This is where we store all datas in a nested dictionary ##########
    datadict = lambda: defaultdict(datadict)
    data_dict = datadict()
    data_counter = 0

    ########## This is where we start the loading of the data file ######################
    print("\n\n-------------------------------------------------------------------")
    print("STEP 1) Extract Data from Source")
    print("-------------------------------------------------------------------\n")

    # logger.info("Test123.")
    print("Begin extracting the data from source...")
    ts_df = load_ts_data(data, ts_column, sep)
    new_key = f'{data_counter}) Original'
    data_dict[new_key] = ts_df
    print(f"\n--> Extracted data saved in data_dict[{new_key}], see head below:")
    display(HTML(ts_df.head().to_html()))
    data_counter += 1
    # print(ts_df[target].head())
    freq, _ = interval_to_freq(time_interval)

    print("\n\n-------------------------------------------------------------------")
    print("STEP 2) Preprocessing I (Cleaning)")
    print("-------------------------------------------------------------------\n")

    if auto_clean:
        print("Begin initial cleaning of the extract dataset...")
        ts_df = clean_ts_data(ts_df, target, as_freq=freq)
        new_key = f'{data_counter}) Clean'
        data_dict[new_key] = ts_df
        print(f"\n--> Cleaned data saved in data_dict[{new_key}], see head below:")
        display(HTML(ts_df.head().to_html()))
        data_counter += 1
    ipdb.set_trace()
    print("\n\n-------------------------------------------------------------------")
    print("STEP 3) EDA I (General)")
    print("-------------------------------------------------------------------\n")

    # Prevent errors
    pd.plotting.register_matplotlib_converters()

    # Define plot labels
    # title = "Total Electrity Demand in Spain Time-Series"
    title = "PJME Regional Power Demand Time-Series"
    x_label = f'Datetime'
    y_label = f"Total Demand (MW)"

    ts_plot(ts_df, ts_column, target,
            title=title,
            y_label=y_label
            )

    print("\n\n-------------------------------------------------------------------")
    print("STEP 4) EDA II (Time-Series Stats)")
    print("-------------------------------------------------------------------\n")

    print("4.1) Check unit root stationarity of a time series array or an entire dataframe.")
    print("4.2) Using Augmented Dickey-Fuller (ADF) Test.\n")
    print(test_stationarity(ts_df))

    print("4.3) Printing out ETS decomposition plot.\n")
    # ets = ets_decomposition_plot(ts_df, ts_column, target, title, y_label);
    # ets = ets_decomposition_plot(ts_df, ts_column, target, title, y_label,
    #                        prophet=True);
    ets = ets_decomposition_plot(ts_df, ts_column, target, title, y_label,
                                 plotly=True);

    print("Plot out ACF/PACF graph..\n")
    title = "Total Electricity Demand"
    lags_7 = 24*7  # 7-days lag
    lags_30 = 24*30  # 30-days lag
    lags_90 = 24*90  # 90-days lag
    acf_pacf_plot(ts_df, target, title, lags=[lags_7, lags_30])

    print("4.4) Expotential Smoothing Holt-Winters.\n")

    # Set target if not already done so
    if target is None:
        if ts_df.shape[1] == 1:
            ### If there is only one column, you assume that to be the target column ####
            target = ts_df.columns[0]
        else:
            raise ValueError("No target column name specified.")
            return
    elif target in ['first_col', 'first_column']:
        target = ts_df.columns[0]
        print(f"    Taking the first column '{target}' in dataset as target variable.")
    elif target in ['last_col', 'last_column']:
        target = ts_df.columns[-1]
        print(f"    Taking the last column '{target}' in dataset as target variable.")
    # Create univerate time-series from dataset if specified, else leave as it is
    if univarate:
        print(f"Set the dataset to univarate using target col of {target}.")
        ts_df = ts_df[target].to_frame()
        new_key = f'{data_counter}) Univarate'
        data_dict[new_key] = ts_df
        print(f"\n--> Extracted data saved in data_dict[{new_key}] .")
        data_counter += 1

    print("\n\n-------------------------------------------------------------------")
    print("STEP 5) Preprocessing II (Transformations)")
    print("-------------------------------------------------------------------\n")

    # Performs log or power transform and then normalize in one function
    if True:
        print(f"5.1) Performed power transformation using Box-Cox method. Then standardized data.")
    else:
        print(f"5.1) Performed power transformation using Box-Cox method.")
    ts_df, trans_type = log_power_transform(ts_df, target, method='box-cox',
                                            standardize=True)
    new_key = f'{data_counter}) {trans_type}'
    data_dict[new_key] = ts_df
    print(f"\n--> Transformed data saved in data_dict[{new_key}], see head below:")
    display(HTML(ts_df.head().to_html()))
    data_counter += 1

    # Performs log or power transform and then normalize in one function
    print(f"\n5.2) Performed seaonsal adjustment.")
    ts_df, seasonality = decompose(ts_df, target, type='deseasonalize',
                                   model='additive')
    new_key = f'{data_counter}) Deseasonalize'
    data_dict[new_key] = ts_df
    print(f"\n--> Seasonality adjusted data saved in data_dict[{new_key}], see head below:")
    display(HTML(ts_df.head().to_html()))
    data_counter += 1


    ##################################################################################################
    ### Turn the time series index into a variable and calculate the difference.
    ### If the difference is not in days, then it is a hourly or minute based time series
    ### If the difference a multiple of days, then test it for weekly, monthly, qtrly, annual etc.
    ##################################################################################################
    # if ts_df.index.dtype=='int' or ts_df.index.dtype=='float':
    #     ### You must convert the ts_df index into a date-time series using the ts_column given ####
    #     ts_df = ts_df.set_index(ts_column)
    # ts_index = ts_df.index

    ################    IF TIME INTERVAL IS NOT GIVEN DO THIS   ########################
    #######   This is where the program tries to tease out the time period in the data set ###########
    ##################################################################################################
    # if time_interval == '':
    #     ts_index = pd.to_datetime(ts_df.index)
    #     diff = (ts_index[1] - ts_index[0]).to_pytimedelta()
    #     diffdays = diff.days
    #     diffsecs = diff.seconds
    #     if diffsecs == 0:
    #         diff_in_hours = 0
    #         diff_in_days = abs(diffdays)
    #     else:
    #         diff_in_hours = abs(diffdays*24*3600 + diffsecs)/3600
    #     if diff_in_hours == 0 and diff_in_days >= 1:
    #         print('Time series input in days = %s' % diff_in_days)
    #         if diff_in_days == 7:
    #             print('it is a Weekly time series.')
    #             time_interval = 'weeks'
    #         elif diff_in_days == 1:
    #             print('it is a Daily time series.')
    #             time_interval = 'days'
    #         elif 28 <= diff_in_days < 89:
    #             print('it is a Monthly time series.')
    #             time_interval = 'months'
    #         elif 89 <= diff_in_days < 178:
    #             print('it is a Quarterly time series.')
    #             time_interval = 'qtr'
    #         elif 178 <= diff_in_days < 360:
    #             print('it is a Semi Annual time series.')
    #             time_interval = 'qtr'
    #         elif diff_in_days >= 360:
    #             print('it is an Annual time series.')
    #             time_interval = 'years'
    #         else:
    #             print('Time Series time delta is unknown')
    #             return
    #     if diff_in_days == 0:
    #         if diff_in_hours == 0:
    #             print('Time series input in Minutes or Seconds = %s' % diff_in_hours)
    #             print('it is a Minute time series.')
    #             time_interval = 'minutes'
    #         elif diff_in_hours >= 1:
    #             print('it is an Hourly time series.')
    #             time_interval = 'hours'
    #         else:
    #             print('It is an Unknown Time Series delta')
    #             return
    # else:
    #     print('Time Interval is given as %s' % time_interval)

    ##################################################################################################
    ### Transform dataset into supervised ML problem with walk-forward validation.
    ### Shifting time-steps
    ##################################################################################################
    print("\n\n-------------------------------------------------------------------")
    print("STEP 6) Preprocessing III (Make Supervised)")
    print("-------------------------------------------------------------------\n")

    ################# This is where you test the data and find the time interval #######
    #create train, test data
    n_input = interval_to_timesteps('biweek', freq)  # let's input the two weeks (24*14 timesteps)
    n_output = interval_to_timesteps(forecast_period, freq)  # let's forecast the next day (24 timesteps)
    n_val = interval_to_timesteps('biweek', freq)  # validation dataset size
    n_test = interval_to_timesteps('month', freq)

    # Hyperparameterss
    n_features = 1  # number of feature(s)
    n_units = 128   # number of units per layer
    d_rate = 0.15   # dropout rate

    n_batch = batch_size  # batch size
    n_epoch = epochs  # number of epochs

    orig, train, val, test = split_data(ts_df,
                                        n_test=n_test,  # size of test set
                                        n_val=n_val,  # size of validation set
                                        n_input=n_input,   # input timestep seq
                                        n_output=n_output, # output timestep seq
                                        g_min=0,     # min gap ratio
                                        g_max=0.01)  # max gap ratio

    X, y, t = orig  # original data tuple in supervised format
    X_train, y_train, t_train = train
    X_val, y_val, t_val = val
    X_test, y_test, t_test = test

    print("Converted time-series into supervised leraning problem using walk-forward validation:")
    print(f"    Time-series frequency: '{freq}'.")
    print(f"    Input period: {X.shape[1]} timesteps, or 'bikweek'.")
    print(f"    Output (forecast) period: {y.shape[1]} timesteps, or 'day'.")
    print(f"    Original dataset: {ts_df.shape[0]} observations.")
    print(f"    Supervised dataset: {X.shape[0]} observations.")
    print(f"    Training dataset: {X_train.shape[0]} observations.")
    print(f"    Validation dataset: {X_val.shape[0]} observations, or 'biweek'.")
    print(f"    Testing dataset: {X_test.shape[0]} observations, or 'month'.")

    train_prct = round(len(X_train)/len(X)*100, 2)
    val_prct = round(len(X_val)/len(X)*100, 2)
    test_prct = round(len(X_test)/len(X)*100, 2)
    gap_prct = round(100-train_prct-val_prct-test_prct, 2)
    print("\nSplit %:")
    print(f"Train: {train_prct}%, Val: {val_prct}%, Test: {test_prct}%, Gap: {gap_prct}%")

    print("\nDataset shapes:")
    print(f"    Original:")
    print(f"        data shape = {ts_df.shape}")
    print(f"    Supervised:")
    print(f"        X.shape = {X.shape}")
    print(f"        y.shape = {y.shape}")
    print(f"        t.shape = ", t.shape)
    print(f"    Training:")
    print(f"        X_train.shape = {X_train.shape}")
    print(f"        y_train.shape = {y_train.shape}")
    print(f"        t_train.shape = {t_train.shape}")
    print(f"    Validation:")
    print(f"        X_val.shape = {X_val.shape}")
    print(f"        y_val.shape = {y_val.shape}")
    print(f"        t_val.shape = {t_val.shape}")
    print(f"    Testing:")
    print(f"        X_test.shape = {X_test.shape}")
    print(f"        y_test.shape = {y_test.shape}")
    print(f"        t_test.shape = {t_test.shape}")

    new_key = f'{data_counter}) Make Supervised'
    data_dict[new_key]['X_train'] = X_train
    data_dict[new_key]['y_train'] = y_train
    data_dict[new_key]['t_train'] = t_train
    data_dict[new_key]['X_val'] = X_val
    data_dict[new_key]['y_val'] = y_val
    data_dict[new_key]['t_val'] = t_val
    data_dict[new_key]['X_test'] = X_test
    data_dict[new_key]['y_test'] = y_test
    data_dict[new_key]['t_test'] = t_test
    print(f"\n--> Supervised data saved in data_dict[{new_key}].")
    data_counter += 1


    print("\n\n-------------------------------------------------------------------")
    print("STEP 7) Model Search (NNs)")
    print("-------------------------------------------------------------------\n")

    if len(tf.config.list_physical_devices('GPU')) > 0:
        print("GPU is enabled.")
    else:
        print("Running on CPU as GPU is not enabled.")

    ########################### This is where we store all models in a nested dictionary ##########
    mldict = lambda: defaultdict(mldict)
    ml_dict = mldict()
    try:
        if model_type.lower() == 'all':
            print('Running all model types. This will take a long time. Be Patient...')
    except:
        print('Check if your model type is a string or one of the available types of models')
    ######### This is when you need to use FB Prophet ###################################
    ### When the time interval given does not match the tested_time_interval, then use FB.
    #### Also when the number of rows in data set is very large, use FB Prophet, It is fast.
    #########                RNN              ###################################
    if model_type.lower() in ['rnn', 'all']:
        name = 'RNN'
        print(colorful.BOLD + '\n\n7.1) Running a vanilla RNN Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_rnn_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    RNN may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    if model_type.lower() in ['lstm', 'all']:
        name = 'LSTM'
        print(colorful.BOLD + '\n\n7.2) Running a LSTM Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_lstm_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    LSTM may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    if model_type.lower() in ['gru', 'all']:
        name = 'GRU'
        print(colorful.BOLD + '\n\n7.3) Running a GRU Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_gru_model(
                                        X_train, y_train, X_val, y_val, n_input,
                                        n_output, n_units=n_units, d_rate=d_rate,
                                        n_epoch=n_epoch, n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    GRU may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val
    if model_type.lower() in ['convlstm', 'all']:
        name = 'CONVLSTM'
        print(colorful.BOLD + '\n\n7.4) Running a ConvLSTM Model...' + colorful.END)
        try:
            #### If RNN needs to run, tensorflow needs to be installed. Check it here ###
            model, pred, rmse, norm_rmse = build_convlstm_model(X_train, y_train, X_val, y_val,
                                                                l_subseq=n_output, # length of subsequence
                                                                n_col=n_output,    # length of "image" col
                                                                n_units=n_units,
                                                                d_rate=d_rate,
                                                                n_epoch=n_epoch,
                                                                n_batch=n_batch)
            ml_dict[name]['model'] = model
            ml_dict[name]['forecast'] = pred
            ##### Make sure that RMSE works, if not set it to np.inf  #########
            if score_type == 'rmse':
                score_val = rmse
            else:
                score_val = norm_rmse
        except:
            print('    ConvLSTM may not be installed or Model is not running...')
            score_val = np.inf
        ml_dict[name][score_type] = score_val

    ######## Selecting the best model based on the lowest rmse score ######
    f1_stats = {}
    for key, val in ml_dict.items():
        f1_stats[key] = ml_dict[key][score_type]
    best_model_name = min(f1_stats.items(), key=operator.itemgetter(1))[0]

    print("\n-----------------------------------------------------------------")
    print("-----------------------------------------------------------------")
    print(colorful.BOLD + '\nBest Model is:' + colorful.END)
    print('    %s' % best_model_name)
    best_model = ml_dict[best_model_name]['model']
    #print('    Best Model Forecasts: %s' %ml_dict[best_model_name]['forecast'])
    print('    Best Model Score: %0.2f' % ml_dict[best_model_name][score_type])

    return ml_dict, data_dict


##########################################################
#Defining DEEP_TIMESERIES here
##########################################################


if	__name__	== "__main__":
    version_number = __version__
    print("""Running Deep Timeseries version: %s...Call by using:
        auto_ts.Auto_Timeseries(trainfile, ts_column,
                            sep=',', target=None, score_type='rmse', forecast_period=2,
                            time_interval='Month', non_seasonal_pdq=None, seasonality=False,
                            seasonal_period=12, seasonal_PDQ=None,
                            verbose=0)
    To get detailed charts of actuals and forecasts, set verbose = 1""" % version_number)
else:
    version_number = __version__
    print("""Imported Deep_Timeseries version: %s. Call by using:
        auto_ts.Auto_Timeseries(trainfile, ts_column,
                            sep=',', target=None, score_type='rmse', forecast_period=2,
                            time_interval='Month', non_seasonal_pdq=None, seasonality=False,
                            seasonal_period=12, seasonal_PDQ=None,
                            verbose=0)
    To get detailed charts of actuals and forecasts, set verbose = 1""" % version_number)
