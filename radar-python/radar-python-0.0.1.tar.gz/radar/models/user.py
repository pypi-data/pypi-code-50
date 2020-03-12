from .model import Model
from radar.models.geofence import Geofence
from radar.models.place import Place


class User(Model):
    OBJECT_NAME = "User"
    _DISPLAY_ATTRIBUTES = ("userId", "_id", "deviceId")

    def __init__(self, radar, data={}):
        """Initialize a Radar Model instance

        Args:
            radar (RadarClient): RadarClient for instance CRUD actions
            data (dict): raw data to initialize the model with
        """
        self._radar = radar
        self.raw_json = data
        for attribute, value in data.items():
            if attribute == "geofences":
                geofences = [Geofence(radar, geofence) for geofence in data[attribute]]
                setattr(self, attribute, geofences)
            elif attribute == "place":
                place = Place(radar, data[attribute])
                setattr(self, attribute, place)
            else:
                setattr(self, attribute, value)

    def delete(self):
        return self._radar.users.delete(id=self._id)
