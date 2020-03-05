'''_3446.py

AssemblyParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model import _1958
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6031
from mastapy.system_model.analyses_and_results.parametric_study_tools import (
    _3489, _3447, _3449, _3452,
    _3459, _3458, _3462, _3467,
    _3470, _3480, _3484, _3496,
    _3497, _3504, _3505, _3512,
    _3515, _3516, _3517, _3520,
    _3533, _3536, _3537, _3538,
    _3544, _3540, _3545, _3550,
    _3553, _3556, _3559, _3563,
    _3567, _3570, _3574, _3577,
    _3441
)
from mastapy.system_model.analyses_and_results.system_deflections import _2190
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'AssemblyParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyParametricStudyTool',)


class AssemblyParametricStudyTool(_3441.AbstractAssemblyParametricStudyTool):
    '''AssemblyParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def assembly_design(self) -> '_1958.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1958.Assembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign else None

    @property
    def assembly_load_case(self) -> '_6031.AssemblyLoadCase':
        '''AssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6031.AssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase else None

    @property
    def all_duty_cycle_results(self) -> 'List[_3489.DutyCycleResultsForAllComponents]':
        '''List[DutyCycleResultsForAllComponents]: 'AllDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AllDutyCycleResults, constructor.new(_3489.DutyCycleResultsForAllComponents))
        return value

    @property
    def bearings(self) -> 'List[_3447.BearingParametricStudyTool]':
        '''List[BearingParametricStudyTool]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3447.BearingParametricStudyTool))
        return value

    @property
    def belt_drives(self) -> 'List[_3449.BeltDriveParametricStudyTool]':
        '''List[BeltDriveParametricStudyTool]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3449.BeltDriveParametricStudyTool))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3452.BevelDifferentialGearSetParametricStudyTool]':
        '''List[BevelDifferentialGearSetParametricStudyTool]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3452.BevelDifferentialGearSetParametricStudyTool))
        return value

    @property
    def bolts(self) -> 'List[_3459.BoltParametricStudyTool]':
        '''List[BoltParametricStudyTool]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3459.BoltParametricStudyTool))
        return value

    @property
    def bolted_joints(self) -> 'List[_3458.BoltedJointParametricStudyTool]':
        '''List[BoltedJointParametricStudyTool]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3458.BoltedJointParametricStudyTool))
        return value

    @property
    def clutches(self) -> 'List[_3462.ClutchParametricStudyTool]':
        '''List[ClutchParametricStudyTool]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3462.ClutchParametricStudyTool))
        return value

    @property
    def concept_couplings(self) -> 'List[_3467.ConceptCouplingParametricStudyTool]':
        '''List[ConceptCouplingParametricStudyTool]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3467.ConceptCouplingParametricStudyTool))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3470.ConceptGearSetParametricStudyTool]':
        '''List[ConceptGearSetParametricStudyTool]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3470.ConceptGearSetParametricStudyTool))
        return value

    @property
    def cv_ts(self) -> 'List[_3480.CVTParametricStudyTool]':
        '''List[CVTParametricStudyTool]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3480.CVTParametricStudyTool))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3484.CylindricalGearSetParametricStudyTool]':
        '''List[CylindricalGearSetParametricStudyTool]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3484.CylindricalGearSetParametricStudyTool))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3496.FaceGearSetParametricStudyTool]':
        '''List[FaceGearSetParametricStudyTool]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3496.FaceGearSetParametricStudyTool))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3497.FlexiblePinAssemblyParametricStudyTool]':
        '''List[FlexiblePinAssemblyParametricStudyTool]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3497.FlexiblePinAssemblyParametricStudyTool))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3504.HypoidGearSetParametricStudyTool]':
        '''List[HypoidGearSetParametricStudyTool]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3504.HypoidGearSetParametricStudyTool))
        return value

    @property
    def imported_fe_components(self) -> 'List[_3505.ImportedFEComponentParametricStudyTool]':
        '''List[ImportedFEComponentParametricStudyTool]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_3505.ImportedFEComponentParametricStudyTool))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3512.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3512.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3515.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3515.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool))
        return value

    @property
    def mass_discs(self) -> 'List[_3516.MassDiscParametricStudyTool]':
        '''List[MassDiscParametricStudyTool]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3516.MassDiscParametricStudyTool))
        return value

    @property
    def measurement_components(self) -> 'List[_3517.MeasurementComponentParametricStudyTool]':
        '''List[MeasurementComponentParametricStudyTool]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3517.MeasurementComponentParametricStudyTool))
        return value

    @property
    def oil_seals(self) -> 'List[_3520.OilSealParametricStudyTool]':
        '''List[OilSealParametricStudyTool]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3520.OilSealParametricStudyTool))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3533.PartToPartShearCouplingParametricStudyTool]':
        '''List[PartToPartShearCouplingParametricStudyTool]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3533.PartToPartShearCouplingParametricStudyTool))
        return value

    @property
    def planet_carriers(self) -> 'List[_3536.PlanetCarrierParametricStudyTool]':
        '''List[PlanetCarrierParametricStudyTool]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3536.PlanetCarrierParametricStudyTool))
        return value

    @property
    def point_loads(self) -> 'List[_3537.PointLoadParametricStudyTool]':
        '''List[PointLoadParametricStudyTool]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3537.PointLoadParametricStudyTool))
        return value

    @property
    def power_loads(self) -> 'List[_3538.PowerLoadParametricStudyTool]':
        '''List[PowerLoadParametricStudyTool]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3538.PowerLoadParametricStudyTool))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3544.ShaftHubConnectionParametricStudyTool]':
        '''List[ShaftHubConnectionParametricStudyTool]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3544.ShaftHubConnectionParametricStudyTool))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3540.RollingRingAssemblyParametricStudyTool]':
        '''List[RollingRingAssemblyParametricStudyTool]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3540.RollingRingAssemblyParametricStudyTool))
        return value

    @property
    def shafts(self) -> 'List[_3545.ShaftParametricStudyTool]':
        '''List[ShaftParametricStudyTool]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3545.ShaftParametricStudyTool))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3550.SpiralBevelGearSetParametricStudyTool]':
        '''List[SpiralBevelGearSetParametricStudyTool]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3550.SpiralBevelGearSetParametricStudyTool))
        return value

    @property
    def spring_dampers(self) -> 'List[_3553.SpringDamperParametricStudyTool]':
        '''List[SpringDamperParametricStudyTool]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3553.SpringDamperParametricStudyTool))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3556.StraightBevelDiffGearSetParametricStudyTool]':
        '''List[StraightBevelDiffGearSetParametricStudyTool]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3556.StraightBevelDiffGearSetParametricStudyTool))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3559.StraightBevelGearSetParametricStudyTool]':
        '''List[StraightBevelGearSetParametricStudyTool]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3559.StraightBevelGearSetParametricStudyTool))
        return value

    @property
    def synchronisers(self) -> 'List[_3563.SynchroniserParametricStudyTool]':
        '''List[SynchroniserParametricStudyTool]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3563.SynchroniserParametricStudyTool))
        return value

    @property
    def torque_converters(self) -> 'List[_3567.TorqueConverterParametricStudyTool]':
        '''List[TorqueConverterParametricStudyTool]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3567.TorqueConverterParametricStudyTool))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3570.UnbalancedMassParametricStudyTool]':
        '''List[UnbalancedMassParametricStudyTool]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3570.UnbalancedMassParametricStudyTool))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3574.WormGearSetParametricStudyTool]':
        '''List[WormGearSetParametricStudyTool]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3574.WormGearSetParametricStudyTool))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3577.ZerolBevelGearSetParametricStudyTool]':
        '''List[ZerolBevelGearSetParametricStudyTool]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3577.ZerolBevelGearSetParametricStudyTool))
        return value

    @property
    def assembly_system_deflection_results(self) -> 'List[_2190.AssemblySystemDeflection]':
        '''List[AssemblySystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionResults, constructor.new(_2190.AssemblySystemDeflection))
        return value
