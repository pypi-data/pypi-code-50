'''_5514.py

AssemblyCompoundSingleMeshWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1958
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses import _5391
from mastapy.system_model.analyses_and_results.gear_whine_analyses.single_mesh_whine_analyses.compound import (
    _5515, _5517, _5520, _5526,
    _5527, _5528, _5533, _5538,
    _5548, _5552, _5558, _5559,
    _5566, _5567, _5574, _5577,
    _5578, _5579, _5581, _5583,
    _5588, _5589, _5590, _5597,
    _5592, _5596, _5602, _5603,
    _5608, _5611, _5614, _5618,
    _5622, _5626, _5629, _5509
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.SingleMeshWhineAnalyses.Compound', 'AssemblyCompoundSingleMeshWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundSingleMeshWhineAnalysis',)


class AssemblyCompoundSingleMeshWhineAnalysis(_5509.AbstractAssemblyCompoundSingleMeshWhineAnalysis):
    '''AssemblyCompoundSingleMeshWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_SINGLE_MESH_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundSingleMeshWhineAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1958.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1958.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_1958.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1958.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_5391.AssemblySingleMeshWhineAnalysis]':
        '''List[AssemblySingleMeshWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5391.AssemblySingleMeshWhineAnalysis))
        return value

    @property
    def assembly_single_mesh_whine_analysis_load_cases(self) -> 'List[_5391.AssemblySingleMeshWhineAnalysis]':
        '''List[AssemblySingleMeshWhineAnalysis]: 'AssemblySingleMeshWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySingleMeshWhineAnalysisLoadCases, constructor.new(_5391.AssemblySingleMeshWhineAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5515.BearingCompoundSingleMeshWhineAnalysis]':
        '''List[BearingCompoundSingleMeshWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5515.BearingCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5517.BeltDriveCompoundSingleMeshWhineAnalysis]':
        '''List[BeltDriveCompoundSingleMeshWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5517.BeltDriveCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5520.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5520.BevelDifferentialGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5526.BoltCompoundSingleMeshWhineAnalysis]':
        '''List[BoltCompoundSingleMeshWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5526.BoltCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5527.BoltedJointCompoundSingleMeshWhineAnalysis]':
        '''List[BoltedJointCompoundSingleMeshWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5527.BoltedJointCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5528.ClutchCompoundSingleMeshWhineAnalysis]':
        '''List[ClutchCompoundSingleMeshWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5528.ClutchCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5533.ConceptCouplingCompoundSingleMeshWhineAnalysis]':
        '''List[ConceptCouplingCompoundSingleMeshWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5533.ConceptCouplingCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5538.ConceptGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[ConceptGearSetCompoundSingleMeshWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5538.ConceptGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5548.CVTCompoundSingleMeshWhineAnalysis]':
        '''List[CVTCompoundSingleMeshWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5548.CVTCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5552.CylindricalGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[CylindricalGearSetCompoundSingleMeshWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5552.CylindricalGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5558.FaceGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[FaceGearSetCompoundSingleMeshWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5558.FaceGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5559.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis]':
        '''List[FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5559.FlexiblePinAssemblyCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5566.HypoidGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[HypoidGearSetCompoundSingleMeshWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5566.HypoidGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5567.ImportedFEComponentCompoundSingleMeshWhineAnalysis]':
        '''List[ImportedFEComponentCompoundSingleMeshWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5567.ImportedFEComponentCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5574.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5574.KlingelnbergCycloPalloidHypoidGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5577.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5577.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5578.MassDiscCompoundSingleMeshWhineAnalysis]':
        '''List[MassDiscCompoundSingleMeshWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5578.MassDiscCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5579.MeasurementComponentCompoundSingleMeshWhineAnalysis]':
        '''List[MeasurementComponentCompoundSingleMeshWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5579.MeasurementComponentCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5581.OilSealCompoundSingleMeshWhineAnalysis]':
        '''List[OilSealCompoundSingleMeshWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5581.OilSealCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5583.PartToPartShearCouplingCompoundSingleMeshWhineAnalysis]':
        '''List[PartToPartShearCouplingCompoundSingleMeshWhineAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5583.PartToPartShearCouplingCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5588.PlanetCarrierCompoundSingleMeshWhineAnalysis]':
        '''List[PlanetCarrierCompoundSingleMeshWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5588.PlanetCarrierCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5589.PointLoadCompoundSingleMeshWhineAnalysis]':
        '''List[PointLoadCompoundSingleMeshWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5589.PointLoadCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5590.PowerLoadCompoundSingleMeshWhineAnalysis]':
        '''List[PowerLoadCompoundSingleMeshWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5590.PowerLoadCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5597.ShaftHubConnectionCompoundSingleMeshWhineAnalysis]':
        '''List[ShaftHubConnectionCompoundSingleMeshWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5597.ShaftHubConnectionCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5592.RollingRingAssemblyCompoundSingleMeshWhineAnalysis]':
        '''List[RollingRingAssemblyCompoundSingleMeshWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5592.RollingRingAssemblyCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5596.ShaftCompoundSingleMeshWhineAnalysis]':
        '''List[ShaftCompoundSingleMeshWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5596.ShaftCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5602.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[SpiralBevelGearSetCompoundSingleMeshWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5602.SpiralBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5603.SpringDamperCompoundSingleMeshWhineAnalysis]':
        '''List[SpringDamperCompoundSingleMeshWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5603.SpringDamperCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5608.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5608.StraightBevelDiffGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5611.StraightBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[StraightBevelGearSetCompoundSingleMeshWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5611.StraightBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5614.SynchroniserCompoundSingleMeshWhineAnalysis]':
        '''List[SynchroniserCompoundSingleMeshWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5614.SynchroniserCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5618.TorqueConverterCompoundSingleMeshWhineAnalysis]':
        '''List[TorqueConverterCompoundSingleMeshWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5618.TorqueConverterCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5622.UnbalancedMassCompoundSingleMeshWhineAnalysis]':
        '''List[UnbalancedMassCompoundSingleMeshWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5622.UnbalancedMassCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5626.WormGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[WormGearSetCompoundSingleMeshWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5626.WormGearSetCompoundSingleMeshWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5629.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis]':
        '''List[ZerolBevelGearSetCompoundSingleMeshWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5629.ZerolBevelGearSetCompoundSingleMeshWhineAnalysis))
        return value
