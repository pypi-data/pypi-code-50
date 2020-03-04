from .baseobject import BaseObject

class Period(BaseObject):
  PROP_KEYS = [
    'number',
    'name',
    'startTime',
    'endTime',
    'isDayTime',
    'temperature',
    'temperatureUnit',
    'temperatureTrend',
    'windSpeed',
    'windDirection',
    'shortForecast',
    'detailedForecast',
    'icon'
  ]

  def __init__(self, data):
    super().__init__()

    self._data = data
    self._load_data()
    
  def _load_data(self):
    self._get_properties()
  