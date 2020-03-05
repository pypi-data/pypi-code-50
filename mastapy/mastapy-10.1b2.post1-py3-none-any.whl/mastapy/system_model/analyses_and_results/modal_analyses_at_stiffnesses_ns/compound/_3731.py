'''_3731.py

AssemblyCompoundModalAnalysesAtStiffnesses
'''


from typing import List

from mastapy.system_model.part_model import _1906
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns import _3610
from mastapy.system_model.analyses_and_results.modal_analyses_at_stiffnesses_ns.compound import (
    _3732, _3734, _3737, _3743,
    _3744, _3745, _3750, _3755,
    _3765, _3769, _3775, _3776,
    _3783, _3784, _3791, _3794,
    _3795, _3796, _3798, _3802,
    _3803, _3804, _3811, _3806,
    _3810, _3816, _3817, _3822,
    _3825, _3828, _3832, _3836,
    _3840, _3843, _3726
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtStiffnessesNS.Compound', 'AssemblyCompoundModalAnalysesAtStiffnesses')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundModalAnalysesAtStiffnesses',)


class AssemblyCompoundModalAnalysesAtStiffnesses(_3726.AbstractAssemblyCompoundModalAnalysesAtStiffnesses):
    '''AssemblyCompoundModalAnalysesAtStiffnesses

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_MODAL_ANALYSES_AT_STIFFNESSES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundModalAnalysesAtStiffnesses.TYPE'):
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
    def load_case_analyses_ready(self) -> 'List[_3610.AssemblyModalAnalysesAtStiffnesses]':
        '''List[AssemblyModalAnalysesAtStiffnesses]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3610.AssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def assembly_modal_analyses_at_stiffnesses_load_cases(self) -> 'List[_3610.AssemblyModalAnalysesAtStiffnesses]':
        '''List[AssemblyModalAnalysesAtStiffnesses]: 'AssemblyModalAnalysesAtStiffnessesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyModalAnalysesAtStiffnessesLoadCases, constructor.new(_3610.AssemblyModalAnalysesAtStiffnesses))
        return value

    @property
    def bearings(self) -> 'List[_3732.BearingCompoundModalAnalysesAtStiffnesses]':
        '''List[BearingCompoundModalAnalysesAtStiffnesses]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3732.BearingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def belt_drives(self) -> 'List[_3734.BeltDriveCompoundModalAnalysesAtStiffnesses]':
        '''List[BeltDriveCompoundModalAnalysesAtStiffnesses]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3734.BeltDriveCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3737.BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3737.BevelDifferentialGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bolts(self) -> 'List[_3743.BoltCompoundModalAnalysesAtStiffnesses]':
        '''List[BoltCompoundModalAnalysesAtStiffnesses]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3743.BoltCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def bolted_joints(self) -> 'List[_3744.BoltedJointCompoundModalAnalysesAtStiffnesses]':
        '''List[BoltedJointCompoundModalAnalysesAtStiffnesses]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3744.BoltedJointCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def clutches(self) -> 'List[_3745.ClutchCompoundModalAnalysesAtStiffnesses]':
        '''List[ClutchCompoundModalAnalysesAtStiffnesses]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3745.ClutchCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_couplings(self) -> 'List[_3750.ConceptCouplingCompoundModalAnalysesAtStiffnesses]':
        '''List[ConceptCouplingCompoundModalAnalysesAtStiffnesses]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3750.ConceptCouplingCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3755.ConceptGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[ConceptGearSetCompoundModalAnalysesAtStiffnesses]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3755.ConceptGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def cv_ts(self) -> 'List[_3765.CVTCompoundModalAnalysesAtStiffnesses]':
        '''List[CVTCompoundModalAnalysesAtStiffnesses]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3765.CVTCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3769.CylindricalGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[CylindricalGearSetCompoundModalAnalysesAtStiffnesses]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3769.CylindricalGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3775.FaceGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[FaceGearSetCompoundModalAnalysesAtStiffnesses]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3775.FaceGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3776.FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses]':
        '''List[FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3776.FlexiblePinAssemblyCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3783.HypoidGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[HypoidGearSetCompoundModalAnalysesAtStiffnesses]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3783.HypoidGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3784.ImportedFEComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[ImportedFEComponentCompoundModalAnalysesAtStiffnesses]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3784.ImportedFEComponentCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3791.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3791.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3794.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3794.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def mass_discs(self) -> 'List[_3795.MassDiscCompoundModalAnalysesAtStiffnesses]':
        '''List[MassDiscCompoundModalAnalysesAtStiffnesses]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3795.MassDiscCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def measurement_components(self) -> 'List[_3796.MeasurementComponentCompoundModalAnalysesAtStiffnesses]':
        '''List[MeasurementComponentCompoundModalAnalysesAtStiffnesses]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3796.MeasurementComponentCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def oil_seals(self) -> 'List[_3798.OilSealCompoundModalAnalysesAtStiffnesses]':
        '''List[OilSealCompoundModalAnalysesAtStiffnesses]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3798.OilSealCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def planet_carriers(self) -> 'List[_3802.PlanetCarrierCompoundModalAnalysesAtStiffnesses]':
        '''List[PlanetCarrierCompoundModalAnalysesAtStiffnesses]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3802.PlanetCarrierCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def point_loads(self) -> 'List[_3803.PointLoadCompoundModalAnalysesAtStiffnesses]':
        '''List[PointLoadCompoundModalAnalysesAtStiffnesses]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3803.PointLoadCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def power_loads(self) -> 'List[_3804.PowerLoadCompoundModalAnalysesAtStiffnesses]':
        '''List[PowerLoadCompoundModalAnalysesAtStiffnesses]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3804.PowerLoadCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3811.ShaftHubConnectionCompoundModalAnalysesAtStiffnesses]':
        '''List[ShaftHubConnectionCompoundModalAnalysesAtStiffnesses]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3811.ShaftHubConnectionCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3806.RollingRingAssemblyCompoundModalAnalysesAtStiffnesses]':
        '''List[RollingRingAssemblyCompoundModalAnalysesAtStiffnesses]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3806.RollingRingAssemblyCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def shafts(self) -> 'List[_3810.ShaftCompoundModalAnalysesAtStiffnesses]':
        '''List[ShaftCompoundModalAnalysesAtStiffnesses]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3810.ShaftCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3816.SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3816.SpiralBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def spring_dampers(self) -> 'List[_3817.SpringDamperCompoundModalAnalysesAtStiffnesses]':
        '''List[SpringDamperCompoundModalAnalysesAtStiffnesses]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3817.SpringDamperCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3822.StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3822.StraightBevelDiffGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3825.StraightBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[StraightBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3825.StraightBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def synchronisers(self) -> 'List[_3828.SynchroniserCompoundModalAnalysesAtStiffnesses]':
        '''List[SynchroniserCompoundModalAnalysesAtStiffnesses]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3828.SynchroniserCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def torque_converters(self) -> 'List[_3832.TorqueConverterCompoundModalAnalysesAtStiffnesses]':
        '''List[TorqueConverterCompoundModalAnalysesAtStiffnesses]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3832.TorqueConverterCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3836.UnbalancedMassCompoundModalAnalysesAtStiffnesses]':
        '''List[UnbalancedMassCompoundModalAnalysesAtStiffnesses]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3836.UnbalancedMassCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3840.WormGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[WormGearSetCompoundModalAnalysesAtStiffnesses]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3840.WormGearSetCompoundModalAnalysesAtStiffnesses))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3843.ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses]':
        '''List[ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3843.ZerolBevelGearSetCompoundModalAnalysesAtStiffnesses))
        return value
