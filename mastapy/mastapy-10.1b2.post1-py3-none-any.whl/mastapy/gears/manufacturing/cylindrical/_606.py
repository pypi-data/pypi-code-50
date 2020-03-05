'''_606.py

CylindricalGearManufacturingConfig
'''


from typing import Callable

from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.gears.manufacturing.cylindrical import _622, _621, _605
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _696, _697, _698, _635,
    _699, _700, _701
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _702, _508
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
    _703, _704, _705, _706
)
from mastapy.gears.manufacturing.cylindrical.process_simulation import _646, _647, _648
from mastapy.gears.analysis import _707

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalGearManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearManufacturingConfig',)


class CylindricalGearManufacturingConfig(_707.GearImplementationDetail):
    '''CylindricalGearManufacturingConfig

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_MANUFACTURING_CONFIG
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def roughing_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods':
        '''enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods: 'RoughingMethod' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods)(self.wrapped.RoughingMethod) if self.wrapped.RoughingMethod else None

    @roughing_method.setter
    def roughing_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.RoughingMethod = value

    @property
    def finishing_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods':
        '''enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods: 'FinishingMethod' is the original name of this property.'''

        return constructor.new(enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods)(self.wrapped.FinishingMethod) if self.wrapped.FinishingMethod else None

    @finishing_method.setter
    def finishing_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.TYPE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.FinishingMethod = value

    @property
    def rough_cutter_database_selector(self) -> 'str':
        '''str: 'RoughCutterDatabaseSelector' is the original name of this property.'''

        return self.wrapped.RoughCutterDatabaseSelector.SelectedItemName

    @rough_cutter_database_selector.setter
    def rough_cutter_database_selector(self, value: 'str'):
        self.wrapped.RoughCutterDatabaseSelector.SetSelectedItem(str(value) if value else None)

    @property
    def finish_cutter_database_selector(self) -> 'str':
        '''str: 'FinishCutterDatabaseSelector' is the original name of this property.'''

        return self.wrapped.FinishCutterDatabaseSelector.SelectedItemName

    @finish_cutter_database_selector.setter
    def finish_cutter_database_selector(self, value: 'str'):
        self.wrapped.FinishCutterDatabaseSelector.SetSelectedItem(str(value) if value else None)

    @property
    def create_new_rough_cutter_compatible_with_gear_in_design_mode(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CreateNewRoughCutterCompatibleWithGearInDesignMode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CreateNewRoughCutterCompatibleWithGearInDesignMode

    @property
    def create_new_finish_cutter_compatible_with_gear_in_design_mode(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CreateNewFinishCutterCompatibleWithGearInDesignMode' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CreateNewFinishCutterCompatibleWithGearInDesignMode

    @property
    def minimum_finish_cutter_gear_root_clearance_factor(self) -> 'float':
        '''float: 'MinimumFinishCutterGearRootClearanceFactor' is the original name of this property.'''

        return self.wrapped.MinimumFinishCutterGearRootClearanceFactor

    @minimum_finish_cutter_gear_root_clearance_factor.setter
    def minimum_finish_cutter_gear_root_clearance_factor(self, value: 'float'):
        self.wrapped.MinimumFinishCutterGearRootClearanceFactor = float(value) if value else 0.0

    @property
    def number_of_points_for_reporting_main_profile_finish_stock(self) -> 'overridable.Overridable_int':
        '''overridable.Overridable_int: 'NumberOfPointsForReportingMainProfileFinishStock' is the original name of this property.'''

        return constructor.new(overridable.Overridable_int)(self.wrapped.NumberOfPointsForReportingMainProfileFinishStock) if self.wrapped.NumberOfPointsForReportingMainProfileFinishStock else None

    @number_of_points_for_reporting_main_profile_finish_stock.setter
    def number_of_points_for_reporting_main_profile_finish_stock(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.TYPE
        enclosed_type = overridable.Overridable_int.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0)
        self.wrapped.NumberOfPointsForReportingMainProfileFinishStock = value

    @property
    def rough_cutter(self) -> '_696.CylindricalGearRealCutterDesign':
        '''CylindricalGearRealCutterDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_696.CylindricalGearRealCutterDesign)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def rough_cutter_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_697.CylindricalGearFormGrindingWheel':
        '''CylindricalGearFormGrindingWheel: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutter.__class__.__qualname__ != 'CylindricalGearFormGrindingWheel':
            raise CastException('Failed to cast rough_cutter to CylindricalGearFormGrindingWheel. Expected: {}.'.format(self.wrapped.RoughCutter.__class__.__qualname__))

        return constructor.new(_697.CylindricalGearFormGrindingWheel)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def rough_cutter_of_type_cylindrical_gear_grinding_worm(self) -> '_698.CylindricalGearGrindingWorm':
        '''CylindricalGearGrindingWorm: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutter.__class__.__qualname__ != 'CylindricalGearGrindingWorm':
            raise CastException('Failed to cast rough_cutter to CylindricalGearGrindingWorm. Expected: {}.'.format(self.wrapped.RoughCutter.__class__.__qualname__))

        return constructor.new(_698.CylindricalGearGrindingWorm)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def rough_cutter_of_type_cylindrical_gear_hob_design(self) -> '_635.CylindricalGearHobDesign':
        '''CylindricalGearHobDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutter.__class__.__qualname__ != 'CylindricalGearHobDesign':
            raise CastException('Failed to cast rough_cutter to CylindricalGearHobDesign. Expected: {}.'.format(self.wrapped.RoughCutter.__class__.__qualname__))

        return constructor.new(_635.CylindricalGearHobDesign)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def rough_cutter_of_type_cylindrical_gear_plunge_shaver(self) -> '_699.CylindricalGearPlungeShaver':
        '''CylindricalGearPlungeShaver: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutter.__class__.__qualname__ != 'CylindricalGearPlungeShaver':
            raise CastException('Failed to cast rough_cutter to CylindricalGearPlungeShaver. Expected: {}.'.format(self.wrapped.RoughCutter.__class__.__qualname__))

        return constructor.new(_699.CylindricalGearPlungeShaver)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def rough_cutter_of_type_cylindrical_gear_shaper(self) -> '_700.CylindricalGearShaper':
        '''CylindricalGearShaper: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutter.__class__.__qualname__ != 'CylindricalGearShaper':
            raise CastException('Failed to cast rough_cutter to CylindricalGearShaper. Expected: {}.'.format(self.wrapped.RoughCutter.__class__.__qualname__))

        return constructor.new(_700.CylindricalGearShaper)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def rough_cutter_of_type_cylindrical_gear_shaver(self) -> '_701.CylindricalGearShaver':
        '''CylindricalGearShaver: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutter.__class__.__qualname__ != 'CylindricalGearShaver':
            raise CastException('Failed to cast rough_cutter to CylindricalGearShaver. Expected: {}.'.format(self.wrapped.RoughCutter.__class__.__qualname__))

        return constructor.new(_701.CylindricalGearShaver)(self.wrapped.RoughCutter) if self.wrapped.RoughCutter else None

    @property
    def finish_cutter(self) -> '_696.CylindricalGearRealCutterDesign':
        '''CylindricalGearRealCutterDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_696.CylindricalGearRealCutterDesign)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_cutter_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_697.CylindricalGearFormGrindingWheel':
        '''CylindricalGearFormGrindingWheel: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutter.__class__.__qualname__ != 'CylindricalGearFormGrindingWheel':
            raise CastException('Failed to cast finish_cutter to CylindricalGearFormGrindingWheel. Expected: {}.'.format(self.wrapped.FinishCutter.__class__.__qualname__))

        return constructor.new(_697.CylindricalGearFormGrindingWheel)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_cutter_of_type_cylindrical_gear_grinding_worm(self) -> '_698.CylindricalGearGrindingWorm':
        '''CylindricalGearGrindingWorm: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutter.__class__.__qualname__ != 'CylindricalGearGrindingWorm':
            raise CastException('Failed to cast finish_cutter to CylindricalGearGrindingWorm. Expected: {}.'.format(self.wrapped.FinishCutter.__class__.__qualname__))

        return constructor.new(_698.CylindricalGearGrindingWorm)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_cutter_of_type_cylindrical_gear_hob_design(self) -> '_635.CylindricalGearHobDesign':
        '''CylindricalGearHobDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutter.__class__.__qualname__ != 'CylindricalGearHobDesign':
            raise CastException('Failed to cast finish_cutter to CylindricalGearHobDesign. Expected: {}.'.format(self.wrapped.FinishCutter.__class__.__qualname__))

        return constructor.new(_635.CylindricalGearHobDesign)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_cutter_of_type_cylindrical_gear_plunge_shaver(self) -> '_699.CylindricalGearPlungeShaver':
        '''CylindricalGearPlungeShaver: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutter.__class__.__qualname__ != 'CylindricalGearPlungeShaver':
            raise CastException('Failed to cast finish_cutter to CylindricalGearPlungeShaver. Expected: {}.'.format(self.wrapped.FinishCutter.__class__.__qualname__))

        return constructor.new(_699.CylindricalGearPlungeShaver)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_cutter_of_type_cylindrical_gear_shaper(self) -> '_700.CylindricalGearShaper':
        '''CylindricalGearShaper: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutter.__class__.__qualname__ != 'CylindricalGearShaper':
            raise CastException('Failed to cast finish_cutter to CylindricalGearShaper. Expected: {}.'.format(self.wrapped.FinishCutter.__class__.__qualname__))

        return constructor.new(_700.CylindricalGearShaper)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_cutter_of_type_cylindrical_gear_shaver(self) -> '_701.CylindricalGearShaver':
        '''CylindricalGearShaver: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutter.__class__.__qualname__ != 'CylindricalGearShaver':
            raise CastException('Failed to cast finish_cutter to CylindricalGearShaver. Expected: {}.'.format(self.wrapped.FinishCutter.__class__.__qualname__))

        return constructor.new(_701.CylindricalGearShaver)(self.wrapped.FinishCutter) if self.wrapped.FinishCutter else None

    @property
    def finish_stock_specification(self) -> '_702.FinishStockSpecification':
        '''FinishStockSpecification: 'FinishStockSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_702.FinishStockSpecification)(self.wrapped.FinishStockSpecification) if self.wrapped.FinishStockSpecification else None

    @property
    def rough_cutter_simulation(self) -> '_703.GearCutterSimulation':
        '''GearCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_703.GearCutterSimulation)(self.wrapped.RoughCutterSimulation) if self.wrapped.RoughCutterSimulation else None

    @property
    def rough_cutter_simulation_of_type_finish_cutter_simulation(self) -> '_704.FinishCutterSimulation':
        '''FinishCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutterSimulation.__class__.__qualname__ != 'FinishCutterSimulation':
            raise CastException('Failed to cast rough_cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(self.wrapped.RoughCutterSimulation.__class__.__qualname__))

        return constructor.new(_704.FinishCutterSimulation)(self.wrapped.RoughCutterSimulation) if self.wrapped.RoughCutterSimulation else None

    @property
    def rough_cutter_simulation_of_type_rough_cutter_simulation(self) -> '_705.RoughCutterSimulation':
        '''RoughCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughCutterSimulation.__class__.__qualname__ != 'RoughCutterSimulation':
            raise CastException('Failed to cast rough_cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(self.wrapped.RoughCutterSimulation.__class__.__qualname__))

        return constructor.new(_705.RoughCutterSimulation)(self.wrapped.RoughCutterSimulation) if self.wrapped.RoughCutterSimulation else None

    @property
    def rough_process_simulation(self) -> '_646.CutterProcessSimulation':
        '''CutterProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_646.CutterProcessSimulation)(self.wrapped.RoughProcessSimulation) if self.wrapped.RoughProcessSimulation else None

    @property
    def rough_process_simulation_of_type_form_wheel_grinding_process_simulation(self) -> '_647.FormWheelGrindingProcessSimulation':
        '''FormWheelGrindingProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughProcessSimulation.__class__.__qualname__ != 'FormWheelGrindingProcessSimulation':
            raise CastException('Failed to cast rough_process_simulation to FormWheelGrindingProcessSimulation. Expected: {}.'.format(self.wrapped.RoughProcessSimulation.__class__.__qualname__))

        return constructor.new(_647.FormWheelGrindingProcessSimulation)(self.wrapped.RoughProcessSimulation) if self.wrapped.RoughProcessSimulation else None

    @property
    def rough_process_simulation_of_type_shaping_process_simulation(self) -> '_648.ShapingProcessSimulation':
        '''ShapingProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.RoughProcessSimulation.__class__.__qualname__ != 'ShapingProcessSimulation':
            raise CastException('Failed to cast rough_process_simulation to ShapingProcessSimulation. Expected: {}.'.format(self.wrapped.RoughProcessSimulation.__class__.__qualname__))

        return constructor.new(_648.ShapingProcessSimulation)(self.wrapped.RoughProcessSimulation) if self.wrapped.RoughProcessSimulation else None

    @property
    def finish_cutter_simulation(self) -> '_703.GearCutterSimulation':
        '''GearCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_703.GearCutterSimulation)(self.wrapped.FinishCutterSimulation) if self.wrapped.FinishCutterSimulation else None

    @property
    def finish_cutter_simulation_of_type_finish_cutter_simulation(self) -> '_704.FinishCutterSimulation':
        '''FinishCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutterSimulation.__class__.__qualname__ != 'FinishCutterSimulation':
            raise CastException('Failed to cast finish_cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(self.wrapped.FinishCutterSimulation.__class__.__qualname__))

        return constructor.new(_704.FinishCutterSimulation)(self.wrapped.FinishCutterSimulation) if self.wrapped.FinishCutterSimulation else None

    @property
    def finish_cutter_simulation_of_type_rough_cutter_simulation(self) -> '_705.RoughCutterSimulation':
        '''RoughCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishCutterSimulation.__class__.__qualname__ != 'RoughCutterSimulation':
            raise CastException('Failed to cast finish_cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(self.wrapped.FinishCutterSimulation.__class__.__qualname__))

        return constructor.new(_705.RoughCutterSimulation)(self.wrapped.FinishCutterSimulation) if self.wrapped.FinishCutterSimulation else None

    @property
    def finish_process_simulation(self) -> '_646.CutterProcessSimulation':
        '''CutterProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_646.CutterProcessSimulation)(self.wrapped.FinishProcessSimulation) if self.wrapped.FinishProcessSimulation else None

    @property
    def finish_process_simulation_of_type_form_wheel_grinding_process_simulation(self) -> '_647.FormWheelGrindingProcessSimulation':
        '''FormWheelGrindingProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishProcessSimulation.__class__.__qualname__ != 'FormWheelGrindingProcessSimulation':
            raise CastException('Failed to cast finish_process_simulation to FormWheelGrindingProcessSimulation. Expected: {}.'.format(self.wrapped.FinishProcessSimulation.__class__.__qualname__))

        return constructor.new(_647.FormWheelGrindingProcessSimulation)(self.wrapped.FinishProcessSimulation) if self.wrapped.FinishProcessSimulation else None

    @property
    def finish_process_simulation_of_type_shaping_process_simulation(self) -> '_648.ShapingProcessSimulation':
        '''ShapingProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.FinishProcessSimulation.__class__.__qualname__ != 'ShapingProcessSimulation':
            raise CastException('Failed to cast finish_process_simulation to ShapingProcessSimulation. Expected: {}.'.format(self.wrapped.FinishProcessSimulation.__class__.__qualname__))

        return constructor.new(_648.ShapingProcessSimulation)(self.wrapped.FinishProcessSimulation) if self.wrapped.FinishProcessSimulation else None

    @property
    def design(self) -> '_508.CylindricalGearDesign':
        '''CylindricalGearDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_508.CylindricalGearDesign)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def rough_gear_specification(self) -> '_706.CylindricalGearSpecification':
        '''CylindricalGearSpecification: 'RoughGearSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_706.CylindricalGearSpecification)(self.wrapped.RoughGearSpecification) if self.wrapped.RoughGearSpecification else None

    @property
    def finished_gear_specification(self) -> '_706.CylindricalGearSpecification':
        '''CylindricalGearSpecification: 'FinishedGearSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_706.CylindricalGearSpecification)(self.wrapped.FinishedGearSpecification) if self.wrapped.FinishedGearSpecification else None

    @property
    def gear_blank(self) -> '_605.CylindricalGearBlank':
        '''CylindricalGearBlank: 'GearBlank' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_605.CylindricalGearBlank)(self.wrapped.GearBlank) if self.wrapped.GearBlank else None
