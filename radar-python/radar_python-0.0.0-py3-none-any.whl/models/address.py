from .model import Model


class Address(Model):
    OBJECT_NAME = "Address"
    _DISPLAY_ATTRIBUTES = (
        "latitude",
        "longitude",
        "formattedAddress",
    )
