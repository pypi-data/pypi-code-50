from .model import Model


class Place(Model):
    OBJECT_NAME = "Place"
    _DISPLAY_ATTRIBUTES = (
        "_id",
        "name",
    )
