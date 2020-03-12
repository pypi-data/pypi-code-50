"""
data_prep.py - Extract data from date range and create models
Usage:
    data_prep.py [options]
    data_prep.py -h | --help

Options:
    -h --help             Show this message.
    --output_folder=OUT   Output folder for the data and reports to be saved.
    --source=SRC          Datasource for where the data will be downloaded from.
    --country=CNT         Arg for filtering by a specific country
"""
from __future__ import print_function
import os
import sys
import docopt
import pandas as pd
from string import capwords
from difflib import get_close_matches
from datetime import datetime, date, time 

from covidify.sources import github, wiki
from covidify.config import REPO, TMP_FOLDER, TMP_GIT, DATA
from covidify.utils.utils import replace_arg_score


args = docopt.docopt(__doc__)
out = args['--output_folder']
country = args['--country']
source = args['--source']

    
if '_' in country:
    country = replace_arg_score(country)

if country == 'Global':
    country = None

if source == 'git':
    df = github.get()
    
elif source == 'wiki':
    print('Apologies, the wikipedia source is not ready yet - getting github data')
    df = github.get()
    


def get_similar_countries(c, country_list):
    pos_countries = get_close_matches(c, country_list)
    
    if len(pos_countries) > 0:
        print('\033[1;31m'+c, 'was not listed. did you mean', pos_countries[0].capitalize() + '?\033[0;0m')
        
        #Only delete if its a covidify generated folder
        if 'Desktop/covidify-output-' in out:
            os.system('rm -rf ' + out)
        sys.exit(1)
    else:
        print('\033[1;31m'+c, 'was not listed.\033[0;0m')
        if 'Desktop/covidify-output-' in out:
            os.system('rm -rf ' + out)
        sys.exit(1)
        
def check_specified_country(df, country):
    '''
    let user filter reports by country, if not found
    then give a option if the string is similar
    '''
    
    # Get all unique countries in the data
    country_list = list(map(lambda x:x.lower().strip(), set(df.country.values)))

    if country:
        
        print('Country specified!')
        if country.lower() == 'china': #Mainland china china dont come up as similar
            print(country, 'was not listed. did you mean Mainland China??')
            sys.exit(1)
        # give similar option if similarity found
        if country.lower() not in country_list:
            get_similar_countries(country, country_list)
            
        else:
            #Return filtered dataframe
            print('... filtering data for', country)
            if len(country) == 2:
                print('LEN OF COUNTRY:', len(country))
                df = df[df.country == country.upper()]
            else:
                df = df[df.country == capwords(country)]
            return df
    else:
        print('No specific country specified')
        return df

df = check_specified_country(df, country)


# sheets need to be sorted by date value
print('Sorting by datetime...')
current_date = str(datetime.date(datetime.now()))

# if df.date.max() == current_date:
#     df = df[df.date != df.date.max()]
# else:
#     df = df[df.date != current_date]

df = df.sort_values('datetime')

'''
Get the difference of the sum totals for each
date and plot them on a trendline graph
'''
def get_new_cases(tmp, col):
    diff_list = []
    tmp_df_list = []
    df = tmp.copy()

    for i, day in enumerate(df.sort_values('date').date.unique()):    
        tmp_df = df[df.date == day]
        tmp_df_list.append(tmp_df[col].sum())
        
        if i == 0:
            diff_list.append(tmp_df[col].sum())
        else:
            diff_list.append(tmp_df[col].sum() - tmp_df_list[i-1])
        
    return diff_list

def get_moving_average(tmp, col):
    df = tmp.copy()
    return df[col].rolling(window=2).mean()

def get_exp_moving_average(tmp, col):
    df = tmp.copy()
    return df[col].ewm(span=2, adjust=True).mean()


print('Calculating dataframe for new cases...')
daily_cases_df = pd.DataFrame([])
daily_cases_df['new_confirmed_cases'] = get_new_cases(df, 'confirmed')
daily_cases_df['new_deaths'] = get_new_cases(df, 'deaths')
daily_cases_df['new_recoveries'] = get_new_cases(df, 'recovered')
daily_cases_df['date'] = df.date.unique()

#Moving average
daily_cases_df['confirmed_MA'] = get_moving_average(daily_cases_df, 'new_confirmed_cases')
daily_cases_df['deaths_MA'] = get_moving_average(daily_cases_df, 'new_deaths')
daily_cases_df['recovered_MA'] = get_moving_average(daily_cases_df, 'new_recoveries')

#Exponential moving average
daily_cases_df['confirmed_exp_MA'] = get_exp_moving_average(daily_cases_df, 'new_confirmed_cases')
daily_cases_df['deaths_exp_MA'] = get_exp_moving_average(daily_cases_df, 'new_deaths')
daily_cases_df['recovered_exp_MA'] = get_exp_moving_average(daily_cases_df, 'new_recoveries')


'''
Calculate the number of people that are ACTUALLY infected on a given day
currently infected = sum of people date - (recovored + died)
ex: 5 = 10 - (4 - 1)

'''
current_infected = pd.DataFrame([])
current_infected['currently_infected'] = (df.groupby('date').confirmed.sum() - \
                                          (df.groupby('date').deaths.sum() + df.groupby('date').recovered.sum()))
current_infected['delta'] = (current_infected['currently_infected'] - df.groupby('date').confirmed.sum())
daily_cases_df = pd.merge(daily_cases_df, current_infected, how='outer', on='date')


#Create date of extraction folder
data_folder = os.path.join('data', str(datetime.date(datetime.now())))
save_dir = os.path.join(out, data_folder)

if not os.path.exists(save_dir):
    os.system('mkdir -p ' + save_dir)

print('Creating subdirectory for data...')
print('...', save_dir)

print('Saving...')
file_name = 'agg_data_{}.parquet.gzip'.format(datetime.date(datetime.now()))
df.astype(str).to_parquet(os.path.join(save_dir, file_name), compression='gzip')
print('...', file_name)


csv_file_name = 'agg_data_{}.csv'.format(datetime.date(datetime.now()))
df.astype(str).to_csv(os.path.join(save_dir, csv_file_name))
print('...', csv_file_name)


daily_cases_file_name = 'trend_{}.csv'.format(datetime.date(datetime.now()))
daily_cases_df.astype(str).to_csv(os.path.join(save_dir, daily_cases_file_name))
print('...', daily_cases_file_name)

print('Done!')