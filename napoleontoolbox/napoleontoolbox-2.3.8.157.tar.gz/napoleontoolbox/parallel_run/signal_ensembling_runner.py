#!/usr/bin/env python
# coding: utf-8

from abc import ABC, abstractmethod

import pandas as pd

from napoleontoolbox.file_saver import dropbox_file_saver
from napoleontoolbox.utility import metrics
from numpy.lib.stride_tricks import as_strided as stride
from napoleontoolbox.signal import signal_generator

import json


def reconstitute_signal_perf(data=None, initial_price = 1. , average_execution_cost = 7.5e-4 , transaction_cost = True):
    data['turn_over'] = abs(data['signal'] - data['signal'].shift(-1).fillna(0.))
    print('average hourly turn over')
    print(data['turn_over'].sum() / len(data))
    data['close_return'] = data['close'].pct_change()
    data['reconstituted_close'] = metrics.from_ret_to_price(data['close_return'],initial_price=initial_price)
    data['non_adjusted_perf_return'] = data['close_return'] * data['signal']
    if transaction_cost :
        data['perf_return'] = data['non_adjusted_perf_return']- data['turn_over']*average_execution_cost
    else :
        data['perf_return'] = data['non_adjusted_perf_return']
    data['reconstituted_perf'] = metrics.from_ret_to_price(data['perf_return'],initial_price=initial_price)
    return data

def roll_wrapper(rolled_df, lookback_window, skipping_size, function_to_apply, trigger):
    signal_df = roll(rolled_df, lookback_window).apply(function_to_apply)
    signal_df = signal_df.to_frame()
    signal_df.columns = ['signal_gen']
    signal_df['signal'] = signal_df['signal_gen'].shift()
    if trigger:
        signal_df['signal'] =  signal_df['signal'].fillna(method='ffill')

    signal_df = signal_df.fillna(0.)
    rolled_df = pd.merge(rolled_df, signal_df, how='left', left_index=True, right_index= True)
    rolled_df = rolled_df.iloc[skipping_size:]
    return rolled_df

def roll(df, w):
    v = df.values
    d0, d1 = v.shape
    s0, s1 = v.strides
    restricted_length = d0 - (w - 1)
    a = stride(v, (restricted_length, w, d1), (s0, s0, s1))
    rolled_df = pd.concat({
        row: pd.DataFrame(values, columns=df.columns)
        for row, values in zip(df.index[-restricted_length:], a)
    })
    return rolled_df.groupby(level=0)

def convert_to_sql_column_format(run):
    run = run.replace('[', 'ccg')
    run = run.replace(']', 'ccd')
    run = run.replace(',', 'comma')
    run = run.replace(' ', 'space')
    run = run.replace('.', 'dot')
    run = run.replace('-', 'minus')
    run = run.replace('"', 'dqq')
    run = run.replace("'", 'sqq')
    run = run.replace('{', 'aag')
    run = run.replace('}', 'aad')
    run = run.replace(':', 'dodo')
    return run

def recover_to_sql_column_format(run):
    run = run.replace('ccg','[')
    run = run.replace('ccd',']')
    run = run.replace('comma',',')
    run = run.replace('space',' ')
    run = run.replace('dot','.')
    run = run.replace('minus','-')
    run = run.replace('dqq','"')
    run = run.replace('sqq',"'")
    run = run.replace('aag','{')
    run = run.replace('aad','}')
    run = run.replace('dodo',':')
    return run

class AbstractRunner(ABC):
    def __init__(self, starting_date = None, running_date = None, drop_token=None, dropbox_backup = True, hourly_pkl_file_name='hourly_candels.pkl', signals_list = None, local_root_directory='../data/', user = 'napoleon'):
        super().__init__()
        self.hourly_pkl_file_name=hourly_pkl_file_name
        self.signals_list = signals_list
        self.local_root_directory=local_root_directory
        self.user=user
        self.dropbox_backup = dropbox_backup
        self.dbx = dropbox_file_saver.NaPoleonDropboxConnector(drop_token=drop_token,dropbox_backup=dropbox_backup)
        self.running_date = running_date
        self.starting_date = starting_date

    @abstractmethod
    def runTrial(self,saver,  seed, trigger, signal_type, idios_string, transaction_costs):
        pass


class EnsemblingSignalRunner(AbstractRunner):
    def runTrial(self, saver, seed, trigger, transaction_costs):
        hourly_df = pd.read_pickle(self.local_root_directory + self.hourly_pkl_file_name)
        hourly_df = hourly_df.sort_index()
        print('time range before filtering ')
        print(max(hourly_df.index))
        print(min(hourly_df.index))
        hourly_df = hourly_df[hourly_df.index >= self.starting_date]
        hourly_df = hourly_df[hourly_df.index <= self.running_date]
        print('time range after filtering ')
        print(max(hourly_df.index))
        print(min(hourly_df.index))

        cumulated_signals = None
        counter = 0
        for me_signal in self.signals_list:
            run_json_string = recover_to_sql_column_format(me_signal)
            params = json.loads(run_json_string)
            signal_type = params['signal_type']

            print('Launching computation with parameters : '+run_json_string)
            if signal_type == 'long_only':
                hourly_df['signal']=1.
            else:
                lookback_window = params['lookback_window']
                skipping_size = lookback_window
                # kwargs = {**generics, **idios}
                signal_generation_method_to_call = getattr(signal_generator, signal_type)
                hourly_df = roll_wrapper(hourly_df, lookback_window, skipping_size,
                                          lambda x: signal_generation_method_to_call(data=x, **params), trigger)
                hourly_df = reconstitute_signal_perf(data = hourly_df, transaction_cost = False)

            if cumulated_signals is None:
                cumulated_signals = hourly_df[['close','signal','turn_over']]
                cumulated_signals = cumulated_signals.rename(columns={'signal': 'signal'+str(counter),'turn_over':'turn_over'+str(counter)})
            else :
                cumulated_signals['signal'+str(counter)]=None
                cumulated_signals['turn_over'+str(counter)]=None
            hourly_df = hourly_df.drop(columns = ['signal','turn_over','reconstituted_perf','non_adjusted_perf_return','perf_return'])
            counter = counter + 1
        print('done')






