'''_1721.py

Design
'''


from typing import (
    List, Callable, Optional, TypeVar
)
from os import path

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy.utility_gui import _1451
from mastapy import _4, _6318, _1
from mastapy._internal.python_net import python_net_import
from mastapy.materials.efficiency import _237
from mastapy._internal.implicit import enum_with_selected_value, overridable, list_with_selected_item
from mastapy.system_model.part_model import (
    _1939, _1937, _1938, _1933,
    _1906, _1907, _1908, _1910,
    _1912, _1913, _1914, _1917,
    _1918, _1921, _1922, _1923,
    _1926, _1928, _1929, _1930,
    _1931, _1934, _1936, _1940,
    _1941, _1942
)
from mastapy.gears import _254, _260
from mastapy.gears.materials import _504
from mastapy.utility import _1241, _1240, _1239
from mastapy.system_model import _1740, _1739
from mastapy.shafts import _35
from mastapy.detailed_rigid_connectors.splines import _1086
from mastapy._internal.vector_3d import Vector3D
from mastapy.system_model.part_model.gears import (
    _1974, _1995, _1975, _1976,
    _1977, _1978, _1979, _1980,
    _1981, _1982, _1983, _1984,
    _1985, _1986, _1987, _1988,
    _1989, _1990, _1991, _1992,
    _1994, _1996, _1997, _1998,
    _1999, _2000, _2001, _2002,
    _2003, _2004, _2005, _2006,
    _2007, _2008, _2009, _2010,
    _2011, _2012, _2013, _2014,
    _2015, _2016
)
from mastapy.system_model.imported_fes import _1841
from mastapy.bearings.bearing_results.rolling import _1547
from mastapy.system_model.part_model.configurations import _2068, _2066, _2069
from mastapy.system_model.analyses_and_results.load_case_groups import _5085, _5086
from mastapy.system_model.analyses_and_results.static_loads import _6008
from mastapy.utility.model_validation import _1412
from mastapy.system_model.database_access import _1760
from mastapy.system_model.analyses_and_results.synchroniser_analysis import _2392
from mastapy.system_model.part_model.shaft_model import _1945
from mastapy.system_model.part_model.couplings import (
    _2034, _2036, _2037, _2039,
    _2040, _2041, _2042, _2043,
    _2044, _2045, _2051, _2052,
    _2053, _2054, _2055, _2056,
    _2058, _2059, _2060, _2061,
    _2062, _2064
)
from mastapy.system_model.part_model.creation_options import (
    _2030, _2032, _2033, _2031
)
from mastapy.gears.gear_designs.creation_options import _992, _995
from mastapy.nodal_analysis import _72
from mastapy.bearings.bearing_designs.rolling import _1687

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_DESIGN = python_net_import('SMT.MastaAPI.SystemModel', 'Design')


__docformat__ = 'restructuredtext en'
__all__ = ('Design',)


