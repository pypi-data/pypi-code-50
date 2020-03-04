import requests
import weathergovapi

class BaseObject:
  PROP_KEYS = []

  def __init__(self):
    self._data = {}
    self._properties = {}

  def _load_data(self):
    data = weathergovapi.WeatherGovApi.get(self._url())
    self._data = data['properties']
    self._get_properties()

  def _get_properties(self):
    self._properties = {}
    for property in self.PROP_KEYS:
      if type(property) is str:
        property = {'key': property}
      
      if 'name' not in property:
        property['name'] = property['key'].split('.').pop()

      if 'type' not in property:
        property['type'] = 'string'
      
      self._processProp(property, self._data)
    
  def _url(self):
    pass

  def _processProp(self, property, data):
    parts = property['key'].split('.')
    d = data
    for prop in parts:
      if prop in d:
        d = d[prop]
      else:
        d = None
        break
    self._properties[property['name']] = d

  def __getattr__(self, attr):
    if attr in self._properties:
      return self._properties[attr]
    else:
      raise AttributeError("'%s' object has no attribute '%s'" % (self.__class__.__name__, attr))