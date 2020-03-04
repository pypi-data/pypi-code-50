# This file was used to pull all the water data from http://lakepowell.water-data.com/
# which was upladed to box. Don't use this to redownload all the data because it
# has to make a bunch of post requests from the website

import requests
from datetime import date
import pandas as pd
from bs4 import BeautifulSoup

def pull_data(request_data):
    r = requests.post("http://lakepowell.water-data.com/index2.php", request_data)

    soup = BeautifulSoup(r.text, features="lxml")
    found_items = soup(text="Water Data for Selected Dates") #look for the title of the table
    parent = list(found_items)[0].parent #go to object containing the title (and table)
    table = parent.findNext('table') #find the next table in the page
    rows = table.findAll("tr") #find all table rows

    header = rows[0]
    data = rows[1:-1]#all_but first and last row (first is header, last is website computed means)

    text_headers = []
    for column in header.findAll("th"):
        text_headers.append(column.text)

    text_data = []
    for row in data:
        text_row = []
        for column in row.findAll("td"):
            text_row.append(column.text)
        text_data.append(text_row)

    return text_headers,  text_data

def full_download():
    request_data = {}
    headers = []
    all_data = [[None, None, None, None, None, None, None, None]]

    request_data["Get10DateData"] = "Get+Data"
    calendar = {"January" : list(range(1, 31+1)) , "February" : list(range(1, 29+1)),
                "March" : list(range(1, 31+1)), "April" : list(range(1, 30+1)),
                "May" : list(range(1, 31+1)), "June" : list(range(1, 30+1)),
                "July": list(range(1, 31+1)), "August" : list(range(1, 31+1)),
                "September" : list(range(1, 30+1)), "October" : list(range(1, 31+1)),
                "November" : list(range(1, 30+1)), "December": list(range(1, 31+1))}

    req_num = 0
    cur_year = date.today().year
    start_year = 1963
    for year in range(start_year, int(cur_year) + 1):
    # for year in range(1964, 1965):
        print(year)
        for month in calendar:
            days = calendar[month]

            for i in days:
                req_num = req_num + 1
                request_data["datemonth" + str(req_num)] = month
                request_data["dateday" + str(req_num)] = str(i)
                request_data["dateyear" + str(req_num)] = year

                if req_num == 10:
                    req_num = 0
                    headers, data = pull_data(request_data)
                    all_data.extend(data)
                    request_data.clear()
                    request_data["Get10DateData"] = "Get+Data"

    df = pd.DataFrame.from_records(all_data, columns=headers)

    df.to_csv("lake_powell_conditions.csv")

def update_water_data(water_data_path =  "data/water_data"):
    water_df = pd.read_csv(water_data_path)
    request_data = {}
    headers = []
    all_data = []

    request_data["Get10DateData"] = "Get+Data"
    calendar = {"January" : list(range(1, 31+1)) , "February" : list(range(1, 29+1)),
                "March" : list(range(1, 31+1)), "April" : list(range(1, 30+1)),
                "May" : list(range(1, 31+1)), "June" : list(range(1, 30+1)),
                "July": list(range(1, 31+1)), "August" : list(range(1, 31+1)),
                "September" : list(range(1, 30+1)), "October" : list(range(1, 31+1)),
                "November" : list(range(1, 30+1)), "December": list(range(1, 31+1))}

    req_num = 0
    cur_year = date.today().year
    last_row = water_df.iloc[[-1]]
    start_year = last_row.Year
    start_month = calendar[last_row.Month - 1]
    start_day = last_row.iloc[[-1]].Day

    for year in range(start_year, int(cur_year) + 1):
        print(year)

        for month in calendar:
            if year == start_year and month <= start_month:
                continue

            days = calendar[month]

            for i in days:
                request_data["datemonth" + str(req_num)] = month
                request_data["dateday" + str(req_num)] = str(i)
                request_data["dateyear" + str(req_num)] = year
                req_num = req_num + 1

                if req_num == 9:
                    req_num = 0
                    headers, data = pull_data(request_data)
                    all_data.extend(data)
                    request_data.clear()
                    request_data["Get10DateData"] = "Get+Data"

    df = pd.DataFrame.from_records(all_data, columns=headers)

    df.to_csv("lake_powell_conditions.csv")
