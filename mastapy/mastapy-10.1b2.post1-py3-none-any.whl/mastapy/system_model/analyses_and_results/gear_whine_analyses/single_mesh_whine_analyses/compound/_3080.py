'''_3080.py

AssemblyCompoundSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1855
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _4272
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound import (
    _3072, _3136, _3103, _3073,
    _3074, _3137, _3139, _3097,
    _3143, _3111, _3099, _3079,
    _3116, _3082, _3120, _3122,
    _3083, _3084, _3086, _3088,
    _3089, _3090, _3146, _3148,
    _3095, _3125, _3149, _3127,
    _3129, _3151, _3155, _3093,
    _3133, _3135, _3070
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses.Compound', 'AssemblyCompoundSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundSingleMeshWhineAnalysis',)


class AssemblyCompoundSingleMeshWhineAnalysis(_3070.AbstractAssemblyCompoundSingleMeshWhineAnalysis):
    '''AssemblyCompoundSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1855.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1855.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_1855.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1855.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4272.AssemblySingleMeshWhineAnalysis]':
        '''List[AssemblySingleMeshWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4272.AssemblySingleMeshWhineAnalysis))
        return value

    @property
    def assembly_single_mesh_whine_analysis_load_cases(self) -> 'List[_4272.AssemblySingleMeshWhineAnalysis]':
        '''List[AssemblySingleMeshWhineAnalysis]: 'AssemblySingleMeshWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySingleMeshWhineAnalysisLoadCases, constructor.new(_4272.AssemblySingleMeshWhineAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_3072.BearingCompoundSingleMeshWhineAnalysis]':
        '''List[BearingCompoundSingleMeshWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3072.BearingCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_3136.BeltDriveCompoundSingleMeshWhineAnalysis]':
        '''List[BeltDriveCompoundSingleMeshWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3136.BeltDriveCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3103.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3103.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_3073.BoltCompoundSingleMeshWhineAnalysis]':
        '''List[BoltCompoundSingleMeshWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3073.BoltCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_3074.BoltedJointCompoundSingleMeshWhineAnalysis]':
        '''List[BoltedJointCompoundSingleMeshWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3074.BoltedJointCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_3137.ClutchCompoundSingleMeshWhineAnalysis]':
        '''List[ClutchCompoundSingleMeshWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3137.ClutchCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_3139.ConceptCouplingCompoundSingleMeshWhineAnalysis]':
        '''List[ConceptCouplingCompoundSingleMeshWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3139.ConceptCouplingCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3097.ConceptGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[ConceptGearSetCompoundSingleMeshWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3097.ConceptGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_3143.CVTCompoundSingleMeshWhineAnalysis]':
        '''List[CVTCompoundSingleMeshWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3143.CVTCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3111.CylindricalGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[CylindricalGearSetCompoundSingleMeshWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3111.CylindricalGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3099.FaceGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[FaceGearSetCompoundSingleMeshWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3099.FaceGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3079.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis]':
        '''List[FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3079.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3116.HypoidGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[HypoidGearSetCompoundSingleMeshWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3116.HypoidGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3082.ImportedFEComponentCompoundSingleMeshWhineAnalysis]':
        '''List[ImportedFEComponentCompoundSingleMeshWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3082.ImportedFEComponentCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3120.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3120.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3122.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3122.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_3083.MassDiscCompoundSingleMeshWhineAnalysis]':
        '''List[MassDiscCompoundSingleMeshWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3083.MassDiscCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_3084.MeasurementComponentCompoundSingleMeshWhineAnalysis]':
        '''List[MeasurementComponentCompoundSingleMeshWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3084.MeasurementComponentCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_3086.OilSealCompoundSingleMeshWhineAnalysis]':
        '''List[OilSealCompoundSingleMeshWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3086.OilSealCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_3088.PlanetCarrierCompoundSingleMeshWhineAnalysis]':
        '''List[PlanetCarrierCompoundSingleMeshWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3088.PlanetCarrierCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_3089.PointLoadCompoundSingleMeshWhineAnalysis]':
        '''List[PointLoadCompoundSingleMeshWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3089.PointLoadCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_3090.PowerLoadCompoundSingleMeshWhineAnalysis]':
        '''List[PowerLoadCompoundSingleMeshWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3090.PowerLoadCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3146.ShaftHubConnectionCompoundSingleMeshWhineAnalysis]':
        '''List[ShaftHubConnectionCompoundSingleMeshWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3146.ShaftHubConnectionCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3148.RollingRingAssemblyCompoundSingleMeshWhineAnalysis]':
        '''List[RollingRingAssemblyCompoundSingleMeshWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3148.RollingRingAssemblyCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_3095.ShaftCompoundSingleMeshWhineAnalysis]':
        '''List[ShaftCompoundSingleMeshWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3095.ShaftCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3125.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[SpiralBevelGearSetCompoundSingleMeshWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3125.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_3149.SpringDamperCompoundSingleMeshWhineAnalysis]':
        '''List[SpringDamperCompoundSingleMeshWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3149.SpringDamperCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3127.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3127.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3129.StraightBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[StraightBevelGearSetCompoundSingleMeshWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3129.StraightBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_3151.SynchroniserCompoundSingleMeshWhineAnalysis]':
        '''List[SynchroniserCompoundSingleMeshWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3151.SynchroniserCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_3155.TorqueConverterCompoundSingleMeshWhineAnalysis]':
        '''List[TorqueConverterCompoundSingleMeshWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3155.TorqueConverterCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3093.UnbalancedMassCompoundSingleMeshWhineAnalysis]':
        '''List[UnbalancedMassCompoundSingleMeshWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3093.UnbalancedMassCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3133.WormGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[WormGearSetCompoundSingleMeshWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3133.WormGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3135.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[ZerolBevelGearSetCompoundSingleMeshWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3135.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value
