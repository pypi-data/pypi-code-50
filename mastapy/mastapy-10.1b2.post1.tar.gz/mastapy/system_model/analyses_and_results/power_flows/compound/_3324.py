'''_3324.py

AssemblyCompoundPowerFlow
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1958
from mastapy.gears.analysis import _949
from mastapy.system_model.analyses_and_results.power_flows import _3199
from mastapy.system_model.analyses_and_results.power_flows.compound import (
    _3325, _3327, _3330, _3336,
    _3337, _3339, _3344, _3349,
    _3359, _3363, _3369, _3370,
    _3377, _3378, _3385, _3388,
    _3389, _3390, _3392, _3394,
    _3399, _3400, _3401, _3408,
    _3403, _3407, _3413, _3414,
    _3419, _3422, _3425, _3429,
    _3433, _3437, _3440, _3319
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'AssemblyCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundPowerFlow',)


class AssemblyCompoundPowerFlow(_3319.AbstractAssemblyCompoundPowerFlow):
    '''AssemblyCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def input_power_load_ratio_warning(self) -> 'str':
        '''str: 'InputPowerLoadRatioWarning' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InputPowerLoadRatioWarning

    @property
    def output_power_load_ratio_warning(self) -> 'str':
        '''str: 'OutputPowerLoadRatioWarning' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OutputPowerLoadRatioWarning

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
    def rating_for_all_gear_sets(self) -> '_949.GearSetGroupDutyCycle':
        '''GearSetGroupDutyCycle: 'RatingForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_949.GearSetGroupDutyCycle)(self.wrapped.RatingForAllGearSets) if self.wrapped.RatingForAllGearSets else None

    @property
    def load_case_analyses_ready(self) -> 'List[_3199.AssemblyPowerFlow]':
        '''List[AssemblyPowerFlow]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_3199.AssemblyPowerFlow))
        return value

    @property
    def assembly_power_flow_load_cases(self) -> 'List[_3199.AssemblyPowerFlow]':
        '''List[AssemblyPowerFlow]: 'AssemblyPowerFlowLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyPowerFlowLoadCases, constructor.new(_3199.AssemblyPowerFlow))
        return value

    @property
    def bearings(self) -> 'List[_3325.BearingCompoundPowerFlow]':
        '''List[BearingCompoundPowerFlow]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3325.BearingCompoundPowerFlow))
        return value

    @property
    def belt_drives(self) -> 'List[_3327.BeltDriveCompoundPowerFlow]':
        '''List[BeltDriveCompoundPowerFlow]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3327.BeltDriveCompoundPowerFlow))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3330.BevelDifferentialGearSetCompoundPowerFlow]':
        '''List[BevelDifferentialGearSetCompoundPowerFlow]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3330.BevelDifferentialGearSetCompoundPowerFlow))
        return value

    @property
    def bolts(self) -> 'List[_3336.BoltCompoundPowerFlow]':
        '''List[BoltCompoundPowerFlow]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3336.BoltCompoundPowerFlow))
        return value

    @property
    def bolted_joints(self) -> 'List[_3337.BoltedJointCompoundPowerFlow]':
        '''List[BoltedJointCompoundPowerFlow]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3337.BoltedJointCompoundPowerFlow))
        return value

    @property
    def clutches(self) -> 'List[_3339.ClutchCompoundPowerFlow]':
        '''List[ClutchCompoundPowerFlow]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3339.ClutchCompoundPowerFlow))
        return value

    @property
    def concept_couplings(self) -> 'List[_3344.ConceptCouplingCompoundPowerFlow]':
        '''List[ConceptCouplingCompoundPowerFlow]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3344.ConceptCouplingCompoundPowerFlow))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3349.ConceptGearSetCompoundPowerFlow]':
        '''List[ConceptGearSetCompoundPowerFlow]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3349.ConceptGearSetCompoundPowerFlow))
        return value

    @property
    def cv_ts(self) -> 'List[_3359.CVTCompoundPowerFlow]':
        '''List[CVTCompoundPowerFlow]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3359.CVTCompoundPowerFlow))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3363.CylindricalGearSetCompoundPowerFlow]':
        '''List[CylindricalGearSetCompoundPowerFlow]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3363.CylindricalGearSetCompoundPowerFlow))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3369.FaceGearSetCompoundPowerFlow]':
        '''List[FaceGearSetCompoundPowerFlow]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3369.FaceGearSetCompoundPowerFlow))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3370.FlexiblePinAssemblyCompoundPowerFlow]':
        '''List[FlexiblePinAssemblyCompoundPowerFlow]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3370.FlexiblePinAssemblyCompoundPowerFlow))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3377.HypoidGearSetCompoundPowerFlow]':
        '''List[HypoidGearSetCompoundPowerFlow]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3377.HypoidGearSetCompoundPowerFlow))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3378.ImportedFEComponentCompoundPowerFlow]':
        '''List[ImportedFEComponentCompoundPowerFlow]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3378.ImportedFEComponentCompoundPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3385.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3385.KlingelnbergCycloPalloidHypoidGearSetCompoundPowerFlow))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3388.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3388.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundPowerFlow))
        return value

    @property
    def mass_discs(self) -> 'List[_3389.MassDiscCompoundPowerFlow]':
        '''List[MassDiscCompoundPowerFlow]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3389.MassDiscCompoundPowerFlow))
        return value

    @property
    def measurement_components(self) -> 'List[_3390.MeasurementComponentCompoundPowerFlow]':
        '''List[MeasurementComponentCompoundPowerFlow]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3390.MeasurementComponentCompoundPowerFlow))
        return value

    @property
    def oil_seals(self) -> 'List[_3392.OilSealCompoundPowerFlow]':
        '''List[OilSealCompoundPowerFlow]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3392.OilSealCompoundPowerFlow))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3394.PartToPartShearCouplingCompoundPowerFlow]':
        '''List[PartToPartShearCouplingCompoundPowerFlow]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3394.PartToPartShearCouplingCompoundPowerFlow))
        return value

    @property
    def planet_carriers(self) -> 'List[_3399.PlanetCarrierCompoundPowerFlow]':
        '''List[PlanetCarrierCompoundPowerFlow]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3399.PlanetCarrierCompoundPowerFlow))
        return value

    @property
    def point_loads(self) -> 'List[_3400.PointLoadCompoundPowerFlow]':
        '''List[PointLoadCompoundPowerFlow]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3400.PointLoadCompoundPowerFlow))
        return value

    @property
    def power_loads(self) -> 'List[_3401.PowerLoadCompoundPowerFlow]':
        '''List[PowerLoadCompoundPowerFlow]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3401.PowerLoadCompoundPowerFlow))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3408.ShaftHubConnectionCompoundPowerFlow]':
        '''List[ShaftHubConnectionCompoundPowerFlow]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3408.ShaftHubConnectionCompoundPowerFlow))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3403.RollingRingAssemblyCompoundPowerFlow]':
        '''List[RollingRingAssemblyCompoundPowerFlow]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3403.RollingRingAssemblyCompoundPowerFlow))
        return value

    @property
    def shafts(self) -> 'List[_3407.ShaftCompoundPowerFlow]':
        '''List[ShaftCompoundPowerFlow]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3407.ShaftCompoundPowerFlow))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3413.SpiralBevelGearSetCompoundPowerFlow]':
        '''List[SpiralBevelGearSetCompoundPowerFlow]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3413.SpiralBevelGearSetCompoundPowerFlow))
        return value

    @property
    def spring_dampers(self) -> 'List[_3414.SpringDamperCompoundPowerFlow]':
        '''List[SpringDamperCompoundPowerFlow]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3414.SpringDamperCompoundPowerFlow))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3419.StraightBevelDiffGearSetCompoundPowerFlow]':
        '''List[StraightBevelDiffGearSetCompoundPowerFlow]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3419.StraightBevelDiffGearSetCompoundPowerFlow))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3422.StraightBevelGearSetCompoundPowerFlow]':
        '''List[StraightBevelGearSetCompoundPowerFlow]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3422.StraightBevelGearSetCompoundPowerFlow))
        return value

    @property
    def synchronisers(self) -> 'List[_3425.SynchroniserCompoundPowerFlow]':
        '''List[SynchroniserCompoundPowerFlow]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3425.SynchroniserCompoundPowerFlow))
        return value

    @property
    def torque_converters(self) -> 'List[_3429.TorqueConverterCompoundPowerFlow]':
        '''List[TorqueConverterCompoundPowerFlow]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3429.TorqueConverterCompoundPowerFlow))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3433.UnbalancedMassCompoundPowerFlow]':
        '''List[UnbalancedMassCompoundPowerFlow]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3433.UnbalancedMassCompoundPowerFlow))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3437.WormGearSetCompoundPowerFlow]':
        '''List[WormGearSetCompoundPowerFlow]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3437.WormGearSetCompoundPowerFlow))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3440.ZerolBevelGearSetCompoundPowerFlow]':
        '''List[ZerolBevelGearSetCompoundPowerFlow]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3440.ZerolBevelGearSetCompoundPowerFlow))
        return value
