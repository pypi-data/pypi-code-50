'''_2282.py

RootAssemblySystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _1993
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2307, _2209, _2190
from mastapy.system_model.analyses_and_results.power_flows import _3283
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'RootAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblySystemDeflection',)


class RootAssemblySystemDeflection(_2190.AssemblySystemDeflection):
    '''RootAssemblySystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ROOT_ASSEMBLY_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1993.RootAssembly':
        '''RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1993.RootAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def system_deflection_inputs(self) -> '_2307.SystemDeflection':
        '''SystemDeflection: 'SystemDeflectionInputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2307.SystemDeflection)(self.wrapped.SystemDeflectionInputs) if self.wrapped.SystemDeflectionInputs else None

    @property
    def power_flow_results(self) -> '_3283.RootAssemblyPowerFlow':
        '''RootAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3283.RootAssemblyPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def shaft_deflection_results(self) -> 'List[_2209.ConcentricPartGroupCombinationSystemDeflectionResults]':
        '''List[ConcentricPartGroupCombinationSystemDeflectionResults]: 'ShaftDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftDeflectionResults, constructor.new(_2209.ConcentricPartGroupCombinationSystemDeflectionResults))
        return value
