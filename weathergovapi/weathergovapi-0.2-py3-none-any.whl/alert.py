from .baseobject import PreloadedObject

class Alert(PreloadedObject):
  PROP_KEYS = [
    "id",
    "type",
    "properties.areaDesc",
    {"key": "properties.sent", "type": "date"},
    {"key": "properties.effective", "type": "date"},
    {"key": "properties.onset", "type": "date"},
    {"key": "properties.expires", "type": "date"},
    {"key": "properties.ends", "type": "date"},
    "properties.status",
    "properties.messageType",
    "properties.category",
    "properties.severity",
    "properties.certainty",
    "properties.urgency",
    "properties.event",
    "properties.sender",
    "properties.senderName",
    "properties.headline",
    "properties.description",
    "properties.instruction",
    "properties.response"
  ]
