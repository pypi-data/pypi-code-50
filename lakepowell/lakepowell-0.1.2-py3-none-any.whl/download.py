import os
import requests
import getpass
import bs4
import csv
from bs4 import BeautifulSoup

def download_fish_file():
    # download_to_path="lakepowell/data/fish_data"
    path_here = os.path.abspath(os.path.dirname(__file__)) #points to parent directory
    dataset_dir = f"fish_data"
    dataset_path = os.path.join(path_here, dataset_dir)
    download_to_path = dataset_path

    url = "https://byu.box.com/shared/static/b9j0opllkxhvelg0ps365ww0xxcihydp.xlsx"
    #                 https://byu.box.com/s/b9j0opllkxhvelg0ps365ww0xxcihydp


    response = requests.get(url, allow_redirects=True)

    with open(download_to_path, 'wb') as dest:
        dest.write(response.content)

    return download_to_path

def download_water_data():
    path_here = os.path.abspath(os.path.dirname(__file__)) #points to parent directory
    dataset_dir = f"water_data"
    dataset_path = os.path.join(path_here, dataset_dir)
    download_to_path = dataset_path


    url = "https://byu.box.com/shared/static/89xn9en4a57twdh4znvaeclk17fx5dmd"
                      #https://byu.box.com/s/89xn9en4a57twdh4znvaeclk17fx5dmd

    response = requests.get(url, allow_redirects=True)

    with open(download_to_path, 'wb') as dest:
        dest.write(response.content)

    return download_to_path

def get_fishdata_path():
    path_here = os.path.abspath(os.path.dirname(__file__)) #points to parent directory
    dataset_dir = f"fish_data"
    dataset_path = os.path.join(path_here, dataset_dir)
    return dataset_path

def get_waterdata_path():
    path_here = os.path.abspath(os.path.dirname(__file__)) #points to parent directory
    dataset_dir = f"water_data"
    dataset_path = os.path.join(path_here, dataset_dir)
    return dataset_path
