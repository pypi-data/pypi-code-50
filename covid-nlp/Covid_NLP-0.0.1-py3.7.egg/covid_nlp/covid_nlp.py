import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tensorflow_text

import pandas as pd

from covid_nlp.constant import *


class covid():
    @staticmethod
    def list_country():
        return unique_countries

    @staticmethod
    def confirmed_country(country_name: str = None):
        """
            > Get all confirmed country with param

        Returns:
            [type] -- [description]
        """

        country_confirmed_cases = []
        no_cases = [] # remove if no case

        for i in unique_countries:
            cases = latest_confirmed[confirmed_df['Country/Region'] == i].sum()
            if cases > 0:
                country_confirmed_cases.append(cases)
            else:
                no_cases.append(i)

        for i in no_cases:
            unique_countries.remove(i)

        dict_countries = dict(zip(unique_countries, country_confirmed_cases))

        if country_name:
            return {country_name: dict_countries[country_name]}
        else:
            return dict_countries


    @staticmethod
    def world_stats(day: int = None):
        world_cases = []
        total_deaths = [] 
        mortality_rate = []
        total_recovered = [] 
    

        try:
            if day:
                if day < 0:
                    raise ValueError('Negative values not allowed.')

                day = day - 1
                world_cases = all_confirmed[dates[day]].sum()
                total_deaths = all_deaths[dates[day]].sum()
                total_recovered = all_recoveries[dates[day]].sum()
                mortality_rate = total_deaths/total_recovered
            else:
                for i in dates:
                    confirmed_sum = all_confirmed[i].sum()
                    death_sum = all_deaths[i].sum()
                    recovered_sum = all_recoveries[i].sum()
                    world_cases.append(confirmed_sum)
                    total_deaths.append(death_sum)
                    mortality_rate.append(death_sum/confirmed_sum) # calculate death per confirmed
                    total_recovered.append(recovered_sum)
            
            return {
                "world_cases": world_cases,
                "total_deaths": total_deaths,
                "mortality_rate": mortality_rate,
                "total_recovered": total_recovered
            }
        except IndexError:
            raise ValueError("Max day is : " + str(len(dates)))


    @staticmethod
    def predict(question):
        question_embeddings = module.signatures['question_encoder'](tf.constant([question]))
        res = np.inner(question_embeddings['outputs'], response_embeddings['outputs'])
        answer = response[np.argmax(res[0])]
        confidence = res[0][np.argmax(res[0])]
        return answer, confidence
