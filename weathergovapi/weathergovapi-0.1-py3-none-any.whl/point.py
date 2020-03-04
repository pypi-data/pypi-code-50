from .baseobject import BaseObject
import weathergovapi

class Point(BaseObject):
  PROP_KEYS = [
    'cwa',
    {'key': 'gridX', 'type': int},
    {'key': 'gridY', 'type': int},
    'relativeLocation.properties.city',
    'relativeLocation.properties.state',
    'forecastOffice',
    {'key': 'forecast', 'name': 'forecastUrl'}, 
    {'key': 'forecastHourly', 'name': 'forecastHourlyUrl'},
    'forecastGridData',
    'observationStations',
    'forecastZone',
    'county',
    'fireWeatherZone',
    'timeZone',
    'radarStation'
  ]

  def __init__(self, lat, lng):
    super().__init__()

    self.lat = lat
    self.lng = lng

    self._load_data()

  def forecast(self):
    return weathergovapi.WeatherGovApi.getForecast(self.forecastUrl)

  def hourly(self):
    return weathergovapi.WeatherGovApi.getForecast(self.forecastHourlyUrl)
  
  def _url(self):
    return "/points/%s,%s" % (self.lat, self.lng)
