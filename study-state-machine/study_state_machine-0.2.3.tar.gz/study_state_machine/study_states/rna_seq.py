from study_state_machine.interfaces import IStudyState


class RNASeqState(IStudyState):

    def add_sample(self, sample=None):
        raise NotImplementedError


class BiokitUploadState(IStudyState):
    """State for studies which are registered with the Biokit"""

    def create_study(self, *args, **kwargs):
        self.context.transition_to(RNASeqState())

