'''_6306.py

PointLoadInputOptions
'''


from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _1943
from mastapy._internal import constructor, conversion
from mastapy.math_utility import _299
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6297
from mastapy.utility_gui import _1463
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_INPUT_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads.DutyCycleDefinition', 'PointLoadInputOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadInputOptions',)


class PointLoadInputOptions(_1463.ColumnInputOptions):
    '''PointLoadInputOptions

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD_INPUT_OPTIONS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadInputOptions.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def point_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PointLoad':
        '''list_with_selected_item.ListWithSelectedItem_PointLoad: 'PointLoad' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_PointLoad)(self.wrapped.PointLoad) if self.wrapped.PointLoad else None

    @point_load.setter
    def point_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PointLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PointLoad.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PointLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.PointLoad = value

    @property
    def axis(self) -> '_299.Axis':
        '''Axis: 'Axis' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Axis)
        return constructor.new(_299.Axis)(value) if value else None

    @axis.setter
    def axis(self, value: '_299.Axis'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Axis = value

    @property
    def conversion_to_load_case(self) -> '_6297.AdditionalForcesObtainedFrom':
        '''AdditionalForcesObtainedFrom: 'ConversionToLoadCase' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ConversionToLoadCase)
        return constructor.new(_6297.AdditionalForcesObtainedFrom)(value) if value else None

    @conversion_to_load_case.setter
    def conversion_to_load_case(self, value: '_6297.AdditionalForcesObtainedFrom'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ConversionToLoadCase = value
