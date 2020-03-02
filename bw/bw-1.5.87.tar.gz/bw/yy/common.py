# coding=utf-8
from __future__ import unicode_literals

from typing import Text, Dict


# nipasbc
class Property(object):
    key = ...  # type: Text
    val = ...  # type: Text
    name = ...  # type: Text
    index = ...  # type: int
    visible = ...  # type: bool

    def __init__(self,
                 key: Text = None,
                 val: Text = None,
                 name: Text = None,
                 index: int = None,
                 visible: bool = None
                 ): ...


# nipasbc
class Filter(object):
    fields = ...  # type: Text
    filter = ...  # type: Text
    sort = ...  # type: Text
    limit = ...  # type: int
    page = ...  # type: int
    pagesize = ...  # type: int
    fromdate = ...  # type: Text
    todate = ...  # type: Text

    def __init__(self, fields: Text = None, filter: Text = None, sort: Text = None, limit: int = None, page: int = None,
                 pagesize: int = None, fromdate: Text = None, todate: Text = None): ...


# nipasbc
class Error(object):
    code = ...  # type: int
    type = ...  # type: Text
    info = ...  # type: Text

    def __init__(self, code: int = None, type: Text = None, info: Text = None): ...


# nipasbc
class ConnectionAddress(object):
    title = ...  # type: Text
    address = ...  # type: Dict[Text, Text]

    def __init__(self, title: Text = None, address: Dict[Text, Text] = None): ...


# nipasbc
class ConnectionStatus(object):
    State_UNKNOWN = 0  # 未知
    State_CONNECTING = 1  # 连接中
    State_CONNECTED = 2  # 已连接
    State_LOGGEDIN = 3  # 已登录
    State_DISCONNECTING = 4  # 断开中
    State_DISCONNECTED = 5  # 已断开
    State_ERROR = 6  # 错误

    state = ...  # type: int
    error = ...  # type: Error

    def __init__(self, state: int = None, error: Error = None): ...


# nipasbc
class Log(object):
    source = ...  # type: Text
    level = ...  # type: Text
    msg = ...  # type: Text
    owner_id = ...  # type: Text
    created_at = ...  # type: int

    # def __init__(self, source: Text = None, level: Text = None, msg: Text = None, owner_id: Text = None,
    #              created_at: int = None): ...


# nipasbc
class Logs(object):
    data = ...  # type: List[Log]

    # def __init__(self, data: List[Log] = None): ...


# nipasbc
class Heartbeat(object):
    created_at = ...  # type: int

    # def __init__(self, created_at: int = None): ...



class EnumTypeWrapper(object):
  """A utility for finding the names of enum values."""

  DESCRIPTOR = None

  def __init__(self, enum_type):
    """Inits EnumTypeWrapper with an EnumDescriptor."""
    self._enum_type = enum_type
    self.DESCRIPTOR = enum_type

  def Name(self, number):
    """Returns a string containing the name of an enum value."""
    if number in self._enum_type.values_by_number:
      return self._enum_type.values_by_number[number].name
    raise ValueError('Enum %s has no name defined for value %d' % (
        self._enum_type.name, number))

  def Value(self, name):
    """Returns the value corresponding to the given enum name."""
    if name in self._enum_type.values_by_name:
      return self._enum_type.values_by_name[name].number
    raise ValueError('Enum %s has no value defined for name %s' % (
        self._enum_type.name, name))

  def keys(self):
    """Return a list of the string names in the enum.
    These are returned in the order they were defined in the .proto file.
    """

    return [value_descriptor.name
            for value_descriptor in self._enum_type.values]

  def values(self):
    """Return a list of the integer values in the enum.
    These are returned in the order they were defined in the .proto file.
    """

    return [value_descriptor.number
            for value_descriptor in self._enum_type.values]

  def items(self):
    """Return a list of the (name, value) pairs of the enum.
    These are returned in the order they were defined in the .proto file.
    """
    return [(value_descriptor.name, value_descriptor.number)
            for value_descriptor in self._enum_type.values]

  def __getattr__(self, name):
    """Returns the value corresponding to the given enum name."""
    if name in self._enum_type.values_by_name:
      return self._enum_type.values_by_name[name].number
    raise AttributeError