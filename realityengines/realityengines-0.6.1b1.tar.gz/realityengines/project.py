from .dataset import Dataset


class Project():
    '''

    '''

    def __init__(self, client, projectId=None, name=None, useCase=None, createdAt=None, datasets=[]):
        self.client = client
        self.id = projectId
        self.project_id = projectId
        self.name = name
        self.use_case = useCase
        self.created_at = createdAt
        self.datasets = [Dataset(client, **args) for args in datasets if args]

    def __repr__(self):
        return f"Project(project_id={repr(self.project_id)}, name={repr(self.name)}, use_case={repr(self.use_case)}, created_at={repr(self.created_at)}, datasets={repr(self.datasets)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'project_id': self.project_id, 'name': self.name, 'use_case': self.use_case, 'created_at': self.created_at, 'datasets': [val.to_dict() for val in self.datasets if val is not None] if self.datasets else []}

    def add_dataset_column_type_override(self, dataset_id, column, column_type):
        return self.client.add_project_dataset_column_type_override(self.project_id, dataset_id, column, column_type)

    def delete(self):
        return self.client.delete_project(self.project_id)

    def refresh(self):
        self = self.describe()
        return self

    def describe(self):
        return self.client.describe_project(self.project_id)

    def get_dataset_schema(self, dataset_id):
        return self.client.get_project_dataset_schema(self.project_id, dataset_id)

    def list_datasets(self):
        return self.client.list_project_datasets(self.project_id)

    def list_dataset_latest_instances(self):
        return self.client.list_project_dataset_latest_instances(self.project_id)

    def remove_dataset_column_type_override(self, dataset_id, column):
        return self.client.remove_project_dataset_column_type_override(self.project_id, dataset_id, column)

    def set_dataset_column_types(self, dataset_id, column_overrides):
        return self.client.set_project_dataset_column_types(self.project_id, dataset_id, column_overrides)

    def update(self, name):
        return self.client.update_project(self.project_id, name)

    def validate_datasets(self):
        return self.client.validate_project_datasets(self.project_id)

    def create_deployment_token(self):
        return self.client.create_deployment_token(self.project_id)

    def list_deployments(self):
        return self.client.list_deployments(self.project_id)

    def list_deployment_tokens(self):
        return self.client.list_deployment_tokens(self.project_id)

    def train_model(self, training_config=None):
        return self.client.train_model(self.project_id, training_config)

    def get_training_config_options(self):
        return self.client.get_training_config_options(self.project_id)

    def list_models(self):
        return self.client.list_models(self.project_id)

    def attach_dataset(self, dataset_id, project_dataset_type):
        return self.client.attach_dataset_to_project(dataset_id, self.project_id, project_dataset_type)

    def remove_dataset(self, dataset_id):
        return self.client.remove_dataset_from_project(dataset_id, self.project_id)
