from .schema_validation import SchemaValidation
from .schema import Schema
from .metadata import Metadata


class ProjectDatasetSchema():
    '''

    '''

    def __init__(self, client, schemaValidation=[], schema=[], metadata=[]):
        self.client = client
        self.id = None
        self.schema_validation = SchemaValidation(
            client, **schemaValidation) if schemaValidation else None
        self.schema = Schema(client, **schema) if schema else None
        self.metadata = Metadata(client, **metadata) if metadata else None

    def __repr__(self):
        return f"ProjectDatasetSchema(schema_validation={repr(self.schema_validation)}, schema={repr(self.schema)}, metadata={repr(self.metadata)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'schema_validation': self.schema_validation.to_dict() if self.schema_validation else None, 'schema': self.schema.to_dict() if self.schema else None, 'metadata': self.metadata.to_dict() if self.metadata else None}
