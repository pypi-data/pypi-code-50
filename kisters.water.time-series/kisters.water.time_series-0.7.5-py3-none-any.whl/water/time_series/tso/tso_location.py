import json
from datetime import datetime
from typing import Mapping, Optional

import dateutil

from kisters.water.time_series.core.entity import Entity


class TSOLocation(Entity):
    """
        This is the specific Location entity class for TSO.
    """

    def __init__(self, data: Mapping):
        super().__init__(data)

    @property
    def id(self):
        return self.get("id")

    @property
    def creation_time(self) -> Optional[datetime]:
        if self.get("creationTime") is None:
            return None
        try:
            return datetime.fromtimestamp(self.__data["creationTime"])
        except (OverflowError, OSError, TypeError):
            return dateutil.parser.parse(self.__data['creationTime'])

    @property
    def creator(self):
        return self.get("creator")

    @property
    def edit_time(self) -> Optional[datetime]:
        if self.get("editTime") is None:
            return None
        try:
            return datetime.fromtimestamp(self.__data["editTime"])
        except (OverflowError, OSError, TypeError):
            return dateutil.parser.parse(self.__data['editTime'])

    @property
    def editor(self):
        return self.get("editor")

    @property
    def latitude(self):
        return self.get("latitude")

    @property
    def longitude(self):
        return self.get("longitude")

    @property
    def geometry_type(self):
        return self.get("geometryType")

    @property
    def wkt(self):
        return self.get("wkt")

    @property
    def name(self):
        return self.get("name")

    @property
    def area(self):
        return self.get("area")

    @property
    def name2(self):
        return self.get("name2")

    @property
    def icon_reference(self):
        return self.get("iconReference")

    @property
    def type(self):
        return self.get("type")

    @property
    def key(self):
        return self.get("key")

    def to_dict(self):
        return {
            "id": self.id,
            "creationTime": self.creation_time,
            "creator": self.creator,
            "editTime": self.edit_time,
            "editor": self.editor,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "geometryType": self.geometry_type,
            "wkt": self.wkt,
            "name": self.name,
            "area": self.area,
            "name2": self.name2,
            "iconReference": self.icon_reference,
            "type": self.type,
            "key": self.key
        }

    def to_json(self):
        def cleandict(d):
            if not isinstance(d, dict):
                return d
            return {k: cleandict(v) for k, v in d.items() if v is not None}

        return json.dumps(cleandict(self.to_dict()))
