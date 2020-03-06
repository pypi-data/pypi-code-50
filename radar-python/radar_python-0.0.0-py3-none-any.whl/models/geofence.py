from .model import Model


class Geofence(Model):
    OBJECT_NAME = "geofence"
    _DISPLAY_ATTRIBUTES = (
        "_id",
        "externalId",
        "tag",
        "description",
    )

    def delete(self):
        return self._radar.geofences.delete(id=self._id)
