'''_3971.py

AssemblyCompoundModalAnalysesAtSpeeds
'''


from typing import List

from mastapy.system_model.part_model import _1906
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns import _3849
from mastapy.system_model.analyses_and_results.modal_analyses_at_speeds_ns.compound import (
    _3972, _3974, _3977, _3983,
    _3984, _3985, _3990, _3995,
    _4005, _4009, _4015, _4016,
    _4023, _4024, _4031, _4034,
    _4035, _4036, _4038, _4042,
    _4043, _4044, _4051, _4046,
    _4050, _4056, _4057, _4062,
    _4065, _4068, _4072, _4076,
    _4080, _4083, _3966
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_SPEEDS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtSpeedsNS.Compound', 'AssemblyCompoundModalAnalysesAtSpeeds')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysesAtSpeeds',)


class AssemblyCompoundModalAnalysesAtSpeeds(_3966.AbstractAssemblyCompoundModalAnalysesAtSpeeds):
    '''AssemblyCompoundModalAnalysesAtSpeeds

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_SPEEDS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysesAtSpeeds.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_3849.AssemblyModalAnalysesAtSpeeds]':
        '''List[AssemblyModalAnalysesAtSpeeds]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3849.AssemblyModalAnalysesAtSpeeds))
        return value

    @property
    def assembly_modal_analyses_at_speeds_load_cases(self) -> 'List[_3849.AssemblyModalAnalysesAtSpeeds]':
        '''List[AssemblyModalAnalysesAtSpeeds]: 'AssemblyModalAnalysesAtSpeedsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtSpeedsLoadCases, constructor.new(_3849.AssemblyModalAnalysesAtSpeeds))
        return value

    @property
    def bearings(self) -> 'List[_3972.BearingCompoundModalAnalysesAtSpeeds]':
        '''List[BearingCompoundModalAnalysesAtSpeeds]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3972.BearingCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def belt_drives(self) -> 'List[_3974.BeltDriveCompoundModalAnalysesAtSpeeds]':
        '''List[BeltDriveCompoundModalAnalysesAtSpeeds]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3974.BeltDriveCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3977.BevelDifferentialGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysesAtSpeeds]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3977.BevelDifferentialGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def bolts(self) -> 'List[_3983.BoltCompoundModalAnalysesAtSpeeds]':
        '''List[BoltCompoundModalAnalysesAtSpeeds]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3983.BoltCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def bolted_joints(self) -> 'List[_3984.BoltedJointCompoundModalAnalysesAtSpeeds]':
        '''List[BoltedJointCompoundModalAnalysesAtSpeeds]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3984.BoltedJointCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def clutches(self) -> 'List[_3985.ClutchCompoundModalAnalysesAtSpeeds]':
        '''List[ClutchCompoundModalAnalysesAtSpeeds]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3985.ClutchCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def concept_couplings(self) -> 'List[_3990.ConceptCouplingCompoundModalAnalysesAtSpeeds]':
        '''List[ConceptCouplingCompoundModalAnalysesAtSpeeds]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3990.ConceptCouplingCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3995.ConceptGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[ConceptGearSetCompoundModalAnalysesAtSpeeds]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3995.ConceptGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def cv_ts(self) -> 'List[_4005.CVTCompoundModalAnalysesAtSpeeds]':
        '''List[CVTCompoundModalAnalysesAtSpeeds]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_4005.CVTCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_4009.CylindricalGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[CylindricalGearSetCompoundModalAnalysesAtSpeeds]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_4009.CylindricalGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def face_gear_sets(self) -> 'List[_4015.FaceGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[FaceGearSetCompoundModalAnalysesAtSpeeds]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_4015.FaceGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_4016.FlexiblePinAssemblyCompoundModalAnalysesAtSpeeds]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysesAtSpeeds]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_4016.FlexiblePinAssemblyCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_4023.HypoidGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[HypoidGearSetCompoundModalAnalysesAtSpeeds]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_4023.HypoidGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def imported_fe_components(self) -> 'List[_4024.ImportedFEComponentCompoundModalAnalysesAtSpeeds]':
        '''List[ImportedFEComponentCompoundModalAnalysesAtSpeeds]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_4024.ImportedFEComponentCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_4031.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_4031.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_4034.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtSpeeds]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_4034.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def mass_discs(self) -> 'List[_4035.MassDiscCompoundModalAnalysesAtSpeeds]':
        '''List[MassDiscCompoundModalAnalysesAtSpeeds]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_4035.MassDiscCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def measurement_components(self) -> 'List[_4036.MeasurementComponentCompoundModalAnalysesAtSpeeds]':
        '''List[MeasurementComponentCompoundModalAnalysesAtSpeeds]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_4036.MeasurementComponentCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def oil_seals(self) -> 'List[_4038.OilSealCompoundModalAnalysesAtSpeeds]':
        '''List[OilSealCompoundModalAnalysesAtSpeeds]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_4038.OilSealCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def planet_carriers(self) -> 'List[_4042.PlanetCarrierCompoundModalAnalysesAtSpeeds]':
        '''List[PlanetCarrierCompoundModalAnalysesAtSpeeds]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_4042.PlanetCarrierCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def point_loads(self) -> 'List[_4043.PointLoadCompoundModalAnalysesAtSpeeds]':
        '''List[PointLoadCompoundModalAnalysesAtSpeeds]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_4043.PointLoadCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def power_loads(self) -> 'List[_4044.PowerLoadCompoundModalAnalysesAtSpeeds]':
        '''List[PowerLoadCompoundModalAnalysesAtSpeeds]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_4044.PowerLoadCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_4051.ShaftHubConnectionCompoundModalAnalysesAtSpeeds]':
        '''List[ShaftHubConnectionCompoundModalAnalysesAtSpeeds]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_4051.ShaftHubConnectionCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_4046.RollingRingAssemblyCompoundModalAnalysesAtSpeeds]':
        '''List[RollingRingAssemblyCompoundModalAnalysesAtSpeeds]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_4046.RollingRingAssemblyCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def shafts(self) -> 'List[_4050.ShaftCompoundModalAnalysesAtSpeeds]':
        '''List[ShaftCompoundModalAnalysesAtSpeeds]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_4050.ShaftCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_4056.SpiralBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[SpiralBevelGearSetCompoundModalAnalysesAtSpeeds]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_4056.SpiralBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def spring_dampers(self) -> 'List[_4057.SpringDamperCompoundModalAnalysesAtSpeeds]':
        '''List[SpringDamperCompoundModalAnalysesAtSpeeds]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_4057.SpringDamperCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_4062.StraightBevelDiffGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysesAtSpeeds]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_4062.StraightBevelDiffGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_4065.StraightBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[StraightBevelGearSetCompoundModalAnalysesAtSpeeds]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_4065.StraightBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def synchronisers(self) -> 'List[_4068.SynchroniserCompoundModalAnalysesAtSpeeds]':
        '''List[SynchroniserCompoundModalAnalysesAtSpeeds]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_4068.SynchroniserCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def torque_converters(self) -> 'List[_4072.TorqueConverterCompoundModalAnalysesAtSpeeds]':
        '''List[TorqueConverterCompoundModalAnalysesAtSpeeds]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_4072.TorqueConverterCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_4076.UnbalancedMassCompoundModalAnalysesAtSpeeds]':
        '''List[UnbalancedMassCompoundModalAnalysesAtSpeeds]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_4076.UnbalancedMassCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_4080.WormGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[WormGearSetCompoundModalAnalysesAtSpeeds]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_4080.WormGearSetCompoundModalAnalysesAtSpeeds))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_4083.ZerolBevelGearSetCompoundModalAnalysesAtSpeeds]':
        '''List[ZerolBevelGearSetCompoundModalAnalysesAtSpeeds]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_4083.ZerolBevelGearSetCompoundModalAnalysesAtSpeeds))
        return value
