import pandas as pd
import numpy as np
from .download import *
from .cleaner import *
from .join import range_join, join_by_month_or_year


class Data():
    def __init__(self):
        #Download the data
        self.download()

        #initialize a dictionary or somthing to hold dataframes
        self.dataframes = {}
        #+++++++++++++++++++++++++++++++++++++++++++get and parse the fish data ++++++++++++++++++++++++++++++++++++++++++++++++++
        download_msg = "Cleaning fish data . . ."
        print(download_msg, end='\r')
        fish_data_path = "lakepowell/data/fish_data"
        #build the fish data parsar
        fish_df = pd.read_excel(fish_data_path)
        column_headers = ["FishID","Date", "TREND","Gear", "Species", "Sex", "Length",
                          "Mass", "Ktl", "Weight", "Maturity", "Age structure",
                          "stomach", "gonads", "fat_index", "parasite", "misc 1 text",
                          "misc 2 num", "misc 3 text", "misc 4 num", "Site", "KFL"]

        fish_df.columns = column_headers

        #clean fish data
        clean = Cleaner(fish_df)
        fish_df = clean.clean_fish_data() #all clean values default to true
        # print(clean.get_dirty_data())

        #split fish data date into Day, Month, Year columns
        fish_df['Day'] = pd.DatetimeIndex(fish_df['Date']).day
        fish_df['Month'] = pd.DatetimeIndex(fish_df['Date']).month
        fish_df['Year'] = pd.DatetimeIndex(fish_df['Date']).year

        self.dataframes["fish_data"] = fish_df
        print(" " * len(download_msg), end='\r') # Erase the loading message


        #++++++++++++++++++++++++++++++++++++++++++get and parse the water data +++++++++++++++++++++++++++++++++++++++++++++++++++++
        download_msg = "Cleaning water data . . ."
        print(download_msg, end='\r')
        water_data_path =  "lakepowell/data/water_data"
        water_df = pd.read_csv(water_data_path)

        new = water_df["DATE MEASURED"].str.split(r",\s|\s", n = 3, expand = True)

        #------------------- convert month to digit -------------------
        months = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,
                    'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}
        df_months = new[1]
        for i in range(0, len(df_months)):
            df_months[i] = months.get(df_months[i])
        #--------------------------------------------------------------

        water_df["MONTH"]= df_months.astype(int)
        water_df["DAY"]= new[2].astype(int)
        water_df["YEAR"]= new[3].astype(int)

        self.dataframes['water_data'] = water_df
        print(" " * len(download_msg), end='\r') # Erase the loading message


    def download(self):
        download_msg = "Downloading fish data . . ."
        print(download_msg, end='\r')
        fish_data_path = download_fish_file()
        print(" " * len(download_msg), end='\r') # Erase the downloading message

        download_msg = "Downloading water data . . ."
        water_data_path = download_water_data()
        print(" " * len(download_msg), end='\r') # Erase the downloading message


    def get_fish_data(self):
        return self.dataframes["fish_data"]

    def get_water_data(self):
        return self.dataframes["water_data"]

    def join_by_range(self, fish_data, water_data, spread, operation):
        df = range_join(fish_data, water_data, spread, operation)
        return df

    def join_by_year(self, fish_data, water_data):
        df = join_by_month_or_year(fish_data, water_data, time_unit="year")
        return df

    def join_by_month(self, fish_data, water_data):
        df = join_by_month_or_year(fish_data, water_data, time_unit="month")
        return df
