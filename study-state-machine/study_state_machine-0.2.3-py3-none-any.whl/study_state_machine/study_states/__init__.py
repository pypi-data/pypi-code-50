import sys
import inspect

from study_state_machine.study_states.rna_seq import RNASeqState, BiokitUploadState

"""
Store all above imported states in dict <name, class>
"""
available_states = {}

for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    available_states[name] = obj

__all__ = ["RNASeqState", "BiokitUploadState", "available_states"]
