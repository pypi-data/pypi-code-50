import json
import requests

from .baseobject import BaseObject, PreloadedObject
from .alert import Alert
from .point import Point
from .forecast import Forecast
from .period import Period

class WeatherGovApi:
  ENDPOINT = 'https://api.weather.gov'

  @classmethod
  def getPoint(cls, lat, lng):
    return Point(lat, lng)

  @classmethod
  def getForecast(cls, url):
    return Forecast(url)

  @classmethod
  def getPeriod(cls, data):
    return Period(data)

  @classmethod
  def getAlerts(cls, zone):
    path = "/alerts/active/zone/%s" % zone
    data = cls.get(path)
    alerts = []
    for feature in data['features']:
      alerts.append( Alert(feature) )
    return alerts

  @classmethod
  def get(cls, path):
    if path[:4] == 'http':
      url = path
    else:
      url = "%s%s" % (cls.ENDPOINT, path)
      
    resp = requests.get(url)
    data = resp.json()

    if not resp.ok:
      raise ApiException("Error %i: %s" % (data['status'], data['detail']))

    return data

class ApiException(Exception):
  pass