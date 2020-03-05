'''_3737.py

AssemblyGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1855
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _2319
from mastapy.system_model.analyses_and_results.system_deflections import _2143
from mastapy.system_model.analyses_and_results.gear_whine_analyses import (
    _3729, _3675, _3760, _3730,
    _3731, _3676, _3678, _3754,
    _3682, _3768, _3756, _3736,
    _3773, _3739, _3777, _3779,
    _3740, _3741, _3743, _3745,
    _3746, _3747, _3685, _3687,
    _3752, _3782, _3688, _3784,
    _3786, _3690, _3694, _3750,
    _3672, _3674, _3727
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses', 'AssemblyGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyGearWhineAnalysis',)


class AssemblyGearWhineAnalysis(_3727.AbstractAssemblyGearWhineAnalysis):
    '''AssemblyGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1855.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1855.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_2319.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2319.AssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def system_deflection_results(self) -> '_2143.AssemblySystemDeflection':
        '''AssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2143.AssemblySystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults else None

    @property
    def bearings(self) -> 'List[_3729.BearingGearWhineAnalysis]':
        '''List[BearingGearWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3729.BearingGearWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_3675.BeltDriveGearWhineAnalysis]':
        '''List[BeltDriveGearWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3675.BeltDriveGearWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3760.BevelDifferentialGearSetGearWhineAnalysis]':
        '''List[BevelDifferentialGearSetGearWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3760.BevelDifferentialGearSetGearWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_3730.BoltGearWhineAnalysis]':
        '''List[BoltGearWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3730.BoltGearWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_3731.BoltedJointGearWhineAnalysis]':
        '''List[BoltedJointGearWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3731.BoltedJointGearWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_3676.ClutchGearWhineAnalysis]':
        '''List[ClutchGearWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3676.ClutchGearWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_3678.ConceptCouplingGearWhineAnalysis]':
        '''List[ConceptCouplingGearWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3678.ConceptCouplingGearWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3754.ConceptGearSetGearWhineAnalysis]':
        '''List[ConceptGearSetGearWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3754.ConceptGearSetGearWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_3682.CVTGearWhineAnalysis]':
        '''List[CVTGearWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3682.CVTGearWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3768.CylindricalGearSetGearWhineAnalysis]':
        '''List[CylindricalGearSetGearWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3768.CylindricalGearSetGearWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3756.FaceGearSetGearWhineAnalysis]':
        '''List[FaceGearSetGearWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3756.FaceGearSetGearWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3736.FlexiblePinAssemblyGearWhineAnalysis]':
        '''List[FlexiblePinAssemblyGearWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3736.FlexiblePinAssemblyGearWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3773.HypoidGearSetGearWhineAnalysis]':
        '''List[HypoidGearSetGearWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3773.HypoidGearSetGearWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3739.ImportedFEComponentGearWhineAnalysis]':
        '''List[ImportedFEComponentGearWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3739.ImportedFEComponentGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3777.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3777.KlingelnbergCycloPalloidHypoidGearSetGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3779.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3779.KlingelnbergCycloPalloidSpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_3740.MassDiscGearWhineAnalysis]':
        '''List[MassDiscGearWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3740.MassDiscGearWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_3741.MeasurementComponentGearWhineAnalysis]':
        '''List[MeasurementComponentGearWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3741.MeasurementComponentGearWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_3743.OilSealGearWhineAnalysis]':
        '''List[OilSealGearWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3743.OilSealGearWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_3745.PlanetCarrierGearWhineAnalysis]':
        '''List[PlanetCarrierGearWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3745.PlanetCarrierGearWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_3746.PointLoadGearWhineAnalysis]':
        '''List[PointLoadGearWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3746.PointLoadGearWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_3747.PowerLoadGearWhineAnalysis]':
        '''List[PowerLoadGearWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3747.PowerLoadGearWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3685.ShaftHubConnectionGearWhineAnalysis]':
        '''List[ShaftHubConnectionGearWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3685.ShaftHubConnectionGearWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3687.RollingRingAssemblyGearWhineAnalysis]':
        '''List[RollingRingAssemblyGearWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3687.RollingRingAssemblyGearWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_3752.ShaftGearWhineAnalysis]':
        '''List[ShaftGearWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3752.ShaftGearWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3782.SpiralBevelGearSetGearWhineAnalysis]':
        '''List[SpiralBevelGearSetGearWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3782.SpiralBevelGearSetGearWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_3688.SpringDamperGearWhineAnalysis]':
        '''List[SpringDamperGearWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3688.SpringDamperGearWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3784.StraightBevelDiffGearSetGearWhineAnalysis]':
        '''List[StraightBevelDiffGearSetGearWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3784.StraightBevelDiffGearSetGearWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3786.StraightBevelGearSetGearWhineAnalysis]':
        '''List[StraightBevelGearSetGearWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3786.StraightBevelGearSetGearWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_3690.SynchroniserGearWhineAnalysis]':
        '''List[SynchroniserGearWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3690.SynchroniserGearWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_3694.TorqueConverterGearWhineAnalysis]':
        '''List[TorqueConverterGearWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3694.TorqueConverterGearWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3750.UnbalancedMassGearWhineAnalysis]':
        '''List[UnbalancedMassGearWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3750.UnbalancedMassGearWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3672.WormGearSetGearWhineAnalysis]':
        '''List[WormGearSetGearWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3672.WormGearSetGearWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3674.ZerolBevelGearSetGearWhineAnalysis]':
        '''List[ZerolBevelGearSetGearWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3674.ZerolBevelGearSetGearWhineAnalysis))
        return value
