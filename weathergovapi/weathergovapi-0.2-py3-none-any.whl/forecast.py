from .baseobject import BaseObject
import weathergovapi

class Forecast(BaseObject):
  PROP_KEYS = [
    'updated',
    'units',
    'forecastGenerator',
    'generatedAt',
    'updateTime',
    'validTimes',
  ]

  def __init__(self, url):
    super().__init__()

    self.periods = []
    self._the_url = url

    self._load_data()
    self._process_periods()
  
  def _url(self):
    return self._the_url

  def _process_periods(self):
    for each in self._data['periods']:
      self.periods.append(weathergovapi.WeatherGovApi.getPeriod(each))
