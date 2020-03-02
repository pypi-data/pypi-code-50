import datetime


class Event:
    """Timeline event model"""
    def __init__(self):
        self.date = None
        self.total = None

    @classmethod
    def from_json(cls, event_json):
        event = cls()
        event.total = event_json.get('total')
        event.date = datetime.datetime.strptime(event_json.get('date'), '%Y-%m-%d')
        return event

    def __repr__(self):
        return '<Event {0}> {1}'.format(self.date.strftime('%Y-%m-%d'), self.total)