class Design(_1.APIBase):
    '''Design

    This is a mastapy class.
    '''

    TYPE = _DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Design.TYPE' = None):
        super().__init__(instance_to_wrap if instance_to_wrap else Design.TYPE())

    @staticmethod
    def available_examples() -> 'List[str]':
        '''List[str]: 'AvailableExamples' is the original name of this method.'''

        value = conversion.pn_to_mp_objects_in_list(Design.TYPE.AvailableExamples, str)
        return value

    @property
    def masta_gui(self) -> '_1451.MASTAGUI':
        '''MASTAGUI: 'MastaGUI' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1451.MASTAGUI)(self.wrapped.MastaGUI) if self.wrapped.MastaGUI else None

    @property
    def masta_settings(self) -> '_4.MastaSettings':
        '''MastaSettings: 'MastaSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_4.MastaSettings)(self.wrapped.MastaSettings) if self.wrapped.MastaSettings else None

    @property
    def change_gears_to_clones_where_suitable(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ChangeGearsToClonesWhereSuitable' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ChangeGearsToClonesWhereSuitable

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self) -> 'str':
        '''str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase' is the original name of this property.'''

        return self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SelectedItemName

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_external_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshesDatabase.SetSelectedItem(str(value) if value else None)

    @property
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self) -> 'str':
        '''str: 'ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase' is the original name of this property.'''

        return self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SelectedItemName

    @iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database.setter
    def iso14179_part_1_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes_database(self, value: 'str'):
        self.wrapped.ISO14179Part1CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshesDatabase.SetSelectedItem(str(value) if value else None)

    @property
    def coefficient_of_friction(self) -> 'float':
        '''float: 'CoefficientOfFriction' is the original name of this property.'''

        return self.wrapped.CoefficientOfFriction

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'float'):
        self.wrapped.CoefficientOfFriction = float(value) if value else 0.0

    @property
    def efficiency_rating_method_for_bearings(self) -> '_237.EfficiencyRatingMethod':
        '''EfficiencyRatingMethod: 'EfficiencyRatingMethodForBearings' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.EfficiencyRatingMethodForBearings)
        return constructor.new(_237.EfficiencyRatingMethod)(value) if value else None

    @efficiency_rating_method_for_bearings.setter
    def efficiency_rating_method_for_bearings(self, value: '_237.EfficiencyRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EfficiencyRatingMethodForBearings = value

    @property
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing':
        '''enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing: 'ShaftDiameterModificationDueToRollingBearingRings' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.ShaftDiameterModificationDueToRollingBearingRings, value) if self.wrapped.ShaftDiameterModificationDueToRollingBearingRings else None

    @shaft_diameter_modification_due_to_rolling_bearing_rings.setter
    def shaft_diameter_modification_due_to_rolling_bearing_rings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.ShaftDiameterModificationDueToRollingBearingRings = value

    @property
    def manufacturer(self) -> 'str':
        '''str: 'Manufacturer' is the original name of this property.'''

        return self.wrapped.Manufacturer

    @manufacturer.setter
    def manufacturer(self, value: 'str'):
        self.wrapped.Manufacturer = str(value) if value else None

    @property
    def housing_material_for_grounded_connections(self) -> 'str':
        '''str: 'HousingMaterialForGroundedConnections' is the original name of this property.'''

        return self.wrapped.HousingMaterialForGroundedConnections.SelectedItemName

    @housing_material_for_grounded_connections.setter
    def housing_material_for_grounded_connections(self, value: 'str'):
        self.wrapped.HousingMaterialForGroundedConnections.SetSelectedItem(str(value) if value else None)

    @property
    def comment(self) -> 'str':
        '''str: 'Comment' is the original name of this property.'''

        return self.wrapped.Comment

    @comment.setter
    def comment(self, value: 'str'):
        self.wrapped.Comment = str(value) if value else None

    @property
    def node_size(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'NodeSize' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.NodeSize) if self.wrapped.NodeSize else None

    @node_size.setter
    def node_size(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.NodeSize = value

    @property
    def use_expanded_2d_projection_mode(self) -> 'bool':
        '''bool: 'UseExpanded2DProjectionMode' is the original name of this property.'''

        return self.wrapped.UseExpanded2DProjectionMode

    @use_expanded_2d_projection_mode.setter
    def use_expanded_2d_projection_mode(self, value: 'bool'):
        self.wrapped.UseExpanded2DProjectionMode = bool(value) if value else False

    @property
    def gravity_magnitude(self) -> 'float':
        '''float: 'GravityMagnitude' is the original name of this property.'''

        return self.wrapped.GravityMagnitude

    @gravity_magnitude.setter
    def gravity_magnitude(self, value: 'float'):
        self.wrapped.GravityMagnitude = float(value) if value else 0.0

    @property
    def input_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        '''list_with_selected_item.ListWithSelectedItem_PowerLoad: 'InputPowerLoad' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_PowerLoad)(self.wrapped.InputPowerLoad) if self.wrapped.InputPowerLoad else None

    @input_power_load.setter
    def input_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.InputPowerLoad = value

    @property
    def output_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        '''list_with_selected_item.ListWithSelectedItem_PowerLoad: 'OutputPowerLoad' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_PowerLoad)(self.wrapped.OutputPowerLoad) if self.wrapped.OutputPowerLoad else None

    @output_power_load.setter
    def output_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.OutputPowerLoad = value

    @property
    def design_name(self) -> 'str':
        '''str: 'DesignName' is the original name of this property.'''

        return self.wrapped.DesignName

    @design_name.setter
    def design_name(self, value: 'str'):
        self.wrapped.DesignName = str(value) if value else None

    @property
    def file_name(self) -> 'str':
        '''str: 'FileName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FileName

    @property
    def clear_undo_redo_stacks(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'ClearUndoRedoStacks' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ClearUndoRedoStacks

    @property
    def gear_set_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'GearSetConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.GearSetConfiguration) if self.wrapped.GearSetConfiguration else None

    @gear_set_configuration.setter
    def gear_set_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else None)
        self.wrapped.GearSetConfiguration = value

    @property
    def number_of_gear_set_configurations(self) -> 'int':
        '''int: 'NumberOfGearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfGearSetConfigurations

    @property
    def delete_all_inactive_gear_set_designs(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteAllInactiveGearSetDesigns' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteAllInactiveGearSetDesigns

    @property
    def add_gear_set_configuration(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddGearSetConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddGearSetConfiguration

    @property
    def delete_multiple_gear_set_configurations(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteMultipleGearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteMultipleGearSetConfigurations

    @property
    def shaft_detail_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'ShaftDetailConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.ShaftDetailConfiguration) if self.wrapped.ShaftDetailConfiguration else None

    @shaft_detail_configuration.setter
    def shaft_detail_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else None)
        self.wrapped.ShaftDetailConfiguration = value

    @property
    def imported_fe_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'ImportedFEConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.ImportedFEConfiguration) if self.wrapped.ImportedFEConfiguration else None

    @imported_fe_configuration.setter
    def imported_fe_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else None)
        self.wrapped.ImportedFEConfiguration = value

    @property
    def bearing_configuration(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        '''list_with_selected_item.ListWithSelectedItem_str: 'BearingConfiguration' is the original name of this property.'''

        return constructor.new(list_with_selected_item.ListWithSelectedItem_str)(self.wrapped.BearingConfiguration) if self.wrapped.BearingConfiguration else None

    @bearing_configuration.setter
    def bearing_configuration(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.TYPE
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else None)
        self.wrapped.BearingConfiguration = value

    @property
    def add_shaft_detail_configuration(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddShaftDetailConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddShaftDetailConfiguration

    @property
    def delete_multiple_shaft_detail_configurations(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteMultipleShaftDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteMultipleShaftDetailConfigurations

    @property
    def add_bearing_detail_configuration_all_bearings(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddBearingDetailConfigurationAllBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddBearingDetailConfigurationAllBearings

    @property
    def add_bearing_detail_configuration_rolling_bearings(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddBearingDetailConfigurationRollingBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddBearingDetailConfigurationRollingBearings

    @property
    def delete_multiple_bearing_detail_configurations(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteMultipleBearingDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteMultipleBearingDetailConfigurations

    @property
    def add_imported_fe_configuration(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'AddImportedFEConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AddImportedFEConfiguration

    @property
    def delete_multiple_imported_fe_configurations(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteMultipleImportedFEConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteMultipleImportedFEConfigurations

    @property
    def delete_all_gear_set_configurations_that_have_errors_or_warnings(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteAllGearSetConfigurationsThatHaveErrorsOrWarnings

    @property
    def delete_all_gear_sets_designs_that_are_not_used_in_configurations(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DeleteAllGearSetsDesignsThatAreNotUsedInConfigurations

    @property
    def safety_factor_of_maximum_axial_contact_ratio(self) -> 'float':
        '''float: 'SafetyFactorOfMaximumAxialContactRatio' is the original name of this property.'''

        return self.wrapped.SafetyFactorOfMaximumAxialContactRatio

    @safety_factor_of_maximum_axial_contact_ratio.setter
    def safety_factor_of_maximum_axial_contact_ratio(self, value: 'float'):
        self.wrapped.SafetyFactorOfMaximumAxialContactRatio = float(value) if value else 0.0

    @property
    def safety_factor_of_maximum_transverse_contact_ratio(self) -> 'float':
        '''float: 'SafetyFactorOfMaximumTransverseContactRatio' is the original name of this property.'''

        return self.wrapped.SafetyFactorOfMaximumTransverseContactRatio

    @safety_factor_of_maximum_transverse_contact_ratio.setter
    def safety_factor_of_maximum_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.SafetyFactorOfMaximumTransverseContactRatio = float(value) if value else 0.0

    @property
    def transverse_contact_ratio_requirement(self) -> '_254.ContactRatioRequirements':
        '''ContactRatioRequirements: 'TransverseContactRatioRequirement' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.TransverseContactRatioRequirement)
        return constructor.new(_254.ContactRatioRequirements)(value) if value else None

    @transverse_contact_ratio_requirement.setter
    def transverse_contact_ratio_requirement(self, value: '_254.ContactRatioRequirements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.TransverseContactRatioRequirement = value

    @property
    def axial_contact_ratio_requirement(self) -> '_254.ContactRatioRequirements':
        '''ContactRatioRequirements: 'AxialContactRatioRequirement' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.AxialContactRatioRequirement)
        return constructor.new(_254.ContactRatioRequirements)(value) if value else None

    @axial_contact_ratio_requirement.setter
    def axial_contact_ratio_requirement(self, value: '_254.ContactRatioRequirements'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AxialContactRatioRequirement = value

    @property
    def maximum_acceptable_axial_contact_ratio(self) -> 'float':
        '''float: 'MaximumAcceptableAxialContactRatio' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableAxialContactRatio

    @maximum_acceptable_axial_contact_ratio.setter
    def maximum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatio = float(value) if value else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio(self) -> 'float':
        '''float: 'MinimumAcceptableAxialContactRatio' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableAxialContactRatio

    @minimum_acceptable_axial_contact_ratio.setter
    def minimum_acceptable_axial_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatio = float(value) if value else 0.0

    @property
    def maximum_acceptable_axial_contact_ratio_above_integer(self) -> 'float':
        '''float: 'MaximumAcceptableAxialContactRatioAboveInteger' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger

    @maximum_acceptable_axial_contact_ratio_above_integer.setter
    def maximum_acceptable_axial_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableAxialContactRatioAboveInteger = float(value) if value else 0.0

    @property
    def minimum_acceptable_axial_contact_ratio_below_integer(self) -> 'float':
        '''float: 'MinimumAcceptableAxialContactRatioBelowInteger' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger

    @minimum_acceptable_axial_contact_ratio_below_integer.setter
    def minimum_acceptable_axial_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableAxialContactRatioBelowInteger = float(value) if value else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio(self) -> 'float':
        '''float: 'MaximumAcceptableTransverseContactRatio' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableTransverseContactRatio

    @maximum_acceptable_transverse_contact_ratio.setter
    def maximum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatio = float(value) if value else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio(self) -> 'float':
        '''float: 'MinimumAcceptableTransverseContactRatio' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableTransverseContactRatio

    @minimum_acceptable_transverse_contact_ratio.setter
    def minimum_acceptable_transverse_contact_ratio(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatio = float(value) if value else 0.0

    @property
    def maximum_acceptable_transverse_contact_ratio_above_integer(self) -> 'float':
        '''float: 'MaximumAcceptableTransverseContactRatioAboveInteger' is the original name of this property.'''

        return self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger

    @maximum_acceptable_transverse_contact_ratio_above_integer.setter
    def maximum_acceptable_transverse_contact_ratio_above_integer(self, value: 'float'):
        self.wrapped.MaximumAcceptableTransverseContactRatioAboveInteger = float(value) if value else 0.0

    @property
    def minimum_acceptable_transverse_contact_ratio_below_integer(self) -> 'float':
        '''float: 'MinimumAcceptableTransverseContactRatioBelowInteger' is the original name of this property.'''

        return self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger

    @minimum_acceptable_transverse_contact_ratio_below_integer.setter
    def minimum_acceptable_transverse_contact_ratio_below_integer(self, value: 'float'):
        self.wrapped.MinimumAcceptableTransverseContactRatioBelowInteger = float(value) if value else 0.0

    @property
    def compare_results_to_previous_masta_version(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CompareResultsToPreviousMASTAVersion' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CompareResultsToPreviousMASTAVersion

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_external_external_meshes(self) -> '_504.ISOTR1417912001CoefficientOfFrictionConstants':
        '''ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_504.ISOTR1417912001CoefficientOfFrictionConstants)(self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes) if self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForExternalExternalMeshes else None

    @property
    def iso14179_coefficient_of_friction_constants_and_exponents_for_internal_external_meshes(self) -> '_504.ISOTR1417912001CoefficientOfFrictionConstants':
        '''ISOTR1417912001CoefficientOfFrictionConstants: 'ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_504.ISOTR1417912001CoefficientOfFrictionConstants)(self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes) if self.wrapped.ISO14179CoefficientOfFrictionConstantsAndExponentsForInternalExternalMeshes else None

    @property
    def file_save_details_most_recent(self) -> '_1241.FileHistoryItem':
        '''FileHistoryItem: 'FileSaveDetailsMostRecent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1241.FileHistoryItem)(self.wrapped.FileSaveDetailsMostRecent) if self.wrapped.FileSaveDetailsMostRecent else None

    @property
    def default_system_temperatures(self) -> '_1740.TransmissionTemperatureSet':
        '''TransmissionTemperatureSet: 'DefaultSystemTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1740.TransmissionTemperatureSet)(self.wrapped.DefaultSystemTemperatures) if self.wrapped.DefaultSystemTemperatures else None

    @property
    def shafts(self) -> '_35.ShaftSafetyFactorSettings':
        '''ShaftSafetyFactorSettings: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_35.ShaftSafetyFactorSettings)(self.wrapped.Shafts) if self.wrapped.Shafts else None

    @property
    def detailed_spline_settings(self) -> '_1086.DetailedSplineJointSettings':
        '''DetailedSplineJointSettings: 'DetailedSplineSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1086.DetailedSplineJointSettings)(self.wrapped.DetailedSplineSettings) if self.wrapped.DetailedSplineSettings else None

    @property
    def gravity_vector_components(self) -> 'Vector3D':
        '''Vector3D: 'GravityVectorComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.GravityVectorComponents)
        return value

    @property
    def gravity_orientation(self) -> 'Vector3D':
        '''Vector3D: 'GravityOrientation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.GravityOrientation)
        return value

    @property
    def file_save_details_all(self) -> '_1240.FileHistory':
        '''FileHistory: 'FileSaveDetailsAll' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1240.FileHistory)(self.wrapped.FileSaveDetailsAll) if self.wrapped.FileSaveDetailsAll else None

    @property
    def gear_set_design_group(self) -> '_260.GearSetDesignGroup':
        '''GearSetDesignGroup: 'GearSetDesignGroup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_260.GearSetDesignGroup)(self.wrapped.GearSetDesignGroup) if self.wrapped.GearSetDesignGroup else None

    @property
    def selected_gear_set_selection_group(self) -> '_1974.ActiveGearSetDesignSelectionGroup':
        '''ActiveGearSetDesignSelectionGroup: 'SelectedGearSetSelectionGroup' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1974.ActiveGearSetDesignSelectionGroup)(self.wrapped.SelectedGearSetSelectionGroup) if self.wrapped.SelectedGearSetSelectionGroup else None

    @property
    def system(self) -> '_1739.SystemReporting':
        '''SystemReporting: 'System' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1739.SystemReporting)(self.wrapped.System) if self.wrapped.System else None

    @property
    def fe_batch_operations(self) -> '_1841.BatchOperations':
        '''BatchOperations: 'FEBatchOperations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1841.BatchOperations)(self.wrapped.FEBatchOperations) if self.wrapped.FEBatchOperations else None

    @property
    def iso14179_settings_per_bearing_type(self) -> 'List[_1547.ISO14179SettingsPerBearingType]':
        '''List[ISO14179SettingsPerBearingType]: 'ISO14179SettingsPerBearingType' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ISO14179SettingsPerBearingType, constructor.new(_1547.ISO14179SettingsPerBearingType))
        return value

    @property
    def gear_set_configurations(self) -> 'List[_1974.ActiveGearSetDesignSelectionGroup]':
        '''List[ActiveGearSetDesignSelectionGroup]: 'GearSetConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearSetConfigurations, constructor.new(_1974.ActiveGearSetDesignSelectionGroup))
        return value

    @property
    def shaft_detail_configurations(self) -> 'List[_2068.ActiveShaftDesignSelectionGroup]':
        '''List[ActiveShaftDesignSelectionGroup]: 'ShaftDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftDetailConfigurations, constructor.new(_2068.ActiveShaftDesignSelectionGroup))
        return value

    @property
    def imported_fe_configurations(self) -> 'List[_2066.ActiveImportedFESelectionGroup]':
        '''List[ActiveImportedFESelectionGroup]: 'ImportedFEConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEConfigurations, constructor.new(_2066.ActiveImportedFESelectionGroup))
        return value

    @property
    def bearing_detail_configurations(self) -> 'List[_2069.BearingDetailConfiguration]':
        '''List[BearingDetailConfiguration]: 'BearingDetailConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BearingDetailConfigurations, constructor.new(_2069.BearingDetailConfiguration))
        return value

    @property
    def design_states(self) -> 'List[_5085.DesignState]':
        '''List[DesignState]: 'DesignStates' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DesignStates, constructor.new(_5085.DesignState))
        return value

    @property
    def static_loads(self) -> 'List[_6008.StaticLoadCase]':
        '''List[StaticLoadCase]: 'StaticLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StaticLoads, constructor.new(_6008.StaticLoadCase))
        return value

    @property
    def duty_cycles(self) -> 'List[_5086.DutyCycle]':
        '''List[DutyCycle]: 'DutyCycles' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DutyCycles, constructor.new(_5086.DutyCycle))
        return value

    @property
    def root_assembly(self) -> '_1938.RootAssembly':
        '''RootAssembly: 'RootAssembly' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1938.RootAssembly)(self.wrapped.RootAssembly) if self.wrapped.RootAssembly else None

    @property
    def gear_set_config(self) -> '_1995.GearSetConfiguration':
        '''GearSetConfiguration: 'GearSetConfig' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1995.GearSetConfiguration)(self.wrapped.GearSetConfig) if self.wrapped.GearSetConfig else None

    @property
    def status(self) -> '_1412.Status':
        '''Status: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1412.Status)(self.wrapped.Status) if self.wrapped.Status else None

    @property
    def databases(self) -> '_1760.Databases':
        '''Databases: 'Databases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1760.Databases)(self.wrapped.Databases) if self.wrapped.Databases else None

    def duty_cycle_named(self, name: 'str') -> '_5086.DutyCycle':
        ''' 'DutyCycleNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        '''

        name = str(name)
        method_result = self.wrapped.DutyCycleNamed(name if name else None)
        return constructor.new(_5086.DutyCycle)(method_result) if method_result else None

    def dispose(self):
        ''' 'Dispose' is the original name of this method.'''

        self.wrapped.Dispose()

    def save(self, file_name: 'str', save_results: 'bool') -> '_1412.Status':
        ''' 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)

        Returns:
            mastapy.utility.model_validation.Status
        '''

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save(file_name if file_name else None, save_results if save_results else False)
        return constructor.new(_1412.Status)(method_result) if method_result else None

    def save_with_progess(self, file_name: 'str', save_results: 'bool', progress: '_6318.TaskProgress') -> '_1412.Status':
        ''' 'Save' is the original name of this method.

        Args:
            file_name (str)
            save_results (bool)
            progress (mastapy.TaskProgress)

        Returns:
            mastapy.utility.model_validation.Status
        '''

        file_name = str(file_name)
        save_results = bool(save_results)
        method_result = self.wrapped.Save(file_name if file_name else None, save_results if save_results else False, progress.wrapped if progress else None)
        return constructor.new(_1412.Status)(method_result) if method_result else None

    def remove_synchroniser_shift(self, shift: '_2392.SynchroniserShift'):
        ''' 'RemoveSynchroniserShift' is the original name of this method.

        Args:
            shift (mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift)
        '''

        self.wrapped.RemoveSynchroniserShift(shift.wrapped if shift else None)

    def add_synchroniser_shift(self, name: 'str') -> '_2392.SynchroniserShift':
        ''' 'AddSynchroniserShift' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        '''

        name = str(name)
        method_result = self.wrapped.AddSynchroniserShift(name if name else None)
        return constructor.new(_2392.SynchroniserShift)(method_result) if method_result else None

    def add_synchroniser_shift_empty(self) -> '_2392.SynchroniserShift':
        ''' 'AddSynchroniserShift' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.synchroniser_analysis.SynchroniserShift
        '''

        method_result = self.wrapped.AddSynchroniserShift()
        return constructor.new(_2392.SynchroniserShift)(method_result) if method_result else None

    def add_design_state(self, name: Optional['str'] = 'New Design State') -> '_5085.DesignState':
        ''' 'AddDesignState' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        '''

        name = str(name)
        method_result = self.wrapped.AddDesignState(name if name else None)
        return constructor.new(_5085.DesignState)(method_result) if method_result else None

    def add_duty_cycle(self, name: Optional['str'] = 'New Duty Cycle') -> '_5086.DutyCycle':
        ''' 'AddDutyCycle' is the original name of this method.

        Args:
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DutyCycle
        '''

        name = str(name)
        method_result = self.wrapped.AddDutyCycle(name if name else None)
        return constructor.new(_5086.DutyCycle)(method_result) if method_result else None

    def all_parts(self) -> 'List[_1933.Part]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Part]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1933.Part.TYPE](), constructor.new(_1933.Part))

    def all_parts_of_type_assembly(self) -> 'List[_1906.Assembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Assembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1906.Assembly.TYPE](), constructor.new(_1906.Assembly))

    def all_parts_of_type_abstract_assembly(self) -> 'List[_1907.AbstractAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1907.AbstractAssembly.TYPE](), constructor.new(_1907.AbstractAssembly))

    def all_parts_of_type_abstract_shaft_or_housing(self) -> 'List[_1908.AbstractShaftOrHousing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.AbstractShaftOrHousing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1908.AbstractShaftOrHousing.TYPE](), constructor.new(_1908.AbstractShaftOrHousing))

    def all_parts_of_type_bearing(self) -> 'List[_1910.Bearing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bearing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1910.Bearing.TYPE](), constructor.new(_1910.Bearing))

    def all_parts_of_type_bolt(self) -> 'List[_1912.Bolt]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Bolt]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1912.Bolt.TYPE](), constructor.new(_1912.Bolt))

    def all_parts_of_type_bolted_joint(self) -> 'List[_1913.BoltedJoint]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.BoltedJoint]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1913.BoltedJoint.TYPE](), constructor.new(_1913.BoltedJoint))

    def all_parts_of_type_component(self) -> 'List[_1914.Component]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Component]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1914.Component.TYPE](), constructor.new(_1914.Component))

    def all_parts_of_type_connector(self) -> 'List[_1917.Connector]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Connector]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1917.Connector.TYPE](), constructor.new(_1917.Connector))

    def all_parts_of_type_datum(self) -> 'List[_1918.Datum]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.Datum]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1918.Datum.TYPE](), constructor.new(_1918.Datum))

    def all_parts_of_type_external_cad_model(self) -> 'List[_1921.ExternalCADModel]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ExternalCADModel]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1921.ExternalCADModel.TYPE](), constructor.new(_1921.ExternalCADModel))

    def all_parts_of_type_flexible_pin_assembly(self) -> 'List[_1922.FlexiblePinAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.FlexiblePinAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1922.FlexiblePinAssembly.TYPE](), constructor.new(_1922.FlexiblePinAssembly))

    def all_parts_of_type_guide_dxf_model(self) -> 'List[_1923.GuideDxfModel]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.GuideDxfModel]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1923.GuideDxfModel.TYPE](), constructor.new(_1923.GuideDxfModel))

    def all_parts_of_type_imported_fe_component(self) -> 'List[_1926.ImportedFEComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.ImportedFEComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1926.ImportedFEComponent.TYPE](), constructor.new(_1926.ImportedFEComponent))

    def all_parts_of_type_mass_disc(self) -> 'List[_1928.MassDisc]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MassDisc]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1928.MassDisc.TYPE](), constructor.new(_1928.MassDisc))

    def all_parts_of_type_measurement_component(self) -> 'List[_1929.MeasurementComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MeasurementComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1929.MeasurementComponent.TYPE](), constructor.new(_1929.MeasurementComponent))

    def all_parts_of_type_mountable_component(self) -> 'List[_1930.MountableComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.MountableComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1930.MountableComponent.TYPE](), constructor.new(_1930.MountableComponent))

    def all_parts_of_type_oil_seal(self) -> 'List[_1931.OilSeal]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.OilSeal]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1931.OilSeal.TYPE](), constructor.new(_1931.OilSeal))

    def all_parts_of_type_planet_carrier(self) -> 'List[_1934.PlanetCarrier]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PlanetCarrier]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1934.PlanetCarrier.TYPE](), constructor.new(_1934.PlanetCarrier))

    def all_parts_of_type_point_load(self) -> 'List[_1936.PointLoad]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PointLoad]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1936.PointLoad.TYPE](), constructor.new(_1936.PointLoad))

    def all_parts_of_type_power_load(self) -> 'List[_1937.PowerLoad]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.PowerLoad]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1937.PowerLoad.TYPE](), constructor.new(_1937.PowerLoad))

    def all_parts_of_type_root_assembly(self) -> 'List[_1938.RootAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.RootAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1938.RootAssembly.TYPE](), constructor.new(_1938.RootAssembly))

    def all_parts_of_type_specialised_assembly(self) -> 'List[_1940.SpecialisedAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.SpecialisedAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1940.SpecialisedAssembly.TYPE](), constructor.new(_1940.SpecialisedAssembly))

    def all_parts_of_type_unbalanced_mass(self) -> 'List[_1941.UnbalancedMass]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.UnbalancedMass]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1941.UnbalancedMass.TYPE](), constructor.new(_1941.UnbalancedMass))

    def all_parts_of_type_virtual_component(self) -> 'List[_1942.VirtualComponent]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.VirtualComponent]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1942.VirtualComponent.TYPE](), constructor.new(_1942.VirtualComponent))

    def all_parts_of_type_shaft(self) -> 'List[_1945.Shaft]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.shaft_model.Shaft]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1945.Shaft.TYPE](), constructor.new(_1945.Shaft))

    def all_parts_of_type_agma_gleason_conical_gear(self) -> 'List[_1975.AGMAGleasonConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1975.AGMAGleasonConicalGear.TYPE](), constructor.new(_1975.AGMAGleasonConicalGear))

    def all_parts_of_type_agma_gleason_conical_gear_set(self) -> 'List[_1976.AGMAGleasonConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1976.AGMAGleasonConicalGearSet.TYPE](), constructor.new(_1976.AGMAGleasonConicalGearSet))

    def all_parts_of_type_bevel_differential_gear(self) -> 'List[_1977.BevelDifferentialGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1977.BevelDifferentialGear.TYPE](), constructor.new(_1977.BevelDifferentialGear))

    def all_parts_of_type_bevel_differential_gear_set(self) -> 'List[_1978.BevelDifferentialGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1978.BevelDifferentialGearSet.TYPE](), constructor.new(_1978.BevelDifferentialGearSet))

    def all_parts_of_type_bevel_differential_planet_gear(self) -> 'List[_1979.BevelDifferentialPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1979.BevelDifferentialPlanetGear.TYPE](), constructor.new(_1979.BevelDifferentialPlanetGear))

    def all_parts_of_type_bevel_differential_sun_gear(self) -> 'List[_1980.BevelDifferentialSunGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelDifferentialSunGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1980.BevelDifferentialSunGear.TYPE](), constructor.new(_1980.BevelDifferentialSunGear))

    def all_parts_of_type_bevel_gear(self) -> 'List[_1981.BevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1981.BevelGear.TYPE](), constructor.new(_1981.BevelGear))

    def all_parts_of_type_bevel_gear_set(self) -> 'List[_1982.BevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.BevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1982.BevelGearSet.TYPE](), constructor.new(_1982.BevelGearSet))

    def all_parts_of_type_concept_gear(self) -> 'List[_1983.ConceptGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1983.ConceptGear.TYPE](), constructor.new(_1983.ConceptGear))

    def all_parts_of_type_concept_gear_set(self) -> 'List[_1984.ConceptGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConceptGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1984.ConceptGearSet.TYPE](), constructor.new(_1984.ConceptGearSet))

    def all_parts_of_type_conical_gear(self) -> 'List[_1985.ConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1985.ConicalGear.TYPE](), constructor.new(_1985.ConicalGear))

    def all_parts_of_type_conical_gear_set(self) -> 'List[_1986.ConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1986.ConicalGearSet.TYPE](), constructor.new(_1986.ConicalGearSet))

    def all_parts_of_type_cylindrical_gear(self) -> 'List[_1987.CylindricalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1987.CylindricalGear.TYPE](), constructor.new(_1987.CylindricalGear))

    def all_parts_of_type_cylindrical_gear_set(self) -> 'List[_1988.CylindricalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1988.CylindricalGearSet.TYPE](), constructor.new(_1988.CylindricalGearSet))

    def all_parts_of_type_cylindrical_planet_gear(self) -> 'List[_1989.CylindricalPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.CylindricalPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1989.CylindricalPlanetGear.TYPE](), constructor.new(_1989.CylindricalPlanetGear))

    def all_parts_of_type_face_gear(self) -> 'List[_1990.FaceGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1990.FaceGear.TYPE](), constructor.new(_1990.FaceGear))

    def all_parts_of_type_face_gear_set(self) -> 'List[_1991.FaceGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.FaceGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1991.FaceGearSet.TYPE](), constructor.new(_1991.FaceGearSet))

    def all_parts_of_type_gear(self) -> 'List[_1992.Gear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.Gear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1992.Gear.TYPE](), constructor.new(_1992.Gear))

    def all_parts_of_type_gear_set(self) -> 'List[_1994.GearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.GearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1994.GearSet.TYPE](), constructor.new(_1994.GearSet))

    def all_parts_of_type_hypoid_gear(self) -> 'List[_1996.HypoidGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1996.HypoidGear.TYPE](), constructor.new(_1996.HypoidGear))

    def all_parts_of_type_hypoid_gear_set(self) -> 'List[_1997.HypoidGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.HypoidGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1997.HypoidGearSet.TYPE](), constructor.new(_1997.HypoidGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> 'List[_1998.KlingelnbergCycloPalloidConicalGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1998.KlingelnbergCycloPalloidConicalGear.TYPE](), constructor.new(_1998.KlingelnbergCycloPalloidConicalGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> 'List[_1999.KlingelnbergCycloPalloidConicalGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_1999.KlingelnbergCycloPalloidConicalGearSet.TYPE](), constructor.new(_1999.KlingelnbergCycloPalloidConicalGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> 'List[_2000.KlingelnbergCycloPalloidHypoidGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2000.KlingelnbergCycloPalloidHypoidGear.TYPE](), constructor.new(_2000.KlingelnbergCycloPalloidHypoidGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> 'List[_2001.KlingelnbergCycloPalloidHypoidGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2001.KlingelnbergCycloPalloidHypoidGearSet.TYPE](), constructor.new(_2001.KlingelnbergCycloPalloidHypoidGearSet))

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> 'List[_2002.KlingelnbergCycloPalloidSpiralBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2002.KlingelnbergCycloPalloidSpiralBevelGear.TYPE](), constructor.new(_2002.KlingelnbergCycloPalloidSpiralBevelGear))

    def all_parts_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> 'List[_2003.KlingelnbergCycloPalloidSpiralBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2003.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE](), constructor.new(_2003.KlingelnbergCycloPalloidSpiralBevelGearSet))

    def all_parts_of_type_planetary_gear_set(self) -> 'List[_2004.PlanetaryGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.PlanetaryGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2004.PlanetaryGearSet.TYPE](), constructor.new(_2004.PlanetaryGearSet))

    def all_parts_of_type_spiral_bevel_gear(self) -> 'List[_2005.SpiralBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2005.SpiralBevelGear.TYPE](), constructor.new(_2005.SpiralBevelGear))

    def all_parts_of_type_spiral_bevel_gear_set(self) -> 'List[_2006.SpiralBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.SpiralBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2006.SpiralBevelGearSet.TYPE](), constructor.new(_2006.SpiralBevelGearSet))

    def all_parts_of_type_straight_bevel_diff_gear(self) -> 'List[_2007.StraightBevelDiffGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2007.StraightBevelDiffGear.TYPE](), constructor.new(_2007.StraightBevelDiffGear))

    def all_parts_of_type_straight_bevel_diff_gear_set(self) -> 'List[_2008.StraightBevelDiffGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelDiffGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2008.StraightBevelDiffGearSet.TYPE](), constructor.new(_2008.StraightBevelDiffGearSet))

    def all_parts_of_type_straight_bevel_gear(self) -> 'List[_2009.StraightBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2009.StraightBevelGear.TYPE](), constructor.new(_2009.StraightBevelGear))

    def all_parts_of_type_straight_bevel_gear_set(self) -> 'List[_2010.StraightBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2010.StraightBevelGearSet.TYPE](), constructor.new(_2010.StraightBevelGearSet))

    def all_parts_of_type_straight_bevel_planet_gear(self) -> 'List[_2011.StraightBevelPlanetGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelPlanetGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2011.StraightBevelPlanetGear.TYPE](), constructor.new(_2011.StraightBevelPlanetGear))

    def all_parts_of_type_straight_bevel_sun_gear(self) -> 'List[_2012.StraightBevelSunGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.StraightBevelSunGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2012.StraightBevelSunGear.TYPE](), constructor.new(_2012.StraightBevelSunGear))

    def all_parts_of_type_worm_gear(self) -> 'List[_2013.WormGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2013.WormGear.TYPE](), constructor.new(_2013.WormGear))

    def all_parts_of_type_worm_gear_set(self) -> 'List[_2014.WormGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.WormGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2014.WormGearSet.TYPE](), constructor.new(_2014.WormGearSet))

    def all_parts_of_type_zerol_bevel_gear(self) -> 'List[_2015.ZerolBevelGear]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGear]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2015.ZerolBevelGear.TYPE](), constructor.new(_2015.ZerolBevelGear))

    def all_parts_of_type_zerol_bevel_gear_set(self) -> 'List[_2016.ZerolBevelGearSet]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.gears.ZerolBevelGearSet]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2016.ZerolBevelGearSet.TYPE](), constructor.new(_2016.ZerolBevelGearSet))

    def all_parts_of_type_belt_drive(self) -> 'List[_2034.BeltDrive]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.BeltDrive]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2034.BeltDrive.TYPE](), constructor.new(_2034.BeltDrive))

    def all_parts_of_type_clutch(self) -> 'List[_2036.Clutch]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Clutch]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2036.Clutch.TYPE](), constructor.new(_2036.Clutch))

    def all_parts_of_type_clutch_half(self) -> 'List[_2037.ClutchHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ClutchHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2037.ClutchHalf.TYPE](), constructor.new(_2037.ClutchHalf))

    def all_parts_of_type_concept_coupling(self) -> 'List[_2039.ConceptCoupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCoupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2039.ConceptCoupling.TYPE](), constructor.new(_2039.ConceptCoupling))

    def all_parts_of_type_concept_coupling_half(self) -> 'List[_2040.ConceptCouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ConceptCouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2040.ConceptCouplingHalf.TYPE](), constructor.new(_2040.ConceptCouplingHalf))

    def all_parts_of_type_coupling(self) -> 'List[_2041.Coupling]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Coupling]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2041.Coupling.TYPE](), constructor.new(_2041.Coupling))

    def all_parts_of_type_coupling_half(self) -> 'List[_2042.CouplingHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CouplingHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2042.CouplingHalf.TYPE](), constructor.new(_2042.CouplingHalf))

    def all_parts_of_type_cvt(self) -> 'List[_2043.CVT]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVT]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2043.CVT.TYPE](), constructor.new(_2043.CVT))

    def all_parts_of_type_cvt_pulley(self) -> 'List[_2044.CVTPulley]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.CVTPulley]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2044.CVTPulley.TYPE](), constructor.new(_2044.CVTPulley))

    def all_parts_of_type_pulley(self) -> 'List[_2045.Pulley]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Pulley]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2045.Pulley.TYPE](), constructor.new(_2045.Pulley))

    def all_parts_of_type_rolling_ring(self) -> 'List[_2051.RollingRing]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRing]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2051.RollingRing.TYPE](), constructor.new(_2051.RollingRing))

    def all_parts_of_type_rolling_ring_assembly(self) -> 'List[_2052.RollingRingAssembly]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.RollingRingAssembly]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2052.RollingRingAssembly.TYPE](), constructor.new(_2052.RollingRingAssembly))

    def all_parts_of_type_shaft_hub_connection(self) -> 'List[_2053.ShaftHubConnection]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.ShaftHubConnection]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2053.ShaftHubConnection.TYPE](), constructor.new(_2053.ShaftHubConnection))

    def all_parts_of_type_spring_damper(self) -> 'List[_2054.SpringDamper]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamper]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2054.SpringDamper.TYPE](), constructor.new(_2054.SpringDamper))

    def all_parts_of_type_spring_damper_half(self) -> 'List[_2055.SpringDamperHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SpringDamperHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2055.SpringDamperHalf.TYPE](), constructor.new(_2055.SpringDamperHalf))

    def all_parts_of_type_synchroniser(self) -> 'List[_2056.Synchroniser]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.Synchroniser]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2056.Synchroniser.TYPE](), constructor.new(_2056.Synchroniser))

    def all_parts_of_type_synchroniser_half(self) -> 'List[_2058.SynchroniserHalf]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserHalf]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2058.SynchroniserHalf.TYPE](), constructor.new(_2058.SynchroniserHalf))

    def all_parts_of_type_synchroniser_part(self) -> 'List[_2059.SynchroniserPart]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserPart]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2059.SynchroniserPart.TYPE](), constructor.new(_2059.SynchroniserPart))

    def all_parts_of_type_synchroniser_sleeve(self) -> 'List[_2060.SynchroniserSleeve]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.SynchroniserSleeve]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2060.SynchroniserSleeve.TYPE](), constructor.new(_2060.SynchroniserSleeve))

    def all_parts_of_type_torque_converter(self) -> 'List[_2061.TorqueConverter]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverter]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2061.TorqueConverter.TYPE](), constructor.new(_2061.TorqueConverter))

    def all_parts_of_type_torque_converter_pump(self) -> 'List[_2062.TorqueConverterPump]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterPump]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2062.TorqueConverterPump.TYPE](), constructor.new(_2062.TorqueConverterPump))

    def all_parts_of_type_torque_converter_turbine(self) -> 'List[_2064.TorqueConverterTurbine]':
        ''' 'AllParts' is the original name of this method.

        Returns:
            List[mastapy.system_model.part_model.couplings.TorqueConverterTurbine]
        '''

        return conversion.pn_to_mp_objects_in_list(self.wrapped.AllParts[_2064.TorqueConverterTurbine.TYPE](), constructor.new(_2064.TorqueConverterTurbine))

    @staticmethod
    def load(file_path: 'str', load_full_fe_option: Optional['_1239.ExternalFullFEFileOption'] = _1239.ExternalFullFEFileOption.MESH_AND_EXPANSION_VECTORS) -> 'Design':
        ''' 'Load' is the original name of this method.

        Args:
            file_path (str)
            load_full_fe_option (mastapy.utility.ExternalFullFEFileOption, optional)

        Returns:
            mastapy.system_model.Design
        '''

        file_path = str(file_path)
        file_path = path.abspath(file_path)
        load_full_fe_option = conversion.mp_to_pn_enum(load_full_fe_option)
        method_result = Design.TYPE.Load(file_path if file_path else None, load_full_fe_option)
        return constructor.new(Design)(method_result) if method_result else None

    @staticmethod
    def load_example(example_string: 'str') -> 'Design':
        ''' 'LoadExample' is the original name of this method.

        Args:
            example_string (str)

        Returns:
            mastapy.system_model.Design
        '''

        example_string = str(example_string)
        method_result = Design.TYPE.LoadExample(example_string if example_string else None)
        return constructor.new(Design)(method_result) if method_result else None

    def compare_for_test_only(self, design: 'Design', sb: 'str') -> 'bool':
        ''' 'CompareForTestOnly' is the original name of this method.

        Args:
            design (mastapy.system_model.Design)
            sb (str)

        Returns:
            bool
        '''

        sb = str(sb)
        method_result = self.wrapped.CompareForTestOnly(design.wrapped if design else None, sb if sb else None)
        return method_result

    def new_belt_creation_options(self, centre_distance: Optional['float'] = 0.1, pulley_a_diameter: Optional['float'] = 0.1, pulley_b_diameter: Optional['float'] = 0.1, name: Optional['str'] = 'Belt Drive') -> '_2030.BeltCreationOptions':
        ''' 'NewBeltCreationOptions' is the original name of this method.

        Args:
            centre_distance (float, optional)
            pulley_a_diameter (float, optional)
            pulley_b_diameter (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.BeltCreationOptions
        '''

        centre_distance = float(centre_distance)
        pulley_a_diameter = float(pulley_a_diameter)
        pulley_b_diameter = float(pulley_b_diameter)
        name = str(name)
        method_result = self.wrapped.NewBeltCreationOptions(centre_distance if centre_distance else 0.0, pulley_a_diameter if pulley_a_diameter else 0.0, pulley_b_diameter if pulley_b_diameter else 0.0, name if name else None)
        return constructor.new(_2030.BeltCreationOptions)(method_result) if method_result else None

    def new_planet_carrier_creation_options(self, number_of_planets: Optional['int'] = 3, diameter: Optional['float'] = 0.1) -> '_2032.PlanetCarrierCreationOptions':
        ''' 'NewPlanetCarrierCreationOptions' is the original name of this method.

        Args:
            number_of_planets (int, optional)
            diameter (float, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.PlanetCarrierCreationOptions
        '''

        number_of_planets = int(number_of_planets)
        diameter = float(diameter)
        method_result = self.wrapped.NewPlanetCarrierCreationOptions(number_of_planets if number_of_planets else 0, diameter if diameter else 0.0)
        return constructor.new(_2032.PlanetCarrierCreationOptions)(method_result) if method_result else None

    def new_shaft_creation_options(self, length: Optional['float'] = 0.1, outer_diameter: Optional['float'] = 0.0, bore: Optional['float'] = 0.0, name: Optional['str'] = 'Shaft') -> '_2033.ShaftCreationOptions':
        ''' 'NewShaftCreationOptions' is the original name of this method.

        Args:
            length (float, optional)
            outer_diameter (float, optional)
            bore (float, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.ShaftCreationOptions
        '''

        length = float(length)
        outer_diameter = float(outer_diameter)
        bore = float(bore)
        name = str(name)
        method_result = self.wrapped.NewShaftCreationOptions(length if length else 0.0, outer_diameter if outer_diameter else 0.0, bore if bore else 0.0, name if name else None)
        return constructor.new(_2033.ShaftCreationOptions)(method_result) if method_result else None

    def new_cylindrical_gear_pair_creation_options(self) -> '_992.CylindricalGearPairCreationOptions':
        ''' 'NewCylindricalGearPairCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.CylindricalGearPairCreationOptions
        '''

        method_result = self.wrapped.NewCylindricalGearPairCreationOptions()
        return constructor.new(_992.CylindricalGearPairCreationOptions)(method_result) if method_result else None

    def new_cylindrical_gear_linear_train_creation_options(self, number_of_gears: Optional['int'] = 3, name: Optional['str'] = 'Gear Train') -> '_2031.CylindricalGearLinearTrainCreationOptions':
        ''' 'NewCylindricalGearLinearTrainCreationOptions' is the original name of this method.

        Args:
            number_of_gears (int, optional)
            name (str, optional)

        Returns:
            mastapy.system_model.part_model.creation_options.CylindricalGearLinearTrainCreationOptions
        '''

        number_of_gears = int(number_of_gears)
        name = str(name)
        method_result = self.wrapped.NewCylindricalGearLinearTrainCreationOptions(number_of_gears if number_of_gears else 0, name if name else None)
        return constructor.new(_2031.CylindricalGearLinearTrainCreationOptions)(method_result) if method_result else None

    def new_spiral_bevel_gear_set_creation_options(self) -> '_995.SpiralBevelGearSetCreationOptions':
        ''' 'NewSpiralBevelGearSetCreationOptions' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.creation_options.SpiralBevelGearSetCreationOptions
        '''

        method_result = self.wrapped.NewSpiralBevelGearSetCreationOptions()
        return constructor.new(_995.SpiralBevelGearSetCreationOptions)(method_result) if method_result else None

    def new_nodal_matrix(self, dense_matrix: 'List[List[float]]') -> '_72.NodalMatrix':
        ''' 'NewNodalMatrix' is the original name of this method.

        Args:
            dense_matrix (List[List[float]])

        Returns:
            mastapy.nodal_analysis.NodalMatrix
        '''

        dense_matrix = conversion.mp_to_pn_list_float_2d(dense_matrix)
        method_result = self.wrapped.NewNodalMatrix(dense_matrix)
        return constructor.new(_72.NodalMatrix)(method_result) if method_result else None

    def clear_design(self):
        ''' 'ClearDesign' is the original name of this method.'''

        self.wrapped.ClearDesign()

    def remove_bearing_from_database(self, rolling_bearing: '_1687.RollingBearing'):
        ''' 'RemoveBearingFromDatabase' is the original name of this method.

        Args:
            rolling_bearing (mastapy.bearings.bearing_designs.rolling.RollingBearing)
        '''

        self.wrapped.RemoveBearingFromDatabase(rolling_bearing.wrapped if rolling_bearing else None)

    def __copy__(self) -> 'Design':
        ''' 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        '''

        method_result = self.wrapped.Copy()
        return constructor.new(Design)(method_result) if method_result else None

    def __deepcopy__(self, memo) -> 'Design':
        ''' 'Copy' is the original name of this method.

        Returns:
            mastapy.system_model.Design
        '''

        method_result = self.wrapped.Copy()
        return constructor.new(Design)(method_result) if method_result else None

    def design_state_named(self, name: 'str') -> '_5085.DesignState':
        ''' 'DesignStateNamed' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.system_model.analyses_and_results.load_case_groups.DesignState
        '''

        name = str(name)
        method_result = self.wrapped.DesignStateNamed(name if name else None)
        return constructor.new(_5085.DesignState)(method_result) if method_result else None

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.dispose()
