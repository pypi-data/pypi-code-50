

class Metadata():
    '''

    '''

    def __init__(self, client, delimiter=None, rowCount=None):
        self.client = client
        self.id = delimiter
        self.delimiter = delimiter
        self.row_count = rowCount

    def __repr__(self):
        return f"Metadata(delimiter={repr(self.delimiter)}, row_count={repr(self.row_count)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'delimiter': self.delimiter, 'row_count': self.row_count}
