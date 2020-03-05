'''_5467.py

FaceGearSetModalAnalysisAtAStiffness
'''


from typing import List

from mastapy.system_model.part_model.gears import _1996
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2349
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _5466, _5465, _5471
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'FaceGearSetModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetModalAnalysisAtAStiffness',)


class FaceGearSetModalAnalysisAtAStiffness(_5471.GearSetModalAnalysisAtAStiffness):
    '''FaceGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1996.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1996.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2349.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2349.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def face_gears_modal_analysis_at_a_stiffness(self) -> 'List[_5466.FaceGearModalAnalysisAtAStiffness]':
        '''List[FaceGearModalAnalysisAtAStiffness]: 'FaceGearsModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsModalAnalysisAtAStiffness, constructor.new(_5466.FaceGearModalAnalysisAtAStiffness))
        return value

    @property
    def face_meshes_modal_analysis_at_a_stiffness(self) -> 'List[_5465.FaceGearMeshModalAnalysisAtAStiffness]':
        '''List[FaceGearMeshModalAnalysisAtAStiffness]: 'FaceMeshesModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesModalAnalysisAtAStiffness, constructor.new(_5465.FaceGearMeshModalAnalysisAtAStiffness))
        return value
