'''_5816.py

CylindricalGearSetDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2043
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6073
from mastapy.system_model.analyses_and_results.dynamic_analyses import _5814, _5815, _5828
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'CylindricalGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetDynamicAnalysis',)


class CylindricalGearSetDynamicAnalysis(_5828.GearSetDynamicAnalysis):
    '''CylindricalGearSetDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2043.CylindricalGearSet':
        '''CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2043.CylindricalGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6073.CylindricalGearSetLoadCase':
        '''CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6073.CylindricalGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def cylindrical_gears_dynamic_analysis(self) -> 'List[_5814.CylindricalGearDynamicAnalysis]':
        '''List[CylindricalGearDynamicAnalysis]: 'CylindricalGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearsDynamicAnalysis, constructor.new(_5814.CylindricalGearDynamicAnalysis))
        return value

    @property
    def cylindrical_meshes_dynamic_analysis(self) -> 'List[_5815.CylindricalGearMeshDynamicAnalysis]':
        '''List[CylindricalGearMeshDynamicAnalysis]: 'CylindricalMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshesDynamicAnalysis, constructor.new(_5815.CylindricalGearMeshDynamicAnalysis))
        return value
