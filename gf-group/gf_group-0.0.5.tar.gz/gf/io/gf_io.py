# -*- coding: utf-8 -*-
"""
Created on Tue March 10 2020

/*
 * GNU GPL v3 License (by, nc, nd, sa)
 *
 * Copyright 2020 GEOframe group
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

@author: GEOframe group
"""

import os as os
import pandas as pd
import numpy as np
from datetime import datetime


def read_OMS_timeseries(file_name, nan_values):
    '''
    Read a timeseries .csv file formatted for OMS console
   
    :param file_name: file name of the csv file.
    :type file_name: string
   
    :param nan_value: value used for no values.
    :type nan_value: double

    :return pandas dataframe
   
    @author: Niccolò Tubini
    '''
    
    df = pd.read_csv(file_name,skiprows=3,parse_dates=[1],header=1,low_memory=False)
    df = df.drop(['ID'],axis=1)
    df = df.drop([0,1],axis=0)
    df.columns.values[0] = 'Datetime'
    df.set_index('Datetime', inplace = True)
    df = df.astype('float64', copy = True)
    df[df <= nan_values]=np.nan 
   
    return df



def write_OMS_timeseries(df, start_date, frequency, file_name):
    '''
    Save a timeseries dataframe to .csv file with OMS format
   
    :param df: dataframe containing the timeseries. Each column correspond to a station/centroid and the 
	the header contains the ID of the station/centroid.
    :type df: pandas.dataframe
   
    :param start_date: start date of the timeseries. 'dd-mm-yyyy hh:mm'.
    :type start_date: str
   
    :param frequency: frequency of the timeseries. 'H': hourly, 'D': daily
	
    :type frequency: str
   
    :param file_name: output file name.
    :type file_name: str
   
    @author: Niccolò Tubini
    '''
	
    date_rng = pd.date_range(start=start_date, periods=df.shape[0], freq=frequency)
    df_out = pd.DataFrame(date_rng, columns=['date'])
    df_out = pd.concat([df_out, df],sort=False, axis=1)
    # add an empty column
    df_out.insert(loc=0, column='empty', value=np.nan)
    print(df_out.shape)
    n_col = df_out.shape[1]-2
    value = []
    ID = []
    double = []
    commas = []
    for i in range(0,n_col):
        value.append(',value_'+str(df_out.columns[i+2]))
        ID.append(','+str(df_out.columns[i+2]))
        double.append(',double')
        commas.append(',')
   
    line_4 = '@H,timestamp'+' '.join(value) + '\n'
    line_5 = 'ID,'+' '.join(ID) + '\n'
    line_6 = 'Type,Date' + ''.join(double) + '\n'
    line_7 = 'Format,yyyy-MM-dd HH:mm' + ' '.join(commas) + '\n'

    date = datetime.today().strftime('%Y-%m-%d %H:%M')
    with open(file_name,'w') as file:
        file.write('@T,table\nCreated,'+ date +'\nAuthor,HortonMachine library\n')
        file.write(line_4)
        file.write(line_5)
        file.write(line_6)
        file.write(line_7)

    df_out.to_csv(file_name, header=False, index=False, mode="a", date_format='%Y-%m-%d %H:%M')
    print ('\n\n***SUCCESS writing!  '+ file_name)