

class Schema():
    '''

    '''

    def __init__(self, client, name=None, columnType=None, detectedColumnType=None):
        self.client = client
        self.id = name
        self.name = name
        self.column_type = columnType
        self.detected_column_type = detectedColumnType

    def __repr__(self):
        return f"Schema(name={repr(self.name)}, column_type={repr(self.column_type)}, detected_column_type={repr(self.detected_column_type)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'name': self.name, 'column_type': self.column_type, 'detected_column_type': self.detected_column_type}
