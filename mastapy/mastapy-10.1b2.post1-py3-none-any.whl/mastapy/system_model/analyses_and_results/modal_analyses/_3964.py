'''_3964.py

HypoidGearSetModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _1975
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2366
from mastapy.system_model.analyses_and_results.system_deflections import _2211
from mastapy.system_model.analyses_and_results.modal_analyses import _3963, _3909, _3949
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'HypoidGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetModalAnalysis',)


class HypoidGearSetModalAnalysis(_3949.AGMAGleasonConicalGearSetModalAnalysis):
    '''HypoidGearSetModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_MODAL_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1975.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1975.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2366.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2366.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2211.HypoidGearSetSystemDeflection':
        '''HypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2211.HypoidGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def hypoid_gears_modal_analysis(self) -> 'List[_3963.HypoidGearModalAnalysis]':
        '''List[HypoidGearModalAnalysis]: 'HypoidGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsModalAnalysis, constructor.new(_3963.HypoidGearModalAnalysis))
        return value

    @property
    def hypoid_meshes_modal_analysis(self) -> 'List[_3909.HypoidGearMeshModalAnalysis]':
        '''List[HypoidGearMeshModalAnalysis]: 'HypoidMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesModalAnalysis, constructor.new(_3909.HypoidGearMeshModalAnalysis))
        return value
