from .model import Model
from radar.models.geofence import Geofence
from radar.models.region import Region
from radar.models.place import Place


class RadarContext(Model):
    OBJECT_NAME = "Context"
    _DISPLAY_ATTRIBUTES = (
        "live",
        "geofences",
        "place",
        "country",
        "state",
        "dma",
    )

    def __init__(self, radar, data={}):
        """Initialize a Radar Model instance

        Args:
            radar (RadarClient): RadarClient for instance CRUD actions
            raw_json (dict): raw data to initialize the model with
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
            elif attribute in ["country", "state", "dma", "postalCode"]:
                region = Region(radar, data[attribute])
                setattr(self, attribute, region)
            else:
                setattr(self, attribute, value)
