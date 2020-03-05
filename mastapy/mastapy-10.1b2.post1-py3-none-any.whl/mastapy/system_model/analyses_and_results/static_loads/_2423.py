'''_2423.py

FlexiblePinAssemblyLoadCase
'''


from mastapy.utility import _1270
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1924
from mastapy.system_model.analyses_and_results.static_loads import _2436
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FlexiblePinAssemblyLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FlexiblePinAssemblyLoadCase',)


class FlexiblePinAssemblyLoadCase(_2436.SpecialisedAssemblyLoadCase):
    '''FlexiblePinAssemblyLoadCase

    This is a mastapy class.
    '''

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_LOAD_CASE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlexiblePinAssemblyLoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def include_inner_race_distortion_for_flexible_pin_spindle(self) -> '_1270.LoadCaseOverrideOption':
        '''LoadCaseOverrideOption: 'IncludeInnerRaceDistortionForFlexiblePinSpindle' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle)
        return constructor.new(_1270.LoadCaseOverrideOption)(value) if value else None

    @include_inner_race_distortion_for_flexible_pin_spindle.setter
    def include_inner_race_distortion_for_flexible_pin_spindle(self, value: '_1270.LoadCaseOverrideOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle = value

    @property
    def assembly_design(self) -> '_1924.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1924.FlexiblePinAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None
