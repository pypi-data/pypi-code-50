'''_6264.py

FlexiblePinAssemblyAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _1975
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6094
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6254, _6302, _6305
from mastapy.system_model.analyses_and_results.system_deflections import _2283, _2263, _2244
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'FlexiblePinAssemblyAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyAdvancedSystemDeflection',)


class FlexiblePinAssemblyAdvancedSystemDeflection(_6305.SpecialisedAssemblyAdvancedSystemDeflection):
    '''FlexiblePinAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1975.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1975.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6094.FlexiblePinAssemblyLoadCase':
        '''FlexiblePinAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6094.FlexiblePinAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def planet_gear_analyses(self) -> 'List[_6254.CylindricalGearAdvancedSystemDeflection]':
        '''List[CylindricalGearAdvancedSystemDeflection]: 'PlanetGearAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetGearAnalyses, constructor.new(_6254.CylindricalGearAdvancedSystemDeflection))
        return value

    @property
    def pin_advanced_analyses(self) -> 'List[_6302.ShaftAdvancedSystemDeflection]':
        '''List[ShaftAdvancedSystemDeflection]: 'PinAdvancedAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PinAdvancedAnalyses, constructor.new(_6302.ShaftAdvancedSystemDeflection))
        return value

    @property
    def spindle_advanced_analyses(self) -> 'List[_6302.ShaftAdvancedSystemDeflection]':
        '''List[ShaftAdvancedSystemDeflection]: 'SpindleAdvancedAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpindleAdvancedAnalyses, constructor.new(_6302.ShaftAdvancedSystemDeflection))
        return value

    @property
    def pin_spindle_fit_advanced_analyses(self) -> 'List[_2283.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'PinSpindleFitAdvancedAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PinSpindleFitAdvancedAnalyses, constructor.new(_2283.ShaftHubConnectionSystemDeflection))
        return value

    @property
    def load_sharing_factor_reporters(self) -> 'List[_2263.LoadSharingFactorReporter]':
        '''List[LoadSharingFactorReporter]: 'LoadSharingFactorReporters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadSharingFactorReporters, constructor.new(_2263.LoadSharingFactorReporter))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2244.FlexiblePinAssemblySystemDeflection]':
        '''List[FlexiblePinAssemblySystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2244.FlexiblePinAssemblySystemDeflection))
        return value
