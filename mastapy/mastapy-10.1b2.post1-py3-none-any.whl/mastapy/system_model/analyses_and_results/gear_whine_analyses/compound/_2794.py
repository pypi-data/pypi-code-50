'''_2794.py

AssemblyCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1914
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _3810
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import (
    _2786, _2850, _2817, _2787,
    _2788, _2851, _2853, _2811,
    _2857, _2825, _2813, _2793,
    _2830, _2796, _2834, _2836,
    _2797, _2798, _2800, _2802,
    _2803, _2804, _2860, _2862,
    _2809, _2839, _2863, _2841,
    _2843, _2865, _2869, _2807,
    _2847, _2849, _2784
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'AssemblyCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundGearWhineAnalysis',)


class AssemblyCompoundGearWhineAnalysis(_2784.AbstractAssemblyCompoundGearWhineAnalysis):
    '''AssemblyCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_GEAR_WHINE_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundGearWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1914.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1914.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_1914.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1914.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3810.AssemblyGearWhineAnalysis]':
        '''List[AssemblyGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3810.AssemblyGearWhineAnalysis))
        return value

    @property
    def assembly_gear_whine_analysis_load_cases(self) -> 'List[_3810.AssemblyGearWhineAnalysis]':
        '''List[AssemblyGearWhineAnalysis]: 'AssemblyGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyGearWhineAnalysisLoadCases, constructor.new(_3810.AssemblyGearWhineAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_2786.BearingCompoundGearWhineAnalysis]':
        '''List[BearingCompoundGearWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2786.BearingCompoundGearWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_2850.BeltDriveCompoundGearWhineAnalysis]':
        '''List[BeltDriveCompoundGearWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_2850.BeltDriveCompoundGearWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2817.BevelDifferentialGearSetCompoundGearWhineAnalysis]':
        '''List[BevelDifferentialGearSetCompoundGearWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_2817.BevelDifferentialGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_2787.BoltCompoundGearWhineAnalysis]':
        '''List[BoltCompoundGearWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_2787.BoltCompoundGearWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_2788.BoltedJointCompoundGearWhineAnalysis]':
        '''List[BoltedJointCompoundGearWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2788.BoltedJointCompoundGearWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_2851.ClutchCompoundGearWhineAnalysis]':
        '''List[ClutchCompoundGearWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_2851.ClutchCompoundGearWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_2853.ConceptCouplingCompoundGearWhineAnalysis]':
        '''List[ConceptCouplingCompoundGearWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_2853.ConceptCouplingCompoundGearWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2811.ConceptGearSetCompoundGearWhineAnalysis]':
        '''List[ConceptGearSetCompoundGearWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_2811.ConceptGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_2857.CVTCompoundGearWhineAnalysis]':
        '''List[CVTCompoundGearWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_2857.CVTCompoundGearWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2825.CylindricalGearSetCompoundGearWhineAnalysis]':
        '''List[CylindricalGearSetCompoundGearWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_2825.CylindricalGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_2813.FaceGearSetCompoundGearWhineAnalysis]':
        '''List[FaceGearSetCompoundGearWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_2813.FaceGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_2793.FlexiblePinAssemblyCompoundGearWhineAnalysis]':
        '''List[FlexiblePinAssemblyCompoundGearWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_2793.FlexiblePinAssemblyCompoundGearWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2830.HypoidGearSetCompoundGearWhineAnalysis]':
        '''List[HypoidGearSetCompoundGearWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_2830.HypoidGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_2796.ImportedFEComponentCompoundGearWhineAnalysis]':
        '''List[ImportedFEComponentCompoundGearWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_2796.ImportedFEComponentCompoundGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_2834.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_2834.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_2836.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_2836.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_2797.MassDiscCompoundGearWhineAnalysis]':
        '''List[MassDiscCompoundGearWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_2797.MassDiscCompoundGearWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_2798.MeasurementComponentCompoundGearWhineAnalysis]':
        '''List[MeasurementComponentCompoundGearWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_2798.MeasurementComponentCompoundGearWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_2800.OilSealCompoundGearWhineAnalysis]':
        '''List[OilSealCompoundGearWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_2800.OilSealCompoundGearWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_2802.PlanetCarrierCompoundGearWhineAnalysis]':
        '''List[PlanetCarrierCompoundGearWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_2802.PlanetCarrierCompoundGearWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_2803.PointLoadCompoundGearWhineAnalysis]':
        '''List[PointLoadCompoundGearWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_2803.PointLoadCompoundGearWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_2804.PowerLoadCompoundGearWhineAnalysis]':
        '''List[PowerLoadCompoundGearWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_2804.PowerLoadCompoundGearWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2860.ShaftHubConnectionCompoundGearWhineAnalysis]':
        '''List[ShaftHubConnectionCompoundGearWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_2860.ShaftHubConnectionCompoundGearWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_2862.RollingRingAssemblyCompoundGearWhineAnalysis]':
        '''List[RollingRingAssemblyCompoundGearWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_2862.RollingRingAssemblyCompoundGearWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_2809.ShaftCompoundGearWhineAnalysis]':
        '''List[ShaftCompoundGearWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_2809.ShaftCompoundGearWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2839.SpiralBevelGearSetCompoundGearWhineAnalysis]':
        '''List[SpiralBevelGearSetCompoundGearWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_2839.SpiralBevelGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_2863.SpringDamperCompoundGearWhineAnalysis]':
        '''List[SpringDamperCompoundGearWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_2863.SpringDamperCompoundGearWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_2841.StraightBevelDiffGearSetCompoundGearWhineAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundGearWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_2841.StraightBevelDiffGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2843.StraightBevelGearSetCompoundGearWhineAnalysis]':
        '''List[StraightBevelGearSetCompoundGearWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_2843.StraightBevelGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_2865.SynchroniserCompoundGearWhineAnalysis]':
        '''List[SynchroniserCompoundGearWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_2865.SynchroniserCompoundGearWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_2869.TorqueConverterCompoundGearWhineAnalysis]':
        '''List[TorqueConverterCompoundGearWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_2869.TorqueConverterCompoundGearWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_2807.UnbalancedMassCompoundGearWhineAnalysis]':
        '''List[UnbalancedMassCompoundGearWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_2807.UnbalancedMassCompoundGearWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2847.WormGearSetCompoundGearWhineAnalysis]':
        '''List[WormGearSetCompoundGearWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_2847.WormGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_2849.ZerolBevelGearSetCompoundGearWhineAnalysis]':
        '''List[ZerolBevelGearSetCompoundGearWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_2849.ZerolBevelGearSetCompoundGearWhineAnalysis))
        return value
