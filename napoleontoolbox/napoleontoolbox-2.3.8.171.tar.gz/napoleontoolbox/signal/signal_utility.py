#!/usr/bin/env python
# coding: utf-8
from napoleontoolbox.utility import metrics

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


def reconstitute_signal_perf(data=None, initial_price = 1. , average_execution_cost = 7.5e-4 , transaction_cost = True, print_turnover = False):
    data['turn_over'] = abs(data['signal'] - data['signal'].shift(-1).fillna(0.))
    if print_turnover:
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