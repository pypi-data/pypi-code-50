'''_6431.py

SpiralBevelGearSetCompoundAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2061
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _6429, _6430, _6354
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6308
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'SpiralBevelGearSetCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetCompoundAdvancedSystemDeflection',)


class SpiralBevelGearSetCompoundAdvancedSystemDeflection(_6354.BevelGearSetCompoundAdvancedSystemDeflection):
    '''SpiralBevelGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetCompoundAdvancedSystemDeflection.TYPE'):
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
    def spiral_bevel_gears_compound_advanced_system_deflection(self) -> 'List[_6429.SpiralBevelGearCompoundAdvancedSystemDeflection]':
        '''List[SpiralBevelGearCompoundAdvancedSystemDeflection]: 'SpiralBevelGearsCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearsCompoundAdvancedSystemDeflection, constructor.new(_6429.SpiralBevelGearCompoundAdvancedSystemDeflection))
        return value

    @property
    def spiral_bevel_meshes_compound_advanced_system_deflection(self) -> 'List[_6430.SpiralBevelGearMeshCompoundAdvancedSystemDeflection]':
        '''List[SpiralBevelGearMeshCompoundAdvancedSystemDeflection]: 'SpiralBevelMeshesCompoundAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelMeshesCompoundAdvancedSystemDeflection, constructor.new(_6430.SpiralBevelGearMeshCompoundAdvancedSystemDeflection))
        return value

    @property
    def load_case_analyses_ready(self) -> 'List[_6308.SpiralBevelGearSetAdvancedSystemDeflection]':
        '''List[SpiralBevelGearSetAdvancedSystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_6308.SpiralBevelGearSetAdvancedSystemDeflection))
        return value

    @property
    def assembly_advanced_system_deflection_load_cases(self) -> 'List[_6308.SpiralBevelGearSetAdvancedSystemDeflection]':
        '''List[SpiralBevelGearSetAdvancedSystemDeflection]: 'AssemblyAdvancedSystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAdvancedSystemDeflectionLoadCases, constructor.new(_6308.SpiralBevelGearSetAdvancedSystemDeflection))
        return value
