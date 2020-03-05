'''_1858.py

Bearing
'''


from typing import List, Optional

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.bearings.tolerances import (
    _1490, _1491, _1492, _1498,
    _1495, _1501, _1253, _1252,
    _1254
)
from mastapy.bearings.bearing_results import _1534, _1535
from mastapy.bearings import (
    _1462, _1469, _1468, _1476,
    _1464, _1461
)
from mastapy._internal.python_net import python_net_import
from mastapy.materials.efficiency import _280
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs import (
    _1662, _1663, _1664, _1665,
    _1666
)
from mastapy.bearings.bearing_designs.rolling import (
    _1667, _1668, _1669, _1670,
    _1671, _1672, _1674, _1679,
    _1680, _1682, _1684, _1685,
    _1686, _1687, _1690, _1691,
    _1693, _1694, _1695, _1696,
    _1697, _1698
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _1711, _1713, _1715, _1717,
    _1718, _1719
)
from mastapy.bearings.bearing_designs.concept import _1721, _1722, _1723
from mastapy.materials import _261
from mastapy.bearings.bearing_results.rolling import _1638
from mastapy.system_model.part_model import _2011, _2012, _1862
from mastapy.system_model.part_model.shaft_model import _1877

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')


__docformat__ = 'restructuredtext en'
__all__ = ('Bearing',)


