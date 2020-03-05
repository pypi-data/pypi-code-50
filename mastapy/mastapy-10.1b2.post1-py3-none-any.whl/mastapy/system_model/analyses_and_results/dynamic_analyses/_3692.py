'''_3692.py

AssemblyDynamicAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1914
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2327
from mastapy.system_model.analyses_and_results.dynamic_analyses import (
    _3684, _3630, _3715, _3685,
    _3686, _3631, _3633, _3709,
    _3637, _3723, _3711, _3691,
    _3728, _3694, _3732, _3734,
    _3695, _3696, _3698, _3700,
    _3701, _3702, _3640, _3642,
    _3707, _3737, _3643, _3739,
    _3741, _3645, _3649, _3705,
    _3627, _3629, _3682
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'AssemblyDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyDynamicAnalysis',)


class AssemblyDynamicAnalysis(_3682.AbstractAssemblyDynamicAnalysis):
    '''AssemblyDynamicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_DYNAMIC_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1914.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1914.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2327.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2327.AssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def bearings(self) -> 'List[_3684.BearingDynamicAnalysis]':
        '''List[BearingDynamicAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3684.BearingDynamicAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_3630.BeltDriveDynamicAnalysis]':
        '''List[BeltDriveDynamicAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3630.BeltDriveDynamicAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3715.BevelDifferentialGearSetDynamicAnalysis]':
        '''List[BevelDifferentialGearSetDynamicAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3715.BevelDifferentialGearSetDynamicAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_3685.BoltDynamicAnalysis]':
        '''List[BoltDynamicAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3685.BoltDynamicAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_3686.BoltedJointDynamicAnalysis]':
        '''List[BoltedJointDynamicAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3686.BoltedJointDynamicAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_3631.ClutchDynamicAnalysis]':
        '''List[ClutchDynamicAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3631.ClutchDynamicAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_3633.ConceptCouplingDynamicAnalysis]':
        '''List[ConceptCouplingDynamicAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3633.ConceptCouplingDynamicAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3709.ConceptGearSetDynamicAnalysis]':
        '''List[ConceptGearSetDynamicAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3709.ConceptGearSetDynamicAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_3637.CVTDynamicAnalysis]':
        '''List[CVTDynamicAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3637.CVTDynamicAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3723.CylindricalGearSetDynamicAnalysis]':
        '''List[CylindricalGearSetDynamicAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3723.CylindricalGearSetDynamicAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3711.FaceGearSetDynamicAnalysis]':
        '''List[FaceGearSetDynamicAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3711.FaceGearSetDynamicAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3691.FlexiblePinAssemblyDynamicAnalysis]':
        '''List[FlexiblePinAssemblyDynamicAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3691.FlexiblePinAssemblyDynamicAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3728.HypoidGearSetDynamicAnalysis]':
        '''List[HypoidGearSetDynamicAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3728.HypoidGearSetDynamicAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3694.ImportedFEComponentDynamicAnalysis]':
        '''List[ImportedFEComponentDynamicAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3694.ImportedFEComponentDynamicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3732.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3732.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3734.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3734.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_3695.MassDiscDynamicAnalysis]':
        '''List[MassDiscDynamicAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3695.MassDiscDynamicAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_3696.MeasurementComponentDynamicAnalysis]':
        '''List[MeasurementComponentDynamicAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3696.MeasurementComponentDynamicAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_3698.OilSealDynamicAnalysis]':
        '''List[OilSealDynamicAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3698.OilSealDynamicAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_3700.PlanetCarrierDynamicAnalysis]':
        '''List[PlanetCarrierDynamicAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3700.PlanetCarrierDynamicAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_3701.PointLoadDynamicAnalysis]':
        '''List[PointLoadDynamicAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3701.PointLoadDynamicAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_3702.PowerLoadDynamicAnalysis]':
        '''List[PowerLoadDynamicAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3702.PowerLoadDynamicAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3640.ShaftHubConnectionDynamicAnalysis]':
        '''List[ShaftHubConnectionDynamicAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3640.ShaftHubConnectionDynamicAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3642.RollingRingAssemblyDynamicAnalysis]':
        '''List[RollingRingAssemblyDynamicAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3642.RollingRingAssemblyDynamicAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_3707.ShaftDynamicAnalysis]':
        '''List[ShaftDynamicAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3707.ShaftDynamicAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3737.SpiralBevelGearSetDynamicAnalysis]':
        '''List[SpiralBevelGearSetDynamicAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3737.SpiralBevelGearSetDynamicAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_3643.SpringDamperDynamicAnalysis]':
        '''List[SpringDamperDynamicAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3643.SpringDamperDynamicAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3739.StraightBevelDiffGearSetDynamicAnalysis]':
        '''List[StraightBevelDiffGearSetDynamicAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3739.StraightBevelDiffGearSetDynamicAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3741.StraightBevelGearSetDynamicAnalysis]':
        '''List[StraightBevelGearSetDynamicAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3741.StraightBevelGearSetDynamicAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_3645.SynchroniserDynamicAnalysis]':
        '''List[SynchroniserDynamicAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3645.SynchroniserDynamicAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_3649.TorqueConverterDynamicAnalysis]':
        '''List[TorqueConverterDynamicAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3649.TorqueConverterDynamicAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3705.UnbalancedMassDynamicAnalysis]':
        '''List[UnbalancedMassDynamicAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3705.UnbalancedMassDynamicAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3627.WormGearSetDynamicAnalysis]':
        '''List[WormGearSetDynamicAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3627.WormGearSetDynamicAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3629.ZerolBevelGearSetDynamicAnalysis]':
        '''List[ZerolBevelGearSetDynamicAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3629.ZerolBevelGearSetDynamicAnalysis))
        return value
