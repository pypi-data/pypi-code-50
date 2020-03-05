'''_2414.py

PowerLoadCompoundSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model import _1991
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2277
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2448
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'PowerLoadCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadCompoundSystemDeflection',)


class PowerLoadCompoundSystemDeflection(_2448.VirtualComponentCompoundSystemDeflection):
    '''PowerLoadCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _POWER_LOAD_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1991.PowerLoad':
        '''PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1991.PowerLoad)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_2277.PowerLoadSystemDeflection]':
        '''List[PowerLoadSystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2277.PowerLoadSystemDeflection))
        return value

    @property
    def component_system_deflection_load_cases(self) -> 'List[_2277.PowerLoadSystemDeflection]':
        '''List[PowerLoadSystemDeflection]: 'ComponentSystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentSystemDeflectionLoadCases, constructor.new(_2277.PowerLoadSystemDeflection))
        return value
