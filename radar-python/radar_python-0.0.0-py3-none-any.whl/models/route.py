from .model import Model


class RouteDistance:
    def __init__(self, value, text):
        self.value = value
        self.text = text

    def __repr__(self):
        return f"<text={self.text} value={self.value}>"

    def to_feet(self):
        pass


class RouteDuration:
    def __init__(self, value, text):
        self.value = value
        self.text = text

    def __repr__(self):
        return f"<text={self.text} value={self.value}>"

    def to_sec(self):
        pass


class Route:
    def __init__(self, distance=None, duration=None, mode=None):
        self.mode = mode

        if distance:
            self.distance = RouteDuration(
                value=distance.get("value"), text=distance.get("text")
            )
        else:
            self.distance = None

        if duration:
            self.duration = RouteDuration(
                value=duration.get("value"), text=duration.get("text")
            )
        else:
            self.duration = None

    def __repr__(self):
        display_str = f"<distance={self.distance.text}"
        if self.duration:
            display_str += f" duration={self.duration.text}>"
        else:
            display_str += ">"
        return display_str


class Routes(Model):
    OBJECT_NAME = "Routes"
    _DISPLAY_ATTRIBUTES = (
        "geodesic",
        "transit",
        "car",
        "bike",
        "foot",
    )

    def __init__(self, radar, data={}):
        """Initialize a Radar Routes instance

        Args:
            radar (RadarClient): RadarClient for instance CRUD actions
            data (dict): raw data to initialize the model with
        """
        self._radar = radar
        self.raw_json = data
        for attribute, value in data.items():
            if attribute in ["transit", "car", "bike", "foot"]:
                route = Route(
                    distance=value.get("distance"),
                    duration=value.get("duration"),
                    mode=attribute,
                )
                setattr(self, attribute, route)
            elif attribute in ["geodesic"]:
                route = Route(distance=value, mode=attribute)
                setattr(self, attribute, route)
            else:
                setattr(self, attribute, value)
