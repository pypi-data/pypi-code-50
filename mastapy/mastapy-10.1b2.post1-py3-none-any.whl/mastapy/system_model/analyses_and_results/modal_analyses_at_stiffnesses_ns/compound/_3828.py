'''_3828.py

AssemblyCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model import _1958
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3704
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import (
    _3829, _3831, _3834, _3840,
    _3841, _3842, _3847, _3852,
    _3862, _3866, _3872, _3873,
    _3880, _3881, _3888, _3891,
    _3892, _3893, _3895, _3897,
    _3902, _3903, _3904, _3911,
    _3906, _3910, _3916, _3917,
    _3922, _3925, _3928, _3932,
    _3936, _3940, _3943, _3823
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'AssemblyCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysesAtStiffnesses',)


class AssemblyCompoundModalAnalysesAtStiffnesses(_3823.AbstractAssemblyCompoundModalAnalysesAtStiffnesses):
    '''AssemblyCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysesAtStiffnesses.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_3704.AssemblyModalAnalysesAtStiffnesses]':
        '''List[AssemblyModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3704.AssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def assembly_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3704.AssemblyModalAnalysesAtStiffnesses]':
        '''List[AssemblyModalAnalysesAtStiffnesses]: 'AssemblyModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtStiffnessesLoadCases, constructor.new(_3704.AssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def bearings(self) -> 'List[_3829.BearingCompoundModalAnalysesAtStiffnesses]':
        '''List[BearingCompoundModalAnalysesAtStiffnesses]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3829.BearingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def belt_drives(self) -> 'List[_3831.BeltDriveCompoundModalAnalysesAtStiffnesses]':
        '''List[BeltDriveCompoundModalAnalysesAtStiffnesses]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3831.BeltDriveCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3834.BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3834.BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bolts(self) -> 'List[_3840.BoltCompoundModalAnalysesAtStiffnesses]':
        '''List[BoltCompoundModalAnalysesAtStiffnesses]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3840.BoltCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bolted_joints(self) -> 'List[_3841.BoltedJointCompoundModalAnalysesAtStiffnesses]':
        '''List[BoltedJointCompoundModalAnalysesAtStiffnesses]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3841.BoltedJointCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def clutches(self) -> 'List[_3842.ClutchCompoundModalAnalysesAtStiffnesses]':
        '''List[ClutchCompoundModalAnalysesAtStiffnesses]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3842.ClutchCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_couplings(self) -> 'List[_3847.ConceptCouplingCompoundModalAnalysesAtStiffnesses]':
        '''List[ConceptCouplingCompoundModalAnalysesAtStiffnesses]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3847.ConceptCouplingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3852.ConceptGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[ConceptGearSetCompoundModalAnalysesAtStiffnesses]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3852.ConceptGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def cv_ts(self) -> 'List[_3862.CVTCompoundModalAnalysesAtStiffnesses]':
        '''List[CVTCompoundModalAnalysesAtStiffnesses]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3862.CVTCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3866.CylindricalGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[CylindricalGearSetCompoundModalAnalysesAtStiffnesses]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3866.CylindricalGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3872.FaceGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[FaceGearSetCompoundModalAnalysesAtStiffnesses]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3872.FaceGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3873.FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3873.FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3880.HypoidGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[HypoidGearSetCompoundModalAnalysesAtStiffnesses]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3880.HypoidGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3881.ImportedFEComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentCompoundModalAnalysesAtStiffnesses]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3881.ImportedFEComponentCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3888.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3888.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3891.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3891.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def mass_discs(self) -> 'List[_3892.MassDiscCompoundModalAnalysesAtStiffnesses]':
        '''List[MassDiscCompoundModalAnalysesAtStiffnesses]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3892.MassDiscCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def measurement_components(self) -> 'List[_3893.MeasurementComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[MeasurementComponentCompoundModalAnalysesAtStiffnesses]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3893.MeasurementComponentCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def oil_seals(self) -> 'List[_3895.OilSealCompoundModalAnalysesAtStiffnesses]':
        '''List[OilSealCompoundModalAnalysesAtStiffnesses]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3895.OilSealCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3897.PartToPartShearCouplingCompoundModalAnalysesAtStiffnesses]':
        '''List[PartToPartShearCouplingCompoundModalAnalysesAtStiffnesses]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3897.PartToPartShearCouplingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def planet_carriers(self) -> 'List[_3902.PlanetCarrierCompoundModalAnalysesAtStiffnesses]':
        '''List[PlanetCarrierCompoundModalAnalysesAtStiffnesses]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3902.PlanetCarrierCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def point_loads(self) -> 'List[_3903.PointLoadCompoundModalAnalysesAtStiffnesses]':
        '''List[PointLoadCompoundModalAnalysesAtStiffnesses]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3903.PointLoadCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def power_loads(self) -> 'List[_3904.PowerLoadCompoundModalAnalysesAtStiffnesses]':
        '''List[PowerLoadCompoundModalAnalysesAtStiffnesses]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3904.PowerLoadCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3911.ShaftHubConnectionCompoundModalAnalysesAtStiffnesses]':
        '''List[ShaftHubConnectionCompoundModalAnalysesAtStiffnesses]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3911.ShaftHubConnectionCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3906.RollingRingAssemblyCompoundModalAnalysesAtStiffnesses]':
        '''List[RollingRingAssemblyCompoundModalAnalysesAtStiffnesses]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3906.RollingRingAssemblyCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def shafts(self) -> 'List[_3910.ShaftCompoundModalAnalysesAtStiffnesses]':
        '''List[ShaftCompoundModalAnalysesAtStiffnesses]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3910.ShaftCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3916.SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3916.SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spring_dampers(self) -> 'List[_3917.SpringDamperCompoundModalAnalysesAtStiffnesses]':
        '''List[SpringDamperCompoundModalAnalysesAtStiffnesses]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3917.SpringDamperCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3922.StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3922.StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3925.StraightBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[StraightBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3925.StraightBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def synchronisers(self) -> 'List[_3928.SynchroniserCompoundModalAnalysesAtStiffnesses]':
        '''List[SynchroniserCompoundModalAnalysesAtStiffnesses]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3928.SynchroniserCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def torque_converters(self) -> 'List[_3932.TorqueConverterCompoundModalAnalysesAtStiffnesses]':
        '''List[TorqueConverterCompoundModalAnalysesAtStiffnesses]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3932.TorqueConverterCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3936.UnbalancedMassCompoundModalAnalysesAtStiffnesses]':
        '''List[UnbalancedMassCompoundModalAnalysesAtStiffnesses]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3936.UnbalancedMassCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3940.WormGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[WormGearSetCompoundModalAnalysesAtStiffnesses]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3940.WormGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3943.ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3943.ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value
