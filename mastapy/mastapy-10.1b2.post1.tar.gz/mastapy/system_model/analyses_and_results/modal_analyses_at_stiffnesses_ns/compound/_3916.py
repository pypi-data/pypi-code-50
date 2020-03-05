'''_3916.py

SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model.gears import _2061
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import _3914, _3915, _3839
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3795
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses',)


class SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses(_3839.BevelGearSetCompoundModalAnalysesAtStiffnesses):
    '''SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_2061.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2061.SpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def spiral_bevel_gears_compound_modal_analyses_at_stiffnesses(self) -> 'List[_3914.SpiralBevelGearCompoundModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearCompoundModalAnalysesAtStiffnesses]: 'SpiralBevelGearsCompoundModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundModalAnalysesAtStiffnesses, constructor.new(_3914.SpiralBevelGearCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spiral_bevel_meshes_compound_modal_analyses_at_stiffnesses(self) -> 'List[_3915.SpiralBevelGearMeshCompoundModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearMeshCompoundModalAnalysesAtStiffnesses]: 'SpiralBevelMeshesCompoundModalAnalysesAtStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundModalAnalysesAtStiffnesses, constructor.new(_3915.SpiralBevelGearMeshCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_3795.SpiralBevelGearSetModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearSetModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3795.SpiralBevelGearSetModalAnalysesAtStiffnesses))
        return value

    @property
    def assembly_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3795.SpiralBevelGearSetModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearSetModalAnalysesAtStiffnesses]: 'AssemblyModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtStiffnessesLoadCases, constructor.new(_3795.SpiralBevelGearSetModalAnalysesAtStiffnesses))
        return value
