import json
from typing import List, TypeVar, Type

import jsonpickle
from multipledispatch import dispatch

from fxq.commons._reflection_utils import _deserialize_json_object_to, _deserialize_json_list_to

T = TypeVar('T')


class DictMarshal:

    @dispatch(list)
    def to_dict(self, lst: list) -> List[dict]:
        """
        Serializes the given list of objects into a list of dicts
        :param lst: List of Objects to be serialized
        :return: List of dicts representing the objects
        """
        return [self.to_dict(i) for i in lst]

    @dispatch(object)
    def to_dict(self, obj: object) -> dict:
        """
        Serializes the given object into a dict
        :param obj: Object to be serialized
        :return: Dictionary representing the object
        """
        return json.loads(jsonpickle.encode(obj, unpicklable=False))

    @dispatch(dict, object)
    def from_dict(self, dict_: dict, class_: Type[T]) -> T:
        """
        Deserializes the dictionary into an object of the specified class

        Classes with complex field types must include a class level dictionary defining types
        i.e.
        ```python
        class Employee:
            types = {"emergencyContacts": List[EmergencyContact]}

            def __init__(self):
                self.id: int = None
                self.name: str = None
                self.hireDate: str = None
                self.current: bool = None
                self.emergencyContacts: List[EmergencyContact] = None
        ```

        :param dict_: Dictionary to be deserialized
        :param class_: Class to deserialize dictionary to
        :return: Returns an instance of class_
        """
        return _deserialize_json_object_to(dict_, class_)

    @dispatch(list, object)
    def from_dict(self, dict_list: List[dict], class_: Type[T]) -> List[T]:
        """
        Deserializes the dictionary list into an object list of the specified class

        Classes with complex field types must include a class level dictionary defining types
        i.e.
        ```python
        class Employee:
            types = {"emergencyContacts": List[EmergencyContact]}

            def __init__(self):
                self.id: int = None
                self.name: str = None
                self.hireDate: str = None
                self.current: bool = None
                self.emergencyContacts: List[EmergencyContact] = None
        ```

        :param dict_list: Dictionary to be deserialized
        :param class_: Class to deserialize dictionary to
        :return: Returns an list populated with instances of class_
        """
        return _deserialize_json_list_to(dict_list, class_)
