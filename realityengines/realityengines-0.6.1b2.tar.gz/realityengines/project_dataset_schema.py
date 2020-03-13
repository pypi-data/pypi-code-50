from .metadata import Metadata
from .schema import Schema
from .schema_validation import SchemaValidation


class ProjectDatasetSchema():
    '''

    '''

    def __init__(self, client, schemaValidation=[], schema=[], metadata=[]):
        self.client = client
        self.id = None
        self.schema_validation = client._build_class(
            SchemaValidation, schemaValidation)
        self.schema = client._build_class(Schema, schema)
        self.metadata = client._build_class(Metadata, metadata)

    def __repr__(self):
        return f"ProjectDatasetSchema(schema_validation={repr(self.schema_validation)}, schema={repr(self.schema)}, metadata={repr(self.metadata)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'schema_validation': self.schema_validation.to_dict() if self.schema_validation else None, 'schema': self.schema.to_dict() if self.schema else None, 'metadata': self.metadata.to_dict() if self.metadata else None}
