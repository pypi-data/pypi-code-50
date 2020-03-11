from dataclasses import dataclass, field
from typing import List

from frater.component import BatchComponent, BatchComponentConfig
from frater.stream import InputStream, OutputStream
from ...data_type import Activity, ActivityProposal, Modality


@dataclass
class ActivityClassifierConfig(BatchComponentConfig):
    classifier_name: str = ''
    weights: str = ''
    num_categories: int = 0
    batch_size: int = 1
    modality: str = field(default='RGB')
    gpus: List[int] = field(default_factory=list)
    input_components: int = 1

    @property
    def modality_type(self) -> Modality:
        return Modality[self.modality]


class ActivityClassifier(BatchComponent):
    def __init__(self, config: ActivityClassifierConfig, input_stream: InputStream, output_stream: OutputStream):
        super(ActivityClassifier, self).__init__(config, input_stream, output_stream)

    def process(self, proposals: List[ActivityProposal]) -> List[Activity]:
        raise NotImplementedError
