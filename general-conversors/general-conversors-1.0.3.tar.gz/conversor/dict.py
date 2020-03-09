"""
Dictionary Conversors
"""

import json

class ToMultiLevel:
  """
  Conversor
  Convert a 1-Level dict to N-level dict

  Since : 2020-03-08

  Notes
  -----
  Covnert method = convert()

  Attributes
  ----------
  _result : dict : private
    Final result after conversion
  _source : dict : private
    Source or original dict to convert

  Methods
  -------
  _scan_down(key=str, value=any)      : private
    Iterate values and append in result
  set_source(source=dict)             : public
    Set new source and reset result
  convert()                           : public
    Convert method
  """

  _result = {}
  _source = {}

  def __init__(self, source):
    """
    Constructor

    Parameters
    ----------
    source : dict
      Original dict to convert
    """

    self._source = source

  def _scan_down(self, key, value, element):
    """
    Convert to dictionary

    Parameters
    ----------
    key     : str
      Key to scan
    value   : any
      Value to scan

    Return
    ------
    element : dict
      Final dictionary
    """

    if '.' in key:
      key = key.split('.')

      key_list = []

      for index, key_down in enumerate(key):
        if index == 0:
          continue

        key_list.append(key_down)

      key = key[0]

      if key not in element:
        element[key] = {}

      element[key] = self._scan_down('.'.join(key_list), value, element[key])
    else:
      element[key] = value

    return element

  def set_source(self, source):
    """
    Set a new source

    Parameters
    ----------
    source : dict
      New source
    """

    self._source = source
    self._result = {}

  def convert(self):
    """
    Conversor

    Return
    ------
    _result : dict
      Converted dictionary
    """

    self._result = {}

    for key, value in self._source.items():
      self._scan_down(key, value, self._result)

    return self._result

class ToOneLevel:
  """
  Conversor
  Convert a N-level dict to 1-Level dict

  Since : 2020-03-08

  Notes
  -----
  Covnert method = convert()

  Attributes
  ----------
  _result             : dict : private
    Final result after conversion
  _source             : dict : private
    Source or original dict to convert
  _replace_underscore : bool : private
    Underscore replacing mode (Default = False)

  Methods
  -------
  _validate_is_array_dict(value=any)    : private
    Validate if is an array or dict
  _validate_replace_underscore(key=str) : private
    Validate and replace (if is enabled) any underscore (_) to dot (.)
  _scan_down(key=str, value=any)        : private
    Iterate values and append in result
  set_source(source=dict)               : public
    Set new source and reset result
  to_json()                             : public
    Converts convert() return to JSON object
  convert()                             : public
    Convert method
  """

  _result = {}
  _source = {}
  _replace_underscore = False

  def __init__(self, source, replace_underscore=False):
    """
    Constructor

    Parameters
    ----------
    source              : dict
      Original dict to convert
    replace_underscore  : bool
      Set True if you want to replace any underscore (_) to dot (.)
    """

    self._source = source
    self._replace_underscore = replace_underscore

  def _validate_is_array_dict(self, value):
    """
    Validate if is an array or a dict

    Parameters
    ----------
    value : any
      Value to compare

    Return
    ------
    bool
      If true when is a dict or list
    """

    return isinstance(value, (dict, list,))

  def _validate_replace_underscore(self, key):
    """
    Validate and replace (if is enabled) underscore (_) to dot (.)

    Parameters
    ----------
    key : str
      Key to validate and replace

    Return
    ------
    key : str
      Key validated
    """

    if '_' in key and self._replace_underscore:
      return key.replace('_', '.')

    return key

  def _scan_down(self, key, value):
    """
    Down scanner

    Parameters
    ----------
    key   : str
      Key to scan
    value : any
      Value to scan
    """

    key = self._validate_replace_underscore(key)

    iteration = None
    if isinstance(value, list):
      iteration = enumerate(value)
    else:
      iteration = value.items()

    for i, v in iteration:
      i = self._validate_replace_underscore(i)

      if self._validate_is_array_dict(v):
        self._scan_down(f'{key}.{i}', v)
      else:
        self._result[f'{key}.{i}'] = v

  def set_source(self, source):
    """
    Set a new source

    Parameters
    ----------
    source : dict
      New source
    """

    self._source = source
    self._result = {}

  def to_json(self):
    """
    Final result as JSON object

    Return
    ------
    result : json
      JSON-converted dict
    """

    return json.dumps(self.convert())

  def convert(self):
    """
    Conversor

    Return
    ------
    _result : dict
      Converted dictionary
    """

    for key, value in self._source.items():
      if self._validate_is_array_dict(value):
        self._scan_down(key, value)
      else:
        self._result[key] = value

    return self._result
