from .model import Model


class Event(Model):
    OBJECT_NAME = "Event"
    _DISPLAY_ATTRIBUTES = ("_id", "type", "createdAt")

    def verify(self, verification=None, value=None, verifiedPlaceId=None):
        return self._radar.events.verify(
            id=self._id,
            verification=verification,
            value=value,
            verifiedPlaceId=verifiedPlaceId,
        )

    def delete(self):
        return self._radar.events.delete(id=self._id)
