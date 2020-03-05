'''_6006.py

SpringDamperHalfLoadCase
'''


from mastapy.system_model.part_model.couplings import _2055
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _5916
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpringDamperHalfLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfLoadCase',)


class SpringDamperHalfLoadCase(_5916.CouplingHalfLoadCase):
    '''SpringDamperHalfLoadCase

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_HALF_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_2055.SpringDamperHalf':
        '''SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2055.SpringDamperHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None
