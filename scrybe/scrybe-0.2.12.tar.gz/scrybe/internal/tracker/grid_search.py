from typing import Dict


class GridModelTrainedInfo(object):
    """
    In case of GridSearch with CV, we need to keep a track of model info which have been trained on a
        particular split of the data. In such cases, the only repeated entity is the dataset holding
        the split indexes. So we keep a list a CVModelInfo around here to allow lookups
    """
    def __init__(self, architecture: Dict, params: Dict):
        self.architecture = architecture
        self.params = params

    def __eq__(self, other: 'GridModelTrainedInfo'):
        return self.architecture == other.architecture and self.params == other.params

