class Marker:
    """Map marker model"""
    def __init__(self):
        self.lat = None
        self.long = None
        self.label = None

    @classmethod
    def from_json(cls, marker_json):
        marker = cls()
        marker.lat = marker_json.get('lat')
        marker.long = marker_json.get('long')
        marker.label = marker_json.get('label')
        return marker

    def __repr__(self):
        return '<Marker> {0}'.format(self.label)
