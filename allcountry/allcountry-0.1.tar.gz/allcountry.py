
# -*- encoding: utf-8 *-*

from os import path
from json import load


class Country:

    def __init__(self,country_name= "Turkey"):
        self.country_name = country_name

        data_file_path = path.dirname(__file__)+ "/data/data.json"
        with open(data_file_path, encoding='utf-8') as file:
            json_file = load(file)

        self.country_information = [country for country in json_file if country["name"] == self.country_name ][0]

    def get_phone_code(self):
        return self.country_information["phone_code"]

    def get_capital(self):
        return self.country_information["capital"]

    def get_currency(self):
        return self.country_information["currency"]

    def get_city(self, city_name = None):
        if city_name:
            return [state for state in self.country_information["states"] if state == city_name]
        return [state for state in self.country_information["states"].keys()]

    def get_town(self,city_name = None):
        if city_name:
            return self.country_information["states"][city_name]
