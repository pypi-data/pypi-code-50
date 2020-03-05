'''_490.py

GearCutterSimulation
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
    _487, _494, _482, _489,
    _491, _493, _495, _496,
    _497, _498, _485, _486
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
    def cutter_simulation_of_type_finish_cutter_simulation(self) -> '_487.FinishCutterSimulation':
        '''FinishCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _487.FinishCutterSimulation.TYPE not in self.wrapped.CutterSimulation.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(self.wrapped.CutterSimulation.__class__.__qualname__))

        return constructor.new(_487.FinishCutterSimulation)(self.wrapped.CutterSimulation) if self.wrapped.CutterSimulation else None

    @property
    def cutter_simulation_of_type_rough_cutter_simulation(self) -> '_494.RoughCutterSimulation':
        '''RoughCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _494.RoughCutterSimulation.TYPE not in self.wrapped.CutterSimulation.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(self.wrapped.CutterSimulation.__class__.__qualname__))

        return constructor.new(_494.RoughCutterSimulation)(self.wrapped.CutterSimulation) if self.wrapped.CutterSimulation else None

    @property
    def minimum_thickness(self) -> '_482.CutterSimulationCalc':
        '''CutterSimulationCalc: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_482.CutterSimulationCalc)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_489.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_489.FormWheelGrindingSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_hob_simulation_calculator(self) -> '_491.HobSimulationCalculator':
        '''HobSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _491.HobSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_491.HobSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_rack_simulation_calculator(self) -> '_493.RackSimulationCalculator':
        '''RackSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _493.RackSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_493.RackSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_shaper_simulation_calculator(self) -> '_495.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _495.ShaperSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_495.ShaperSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_shaving_simulation_calculator(self) -> '_496.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _496.ShavingSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_496.ShavingSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_virtual_simulation_calculator(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _497.VirtualSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def minimum_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_498.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _498.WormGrinderSimulationCalculator.TYPE not in self.wrapped.MinimumThickness.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.MinimumThickness.__class__.__qualname__))

        return constructor.new(_498.WormGrinderSimulationCalculator)(self.wrapped.MinimumThickness) if self.wrapped.MinimumThickness else None

    @property
    def average_thickness(self) -> '_482.CutterSimulationCalc':
        '''CutterSimulationCalc: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_482.CutterSimulationCalc)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_489.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_489.FormWheelGrindingSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_hob_simulation_calculator(self) -> '_491.HobSimulationCalculator':
        '''HobSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _491.HobSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_491.HobSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_rack_simulation_calculator(self) -> '_493.RackSimulationCalculator':
        '''RackSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _493.RackSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_493.RackSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_shaper_simulation_calculator(self) -> '_495.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _495.ShaperSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_495.ShaperSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_shaving_simulation_calculator(self) -> '_496.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _496.ShavingSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_496.ShavingSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_virtual_simulation_calculator(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _497.VirtualSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def average_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_498.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _498.WormGrinderSimulationCalculator.TYPE not in self.wrapped.AverageThickness.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.AverageThickness.__class__.__qualname__))

        return constructor.new(_498.WormGrinderSimulationCalculator)(self.wrapped.AverageThickness) if self.wrapped.AverageThickness else None

    @property
    def maximum_thickness(self) -> '_482.CutterSimulationCalc':
        '''CutterSimulationCalc: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_482.CutterSimulationCalc)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_489.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_489.FormWheelGrindingSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_hob_simulation_calculator(self) -> '_491.HobSimulationCalculator':
        '''HobSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _491.HobSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_491.HobSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_rack_simulation_calculator(self) -> '_493.RackSimulationCalculator':
        '''RackSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _493.RackSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_493.RackSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_shaper_simulation_calculator(self) -> '_495.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _495.ShaperSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_495.ShaperSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_shaving_simulation_calculator(self) -> '_496.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _496.ShavingSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_496.ShavingSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_virtual_simulation_calculator(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _497.VirtualSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def maximum_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_498.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _498.WormGrinderSimulationCalculator.TYPE not in self.wrapped.MaximumThickness.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.MaximumThickness.__class__.__qualname__))

        return constructor.new(_498.WormGrinderSimulationCalculator)(self.wrapped.MaximumThickness) if self.wrapped.MaximumThickness else None

    @property
    def smallest_active_profile(self) -> '_482.CutterSimulationCalc':
        '''CutterSimulationCalc: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_482.CutterSimulationCalc)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_form_wheel_grinding_simulation_calculator(self) -> '_489.FormWheelGrindingSimulationCalculator':
        '''FormWheelGrindingSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _489.FormWheelGrindingSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_489.FormWheelGrindingSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_hob_simulation_calculator(self) -> '_491.HobSimulationCalculator':
        '''HobSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _491.HobSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to HobSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_491.HobSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_rack_simulation_calculator(self) -> '_493.RackSimulationCalculator':
        '''RackSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _493.RackSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to RackSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_493.RackSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_shaper_simulation_calculator(self) -> '_495.ShaperSimulationCalculator':
        '''ShaperSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _495.ShaperSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to ShaperSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_495.ShaperSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_shaving_simulation_calculator(self) -> '_496.ShavingSimulationCalculator':
        '''ShavingSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _496.ShavingSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to ShavingSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_496.ShavingSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_virtual_simulation_calculator(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _497.VirtualSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to VirtualSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def smallest_active_profile_of_type_worm_grinder_simulation_calculator(self) -> '_498.WormGrinderSimulationCalculator':
        '''WormGrinderSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _498.WormGrinderSimulationCalculator.TYPE not in self.wrapped.SmallestActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to WormGrinderSimulationCalculator. Expected: {}.'.format(self.wrapped.SmallestActiveProfile.__class__.__qualname__))

        return constructor.new(_498.WormGrinderSimulationCalculator)(self.wrapped.SmallestActiveProfile) if self.wrapped.SmallestActiveProfile else None

    @property
    def minimum_thickness_virtual(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MinimumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.MinimumThicknessVirtual) if self.wrapped.MinimumThicknessVirtual else None

    @property
    def average_thickness_virtual(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'AverageThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.AverageThicknessVirtual) if self.wrapped.AverageThicknessVirtual else None

    @property
    def maximum_thickness_virtual(self) -> '_497.VirtualSimulationCalculator':
        '''VirtualSimulationCalculator: 'MaximumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_497.VirtualSimulationCalculator)(self.wrapped.MaximumThicknessVirtual) if self.wrapped.MaximumThicknessVirtual else None

    @property
    def thickness_calculators(self) -> 'List[_482.CutterSimulationCalc]':
        '''List[CutterSimulationCalc]: 'ThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ThicknessCalculators, constructor.new(_482.CutterSimulationCalc))
        return value

    @property
    def virtual_thickness_calculators(self) -> 'List[_497.VirtualSimulationCalculator]':
        '''List[VirtualSimulationCalculator]: 'VirtualThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.VirtualThicknessCalculators, constructor.new(_497.VirtualSimulationCalculator))
        return value

    @property
    def gear_mesh_cutter_simulations(self) -> 'List[_485.CylindricalManufacturedRealGearInMesh]':
        '''List[CylindricalManufacturedRealGearInMesh]: 'GearMeshCutterSimulations' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshCutterSimulations, constructor.new(_485.CylindricalManufacturedRealGearInMesh))
        return value

    @property
    def gear_mesh_cutter_simulations_virtual(self) -> 'List[_486.CylindricalManufacturedVirtualGearInMesh]':
        '''List[CylindricalManufacturedVirtualGearInMesh]: 'GearMeshCutterSimulationsVirtual' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshCutterSimulationsVirtual, constructor.new(_486.CylindricalManufacturedVirtualGearInMesh))
        return value
