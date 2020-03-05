'''_747.py

GearCutterSimulation
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
    _732, _750, _728, _734,
    _748, _749, _752, _753,
    _754, _755, _730, _731
)
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_GEAR_CUTTER_SIMULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'GearCutterSimulation')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCutterSimulation',)


class GearCutterSimulation(_1.APIBase):
    '''GearCutterSimulation

    This is a mastapy class.
    '''

    TYPE = _GEAR_CUTTER_SIMULATION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearCutterSimulation.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def highest_finished_form_diameter(self) -> 'float':
        '''float: 'HighestFinishedFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HighestFinishedFormDiameter

    @property
    def lowest_finished_tip_form_diameter(self) -> 'float':
        '''float: 'LowestFinishedTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LowestFinishedTipFormDiameter

    @property
    def least_sap_to_form_radius_clearance(self) -> 'float':
        '''float: 'LeastSAPToFormRadiusClearance' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LeastSAPToFormRadiusClearance

    @property
    def cutter_simulation(self) -> 'GearCutterSimulation':
        '''GearCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(GearCutterSimulation)(self.wrapped.CutterSimulation) if self.wrapped.CutterSimulation else None

    @property
    def cutter_simulation_of_type_finish_cutter_simulation(self) -> '_732.FinishCutterSimulation':
        '''FinishCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _732.FinishCutterSimulation.TYPE not in self.wrapped.CutterSimulation.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(self.wrapped.CutterSimulation.__class__.__qualname__))

        return constructor.new(_732.FinishCutterSimulation)(self.wrapped.CutterSimulation) if self.wrapped.CutterSimulation else None

    @property
    def cutter_simulation_of_type_rough_cutter_simulation(self) -> '_750.RoughCutterSimulation':
        '''RoughCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _750.RoughCutterSimulation.TYPE not in self.wrapped.CutterSimulation.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(self.wrapped.CutterSimulation.__class__.__qualname__))

        return constructor.new(_750.RoughCutterSimulation)(self.wrapped.CutterSimulation) if self.wrapped.CutterSimulation else None

    @property
    def minimum_thickness(self) -> '_728.CutterSimulationCalc':
        '''CutterSimulationCalc: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_728.CutterSimulationCalc)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_734.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _734.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_734.FormWheelGrindingSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_hob_simulation_calculator(self) -> '_748.HobSimulationCalculator':
        '''HobSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _748.HobSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_748.HobSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_rack_simulation_calculator(self) -> '_749.RackSimulationCalculator':
        '''RackSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _749.RackSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_749.RackSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_shaper_simulation_calculator(self) -> '_752.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _752.ShaperSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_752.ShaperSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_shaving_simulation_calculator(self) -> '_753.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _753.ShavingSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_753.ShavingSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_virtual_simulation_calculator(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _754.VirtualSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_755.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _755.WormGrinderSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_755.WormGrinderSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def average_thickness(self) -> '_728.CutterSimulationCalc':
        '''CutterSimulationCalc: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_728.CutterSimulationCalc)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_734.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _734.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_734.FormWheelGrindingSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_hob_simulation_calculator(self) -> '_748.HobSimulationCalculator':
        '''HobSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _748.HobSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_748.HobSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_rack_simulation_calculator(self) -> '_749.RackSimulationCalculator':
        '''RackSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _749.RackSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_749.RackSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_shaper_simulation_calculator(self) -> '_752.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _752.ShaperSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_752.ShaperSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_shaving_simulation_calculator(self) -> '_753.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _753.ShavingSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_753.ShavingSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_virtual_simulation_calculator(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _754.VirtualSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_755.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _755.WormGrinderSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_755.WormGrinderSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def maximum_thickness(self) -> '_728.CutterSimulationCalc':
        '''CutterSimulationCalc: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_728.CutterSimulationCalc)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_734.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _734.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_734.FormWheelGrindingSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_hob_simulation_calculator(self) -> '_748.HobSimulationCalculator':
        '''HobSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _748.HobSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_748.HobSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_rack_simulation_calculator(self) -> '_749.RackSimulationCalculator':
        '''RackSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _749.RackSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_749.RackSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_shaper_simulation_calculator(self) -> '_752.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _752.ShaperSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_752.ShaperSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_shaving_simulation_calculator(self) -> '_753.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _753.ShavingSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_753.ShavingSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_virtual_simulation_calculator(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _754.VirtualSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_755.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _755.WormGrinderSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_755.WormGrinderSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def smallest_active_profile(self) -> '_728.CutterSimulationCalc':
        '''CutterSimulationCalc: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_728.CutterSimulationCalc)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_form_wheel_grinding_simulation_calculator(self) -> '_734.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _734.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_734.FormWheelGrindingSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_hob_simulation_calculator(self) -> '_748.HobSimulationCalculator':
        '''HobSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _748.HobSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_748.HobSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_rack_simulation_calculator(self) -> '_749.RackSimulationCalculator':
        '''RackSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _749.RackSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_749.RackSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_shaper_simulation_calculator(self) -> '_752.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _752.ShaperSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_752.ShaperSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_shaving_simulation_calculator(self) -> '_753.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _753.ShavingSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_753.ShavingSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_virtual_simulation_calculator(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _754.VirtualSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_worm_grinder_simulation_calculator(self) -> '_755.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _755.WormGrinderSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_755.WormGrinderSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def minimum_thickness_virtual(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MinimumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.MinimumThicknessVirtual) if self.wrapped.MinimumThicknessVirtual else None

    @property
    def average_thickness_virtual(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'AverageThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.AverageThicknessVirtual) if self.wrapped.AverageThicknessVirtual else None

    @property
    def maximum_thickness_virtual(self) -> '_754.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MaximumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_754.VirtualSimulationCalculator)(self.wrapped.MaximumThicknessVirtual) if self.wrapped.MaximumThicknessVirtual else None

    @property
    def thickness_calculators(self) -> 'List[_728.CutterSimulationCalc]':
        '''List[CutterSimulationCalc]: 'ThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ThicknessCalculators, constructor.new(_728.CutterSimulationCalc))
        return value

    @property
    def virtual_thickness_calculators(self) -> 'List[_754.VirtualSimulationCalculator]':
        '''List[VirtualSimulationCalculator]: 'VirtualThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.VirtualThicknessCalculators, constructor.new(_754.VirtualSimulationCalculator))
        return value

    @property
    def gear_mesh_cutter_simulations(self) -> 'List[_730.CylindricalManufacturedRealGearInMesh]':
        '''List[CylindricalManufacturedRealGearInMesh]: 'GearMeshCutterSimulations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshCutterSimulations, constructor.new(_730.CylindricalManufacturedRealGearInMesh))
        return value

    @property
    def gear_mesh_cutter_simulations_virtual(self) -> 'List[_731.CylindricalManufacturedVirtualGearInMesh]':
        '''List[CylindricalManufacturedVirtualGearInMesh]: 'GearMeshCutterSimulationsVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshCutterSimulationsVirtual, constructor.new(_731.CylindricalManufacturedVirtualGearInMesh))
        return value
