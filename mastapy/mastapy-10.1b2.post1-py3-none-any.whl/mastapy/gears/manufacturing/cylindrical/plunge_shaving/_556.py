'''_556.py

PlungeShaverOutputs
'''


from mastapy.scripting import _6321
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _548, _554
from mastapy.gears.manufacturing.cylindrical import _532
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_OUTPUTS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving', 'PlungeShaverOutputs')


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShaverOutputs',)


class PlungeShaverOutputs(_1.APIBase):
    '''PlungeShaverOutputs

    This is a mastapy class.
    '''

    TYPE = _PLUNGE_SHAVER_OUTPUTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlungeShaverOutputs.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def profile_modification_on_conjugate_shaver_chart_left_flank(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'ProfileModificationOnConjugateShaverChartLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.ProfileModificationOnConjugateShaverChartLeftFlank) if self.wrapped.ProfileModificationOnConjugateShaverChartLeftFlank else None

    @property
    def profile_modification_on_conjugate_shaver_chart_right_flank(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'ProfileModificationOnConjugateShaverChartRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.ProfileModificationOnConjugateShaverChartRightFlank) if self.wrapped.ProfileModificationOnConjugateShaverChartRightFlank else None

    @property
    def shaver_profile_modification_z_plane(self) -> 'float':
        '''float: 'ShaverProfileModificationZPlane' is the original name of this property.'''

        return self.wrapped.ShaverProfileModificationZPlane

    @shaver_profile_modification_z_plane.setter
    def shaver_profile_modification_z_plane(self, value: 'float'):
        self.wrapped.ShaverProfileModificationZPlane = float(value) if value else 0.0

    @property
    def shaved_gear_profile_modification_z_plane(self) -> 'float':
        '''float: 'ShavedGearProfileModificationZPlane' is the original name of this property.'''

        return self.wrapped.ShavedGearProfileModificationZPlane

    @shaved_gear_profile_modification_z_plane.setter
    def shaved_gear_profile_modification_z_plane(self, value: 'float'):
        self.wrapped.ShavedGearProfileModificationZPlane = float(value) if value else 0.0

    @property
    def difference_between_chart_z_plane(self) -> 'float':
        '''float: 'DifferenceBetweenChartZPlane' is the original name of this property.'''

        return self.wrapped.DifferenceBetweenChartZPlane

    @difference_between_chart_z_plane.setter
    def difference_between_chart_z_plane(self, value: 'float'):
        self.wrapped.DifferenceBetweenChartZPlane = float(value) if value else 0.0

    @property
    def chart(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ChartType':
        '''enum_with_selected_value.EnumWithSelectedValue_ChartType: 'Chart' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ChartType.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.Chart, value) if self.wrapped.Chart else None

    @chart.setter
    def chart(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ChartType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ChartType.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.Chart = value

    @property
    def selected_flank(self) -> 'enum_with_selected_value.EnumWithSelectedValue_Flank':
        '''enum_with_selected_value.EnumWithSelectedValue_Flank: 'SelectedFlank' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_Flank.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.SelectedFlank, value) if self.wrapped.SelectedFlank else None

    @selected_flank.setter
    def selected_flank(self, value: 'enum_with_selected_value.EnumWithSelectedValue_Flank.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_Flank.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.SelectedFlank = value

    @property
    def calculation_details(self) -> '_554.PlungeShaverGeneration':
        '''PlungeShaverGeneration: 'CalculationDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_554.PlungeShaverGeneration)(self.wrapped.CalculationDetails) if self.wrapped.CalculationDetails else None
