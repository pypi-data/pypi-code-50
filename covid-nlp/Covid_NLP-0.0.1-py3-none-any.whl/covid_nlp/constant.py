import os
import pathlib

from enum import Enum

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text

import pandas as pd


class Urls():
    CONFIRMED = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
    DEATH = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"
    RECOVERY = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
    USE = "https://tfhub.dev/google/universal-sentence-encoder-qa/3"



module = hub.load(Urls.USE)

data_path = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(data_path, "data.csv"), delimiter=',')

response = df["Response"].values
context = df["Context"].values

response_embeddings = module.signatures['response_encoder'](
        input=tf.constant(response),
        context=tf.constant(context))


confirmed_df = pd.read_csv(Urls.CONFIRMED)
death_df = pd.read_csv(Urls.DEATH)
recovery_df = pd.read_csv(Urls.RECOVERY)


# slice df to get numbers confirmed, deaths and recoveries
cols = confirmed_df.keys()


all_confirmed = confirmed_df.loc[:, cols[4]:cols[-1]]
all_deaths = death_df.loc[:, cols[4]:cols[-1]]
all_recoveries = recovery_df.loc[:, cols[4]:cols[-1]]

dates = all_confirmed.keys()

# get latest confirmed
latest_confirmed = confirmed_df[dates[-1]]
latest_deaths = death_df[dates[-1]]
latest_recoveries = recovery_df[dates[-1]]


# get cumulative number case by country
unique_countries = list(confirmed_df['Country/Region'].unique())

