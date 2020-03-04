import ipdb
import pandas as pd
import numpy as np
from collections import defaultdict
import dnntime as dt
from dnntime.models import build_rnn_model, build_lstm_model, build_gru_model, \
                           build_convlstm_model
from ..utils import colorful


def run_deep_model(ml_dict, X_train, y_train, X_val, y_val, n_input, n_output,
                   n_units, d_rate, n_epoch, n_batch, score_type):

    name = 'RNN'
    print(colorful.BOLD + '\n10.1) Running a vanilla RNN Model...' + colorful.END)
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

    name = 'LSTM'
    print(colorful.BOLD + '\n\n10.2) Running a LSTM Model...' + colorful.END)
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

    name = 'GRU'
    print(colorful.BOLD + '\n\n10.3) Running a GRU Model...' + colorful.END)
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

    name = 'CONVLSTM'
    print(colorful.BOLD + '\n\n10.4) Running a ConvLSTM Model...' + colorful.END)
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

    return ml_dict
