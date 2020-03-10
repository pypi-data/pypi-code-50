from .dataset import Dataset
from .project import Project
from .project_dataset_schema import ProjectDatasetSchema


class ProjectDataset():
    '''

    '''

    def __init__(self, client, projectDatasetType=None, createdAt=None, dataset=[], project=[], projectDatasetSchema=[]):
        self.client = client
        self.id = projectDatasetType
        self.project_dataset_type = projectDatasetType
        self.created_at = createdAt
        self.dataset = Dataset(client, **dataset) if dataset else None
        self.project = Project(client, **project) if project else None
        self.project_dataset_schema = ProjectDatasetSchema(
            client, **projectDatasetSchema) if projectDatasetSchema else None

    def __repr__(self):
        return f"ProjectDataset(project_dataset_type={repr(self.project_dataset_type)}, created_at={repr(self.created_at)}, dataset={repr(self.dataset)}, project={repr(self.project)}, project_dataset_schema={repr(self.project_dataset_schema)})"

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.id == other.id

    def to_dict(self):
        return {'project_dataset_type': self.project_dataset_type, 'created_at': self.created_at, 'dataset': self.dataset.to_dict() if self.dataset else None, 'project': self.project.to_dict() if self.project else None, 'project_dataset_schema': self.project_dataset_schema.to_dict() if self.project_dataset_schema else None}
