import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date,datetime,timedelta
import gmaps

file_confirmed = 'https://raw.githubusercontent.com/scherala/covid_py/master/covid_py/data/time_series_19-covid-Confirmed.csv'
file_recovered = 'https://raw.githubusercontent.com/scherala/covid_py/master/covid_py/data/time_series_19-covid-Recovered.csv'
file_deaths = 'https://raw.githubusercontent.com/scherala/covid_py/master/covid_py/data/time_series_19-covid-Deaths.csv'

def get_confirmed_cases():
    return pd.read_csv(file_confirmed)

def get_recovered_cases():
    return pd.read_csv(file_recovered)

def get_death_cases():
    return pd.read_csv(file_deaths)

def plot_cases(df,date,y_label):
    columns = [df.columns[1]]
    columns = columns + [c for c in df.columns[4:]]
    df[columns].iloc[:,1:] = df[columns].iloc[:,1:].apply(pd.to_numeric)
    result = df[columns].groupby('Country/Region').sum()
    result = np.log(result)
    plt.figure(figsize=(25, 6))
    result = result.sort_values(by=date,ascending=False)
    y = result.index
    x = result[date]
    plt.bar(y, x, align='center', alpha=0.5)
    plt.ylabel(y_label)
    plt.xticks(rotation=90)
    plt.show()

def plot_confirmed_cases(date_in):
    plot_cases(get_confirmed_cases(),date_in,'confirmed')
    
def plot_recovered_cases(date_in):
    plot_cases(get_recovered_cases(),date_in,'recovered')
    
def plot_death_cases(date_in):
    plot_cases(get_death_cases(),date_in,'deaths')
    
def plot_cumulative_data():
    df_c = get_confirmed_cases()
    df_r = get_recovered_cases()
    df_d = get_death_cases()
    df_c_sum = df_c[df_c.columns[4:]].sum(axis=0)
    df_r_sum = df_r[df_r.columns[4:]].sum(axis=0)
    df_d_sum = df_d[df_d.columns[4:]].sum(axis=0)
    df_a_sum = df_c_sum-df_r_sum
    plt.figure(figsize=(12, 6))
    plt.plot(df_a_sum.index,df_a_sum.values,color='blue')
    plt.plot(df_r_sum.index,df_r_sum.values,color='red')
    plt.plot(df_d_sum.index,df_d_sum.values,color='green')
    plt.xticks(rotation=45)
    
def get_info_by_country():
    df_c = get_confirmed_cases()
    df_r = get_recovered_cases()
    df_d = get_death_cases()
    result = pd.DataFrame()
    columns = [df_c.columns[1]]
    columns = columns + [c for c in df_c.columns[4:]]
    df_c[columns].iloc[:,1:] = df_c[columns].iloc[:,1:].apply(pd.to_numeric)
    df_r[columns].iloc[:,1:] = df_r[columns].iloc[:,1:].apply(pd.to_numeric)
    df_d[columns].iloc[:,1:] = df_d[columns].iloc[:,1:].apply(pd.to_numeric)
    result_c = df_c[columns].groupby('Country/Region').sum()
    result['confirmed'] = result_c[result_c.columns].sum(axis=1)
    result_r = df_r[columns].groupby('Country/Region').sum()
    result['recovered'] = result_r[result_r.columns].sum(axis=1)
    result_d = df_d[columns].groupby('Country/Region').sum()
    result['death'] = result_d[result_d.columns].sum(axis=1)
    result['Recovery rate'] = result['recovered']/result['confirmed']*100
    result['Death rate'] = result['death']/result['confirmed']*100
    result = result.sort_values(ascending=False,by='confirmed')
    return result

def plot_new_cases_china_vs_other():
    data_confirmed = get_confirmed_cases()
    dates = data_confirmed.columns[4:]
    df_new = pd.DataFrame()
    df_new['Country/Region'] = data_confirmed['Country/Region']
    for i in range(1,len(dates)):
        df_new['confirmed'+dates[i]] = data_confirmed[dates[i]] - data_confirmed[dates[i-1]]
    new_cases_china = df_new[df_new['Country/Region'] == 'Mainland China'].sum(axis=0)[1:].values
    new_cases_rest = df_new[df_new['Country/Region'] != 'Mainland China'].sum(axis=0)[1:].values
    plt.figure(figsize=(20, 6))
    plt.plot(dates[1:], new_cases_china,label = 'china')
    plt.plot(dates[1:], new_cases_rest,label = 'rest')
    plt.xticks(rotation=45)
    plt.ylabel('New Cases')
    plt.legend(framealpha=1, frameon=True);
    plt.show()

def show_map(api_key):
    gmaps.configure(api_key)
    data_confirmed = get_confirmed_cases()
    columns = data_confirmed.columns[4:]
    data_confirmed['sum_all'] = data_confirmed[columns].sum(axis=1)
    locations = data_confirmed[['Lat','Long']]
    weights = data_confirmed['sum_all']
    fig = gmaps.figure(center=(1.0, -1.0), zoom_level=2)
    heatmap = gmaps.heatmap_layer(locations,weights)
    heatmap.max_intensity=10
    heatmap.point_radius = 5
    fig.add_layer(heatmap)
    return fig
