'''_4787.py

StraightBevelGearSetModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2065
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6168
from mastapy.system_model.analyses_and_results.system_deflections import _2299
from mastapy.system_model.analyses_and_results.modal_analyses import _4786, _4785, _4693
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'StraightBevelGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetModalAnalysis',)


class StraightBevelGearSetModalAnalysis(_4693.BevelGearSetModalAnalysis):
    '''StraightBevelGearSetModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2065.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2065.StraightBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6168.StraightBevelGearSetLoadCase':
        '''StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6168.StraightBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2299.StraightBevelGearSetSystemDeflection':
        '''StraightBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2299.StraightBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def straight_bevel_gears_modal_analysis(self) -> 'List[_4786.StraightBevelGearModalAnalysis]':
        '''List[StraightBevelGearModalAnalysis]: 'StraightBevelGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearsModalAnalysis, constructor.new(_4786.StraightBevelGearModalAnalysis))
        return value

    @property
    def straight_bevel_meshes_modal_analysis(self) -> 'List[_4785.StraightBevelGearMeshModalAnalysis]':
        '''List[StraightBevelGearMeshModalAnalysis]: 'StraightBevelMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelMeshesModalAnalysis, constructor.new(_4785.StraightBevelGearMeshModalAnalysis))
        return value
