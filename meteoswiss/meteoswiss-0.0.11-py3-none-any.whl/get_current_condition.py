import pandas as pd

def get_current_condition(station):
    data = pd.read_csv("https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv",sep=';',header=1)
    stationData = data.loc[data['stn'].str.contains('GVE')]
    stationData = stationData.to_dict('records')
    return stationData