'''_4030.py

RollingRingAssemblyModalAnalysesAtSpeeds
'''


from mastapy.system_model.part_model.couplings import _2109
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6147
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _4037
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS', 'RollingRingAssemblyModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyModalAnalysesAtSpeeds',)


class RollingRingAssemblyModalAnalysesAtSpeeds(_4037.SpecialisedAssemblyModalAnalysesAtSpeeds):
    '''RollingRingAssemblyModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_ASSEMBLY_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyModalAnalysesAtSpeeds.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_2109.RollingRingAssembly':
        '''RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2109.RollingRingAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6147.RollingRingAssemblyLoadCase':
        '''RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6147.RollingRingAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None
