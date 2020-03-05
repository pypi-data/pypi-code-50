"""
data_exploration.py - Extract data from date range and create models
Usage:
    data_exploration.py [options]
    data_exploration.py -h | --help

Options:
    -h --help             Show this message.
    --output_folder=OUT   Output folder for the data and reports to be saved
"""

from __future__ import print_function
import pandas as pd
import numpy as np
import os
import glob
import docopt
import pickle
import os.path
from datetime import datetime
import pyarrow
import matplotlib.pyplot as plt
# %matplotlib inline

font = {'weight' : 'bold',
        'size'   : 22}
plt.rc('font', **font)


#set ggplot style
plt.style.use('ggplot')
 
args = docopt.docopt(__doc__)
out = args['--output_folder']

# Dynamic parameters
data_dir  = os.path.join(out, 'data', str(datetime.date(datetime.now())))
agg_file  = 'agg_data_{}.parquet.gzip'.format(datetime.date(datetime.now()))
trend_file  = 'trend_{}.csv'.format(datetime.date(datetime.now()))
report  = 'report_{}.xlsx'.format(datetime.date(datetime.now()))


# import data
print('Importing Data...')
agg_df = pd.read_parquet(os.path.join(data_dir, agg_file))
daily_df = pd.read_csv(os.path.join(data_dir, trend_file))

#Create place to save diagrams
image_dir =  os.path.join(out,'reports', 'images')
reports_dir =  os.path.join(out,'reports')

if not os.path.exists(image_dir):
    print('Creating reports folder...')
    os.system('mkdir -p ' + image_dir)

# Convert types
for col in ['confirmed', 'deaths', 'recovered']:
    agg_df[col] = agg_df[col].replace('', 0).astype(int)


##### Define Graphs #####

# Plot and save trendline graph
def create_trend_line(tmp_df, col, col2, col3):
    fig, ax = plt.subplots(figsize=(20,10))
    tmp_df.groupby(['date'])[[col, col2, col3]].sum().plot(ax=ax, marker='o')
    fig = ax.get_figure()
    fig.savefig(os.path.join(image_dir, '{}_trendline.jpg'.format(col)))

def create_bar(tmp_df, col, rgb):
    fig, ax = plt.subplots(figsize=(20,10))
    tmp = tmp_df.groupby(['date'])[[col]].sum()
    tmp.plot.bar(ax=ax, rot=45, color=rgb)
    fig = ax.get_figure()
    fig.savefig(os.path.join(image_dir, '{}_bar.jpg'.format(col)))
    
def create_stacked_bar(tmp_df, col1, col2, fig_title):
    tmp_df = tmp_df.set_index('date')
    fig, ax = plt.subplots(figsize=(20,10))
    tmp_df[[col2, col1]].plot.bar(ax=ax,
                                  rot=45,
                                  stacked=True,
                                  title=fig_title);
    fig = ax.get_figure()
    fig.savefig(os.path.join(image_dir, '{}_stacked_bar.jpg'.format(col2)))
    
    
##### Create Graphs #####
    
print('Creating graphs...')
print('... Time Series Trend Line')
# Time Series Data Plots
create_trend_line(agg_df, 'confirmed', 'deaths', 'recovered')


print('... Daily Figures')
# Daily Figures Data Plots
daily_figures_cols = ['new_confirmed_cases', 'new_deaths', 'new_recoveries', 'currently_infected']
for col, rgb in zip(daily_figures_cols, ['tomato', 'lightblue', 'mediumpurple', 'green']):
    create_bar(daily_df, col, rgb)    
    
# Trend line for new cases
create_trend_line(daily_df, 'new_confirmed_cases', 'new_deaths', 'new_recoveries')
    
    
print('... Daily New Infections Differences')
new_df = pd.DataFrame([])
new_df['date'] = daily_df['date']
new_df['confirmed_cases'] = agg_df.groupby(['date']).confirmed.sum().values - daily_df.new_confirmed_cases
new_df['new_confirmed_cases'] = daily_df.new_confirmed_cases
create_stacked_bar(new_df, 'new_confirmed_cases', 'confirmed_cases', "Stacked bar of confirmed and new cases by day")



print('Creating excel spreadsheet report...')
workbook_writer = pd.ExcelWriter(os.path.join(reports_dir, report), engine='xlsxwriter')


# Add daily summary to spreadsheet
daily_df.to_excel(workbook_writer, sheet_name='daily figures')  


workbook = workbook_writer.book

def get_image_types(path):
    # get all the possible types of images in
    # the passed directory path
    types = []
    for fn in glob.glob(os.path.join(path, '*.jpg')):
        types.append(fn.split('_',)[-1].split('.')[0])
    
    return types

# Get all images for each type
def read_images(path, graph_type):
    image_list = []
    for fn in glob.glob(os.path.join(path, '*_{}.jpg'.format(graph_type))):
        image_list.append(fn)    
    images = {graph_type : image_list}
    return dict(images)

image_types = get_image_types(image_dir)

padding = 1 # Set padding for images in spreadsheet
for types in set(image_types):
    print('... reading images for:', types)
    type_dict = read_images(image_dir, types)
    
    # Add image to the worksheet
    worksheet = workbook.add_worksheet(name='{}_graphs'.format(types))
    for image in type_dict[types]:
        worksheet.insert_image('A' +str(padding), image) 
        padding += 50
    padding = 1
    
workbook.close()

print('Done!')