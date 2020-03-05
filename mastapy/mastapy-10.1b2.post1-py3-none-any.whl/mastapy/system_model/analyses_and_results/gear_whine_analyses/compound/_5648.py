'''_5648.py

AssemblyCompoundGearWhineAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1958
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.gear_whine_analyses import _5236
from mastapy.system_model.analyses_and_results.gear_whine_analyses.compound import (
    _5649, _5651, _5654, _5660,
    _5661, _5662, _5667, _5672,
    _5682, _5686, _5692, _5693,
    _5700, _5701, _5708, _5711,
    _5712, _5713, _5715, _5717,
    _5722, _5723, _5724, _5731,
    _5726, _5730, _5736, _5737,
    _5742, _5745, _5748, _5752,
    _5756, _5760, _5763, _5643
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_GEAR_WHINE_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.Compound', 'AssemblyCompoundGearWhineAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundGearWhineAnalysis',)


class AssemblyCompoundGearWhineAnalysis(_5643.AbstractAssemblyCompoundGearWhineAnalysis):
    '''AssemblyCompoundGearWhineAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_GEAR_WHINE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundGearWhineAnalysis.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_5236.AssemblyGearWhineAnalysis]':
        '''List[AssemblyGearWhineAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_5236.AssemblyGearWhineAnalysis))
        return value

    @property
    def assembly_gear_whine_analysis_load_cases(self) -> 'List[_5236.AssemblyGearWhineAnalysis]':
        '''List[AssemblyGearWhineAnalysis]: 'AssemblyGearWhineAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyGearWhineAnalysisLoadCases, constructor.new(_5236.AssemblyGearWhineAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5649.BearingCompoundGearWhineAnalysis]':
        '''List[BearingCompoundGearWhineAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5649.BearingCompoundGearWhineAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5651.BeltDriveCompoundGearWhineAnalysis]':
        '''List[BeltDriveCompoundGearWhineAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5651.BeltDriveCompoundGearWhineAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5654.BevelDifferentialGearSetCompoundGearWhineAnalysis]':
        '''List[BevelDifferentialGearSetCompoundGearWhineAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5654.BevelDifferentialGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5660.BoltCompoundGearWhineAnalysis]':
        '''List[BoltCompoundGearWhineAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5660.BoltCompoundGearWhineAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5661.BoltedJointCompoundGearWhineAnalysis]':
        '''List[BoltedJointCompoundGearWhineAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5661.BoltedJointCompoundGearWhineAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5662.ClutchCompoundGearWhineAnalysis]':
        '''List[ClutchCompoundGearWhineAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5662.ClutchCompoundGearWhineAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5667.ConceptCouplingCompoundGearWhineAnalysis]':
        '''List[ConceptCouplingCompoundGearWhineAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5667.ConceptCouplingCompoundGearWhineAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5672.ConceptGearSetCompoundGearWhineAnalysis]':
        '''List[ConceptGearSetCompoundGearWhineAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5672.ConceptGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5682.CVTCompoundGearWhineAnalysis]':
        '''List[CVTCompoundGearWhineAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5682.CVTCompoundGearWhineAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5686.CylindricalGearSetCompoundGearWhineAnalysis]':
        '''List[CylindricalGearSetCompoundGearWhineAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5686.CylindricalGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5692.FaceGearSetCompoundGearWhineAnalysis]':
        '''List[FaceGearSetCompoundGearWhineAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5692.FaceGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5693.FlexiblePinAssemblyCompoundGearWhineAnalysis]':
        '''List[FlexiblePinAssemblyCompoundGearWhineAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5693.FlexiblePinAssemblyCompoundGearWhineAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5700.HypoidGearSetCompoundGearWhineAnalysis]':
        '''List[HypoidGearSetCompoundGearWhineAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5700.HypoidGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5701.ImportedFEComponentCompoundGearWhineAnalysis]':
        '''List[ImportedFEComponentCompoundGearWhineAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5701.ImportedFEComponentCompoundGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5708.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5708.KlingelnbergCycloPalloidHypoidGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5711.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5711.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5712.MassDiscCompoundGearWhineAnalysis]':
        '''List[MassDiscCompoundGearWhineAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5712.MassDiscCompoundGearWhineAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5713.MeasurementComponentCompoundGearWhineAnalysis]':
        '''List[MeasurementComponentCompoundGearWhineAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5713.MeasurementComponentCompoundGearWhineAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5715.OilSealCompoundGearWhineAnalysis]':
        '''List[OilSealCompoundGearWhineAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5715.OilSealCompoundGearWhineAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5717.PartToPartShearCouplingCompoundGearWhineAnalysis]':
        '''List[PartToPartShearCouplingCompoundGearWhineAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5717.PartToPartShearCouplingCompoundGearWhineAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5722.PlanetCarrierCompoundGearWhineAnalysis]':
        '''List[PlanetCarrierCompoundGearWhineAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5722.PlanetCarrierCompoundGearWhineAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5723.PointLoadCompoundGearWhineAnalysis]':
        '''List[PointLoadCompoundGearWhineAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5723.PointLoadCompoundGearWhineAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5724.PowerLoadCompoundGearWhineAnalysis]':
        '''List[PowerLoadCompoundGearWhineAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5724.PowerLoadCompoundGearWhineAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5731.ShaftHubConnectionCompoundGearWhineAnalysis]':
        '''List[ShaftHubConnectionCompoundGearWhineAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5731.ShaftHubConnectionCompoundGearWhineAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5726.RollingRingAssemblyCompoundGearWhineAnalysis]':
        '''List[RollingRingAssemblyCompoundGearWhineAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5726.RollingRingAssemblyCompoundGearWhineAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5730.ShaftCompoundGearWhineAnalysis]':
        '''List[ShaftCompoundGearWhineAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5730.ShaftCompoundGearWhineAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5736.SpiralBevelGearSetCompoundGearWhineAnalysis]':
        '''List[SpiralBevelGearSetCompoundGearWhineAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5736.SpiralBevelGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5737.SpringDamperCompoundGearWhineAnalysis]':
        '''List[SpringDamperCompoundGearWhineAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5737.SpringDamperCompoundGearWhineAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5742.StraightBevelDiffGearSetCompoundGearWhineAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundGearWhineAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5742.StraightBevelDiffGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5745.StraightBevelGearSetCompoundGearWhineAnalysis]':
        '''List[StraightBevelGearSetCompoundGearWhineAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5745.StraightBevelGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5748.SynchroniserCompoundGearWhineAnalysis]':
        '''List[SynchroniserCompoundGearWhineAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5748.SynchroniserCompoundGearWhineAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5752.TorqueConverterCompoundGearWhineAnalysis]':
        '''List[TorqueConverterCompoundGearWhineAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5752.TorqueConverterCompoundGearWhineAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5756.UnbalancedMassCompoundGearWhineAnalysis]':
        '''List[UnbalancedMassCompoundGearWhineAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5756.UnbalancedMassCompoundGearWhineAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5760.WormGearSetCompoundGearWhineAnalysis]':
        '''List[WormGearSetCompoundGearWhineAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5760.WormGearSetCompoundGearWhineAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5763.ZerolBevelGearSetCompoundGearWhineAnalysis]':
        '''List[ZerolBevelGearSetCompoundGearWhineAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5763.ZerolBevelGearSetCompoundGearWhineAnalysis))
        return value
