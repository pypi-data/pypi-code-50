'''_3994.py

FaceGearSetModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model.gears import _2046
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6093
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _3993, _3992, _3998
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'FaceGearSetModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetModalAnalysesAtSpeeds',)


class FaceGearSetModalAnalysesAtSpeeds(_3998.GearSetModalAnalysesAtSpeeds):
    '''FaceGearSetModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _FACE_GEAR_SET_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2046.FaceGearSet':
        '''FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2046.FaceGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6093.FaceGearSetLoadCase':
        '''FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6093.FaceGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def face_gears_modal_analyses_at_speeds(self) -> 'List[_3993.FaceGearModalAnalysesAtSpeeds]':
        '''List[FaceGearModalAnalysesAtSpeeds]: 'FaceGearsModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearsModalAnalysesAtSpeeds, constructor.new(_3993.FaceGearModalAnalysesAtSpeeds))
        return value

    @property
    def face_meshes_modal_analyses_at_speeds(self) -> 'List[_3992.FaceGearMeshModalAnalysesAtSpeeds]':
        '''List[FaceGearMeshModalAnalysesAtSpeeds]: 'FaceMeshesModalAnalysesAtSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceMeshesModalAnalysesAtSpeeds, constructor.new(_3992.FaceGearMeshModalAnalysesAtSpeeds))
        return value
