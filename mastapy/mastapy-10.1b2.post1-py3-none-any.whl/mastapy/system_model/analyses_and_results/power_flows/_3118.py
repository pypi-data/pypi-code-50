'''_3118.py

AssemblyPowerFlow
'''


from typing import List

from mastapy.system_model.part_model import _1906
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _5883
from mastapy.gears.analysis import _1070
from mastapy.system_model.analyses_and_results.power_flows import (
    _3119, _3121, _3124, _3131,
    _3130, _3134, _3139, _3142,
    _3152, _3157, _3163, _3164,
    _3171, _3172, _3179, _3182,
    _3183, _3184, _3186, _3190,
    _3191, _3194, _3200, _3196,
    _3201, _3206, _3209, _3212,
    _3215, _3220, _3223, _3226,
    _3230, _3233, _3113
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'AssemblyPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyPowerFlow',)


class AssemblyPowerFlow(_3113.AbstractAssemblyPowerFlow):
    '''AssemblyPowerFlow

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1906.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1906.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_5883.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5883.AssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def rating_for_all_gear_sets(self) -> '_1070.GearSetGroupDutyCycle':
        '''GearSetGroupDutyCycle: 'RatingForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1070.GearSetGroupDutyCycle)(self.wrapped.RatingForAllGearSets) if self.wrapped.RatingForAllGearSets else None

    @property
    def bearings(self) -> 'List[_3119.BearingPowerFlow]':
        '''List[BearingPowerFlow]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3119.BearingPowerFlow))
        return value

    @property
    def belt_drives(self) -> 'List[_3121.BeltDrivePowerFlow]':
        '''List[BeltDrivePowerFlow]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3121.BeltDrivePowerFlow))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3124.BevelDifferentialGearSetPowerFlow]':
        '''List[BevelDifferentialGearSetPowerFlow]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3124.BevelDifferentialGearSetPowerFlow))
        return value

    @property
    def bolts(self) -> 'List[_3131.BoltPowerFlow]':
        '''List[BoltPowerFlow]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3131.BoltPowerFlow))
        return value

    @property
    def bolted_joints(self) -> 'List[_3130.BoltedJointPowerFlow]':
        '''List[BoltedJointPowerFlow]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3130.BoltedJointPowerFlow))
        return value

    @property
    def clutches(self) -> 'List[_3134.ClutchPowerFlow]':
        '''List[ClutchPowerFlow]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3134.ClutchPowerFlow))
        return value

    @property
    def concept_couplings(self) -> 'List[_3139.ConceptCouplingPowerFlow]':
        '''List[ConceptCouplingPowerFlow]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3139.ConceptCouplingPowerFlow))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3142.ConceptGearSetPowerFlow]':
        '''List[ConceptGearSetPowerFlow]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3142.ConceptGearSetPowerFlow))
        return value

    @property
    def cv_ts(self) -> 'List[_3152.CVTPowerFlow]':
        '''List[CVTPowerFlow]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3152.CVTPowerFlow))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3157.CylindricalGearSetPowerFlow]':
        '''List[CylindricalGearSetPowerFlow]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3157.CylindricalGearSetPowerFlow))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3163.FaceGearSetPowerFlow]':
        '''List[FaceGearSetPowerFlow]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3163.FaceGearSetPowerFlow))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3164.FlexiblePinAssemblyPowerFlow]':
        '''List[FlexiblePinAssemblyPowerFlow]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3164.FlexiblePinAssemblyPowerFlow))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3171.HypoidGearSetPowerFlow]':
        '''List[HypoidGearSetPowerFlow]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3171.HypoidGearSetPowerFlow))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3172.ImportedFEComponentPowerFlow]':
        '''List[ImportedFEComponentPowerFlow]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3172.ImportedFEComponentPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3179.KlingelnbergCycloPalloidHypoidGearSetPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetPowerFlow]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3179.KlingelnbergCycloPalloidHypoidGearSetPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3182.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3182.KlingelnbergCycloPalloidSpiralBevelGearSetPowerFlow))
        return value

    @property
    def mass_discs(self) -> 'List[_3183.MassDiscPowerFlow]':
        '''List[MassDiscPowerFlow]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3183.MassDiscPowerFlow))
        return value

    @property
    def measurement_components(self) -> 'List[_3184.MeasurementComponentPowerFlow]':
        '''List[MeasurementComponentPowerFlow]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3184.MeasurementComponentPowerFlow))
        return value

    @property
    def oil_seals(self) -> 'List[_3186.OilSealPowerFlow]':
        '''List[OilSealPowerFlow]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3186.OilSealPowerFlow))
        return value

    @property
    def planet_carriers(self) -> 'List[_3190.PlanetCarrierPowerFlow]':
        '''List[PlanetCarrierPowerFlow]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3190.PlanetCarrierPowerFlow))
        return value

    @property
    def point_loads(self) -> 'List[_3191.PointLoadPowerFlow]':
        '''List[PointLoadPowerFlow]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3191.PointLoadPowerFlow))
        return value

    @property
    def power_loads(self) -> 'List[_3194.PowerLoadPowerFlow]':
        '''List[PowerLoadPowerFlow]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3194.PowerLoadPowerFlow))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3200.ShaftHubConnectionPowerFlow]':
        '''List[ShaftHubConnectionPowerFlow]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3200.ShaftHubConnectionPowerFlow))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3196.RollingRingAssemblyPowerFlow]':
        '''List[RollingRingAssemblyPowerFlow]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3196.RollingRingAssemblyPowerFlow))
        return value

    @property
    def shafts(self) -> 'List[_3201.ShaftPowerFlow]':
        '''List[ShaftPowerFlow]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3201.ShaftPowerFlow))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3206.SpiralBevelGearSetPowerFlow]':
        '''List[SpiralBevelGearSetPowerFlow]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3206.SpiralBevelGearSetPowerFlow))
        return value

    @property
    def spring_dampers(self) -> 'List[_3209.SpringDamperPowerFlow]':
        '''List[SpringDamperPowerFlow]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3209.SpringDamperPowerFlow))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3212.StraightBevelDiffGearSetPowerFlow]':
        '''List[StraightBevelDiffGearSetPowerFlow]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3212.StraightBevelDiffGearSetPowerFlow))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3215.StraightBevelGearSetPowerFlow]':
        '''List[StraightBevelGearSetPowerFlow]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3215.StraightBevelGearSetPowerFlow))
        return value

    @property
    def synchronisers(self) -> 'List[_3220.SynchroniserPowerFlow]':
        '''List[SynchroniserPowerFlow]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3220.SynchroniserPowerFlow))
        return value

    @property
    def torque_converters(self) -> 'List[_3223.TorqueConverterPowerFlow]':
        '''List[TorqueConverterPowerFlow]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3223.TorqueConverterPowerFlow))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3226.UnbalancedMassPowerFlow]':
        '''List[UnbalancedMassPowerFlow]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3226.UnbalancedMassPowerFlow))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3230.WormGearSetPowerFlow]':
        '''List[WormGearSetPowerFlow]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3230.WormGearSetPowerFlow))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3233.ZerolBevelGearSetPowerFlow]':
        '''List[ZerolBevelGearSetPowerFlow]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3233.ZerolBevelGearSetPowerFlow))
        return value
