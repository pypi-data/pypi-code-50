'''_5273.py

SpringDamperModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2027
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _2262
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _5212
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'SpringDamperModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperModalAnalysesAtSpeeds',)


class SpringDamperModalAnalysesAtSpeeds(_5212.CouplingModalAnalysesAtSpeeds):
    '''SpringDamperModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _SPRING_DAMPER_MODAL_ANALYSES_AT_SPEEDS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2027.SpringDamper':
        '''SpringDamper: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2027.SpringDamper)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2262.SpringDamperLoadCase':
        '''SpringDamperLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2262.SpringDamperLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
