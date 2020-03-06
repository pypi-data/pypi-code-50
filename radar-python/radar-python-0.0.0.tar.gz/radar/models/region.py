from .model import Model


class Region(Model):
    OBJECT_NAME = "Region"
    _DISPLAY_ATTRIBUTES = (
        "type",
        "name",
        "code",
    )


class Regions(Model):
    OBJECT_NAME = "Regions"
    _DISPLAY_ATTRIBUTES = (
        "country",
        "state",
    )