class Bearing(_1862.Connector):
    '''Bearing

    This is a mastapy class.
    '''

    TYPE = _BEARING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'Bearing.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def outer_node_position_from_centre(self) -> 'float':
        '''float: 'OuterNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OuterNodePositionFromCentre

    @property
    def inner_node_position_from_centre(self) -> 'float':
        '''float: 'InnerNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InnerNodePositionFromCentre

    @property
    def left_node_position_from_centre(self) -> 'float':
        '''float: 'LeftNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LeftNodePositionFromCentre

    @property
    def right_node_position_from_centre(self) -> 'float':
        '''float: 'RightNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RightNodePositionFromCentre

    @property
    def offset_of_contact_on_inner_race_at_nominal_contact_angle(self) -> 'float':
        '''float: 'OffsetOfContactOnInnerRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OffsetOfContactOnInnerRaceAtNominalContactAngle

    @property
    def offset_of_contact_on_outer_race_at_nominal_contact_angle(self) -> 'float':
        '''float: 'OffsetOfContactOnOuterRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OffsetOfContactOnOuterRaceAtNominalContactAngle

    @property
    def diameter_of_contact_on_inner_race_at_nominal_contact_angle(self) -> 'float':
        '''float: 'DiameterOfContactOnInnerRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DiameterOfContactOnInnerRaceAtNominalContactAngle

    @property
    def diameter_of_contact_on_outer_race_at_nominal_contact_angle(self) -> 'float':
        '''float: 'DiameterOfContactOnOuterRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DiameterOfContactOnOuterRaceAtNominalContactAngle

    @property
    def offset_of_contact_on_left_race(self) -> 'float':
        '''float: 'OffsetOfContactOnLeftRace' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OffsetOfContactOnLeftRace

    @property
    def offset_of_contact_on_right_race(self) -> 'float':
        '''float: 'OffsetOfContactOnRightRace' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OffsetOfContactOnRightRace

    @property
    def diameter_of_contact_on_left_race(self) -> 'float':
        '''float: 'DiameterOfContactOnLeftRace' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DiameterOfContactOnLeftRace

    @property
    def diameter_of_contact_on_right_race(self) -> 'float':
        '''float: 'DiameterOfContactOnRightRace' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DiameterOfContactOnRightRace

    @property
    def bearing_tolerance_class(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass':
        '''enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass: 'BearingToleranceClass' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass)(self.wrapped.BearingToleranceClass) if self.wrapped.BearingToleranceClass else None

    @bearing_tolerance_class.setter
    def bearing_tolerance_class(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.BearingToleranceClass = value

    @property
    def bearing_tolerance_definition(self) -> '_1491.BearingToleranceDefinitionOptions':
        '''BearingToleranceDefinitionOptions: 'BearingToleranceDefinition' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.BearingToleranceDefinition)
        return constructor.new(_1491.BearingToleranceDefinitionOptions)(value) if value else None

    @bearing_tolerance_definition.setter
    def bearing_tolerance_definition(self, value: '_1491.BearingToleranceDefinitionOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BearingToleranceDefinition = value

    @property
    def orientation(self) -> '_1534.Orientations':
        '''Orientations: 'Orientation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Orientation)
        return constructor.new(_1534.Orientations)(value) if value else None

    @orientation.setter
    def orientation(self, value: '_1534.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def has_radial_mounting_clearance(self) -> 'bool':
        '''bool: 'HasRadialMountingClearance' is the original name of this property.'''

        return self.wrapped.HasRadialMountingClearance

    @has_radial_mounting_clearance.setter
    def has_radial_mounting_clearance(self, value: 'bool'):
        self.wrapped.HasRadialMountingClearance = bool(value) if value else False

    @property
    def axial_internal_clearance(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'AxialInternalClearance' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.AxialInternalClearance) if self.wrapped.AxialInternalClearance else None

    @axial_internal_clearance.setter
    def axial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.AxialInternalClearance = value

    @property
    def axial_internal_clearance_class(self) -> '_1462.BearingAxialInternalClearanceClass':
        '''BearingAxialInternalClearanceClass: 'AxialInternalClearanceClass' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AxialInternalClearanceClass)
        return constructor.new(_1462.BearingAxialInternalClearanceClass)(value) if value else None

    @axial_internal_clearance_class.setter
    def axial_internal_clearance_class(self, value: '_1462.BearingAxialInternalClearanceClass'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AxialInternalClearanceClass = value

    @property
    def radial_internal_clearance(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'RadialInternalClearance' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.RadialInternalClearance) if self.wrapped.RadialInternalClearance else None

    @radial_internal_clearance.setter
    def radial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.RadialInternalClearance = value

    @property
    def radial_internal_clearance_class(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingRadialInternalClearanceClass':
        '''enum_with_selected_value.EnumWithSelectedValue_BearingRadialInternalClearanceClass: 'RadialInternalClearanceClass' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_BearingRadialInternalClearanceClass)(self.wrapped.RadialInternalClearanceClass) if self.wrapped.RadialInternalClearanceClass else None

    @radial_internal_clearance_class.setter
    def radial_internal_clearance_class(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingRadialInternalClearanceClass.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_BearingRadialInternalClearanceClass.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingRadialInternalClearanceClass.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.RadialInternalClearanceClass = value

    @property
    def axial_displacement_preload(self) -> 'float':
        '''float: 'AxialDisplacementPreload' is the original name of this property.'''

        return self.wrapped.AxialDisplacementPreload

    @axial_displacement_preload.setter
    def axial_displacement_preload(self, value: 'float'):
        self.wrapped.AxialDisplacementPreload = float(value) if value else 0.0

    @property
    def preload_spring_on_outer(self) -> 'bool':
        '''bool: 'PreloadSpringOnOuter' is the original name of this property.'''

        return self.wrapped.PreloadSpringOnOuter

    @preload_spring_on_outer.setter
    def preload_spring_on_outer(self, value: 'bool'):
        self.wrapped.PreloadSpringOnOuter = bool(value) if value else False

    @property
    def axial_force_preload(self) -> 'float':
        '''float: 'AxialForcePreload' is the original name of this property.'''

        return self.wrapped.AxialForcePreload

    @axial_force_preload.setter
    def axial_force_preload(self, value: 'float'):
        self.wrapped.AxialForcePreload = float(value) if value else 0.0

    @property
    def preload_spring_stiffness(self) -> 'float':
        '''float: 'PreloadSpringStiffness' is the original name of this property.'''

        return self.wrapped.PreloadSpringStiffness

    @preload_spring_stiffness.setter
    def preload_spring_stiffness(self, value: 'float'):
        self.wrapped.PreloadSpringStiffness = float(value) if value else 0.0

    @property
    def preload_spring_initial_compression(self) -> 'float':
        '''float: 'PreloadSpringInitialCompression' is the original name of this property.'''

        return self.wrapped.PreloadSpringInitialCompression

    @preload_spring_initial_compression.setter
    def preload_spring_initial_compression(self, value: 'float'):
        self.wrapped.PreloadSpringInitialCompression = float(value) if value else 0.0

    @property
    def preload_spring_max_travel(self) -> 'float':
        '''float: 'PreloadSpringMaxTravel' is the original name of this property.'''

        return self.wrapped.PreloadSpringMaxTravel

    @preload_spring_max_travel.setter
    def preload_spring_max_travel(self, value: 'float'):
        self.wrapped.PreloadSpringMaxTravel = float(value) if value else 0.0

    @property
    def axial_stiffness_at_mounting_points(self) -> 'float':
        '''float: 'AxialStiffnessAtMountingPoints' is the original name of this property.'''

        return self.wrapped.AxialStiffnessAtMountingPoints

    @axial_stiffness_at_mounting_points.setter
    def axial_stiffness_at_mounting_points(self, value: 'float'):
        self.wrapped.AxialStiffnessAtMountingPoints = float(value) if value else 0.0

    @property
    def preload_is_from_left(self) -> 'bool':
        '''bool: 'PreloadIsFromLeft' is the original name of this property.'''

        return self.wrapped.PreloadIsFromLeft

    @preload_is_from_left.setter
    def preload_is_from_left(self, value: 'bool'):
        self.wrapped.PreloadIsFromLeft = bool(value) if value else False

    @property
    def model(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingModel':
        '''enum_with_selected_value.EnumWithSelectedValue_BearingModel: 'Model' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_BearingModel)(self.wrapped.Model) if self.wrapped.Model else None

    @model.setter
    def model(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_BearingModel.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.Model = value

    @property
    def journal_bearing_type(self) -> '_1476.JournalBearingType':
        '''JournalBearingType: 'JournalBearingType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.JournalBearingType)
        return constructor.new(_1476.JournalBearingType)(value) if value else None

    @journal_bearing_type.setter
    def journal_bearing_type(self, value: '_1476.JournalBearingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.JournalBearingType = value

    @property
    def length(self) -> 'float':
        '''float: 'Length' is the original name of this property.'''

        return self.wrapped.Length

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def outer_diameter(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'OuterDiameter' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.OuterDiameter) if self.wrapped.OuterDiameter else None

    @outer_diameter.setter
    def outer_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.OuterDiameter = value

    @property
    def inner_diameter(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'InnerDiameter' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.InnerDiameter) if self.wrapped.InnerDiameter else None

    @inner_diameter.setter
    def inner_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.InnerDiameter = value

    @property
    def difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(self) -> 'float':
        '''float: 'DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection

    @property
    def percentage_difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(self) -> 'float':
        '''float: 'PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection

    @property
    def difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(self) -> 'float':
        '''float: 'DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection

    @property
    def percentage_difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(self) -> 'float':
        '''float: 'PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection

    @property
    def preload(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PreloadType':
        '''enum_with_selected_value.EnumWithSelectedValue_PreloadType: 'Preload' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_PreloadType)(self.wrapped.Preload) if self.wrapped.Preload else None

    @preload.setter
    def preload(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_PreloadType.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.Preload = value

    @property
    def override_design_lubrication_detail(self) -> 'bool':
        '''bool: 'OverrideDesignLubricationDetail' is the original name of this property.'''

        return self.wrapped.OverrideDesignLubricationDetail

    @override_design_lubrication_detail.setter
    def override_design_lubrication_detail(self, value: 'bool'):
        self.wrapped.OverrideDesignLubricationDetail = bool(value) if value else False

    @property
    def lubrication_detail(self) -> 'str':
        '''str: 'LubricationDetail' is the original name of this property.'''

        return self.wrapped.LubricationDetail.SelectedItemName

    @lubrication_detail.setter
    def lubrication_detail(self, value: 'str'):
        self.wrapped.LubricationDetail.SetSelectedItem(str(value) if value else None)

    @property
    def damping_options(self) -> '_1464.BearingDampingMatrixOption':
        '''BearingDampingMatrixOption: 'DampingOptions' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.DampingOptions)
        return constructor.new(_1464.BearingDampingMatrixOption)(value) if value else None

    @damping_options.setter
    def damping_options(self, value: '_1464.BearingDampingMatrixOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DampingOptions = value

    @property
    def first_element_angle(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'FirstElementAngle' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.FirstElementAngle) if self.wrapped.FirstElementAngle else None

    @first_element_angle.setter
    def first_element_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.FirstElementAngle = value

    @property
    def maximum_bearing_life_modification_factor(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MaximumBearingLifeModificationFactor' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MaximumBearingLifeModificationFactor) if self.wrapped.MaximumBearingLifeModificationFactor else None

    @maximum_bearing_life_modification_factor.setter
    def maximum_bearing_life_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MaximumBearingLifeModificationFactor = value

    @property
    def bearing_life_modification_factor(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'BearingLifeModificationFactor' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.BearingLifeModificationFactor) if self.wrapped.BearingLifeModificationFactor else None

    @bearing_life_modification_factor.setter
    def bearing_life_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.BearingLifeModificationFactor = value

    @property
    def permissible_track_truncation(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'PermissibleTrackTruncation' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.PermissibleTrackTruncation) if self.wrapped.PermissibleTrackTruncation else None

    @permissible_track_truncation.setter
    def permissible_track_truncation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.PermissibleTrackTruncation = value

    @property
    def use_design_iso14179_settings(self) -> 'bool':
        '''bool: 'UseDesignISO14179Settings' is the original name of this property.'''

        return self.wrapped.UseDesignISO14179Settings

    @use_design_iso14179_settings.setter
    def use_design_iso14179_settings(self, value: 'bool'):
        self.wrapped.UseDesignISO14179Settings = bool(value) if value else False

    @property
    def coefficient_of_friction(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'CoefficientOfFriction' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.CoefficientOfFriction) if self.wrapped.CoefficientOfFriction else None

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.CoefficientOfFriction = value

    @property
    def efficiency_rating_method(self) -> 'overridable.Overridable_EfficiencyRatingMethod':
        '''overridable.Overridable_EfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property.'''

        return constructor.new(overridable.Overridable_EfficiencyRatingMethod)(self.wrapped.EfficiencyRatingMethod) if self.wrapped.EfficiencyRatingMethod else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: 'overridable.Overridable_EfficiencyRatingMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_EfficiencyRatingMethod.TYPE
        enclosed_type = overridable.Overridable_EfficiencyRatingMethod.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def race_tolerance_inner(self) -> '_1492.InnerRaceTolerance':
        '''InnerRaceTolerance: 'RaceToleranceInner' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1492.InnerRaceTolerance)(self.wrapped.RaceToleranceInner) if self.wrapped.RaceToleranceInner else None

    @property
    def race_tolerance_left(self) -> '_1498.RaceTolerance':
        '''RaceTolerance: 'RaceToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1498.RaceTolerance)(self.wrapped.RaceToleranceLeft) if self.wrapped.RaceToleranceLeft else None

    @property
    def race_tolerance_left_of_type_inner_race_tolerance(self) -> '_1492.InnerRaceTolerance':
        '''InnerRaceTolerance: 'RaceToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1492.InnerRaceTolerance.TYPE not in self.wrapped.RaceToleranceLeft.__class__.__mro__:
            raise CastException('Failed to cast race_tolerance_left to InnerRaceTolerance. Expected: {}.'.format(self.wrapped.RaceToleranceLeft.__class__.__qualname__))

        return constructor.new(_1492.InnerRaceTolerance)(self.wrapped.RaceToleranceLeft) if self.wrapped.RaceToleranceLeft else None

    @property
    def race_tolerance_left_of_type_outer_race_tolerance(self) -> '_1495.OuterRaceTolerance':
        '''OuterRaceTolerance: 'RaceToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1495.OuterRaceTolerance.TYPE not in self.wrapped.RaceToleranceLeft.__class__.__mro__:
            raise CastException('Failed to cast race_tolerance_left to OuterRaceTolerance. Expected: {}.'.format(self.wrapped.RaceToleranceLeft.__class__.__qualname__))

        return constructor.new(_1495.OuterRaceTolerance)(self.wrapped.RaceToleranceLeft) if self.wrapped.RaceToleranceLeft else None

    @property
    def race_tolerance_outer(self) -> '_1495.OuterRaceTolerance':
        '''OuterRaceTolerance: 'RaceToleranceOuter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1495.OuterRaceTolerance)(self.wrapped.RaceToleranceOuter) if self.wrapped.RaceToleranceOuter else None

    @property
    def race_tolerance_right(self) -> '_1498.RaceTolerance':
        '''RaceTolerance: 'RaceToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1498.RaceTolerance)(self.wrapped.RaceToleranceRight) if self.wrapped.RaceToleranceRight else None

    @property
    def race_tolerance_right_of_type_inner_race_tolerance(self) -> '_1492.InnerRaceTolerance':
        '''InnerRaceTolerance: 'RaceToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1492.InnerRaceTolerance.TYPE not in self.wrapped.RaceToleranceRight.__class__.__mro__:
            raise CastException('Failed to cast race_tolerance_right to InnerRaceTolerance. Expected: {}.'.format(self.wrapped.RaceToleranceRight.__class__.__qualname__))

        return constructor.new(_1492.InnerRaceTolerance)(self.wrapped.RaceToleranceRight) if self.wrapped.RaceToleranceRight else None

    @property
    def race_tolerance_right_of_type_outer_race_tolerance(self) -> '_1495.OuterRaceTolerance':
        '''OuterRaceTolerance: 'RaceToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1495.OuterRaceTolerance.TYPE not in self.wrapped.RaceToleranceRight.__class__.__mro__:
            raise CastException('Failed to cast race_tolerance_right to OuterRaceTolerance. Expected: {}.'.format(self.wrapped.RaceToleranceRight.__class__.__qualname__))

        return constructor.new(_1495.OuterRaceTolerance)(self.wrapped.RaceToleranceRight) if self.wrapped.RaceToleranceRight else None

    @property
    def inner_support_detail(self) -> '_1501.SupportDetail':
        '''SupportDetail: 'InnerSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1501.SupportDetail)(self.wrapped.InnerSupportDetail) if self.wrapped.InnerSupportDetail else None

    @property
    def left_support_detail(self) -> '_1501.SupportDetail':
        '''SupportDetail: 'LeftSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1501.SupportDetail)(self.wrapped.LeftSupportDetail) if self.wrapped.LeftSupportDetail else None

    @property
    def outer_support_detail(self) -> '_1501.SupportDetail':
        '''SupportDetail: 'OuterSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1501.SupportDetail)(self.wrapped.OuterSupportDetail) if self.wrapped.OuterSupportDetail else None

    @property
    def right_support_detail(self) -> '_1501.SupportDetail':
        '''SupportDetail: 'RightSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1501.SupportDetail)(self.wrapped.RightSupportDetail) if self.wrapped.RightSupportDetail else None

    @property
    def support_tolerance_inner(self) -> '_1253.InnerSupportTolerance':
        '''InnerSupportTolerance: 'SupportToleranceInner' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1253.InnerSupportTolerance)(self.wrapped.SupportToleranceInner) if self.wrapped.SupportToleranceInner else None

    @property
    def support_tolerance_left(self) -> '_1252.SupportTolerance':
        '''SupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1252.SupportTolerance)(self.wrapped.SupportToleranceLeft) if self.wrapped.SupportToleranceLeft else None

    @property
    def support_tolerance_left_of_type_inner_support_tolerance(self) -> '_1253.InnerSupportTolerance':
        '''InnerSupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1253.InnerSupportTolerance.TYPE not in self.wrapped.SupportToleranceLeft.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to InnerSupportTolerance. Expected: {}.'.format(self.wrapped.SupportToleranceLeft.__class__.__qualname__))

        return constructor.new(_1253.InnerSupportTolerance)(self.wrapped.SupportToleranceLeft) if self.wrapped.SupportToleranceLeft else None

    @property
    def support_tolerance_left_of_type_outer_support_tolerance(self) -> '_1254.OuterSupportTolerance':
        '''OuterSupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1254.OuterSupportTolerance.TYPE not in self.wrapped.SupportToleranceLeft.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to OuterSupportTolerance. Expected: {}.'.format(self.wrapped.SupportToleranceLeft.__class__.__qualname__))

        return constructor.new(_1254.OuterSupportTolerance)(self.wrapped.SupportToleranceLeft) if self.wrapped.SupportToleranceLeft else None

    @property
    def support_tolerance_outer(self) -> '_1254.OuterSupportTolerance':
        '''OuterSupportTolerance: 'SupportToleranceOuter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1254.OuterSupportTolerance)(self.wrapped.SupportToleranceOuter) if self.wrapped.SupportToleranceOuter else None

    @property
    def support_tolerance_right(self) -> '_1252.SupportTolerance':
        '''SupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1252.SupportTolerance)(self.wrapped.SupportToleranceRight) if self.wrapped.SupportToleranceRight else None

    @property
    def support_tolerance_right_of_type_inner_support_tolerance(self) -> '_1253.InnerSupportTolerance':
        '''InnerSupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1253.InnerSupportTolerance.TYPE not in self.wrapped.SupportToleranceRight.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to InnerSupportTolerance. Expected: {}.'.format(self.wrapped.SupportToleranceRight.__class__.__qualname__))

        return constructor.new(_1253.InnerSupportTolerance)(self.wrapped.SupportToleranceRight) if self.wrapped.SupportToleranceRight else None

    @property
    def support_tolerance_right_of_type_outer_support_tolerance(self) -> '_1254.OuterSupportTolerance':
        '''OuterSupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1254.OuterSupportTolerance.TYPE not in self.wrapped.SupportToleranceRight.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to OuterSupportTolerance. Expected: {}.'.format(self.wrapped.SupportToleranceRight.__class__.__qualname__))

        return constructor.new(_1254.OuterSupportTolerance)(self.wrapped.SupportToleranceRight) if self.wrapped.SupportToleranceRight else None

    @property
    def simple_bearing_detail_property(self) -> '_1662.BearingDesign':
        '''BearingDesign: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1662.BearingDesign)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_detailed_bearing(self) -> '_1663.DetailedBearing':
        '''DetailedBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1663.DetailedBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DetailedBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1663.DetailedBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_dummy_rolling_bearing(self) -> '_1664.DummyRollingBearing':
        '''DummyRollingBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1664.DummyRollingBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DummyRollingBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1664.DummyRollingBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_linear_bearing(self) -> '_1665.LinearBearing':
        '''LinearBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1665.LinearBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to LinearBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1665.LinearBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_non_linear_bearing(self) -> '_1666.NonLinearBearing':
        '''NonLinearBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1666.NonLinearBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NonLinearBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1666.NonLinearBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_angular_contact_ball_bearing(self) -> '_1667.AngularContactBallBearing':
        '''AngularContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1667.AngularContactBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AngularContactBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1667.AngularContactBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_angular_contact_thrust_ball_bearing(self) -> '_1668.AngularContactThrustBallBearing':
        '''AngularContactThrustBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1668.AngularContactThrustBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AngularContactThrustBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1668.AngularContactThrustBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_asymmetric_spherical_roller_bearing(self) -> '_1669.AsymmetricSphericalRollerBearing':
        '''AsymmetricSphericalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1669.AsymmetricSphericalRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AsymmetricSphericalRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1669.AsymmetricSphericalRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_1670.AxialThrustCylindricalRollerBearing':
        '''AxialThrustCylindricalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1670.AxialThrustCylindricalRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1670.AxialThrustCylindricalRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_axial_thrust_needle_roller_bearing(self) -> '_1671.AxialThrustNeedleRollerBearing':
        '''AxialThrustNeedleRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1671.AxialThrustNeedleRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AxialThrustNeedleRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1671.AxialThrustNeedleRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_ball_bearing(self) -> '_1672.BallBearing':
        '''BallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1672.BallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1672.BallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_barrel_roller_bearing(self) -> '_1674.BarrelRollerBearing':
        '''BarrelRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1674.BarrelRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BarrelRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1674.BarrelRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_cylindrical_roller_bearing(self) -> '_1679.CylindricalRollerBearing':
        '''CylindricalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1679.CylindricalRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to CylindricalRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1679.CylindricalRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_deep_groove_ball_bearing(self) -> '_1680.DeepGrooveBallBearing':
        '''DeepGrooveBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1680.DeepGrooveBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DeepGrooveBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1680.DeepGrooveBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_four_point_contact_ball_bearing(self) -> '_1682.FourPointContactBallBearing':
        '''FourPointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1682.FourPointContactBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to FourPointContactBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1682.FourPointContactBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_multi_point_contact_ball_bearing(self) -> '_1684.MultiPointContactBallBearing':
        '''MultiPointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1684.MultiPointContactBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to MultiPointContactBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1684.MultiPointContactBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_needle_roller_bearing(self) -> '_1685.NeedleRollerBearing':
        '''NeedleRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1685.NeedleRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NeedleRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1685.NeedleRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_non_barrel_roller_bearing(self) -> '_1686.NonBarrelRollerBearing':
        '''NonBarrelRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1686.NonBarrelRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NonBarrelRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1686.NonBarrelRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_roller_bearing(self) -> '_1687.RollerBearing':
        '''RollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1687.RollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to RollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1687.RollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_rolling_bearing(self) -> '_1690.RollingBearing':
        '''RollingBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1690.RollingBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to RollingBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1690.RollingBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_self_aligning_ball_bearing(self) -> '_1691.SelfAligningBallBearing':
        '''SelfAligningBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1691.SelfAligningBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SelfAligningBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1691.SelfAligningBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_spherical_roller_bearing(self) -> '_1693.SphericalRollerBearing':
        '''SphericalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1693.SphericalRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SphericalRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1693.SphericalRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_spherical_roller_thrust_bearing(self) -> '_1694.SphericalRollerThrustBearing':
        '''SphericalRollerThrustBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1694.SphericalRollerThrustBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SphericalRollerThrustBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1694.SphericalRollerThrustBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_taper_roller_bearing(self) -> '_1695.TaperRollerBearing':
        '''TaperRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1695.TaperRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TaperRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1695.TaperRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_three_point_contact_ball_bearing(self) -> '_1696.ThreePointContactBallBearing':
        '''ThreePointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1696.ThreePointContactBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ThreePointContactBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1696.ThreePointContactBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_thrust_ball_bearing(self) -> '_1697.ThrustBallBearing':
        '''ThrustBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1697.ThrustBallBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ThrustBallBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1697.ThrustBallBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_toroidal_roller_bearing(self) -> '_1698.ToroidalRollerBearing':
        '''ToroidalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1698.ToroidalRollerBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ToroidalRollerBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1698.ToroidalRollerBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_pad_fluid_film_bearing(self) -> '_1711.PadFluidFilmBearing':
        '''PadFluidFilmBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1711.PadFluidFilmBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PadFluidFilmBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1711.PadFluidFilmBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_plain_grease_filled_journal_bearing(self) -> '_1713.PlainGreaseFilledJournalBearing':
        '''PlainGreaseFilledJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1713.PlainGreaseFilledJournalBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainGreaseFilledJournalBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1713.PlainGreaseFilledJournalBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_plain_journal_bearing(self) -> '_1715.PlainJournalBearing':
        '''PlainJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1715.PlainJournalBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainJournalBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1715.PlainJournalBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_plain_oil_fed_journal_bearing(self) -> '_1717.PlainOilFedJournalBearing':
        '''PlainOilFedJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1717.PlainOilFedJournalBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainOilFedJournalBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1717.PlainOilFedJournalBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_tilting_pad_journal_bearing(self) -> '_1718.TiltingPadJournalBearing':
        '''TiltingPadJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1718.TiltingPadJournalBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TiltingPadJournalBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1718.TiltingPadJournalBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_tilting_pad_thrust_bearing(self) -> '_1719.TiltingPadThrustBearing':
        '''TiltingPadThrustBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1719.TiltingPadThrustBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TiltingPadThrustBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1719.TiltingPadThrustBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_concept_axial_clearance_bearing(self) -> '_1721.ConceptAxialClearanceBearing':
        '''ConceptAxialClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1721.ConceptAxialClearanceBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptAxialClearanceBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1721.ConceptAxialClearanceBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_concept_clearance_bearing(self) -> '_1722.ConceptClearanceBearing':
        '''ConceptClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1722.ConceptClearanceBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptClearanceBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1722.ConceptClearanceBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def simple_bearing_detail_property_of_type_concept_radial_clearance_bearing(self) -> '_1723.ConceptRadialClearanceBearing':
        '''ConceptRadialClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1723.ConceptRadialClearanceBearing.TYPE not in self.wrapped.SimpleBearingDetailProperty.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptRadialClearanceBearing. Expected: {}.'.format(self.wrapped.SimpleBearingDetailProperty.__class__.__qualname__))

        return constructor.new(_1723.ConceptRadialClearanceBearing)(self.wrapped.SimpleBearingDetailProperty) if self.wrapped.SimpleBearingDetailProperty else None

    @property
    def detail(self) -> '_1662.BearingDesign':
        '''BearingDesign: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1662.BearingDesign)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_detailed_bearing(self) -> '_1663.DetailedBearing':
        '''DetailedBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1663.DetailedBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to DetailedBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1663.DetailedBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_dummy_rolling_bearing(self) -> '_1664.DummyRollingBearing':
        '''DummyRollingBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1664.DummyRollingBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to DummyRollingBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1664.DummyRollingBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_linear_bearing(self) -> '_1665.LinearBearing':
        '''LinearBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1665.LinearBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to LinearBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1665.LinearBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_non_linear_bearing(self) -> '_1666.NonLinearBearing':
        '''NonLinearBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1666.NonLinearBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to NonLinearBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1666.NonLinearBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_angular_contact_ball_bearing(self) -> '_1667.AngularContactBallBearing':
        '''AngularContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1667.AngularContactBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to AngularContactBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1667.AngularContactBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_angular_contact_thrust_ball_bearing(self) -> '_1668.AngularContactThrustBallBearing':
        '''AngularContactThrustBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1668.AngularContactThrustBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to AngularContactThrustBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1668.AngularContactThrustBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_asymmetric_spherical_roller_bearing(self) -> '_1669.AsymmetricSphericalRollerBearing':
        '''AsymmetricSphericalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1669.AsymmetricSphericalRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to AsymmetricSphericalRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1669.AsymmetricSphericalRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_1670.AxialThrustCylindricalRollerBearing':
        '''AxialThrustCylindricalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1670.AxialThrustCylindricalRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1670.AxialThrustCylindricalRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_axial_thrust_needle_roller_bearing(self) -> '_1671.AxialThrustNeedleRollerBearing':
        '''AxialThrustNeedleRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1671.AxialThrustNeedleRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to AxialThrustNeedleRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1671.AxialThrustNeedleRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_ball_bearing(self) -> '_1672.BallBearing':
        '''BallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1672.BallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to BallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1672.BallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_barrel_roller_bearing(self) -> '_1674.BarrelRollerBearing':
        '''BarrelRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1674.BarrelRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to BarrelRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1674.BarrelRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_cylindrical_roller_bearing(self) -> '_1679.CylindricalRollerBearing':
        '''CylindricalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1679.CylindricalRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to CylindricalRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1679.CylindricalRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_deep_groove_ball_bearing(self) -> '_1680.DeepGrooveBallBearing':
        '''DeepGrooveBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1680.DeepGrooveBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to DeepGrooveBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1680.DeepGrooveBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_four_point_contact_ball_bearing(self) -> '_1682.FourPointContactBallBearing':
        '''FourPointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1682.FourPointContactBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to FourPointContactBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1682.FourPointContactBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_multi_point_contact_ball_bearing(self) -> '_1684.MultiPointContactBallBearing':
        '''MultiPointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1684.MultiPointContactBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to MultiPointContactBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1684.MultiPointContactBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_needle_roller_bearing(self) -> '_1685.NeedleRollerBearing':
        '''NeedleRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1685.NeedleRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to NeedleRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1685.NeedleRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_non_barrel_roller_bearing(self) -> '_1686.NonBarrelRollerBearing':
        '''NonBarrelRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1686.NonBarrelRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to NonBarrelRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1686.NonBarrelRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_roller_bearing(self) -> '_1687.RollerBearing':
        '''RollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1687.RollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to RollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1687.RollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_rolling_bearing(self) -> '_1690.RollingBearing':
        '''RollingBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1690.RollingBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to RollingBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1690.RollingBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_self_aligning_ball_bearing(self) -> '_1691.SelfAligningBallBearing':
        '''SelfAligningBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1691.SelfAligningBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to SelfAligningBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1691.SelfAligningBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_spherical_roller_bearing(self) -> '_1693.SphericalRollerBearing':
        '''SphericalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1693.SphericalRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to SphericalRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1693.SphericalRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_spherical_roller_thrust_bearing(self) -> '_1694.SphericalRollerThrustBearing':
        '''SphericalRollerThrustBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1694.SphericalRollerThrustBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to SphericalRollerThrustBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1694.SphericalRollerThrustBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_taper_roller_bearing(self) -> '_1695.TaperRollerBearing':
        '''TaperRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1695.TaperRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to TaperRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1695.TaperRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_three_point_contact_ball_bearing(self) -> '_1696.ThreePointContactBallBearing':
        '''ThreePointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1696.ThreePointContactBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to ThreePointContactBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1696.ThreePointContactBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_thrust_ball_bearing(self) -> '_1697.ThrustBallBearing':
        '''ThrustBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1697.ThrustBallBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to ThrustBallBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1697.ThrustBallBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_toroidal_roller_bearing(self) -> '_1698.ToroidalRollerBearing':
        '''ToroidalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1698.ToroidalRollerBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to ToroidalRollerBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1698.ToroidalRollerBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_pad_fluid_film_bearing(self) -> '_1711.PadFluidFilmBearing':
        '''PadFluidFilmBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1711.PadFluidFilmBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to PadFluidFilmBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1711.PadFluidFilmBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_plain_grease_filled_journal_bearing(self) -> '_1713.PlainGreaseFilledJournalBearing':
        '''PlainGreaseFilledJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1713.PlainGreaseFilledJournalBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainGreaseFilledJournalBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1713.PlainGreaseFilledJournalBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_plain_journal_bearing(self) -> '_1715.PlainJournalBearing':
        '''PlainJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1715.PlainJournalBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainJournalBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1715.PlainJournalBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_plain_oil_fed_journal_bearing(self) -> '_1717.PlainOilFedJournalBearing':
        '''PlainOilFedJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1717.PlainOilFedJournalBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainOilFedJournalBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1717.PlainOilFedJournalBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_tilting_pad_journal_bearing(self) -> '_1718.TiltingPadJournalBearing':
        '''TiltingPadJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1718.TiltingPadJournalBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to TiltingPadJournalBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1718.TiltingPadJournalBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_tilting_pad_thrust_bearing(self) -> '_1719.TiltingPadThrustBearing':
        '''TiltingPadThrustBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1719.TiltingPadThrustBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to TiltingPadThrustBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1719.TiltingPadThrustBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_concept_axial_clearance_bearing(self) -> '_1721.ConceptAxialClearanceBearing':
        '''ConceptAxialClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1721.ConceptAxialClearanceBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptAxialClearanceBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1721.ConceptAxialClearanceBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_concept_clearance_bearing(self) -> '_1722.ConceptClearanceBearing':
        '''ConceptClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1722.ConceptClearanceBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptClearanceBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1722.ConceptClearanceBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def detail_of_type_concept_radial_clearance_bearing(self) -> '_1723.ConceptRadialClearanceBearing':
        '''ConceptRadialClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1723.ConceptRadialClearanceBearing.TYPE not in self.wrapped.Detail.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptRadialClearanceBearing. Expected: {}.'.format(self.wrapped.Detail.__class__.__qualname__))

        return constructor.new(_1723.ConceptRadialClearanceBearing)(self.wrapped.Detail) if self.wrapped.Detail else None

    @property
    def overridden_lubrication_detail(self) -> '_261.LubricationDetail':
        '''LubricationDetail: 'OverriddenLubricationDetail' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_261.LubricationDetail)(self.wrapped.OverriddenLubricationDetail) if self.wrapped.OverriddenLubricationDetail else None

    @property
    def friction_coefficients(self) -> '_1638.RollingBearingFrictionCoefficients':
        '''RollingBearingFrictionCoefficients: 'FrictionCoefficients' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1638.RollingBearingFrictionCoefficients)(self.wrapped.FrictionCoefficients) if self.wrapped.FrictionCoefficients else None

    @property
    def mounting(self) -> 'List[_2011.BearingRaceMountingOptions]':
        '''List[BearingRaceMountingOptions]: 'Mounting' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Mounting, constructor.new(_2011.BearingRaceMountingOptions))
        return value

    def set_detail_from_catalogue(self, catalogue: '_1461.BearingCatalog', designation: 'str'):
        ''' 'SetDetailFromCatalogue' is the original name of this method.

        Args:
            catalogue (mastapy.bearings.BearingCatalog)
            designation (str)
        '''

        catalogue = conversion.mp_to_pn_enum(catalogue)
        designation = str(designation)
        self.wrapped.SetDetailFromCatalogue(catalogue, designation if designation else None)

    def try_attach_left_side_to(self, shaft: '_1877.Shaft', offset: Optional['float'] = float('nan')) -> '_2012.ComponentsConnectedResult':
        ''' 'TryAttachLeftSideTo' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        '''

        offset = float(offset)
        method_result = self.wrapped.TryAttachLeftSideTo(shaft.wrapped if shaft else None, offset if offset else 0.0)
        return constructor.new(_2012.ComponentsConnectedResult)(method_result) if method_result else None

    def try_attach_right_side_to(self, shaft: '_1877.Shaft', offset: Optional['float'] = float('nan')) -> '_2012.ComponentsConnectedResult':
        ''' 'TryAttachRightSideTo' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        '''

        offset = float(offset)
        method_result = self.wrapped.TryAttachRightSideTo(shaft.wrapped if shaft else None, offset if offset else 0.0)
        return constructor.new(_2012.ComponentsConnectedResult)(method_result) if method_result else None
