from .baseobject import PreloadedObject

class Period(PreloadedObject):
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
