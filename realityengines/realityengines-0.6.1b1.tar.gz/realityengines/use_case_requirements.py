

class UseCaseRequirements():
    '''

    '''

    def __init__(self, client, projectDatasetType=None, name=None, description=None, required=None, columnTypeOptions=None):
        self.client = client
        self.id = projectDatasetType
        self.project_dataset_type = projectDatasetType
        self.name = name
        self.description = description
        self.required = required
        self.column_type_options = columnTypeOptions

    def __repr__(self):
        return f"UseCaseRequirements(project_dataset_type={repr(self.project_dataset_type)}, name={repr(self.name)}, description={repr(self.description)}, required={repr(self.required)}, column_type_options={repr(self.column_type_options)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'project_dataset_type': self.project_dataset_type, 'name': self.name, 'description': self.description, 'required': self.required, 'column_type_options': self.column_type_options}
