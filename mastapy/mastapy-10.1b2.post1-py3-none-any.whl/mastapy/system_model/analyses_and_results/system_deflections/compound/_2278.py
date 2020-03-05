'''_2278.py

AssemblyCompoundSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1906
from mastapy.nodal_analysis import _46
from mastapy.shafts import _38
from mastapy.gears.analysis import _1070
from mastapy.system_model.analyses_and_results.system_deflections import _2133
from mastapy.system_model.analyses_and_results.system_deflections.compound import (
    _2279, _2281, _2284, _2290,
    _2291, _2292, _2297, _2302,
    _2312, _2316, _2322, _2323,
    _2330, _2331, _2338, _2341,
    _2342, _2343, _2345, _2349,
    _2350, _2351, _2359, _2353,
    _2357, _2364, _2365, _2370,
    _2373, _2376, _2380, _2384,
    _2388, _2391, _2273
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'AssemblyCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundSystemDeflection',)


class AssemblyCompoundSystemDeflection(_2273.AbstractAssemblyCompoundSystemDeflection):
    '''AssemblyCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def overall_duty_cycle_shaft_reliability(self) -> 'float':
        '''float: 'OverallDutyCycleShaftReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallDutyCycleShaftReliability

    @property
    def overall_duty_cycle_bearing_reliability(self) -> 'float':
        '''float: 'OverallDutyCycleBearingReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallDutyCycleBearingReliability

    @property
    def overall_duty_cycle_gear_reliability(self) -> 'float':
        '''float: 'OverallDutyCycleGearReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallDutyCycleGearReliability

    @property
    def overall_oil_seal_duty_cycle_reliability(self) -> 'float':
        '''float: 'OverallOilSealDutyCycleReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallOilSealDutyCycleReliability

    @property
    def overall_system_reliability(self) -> 'float':
        '''float: 'OverallSystemReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallSystemReliability

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
    def analysis_settings(self) -> '_46.AnalysisSettings':
        '''AnalysisSettings: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_46.AnalysisSettings)(self.wrapped.AnalysisSettings) if self.wrapped.AnalysisSettings else None

    @property
    def shaft_settings(self) -> '_38.ShaftSettings':
        '''ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_38.ShaftSettings)(self.wrapped.ShaftSettings) if self.wrapped.ShaftSettings else None

    @property
    def rating_for_all_gear_sets(self) -> '_1070.GearSetGroupDutyCycle':
        '''GearSetGroupDutyCycle: 'RatingForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1070.GearSetGroupDutyCycle)(self.wrapped.RatingForAllGearSets) if self.wrapped.RatingForAllGearSets else None

    @property
    def load_case_analyses_ready(self) -> 'List[_2133.AssemblySystemDeflection]':
        '''List[AssemblySystemDeflection]: 'LoadCaseAnalysesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCaseAnalysesReady, constructor.new(_2133.AssemblySystemDeflection))
        return value

    @property
    def assembly_system_deflection_load_cases(self) -> 'List[_2133.AssemblySystemDeflection]':
        '''List[AssemblySystemDeflection]: 'AssemblySystemDeflectionLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblySystemDeflectionLoadCases, constructor.new(_2133.AssemblySystemDeflection))
        return value

    @property
    def bearings(self) -> 'List[_2279.BearingCompoundSystemDeflection]':
        '''List[BearingCompoundSystemDeflection]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2279.BearingCompoundSystemDeflection))
        return value

    @property
    def belt_drives(self) -> 'List[_2281.BeltDriveCompoundSystemDeflection]':
        '''List[BeltDriveCompoundSystemDeflection]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_2281.BeltDriveCompoundSystemDeflection))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2284.BevelDifferentialGearSetCompoundSystemDeflection]':
        '''List[BevelDifferentialGearSetCompoundSystemDeflection]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_2284.BevelDifferentialGearSetCompoundSystemDeflection))
        return value

    @property
    def bolts(self) -> 'List[_2290.BoltCompoundSystemDeflection]':
        '''List[BoltCompoundSystemDeflection]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_2290.BoltCompoundSystemDeflection))
        return value

    @property
    def bolted_joints(self) -> 'List[_2291.BoltedJointCompoundSystemDeflection]':
        '''List[BoltedJointCompoundSystemDeflection]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2291.BoltedJointCompoundSystemDeflection))
        return value

    @property
    def clutches(self) -> 'List[_2292.ClutchCompoundSystemDeflection]':
        '''List[ClutchCompoundSystemDeflection]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_2292.ClutchCompoundSystemDeflection))
        return value

    @property
    def concept_couplings(self) -> 'List[_2297.ConceptCouplingCompoundSystemDeflection]':
        '''List[ConceptCouplingCompoundSystemDeflection]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_2297.ConceptCouplingCompoundSystemDeflection))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2302.ConceptGearSetCompoundSystemDeflection]':
        '''List[ConceptGearSetCompoundSystemDeflection]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_2302.ConceptGearSetCompoundSystemDeflection))
        return value

    @property
    def cv_ts(self) -> 'List[_2312.CVTCompoundSystemDeflection]':
        '''List[CVTCompoundSystemDeflection]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_2312.CVTCompoundSystemDeflection))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2316.CylindricalGearSetCompoundSystemDeflection]':
        '''List[CylindricalGearSetCompoundSystemDeflection]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_2316.CylindricalGearSetCompoundSystemDeflection))
        return value

    @property
    def face_gear_sets(self) -> 'List[_2322.FaceGearSetCompoundSystemDeflection]':
        '''List[FaceGearSetCompoundSystemDeflection]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_2322.FaceGearSetCompoundSystemDeflection))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_2323.FlexiblePinAssemblyCompoundSystemDeflection]':
        '''List[FlexiblePinAssemblyCompoundSystemDeflection]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_2323.FlexiblePinAssemblyCompoundSystemDeflection))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2330.HypoidGearSetCompoundSystemDeflection]':
        '''List[HypoidGearSetCompoundSystemDeflection]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_2330.HypoidGearSetCompoundSystemDeflection))
        return value

    @property
    def imported_fe_components(self) -> 'List[_2331.ImportedFEComponentCompoundSystemDeflection]':
        '''List[ImportedFEComponentCompoundSystemDeflection]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_2331.ImportedFEComponentCompoundSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_2338.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_2338.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_2341.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_2341.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def mass_discs(self) -> 'List[_2342.MassDiscCompoundSystemDeflection]':
        '''List[MassDiscCompoundSystemDeflection]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_2342.MassDiscCompoundSystemDeflection))
        return value

    @property
    def measurement_components(self) -> 'List[_2343.MeasurementComponentCompoundSystemDeflection]':
        '''List[MeasurementComponentCompoundSystemDeflection]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_2343.MeasurementComponentCompoundSystemDeflection))
        return value

    @property
    def oil_seals(self) -> 'List[_2345.OilSealCompoundSystemDeflection]':
        '''List[OilSealCompoundSystemDeflection]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_2345.OilSealCompoundSystemDeflection))
        return value

    @property
    def planet_carriers(self) -> 'List[_2349.PlanetCarrierCompoundSystemDeflection]':
        '''List[PlanetCarrierCompoundSystemDeflection]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_2349.PlanetCarrierCompoundSystemDeflection))
        return value

    @property
    def point_loads(self) -> 'List[_2350.PointLoadCompoundSystemDeflection]':
        '''List[PointLoadCompoundSystemDeflection]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_2350.PointLoadCompoundSystemDeflection))
        return value

    @property
    def power_loads(self) -> 'List[_2351.PowerLoadCompoundSystemDeflection]':
        '''List[PowerLoadCompoundSystemDeflection]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_2351.PowerLoadCompoundSystemDeflection))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2359.ShaftHubConnectionCompoundSystemDeflection]':
        '''List[ShaftHubConnectionCompoundSystemDeflection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_2359.ShaftHubConnectionCompoundSystemDeflection))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_2353.RollingRingAssemblyCompoundSystemDeflection]':
        '''List[RollingRingAssemblyCompoundSystemDeflection]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_2353.RollingRingAssemblyCompoundSystemDeflection))
        return value

    @property
    def shafts(self) -> 'List[_2357.ShaftCompoundSystemDeflection]':
        '''List[ShaftCompoundSystemDeflection]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_2357.ShaftCompoundSystemDeflection))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2364.SpiralBevelGearSetCompoundSystemDeflection]':
        '''List[SpiralBevelGearSetCompoundSystemDeflection]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_2364.SpiralBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def spring_dampers(self) -> 'List[_2365.SpringDamperCompoundSystemDeflection]':
        '''List[SpringDamperCompoundSystemDeflection]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_2365.SpringDamperCompoundSystemDeflection))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_2370.StraightBevelDiffGearSetCompoundSystemDeflection]':
        '''List[StraightBevelDiffGearSetCompoundSystemDeflection]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_2370.StraightBevelDiffGearSetCompoundSystemDeflection))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2373.StraightBevelGearSetCompoundSystemDeflection]':
        '''List[StraightBevelGearSetCompoundSystemDeflection]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_2373.StraightBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def synchronisers(self) -> 'List[_2376.SynchroniserCompoundSystemDeflection]':
        '''List[SynchroniserCompoundSystemDeflection]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_2376.SynchroniserCompoundSystemDeflection))
        return value

    @property
    def torque_converters(self) -> 'List[_2380.TorqueConverterCompoundSystemDeflection]':
        '''List[TorqueConverterCompoundSystemDeflection]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_2380.TorqueConverterCompoundSystemDeflection))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_2384.UnbalancedMassCompoundSystemDeflection]':
        '''List[UnbalancedMassCompoundSystemDeflection]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_2384.UnbalancedMassCompoundSystemDeflection))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2388.WormGearSetCompoundSystemDeflection]':
        '''List[WormGearSetCompoundSystemDeflection]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_2388.WormGearSetCompoundSystemDeflection))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_2391.ZerolBevelGearSetCompoundSystemDeflection]':
        '''List[ZerolBevelGearSetCompoundSystemDeflection]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_2391.ZerolBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def rolling_bearings(self) -> 'List[_2279.BearingCompoundSystemDeflection]':
        '''List[BearingCompoundSystemDeflection]: 'RollingBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingBearings, constructor.new(_2279.BearingCompoundSystemDeflection))
        return value
