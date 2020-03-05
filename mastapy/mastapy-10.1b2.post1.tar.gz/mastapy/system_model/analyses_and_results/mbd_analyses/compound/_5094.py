'''_5094.py

AssemblyCompoundMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1958
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _4950
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
    _5095, _5097, _5100, _5106,
    _5107, _5108, _5113, _5118,
    _5128, _5132, _5138, _5139,
    _5146, _5147, _5154, _5157,
    _5158, _5159, _5161, _5163,
    _5168, _5169, _5170, _5177,
    _5172, _5176, _5182, _5183,
    _5188, _5191, _5194, _5198,
    _5202, _5206, _5209, _5089
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AssemblyCompoundMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundMultiBodyDynamicsAnalysis',)


class AssemblyCompoundMultiBodyDynamicsAnalysis(_5089.AbstractAssemblyCompoundMultiBodyDynamicsAnalysis):
    '''AssemblyCompoundMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundMultiBodyDynamicsAnalysis.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_4950.AssemblyMultiBodyDynamicsAnalysis]':
        '''List[AssemblyMultiBodyDynamicsAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4950.AssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def assembly_multi_body_dynamics_analysis_load_cases(self) -> 'List[_4950.AssemblyMultiBodyDynamicsAnalysis]':
        '''List[AssemblyMultiBodyDynamicsAnalysis]: 'AssemblyMultiBodyDynamicsAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyMultiBodyDynamicsAnalysisLoadCases, constructor.new(_4950.AssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_5095.BearingCompoundMultiBodyDynamicsAnalysis]':
        '''List[BearingCompoundMultiBodyDynamicsAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_5095.BearingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_5097.BeltDriveCompoundMultiBodyDynamicsAnalysis]':
        '''List[BeltDriveCompoundMultiBodyDynamicsAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_5097.BeltDriveCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_5100.BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_5100.BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_5106.BoltCompoundMultiBodyDynamicsAnalysis]':
        '''List[BoltCompoundMultiBodyDynamicsAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_5106.BoltCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_5107.BoltedJointCompoundMultiBodyDynamicsAnalysis]':
        '''List[BoltedJointCompoundMultiBodyDynamicsAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_5107.BoltedJointCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_5108.ClutchCompoundMultiBodyDynamicsAnalysis]':
        '''List[ClutchCompoundMultiBodyDynamicsAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_5108.ClutchCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_5113.ConceptCouplingCompoundMultiBodyDynamicsAnalysis]':
        '''List[ConceptCouplingCompoundMultiBodyDynamicsAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_5113.ConceptCouplingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_5118.ConceptGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearSetCompoundMultiBodyDynamicsAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_5118.ConceptGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5128.CVTCompoundMultiBodyDynamicsAnalysis]':
        '''List[CVTCompoundMultiBodyDynamicsAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5128.CVTCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5132.CylindricalGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[CylindricalGearSetCompoundMultiBodyDynamicsAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5132.CylindricalGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5138.FaceGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[FaceGearSetCompoundMultiBodyDynamicsAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5138.FaceGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5139.FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis]':
        '''List[FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5139.FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5146.HypoidGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearSetCompoundMultiBodyDynamicsAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5146.HypoidGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5147.ImportedFEComponentCompoundMultiBodyDynamicsAnalysis]':
        '''List[ImportedFEComponentCompoundMultiBodyDynamicsAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5147.ImportedFEComponentCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5154.KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5154.KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5157.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5157.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5158.MassDiscCompoundMultiBodyDynamicsAnalysis]':
        '''List[MassDiscCompoundMultiBodyDynamicsAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5158.MassDiscCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5159.MeasurementComponentCompoundMultiBodyDynamicsAnalysis]':
        '''List[MeasurementComponentCompoundMultiBodyDynamicsAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5159.MeasurementComponentCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5161.OilSealCompoundMultiBodyDynamicsAnalysis]':
        '''List[OilSealCompoundMultiBodyDynamicsAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5161.OilSealCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_5163.PartToPartShearCouplingCompoundMultiBodyDynamicsAnalysis]':
        '''List[PartToPartShearCouplingCompoundMultiBodyDynamicsAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_5163.PartToPartShearCouplingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5168.PlanetCarrierCompoundMultiBodyDynamicsAnalysis]':
        '''List[PlanetCarrierCompoundMultiBodyDynamicsAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5168.PlanetCarrierCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5169.PointLoadCompoundMultiBodyDynamicsAnalysis]':
        '''List[PointLoadCompoundMultiBodyDynamicsAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5169.PointLoadCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5170.PowerLoadCompoundMultiBodyDynamicsAnalysis]':
        '''List[PowerLoadCompoundMultiBodyDynamicsAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5170.PowerLoadCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5177.ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis]':
        '''List[ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5177.ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5172.RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis]':
        '''List[RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5172.RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5176.ShaftCompoundMultiBodyDynamicsAnalysis]':
        '''List[ShaftCompoundMultiBodyDynamicsAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5176.ShaftCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5182.SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5182.SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5183.SpringDamperCompoundMultiBodyDynamicsAnalysis]':
        '''List[SpringDamperCompoundMultiBodyDynamicsAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5183.SpringDamperCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5188.StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5188.StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5191.StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5191.StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5194.SynchroniserCompoundMultiBodyDynamicsAnalysis]':
        '''List[SynchroniserCompoundMultiBodyDynamicsAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5194.SynchroniserCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5198.TorqueConverterCompoundMultiBodyDynamicsAnalysis]':
        '''List[TorqueConverterCompoundMultiBodyDynamicsAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5198.TorqueConverterCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5202.UnbalancedMassCompoundMultiBodyDynamicsAnalysis]':
        '''List[UnbalancedMassCompoundMultiBodyDynamicsAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5202.UnbalancedMassCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5206.WormGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[WormGearSetCompoundMultiBodyDynamicsAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5206.WormGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5209.ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5209.ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value
