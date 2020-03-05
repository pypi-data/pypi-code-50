'''_3801.py

StraightBevelDiffGearSetModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2063
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6165
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3800, _3799, _3715
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS', 'StraightBevelDiffGearSetModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetModalAnalysesAtStiffnesses',)


class StraightBevelDiffGearSetModalAnalysesAtStiffnesses(_3715.BevelGearSetModalAnalysesAtStiffnesses):
    '''StraightBevelDiffGearSetModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2063.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2063.StraightBevelDiffGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6165.StraightBevelDiffGearSetLoadCase':
        '''StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6165.StraightBevelDiffGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def straight_bevel_diff_gears_modal_analyses_at_stiffnesses(self) -> 'List[_3800.StraightBevelDiffGearModalAnalysesAtStiffnesses]':
        '''List[StraightBevelDiffGearModalAnalysesAtStiffnesses]: 'StraightBevelDiffGearsModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearsModalAnalysesAtStiffnesses, constructor.new(_3800.StraightBevelDiffGearModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_diff_meshes_modal_analyses_at_stiffnesses(self) -> 'List[_3799.StraightBevelDiffGearMeshModalAnalysesAtStiffnesses]':
        '''List[StraightBevelDiffGearMeshModalAnalysesAtStiffnesses]: 'StraightBevelDiffMeshesModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffMeshesModalAnalysesAtStiffnesses, constructor.new(_3799.StraightBevelDiffGearMeshModalAnalysesAtStiffnesses))
        return value
