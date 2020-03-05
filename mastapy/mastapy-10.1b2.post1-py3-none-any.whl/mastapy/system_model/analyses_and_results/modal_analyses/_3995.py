'''_3995.py

MassDiscModalAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1936
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2293
from mastapy.system_model.analyses_and_results.system_deflections import _2292
from mastapy.system_model.analyses_and_results.modal_analyses import _4006
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'MassDiscModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscModalAnalysis',)


class MassDiscModalAnalysis(_4006.VirtualComponentModalAnalysis):
    '''MassDiscModalAnalysis

    This is a mastapy class.
    '''

    TYPE = _MASS_DISC_MODAL_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1936.MassDisc':
        '''MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1936.MassDisc)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_2293.MassDiscLoadCase':
        '''MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2293.MassDiscLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def system_deflection_results(self) -> '_2292.MassDiscSystemDeflection':
        '''MassDiscSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2292.MassDiscSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def planetaries(self) -> 'List[MassDiscModalAnalysis]':
        '''List[MassDiscModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(MassDiscModalAnalysis))
        return value
