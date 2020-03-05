'''_4967.py

AssemblyCompoundMultiBodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _1906
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _4826
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
    _4968, _4970, _4973, _4979,
    _4980, _4981, _4986, _4991,
    _5001, _5005, _5011, _5012,
    _5019, _5020, _5027, _5030,
    _5031, _5032, _5034, _5038,
    _5039, _5040, _5047, _5042,
    _5046, _5052, _5053, _5058,
    _5061, _5064, _5068, _5072,
    _5076, _5079, _4962
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MULTI_BODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'AssemblyCompoundMultiBodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundMultiBodyDynamicsAnalysis',)


class AssemblyCompoundMultiBodyDynamicsAnalysis(_4962.AbstractAssemblyCompoundMultiBodyDynamicsAnalysis):
    '''AssemblyCompoundMultiBodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MULTI_BODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundMultiBodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_design(self) -> '_1906.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1906.Assembly)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def assembly_design(self) -> '_1906.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1906.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def load_case_analyses_ready(self) -> 'List[_4826.AssemblyMultiBodyDynamicsAnalysis]':
        '''List[AssemblyMultiBodyDynamicsAnalysis]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_4826.AssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def assembly_multi_body_dynamics_analysis_load_cases(self) -> 'List[_4826.AssemblyMultiBodyDynamicsAnalysis]':
        '''List[AssemblyMultiBodyDynamicsAnalysis]: 'AssemblyMultiBodyDynamicsAnalysisLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyMultiBodyDynamicsAnalysisLoadCases, constructor.new(_4826.AssemblyMultiBodyDynamicsAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_4968.BearingCompoundMultiBodyDynamicsAnalysis]':
        '''List[BearingCompoundMultiBodyDynamicsAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_4968.BearingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_4970.BeltDriveCompoundMultiBodyDynamicsAnalysis]':
        '''List[BeltDriveCompoundMultiBodyDynamicsAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_4970.BeltDriveCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_4973.BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_4973.BevelDifferentialGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_4979.BoltCompoundMultiBodyDynamicsAnalysis]':
        '''List[BoltCompoundMultiBodyDynamicsAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_4979.BoltCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_4980.BoltedJointCompoundMultiBodyDynamicsAnalysis]':
        '''List[BoltedJointCompoundMultiBodyDynamicsAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_4980.BoltedJointCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_4981.ClutchCompoundMultiBodyDynamicsAnalysis]':
        '''List[ClutchCompoundMultiBodyDynamicsAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_4981.ClutchCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_4986.ConceptCouplingCompoundMultiBodyDynamicsAnalysis]':
        '''List[ConceptCouplingCompoundMultiBodyDynamicsAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_4986.ConceptCouplingCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_4991.ConceptGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[ConceptGearSetCompoundMultiBodyDynamicsAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_4991.ConceptGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_5001.CVTCompoundMultiBodyDynamicsAnalysis]':
        '''List[CVTCompoundMultiBodyDynamicsAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_5001.CVTCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_5005.CylindricalGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[CylindricalGearSetCompoundMultiBodyDynamicsAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_5005.CylindricalGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_5011.FaceGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[FaceGearSetCompoundMultiBodyDynamicsAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_5011.FaceGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_5012.FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis]':
        '''List[FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_5012.FlexiblePinAssemblyCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_5019.HypoidGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[HypoidGearSetCompoundMultiBodyDynamicsAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_5019.HypoidGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def imported_fe_components(self) -> 'List[_5020.ImportedFEComponentCompoundMultiBodyDynamicsAnalysis]':
        '''List[ImportedFEComponentCompoundMultiBodyDynamicsAnalysis]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_5020.ImportedFEComponentCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_5027.KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_5027.KlingelnbergCycloPalloidHypoidGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_5030.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_5030.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_5031.MassDiscCompoundMultiBodyDynamicsAnalysis]':
        '''List[MassDiscCompoundMultiBodyDynamicsAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_5031.MassDiscCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_5032.MeasurementComponentCompoundMultiBodyDynamicsAnalysis]':
        '''List[MeasurementComponentCompoundMultiBodyDynamicsAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_5032.MeasurementComponentCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_5034.OilSealCompoundMultiBodyDynamicsAnalysis]':
        '''List[OilSealCompoundMultiBodyDynamicsAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_5034.OilSealCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_5038.PlanetCarrierCompoundMultiBodyDynamicsAnalysis]':
        '''List[PlanetCarrierCompoundMultiBodyDynamicsAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_5038.PlanetCarrierCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_5039.PointLoadCompoundMultiBodyDynamicsAnalysis]':
        '''List[PointLoadCompoundMultiBodyDynamicsAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_5039.PointLoadCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_5040.PowerLoadCompoundMultiBodyDynamicsAnalysis]':
        '''List[PowerLoadCompoundMultiBodyDynamicsAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5040.PowerLoadCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_5047.ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis]':
        '''List[ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_5047.ShaftHubConnectionCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_5042.RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis]':
        '''List[RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_5042.RollingRingAssemblyCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_5046.ShaftCompoundMultiBodyDynamicsAnalysis]':
        '''List[ShaftCompoundMultiBodyDynamicsAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_5046.ShaftCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_5052.SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_5052.SpiralBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_5053.SpringDamperCompoundMultiBodyDynamicsAnalysis]':
        '''List[SpringDamperCompoundMultiBodyDynamicsAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_5053.SpringDamperCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_5058.StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_5058.StraightBevelDiffGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_5061.StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_5061.StraightBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_5064.SynchroniserCompoundMultiBodyDynamicsAnalysis]':
        '''List[SynchroniserCompoundMultiBodyDynamicsAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_5064.SynchroniserCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_5068.TorqueConverterCompoundMultiBodyDynamicsAnalysis]':
        '''List[TorqueConverterCompoundMultiBodyDynamicsAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_5068.TorqueConverterCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_5072.UnbalancedMassCompoundMultiBodyDynamicsAnalysis]':
        '''List[UnbalancedMassCompoundMultiBodyDynamicsAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_5072.UnbalancedMassCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_5076.WormGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[WormGearSetCompoundMultiBodyDynamicsAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_5076.WormGearSetCompoundMultiBodyDynamicsAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_5079.ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis]':
        '''List[ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_5079.ZerolBevelGearSetCompoundMultiBodyDynamicsAnalysis))
        return value
