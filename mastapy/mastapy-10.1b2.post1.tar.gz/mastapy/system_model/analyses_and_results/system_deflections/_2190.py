'''_2190.py

AssemblySystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1958
from mastapy.system_model.analyses_and_results.static_loads import _6031
from mastapy.system_model.analyses_and_results.power_flows import _3199
from mastapy.nodal_analysis import _1339
from mastapy.shafts import _38
from mastapy.gears.analysis import _949
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2191, _2193, _2195, _2203,
    _2202, _2206, _2212, _2214,
    _2227, _2231, _2242, _2244,
    _2250, _2252, _2258, _2261,
    _2264, _2265, _2269, _2273,
    _2275, _2276, _2277, _2283,
    _2279, _2286, _2290, _2294,
    _2296, _2299, _2306, _2312,
    _2316, _2319, _2322, _2186,
    _2220, _2208, _2267, _2245,
    _2185
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'AssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblySystemDeflection',)


class AssemblySystemDeflection(_2185.AbstractAssemblySystemDeflection):
    '''AssemblySystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def overall_bearing_reliability(self) -> 'float':
        '''float: 'OverallBearingReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallBearingReliability

    @property
    def overall_shaft_reliability(self) -> 'float':
        '''float: 'OverallShaftReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallShaftReliability

    @property
    def overall_gear_reliability(self) -> 'float':
        '''float: 'OverallGearReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallGearReliability

    @property
    def overall_oil_seal_reliability(self) -> 'float':
        '''float: 'OverallOilSealReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallOilSealReliability

    @property
    def overall_system_reliability(self) -> 'float':
        '''float: 'OverallSystemReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallSystemReliability

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
    def power_flow_results(self) -> '_3199.AssemblyPowerFlow':
        '''AssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3199.AssemblyPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults else None

    @property
    def analysis_settings(self) -> '_1339.AnalysisSettings':
        '''AnalysisSettings: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1339.AnalysisSettings)(self.wrapped.AnalysisSettings) if self.wrapped.AnalysisSettings else None

    @property
    def shaft_settings(self) -> '_38.ShaftSettings':
        '''ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_38.ShaftSettings)(self.wrapped.ShaftSettings) if self.wrapped.ShaftSettings else None

    @property
    def rating_for_all_gear_sets(self) -> '_949.GearSetGroupDutyCycle':
        '''GearSetGroupDutyCycle: 'RatingForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_949.GearSetGroupDutyCycle)(self.wrapped.RatingForAllGearSets) if self.wrapped.RatingForAllGearSets else None

    @property
    def bearings(self) -> 'List[_2191.BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2191.BearingSystemDeflection))
        return value

    @property
    def belt_drives(self) -> 'List[_2193.BeltDriveSystemDeflection]':
        '''List[BeltDriveSystemDeflection]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_2193.BeltDriveSystemDeflection))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2195.BevelDifferentialGearSetSystemDeflection]':
        '''List[BevelDifferentialGearSetSystemDeflection]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_2195.BevelDifferentialGearSetSystemDeflection))
        return value

    @property
    def bolts(self) -> 'List[_2203.BoltSystemDeflection]':
        '''List[BoltSystemDeflection]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_2203.BoltSystemDeflection))
        return value

    @property
    def bolted_joints(self) -> 'List[_2202.BoltedJointSystemDeflection]':
        '''List[BoltedJointSystemDeflection]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2202.BoltedJointSystemDeflection))
        return value

    @property
    def clutches(self) -> 'List[_2206.ClutchSystemDeflection]':
        '''List[ClutchSystemDeflection]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_2206.ClutchSystemDeflection))
        return value

    @property
    def concept_couplings(self) -> 'List[_2212.ConceptCouplingSystemDeflection]':
        '''List[ConceptCouplingSystemDeflection]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_2212.ConceptCouplingSystemDeflection))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2214.ConceptGearSetSystemDeflection]':
        '''List[ConceptGearSetSystemDeflection]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_2214.ConceptGearSetSystemDeflection))
        return value

    @property
    def cv_ts(self) -> 'List[_2227.CVTSystemDeflection]':
        '''List[CVTSystemDeflection]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_2227.CVTSystemDeflection))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2231.CylindricalGearSetSystemDeflection]':
        '''List[CylindricalGearSetSystemDeflection]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_2231.CylindricalGearSetSystemDeflection))
        return value

    @property
    def face_gear_sets(self) -> 'List[_2242.FaceGearSetSystemDeflection]':
        '''List[FaceGearSetSystemDeflection]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_2242.FaceGearSetSystemDeflection))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_2244.FlexiblePinAssemblySystemDeflection]':
        '''List[FlexiblePinAssemblySystemDeflection]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_2244.FlexiblePinAssemblySystemDeflection))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2250.HypoidGearSetSystemDeflection]':
        '''List[HypoidGearSetSystemDeflection]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_2250.HypoidGearSetSystemDeflection))
        return value

    @property
    def imported_fe_components(self) -> 'List[_2252.ImportedFEComponentSystemDeflection]':
        '''List[ImportedFEComponentSystemDeflection]: 'ImportedFEComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ImportedFEComponents, constructor.new(_2252.ImportedFEComponentSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_2258.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_2258.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_2261.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_2261.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection))
        return value

    @property
    def mass_discs(self) -> 'List[_2264.MassDiscSystemDeflection]':
        '''List[MassDiscSystemDeflection]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_2264.MassDiscSystemDeflection))
        return value

    @property
    def measurement_components(self) -> 'List[_2265.MeasurementComponentSystemDeflection]':
        '''List[MeasurementComponentSystemDeflection]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_2265.MeasurementComponentSystemDeflection))
        return value

    @property
    def oil_seals(self) -> 'List[_2269.OilSealSystemDeflection]':
        '''List[OilSealSystemDeflection]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_2269.OilSealSystemDeflection))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_2273.PartToPartShearCouplingSystemDeflection]':
        '''List[PartToPartShearCouplingSystemDeflection]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_2273.PartToPartShearCouplingSystemDeflection))
        return value

    @property
    def planet_carriers(self) -> 'List[_2275.PlanetCarrierSystemDeflection]':
        '''List[PlanetCarrierSystemDeflection]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_2275.PlanetCarrierSystemDeflection))
        return value

    @property
    def point_loads(self) -> 'List[_2276.PointLoadSystemDeflection]':
        '''List[PointLoadSystemDeflection]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_2276.PointLoadSystemDeflection))
        return value

    @property
    def power_loads(self) -> 'List[_2277.PowerLoadSystemDeflection]':
        '''List[PowerLoadSystemDeflection]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_2277.PowerLoadSystemDeflection))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2283.ShaftHubConnectionSystemDeflection]':
        '''List[ShaftHubConnectionSystemDeflection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_2283.ShaftHubConnectionSystemDeflection))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_2279.RollingRingAssemblySystemDeflection]':
        '''List[RollingRingAssemblySystemDeflection]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_2279.RollingRingAssemblySystemDeflection))
        return value

    @property
    def shafts(self) -> 'List[_2286.ShaftSystemDeflection]':
        '''List[ShaftSystemDeflection]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_2286.ShaftSystemDeflection))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2290.SpiralBevelGearSetSystemDeflection]':
        '''List[SpiralBevelGearSetSystemDeflection]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_2290.SpiralBevelGearSetSystemDeflection))
        return value

    @property
    def spring_dampers(self) -> 'List[_2294.SpringDamperSystemDeflection]':
        '''List[SpringDamperSystemDeflection]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_2294.SpringDamperSystemDeflection))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_2296.StraightBevelDiffGearSetSystemDeflection]':
        '''List[StraightBevelDiffGearSetSystemDeflection]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_2296.StraightBevelDiffGearSetSystemDeflection))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2299.StraightBevelGearSetSystemDeflection]':
        '''List[StraightBevelGearSetSystemDeflection]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_2299.StraightBevelGearSetSystemDeflection))
        return value

    @property
    def synchronisers(self) -> 'List[_2306.SynchroniserSystemDeflection]':
        '''List[SynchroniserSystemDeflection]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_2306.SynchroniserSystemDeflection))
        return value

    @property
    def torque_converters(self) -> 'List[_2312.TorqueConverterSystemDeflection]':
        '''List[TorqueConverterSystemDeflection]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_2312.TorqueConverterSystemDeflection))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_2316.UnbalancedMassSystemDeflection]':
        '''List[UnbalancedMassSystemDeflection]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_2316.UnbalancedMassSystemDeflection))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2319.WormGearSetSystemDeflection]':
        '''List[WormGearSetSystemDeflection]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_2319.WormGearSetSystemDeflection))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_2322.ZerolBevelGearSetSystemDeflection]':
        '''List[ZerolBevelGearSetSystemDeflection]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_2322.ZerolBevelGearSetSystemDeflection))
        return value

    @property
    def shafts_and_housings(self) -> 'List[_2186.AbstractShaftOrHousingSystemDeflection]':
        '''List[AbstractShaftOrHousingSystemDeflection]: 'ShaftsAndHousings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftsAndHousings, constructor.new(_2186.AbstractShaftOrHousingSystemDeflection))
        return value

    @property
    def supercharger_rotor_sets(self) -> 'List[_2231.CylindricalGearSetSystemDeflection]':
        '''List[CylindricalGearSetSystemDeflection]: 'SuperchargerRotorSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SuperchargerRotorSets, constructor.new(_2231.CylindricalGearSetSystemDeflection))
        return value

    @property
    def rolling_bearings(self) -> 'List[_2191.BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'RollingBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingBearings, constructor.new(_2191.BearingSystemDeflection))
        return value

    @property
    def connection_details(self) -> 'List[_2220.ConnectionSystemDeflection]':
        '''List[ConnectionSystemDeflection]: 'ConnectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionDetails, constructor.new(_2220.ConnectionSystemDeflection))
        return value

    @property
    def sorted_converged_connection_details(self) -> 'List[_2220.ConnectionSystemDeflection]':
        '''List[ConnectionSystemDeflection]: 'SortedConvergedConnectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SortedConvergedConnectionDetails, constructor.new(_2220.ConnectionSystemDeflection))
        return value

    @property
    def sorted_unconverged_connection_details(self) -> 'List[_2220.ConnectionSystemDeflection]':
        '''List[ConnectionSystemDeflection]: 'SortedUnconvergedConnectionDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SortedUnconvergedConnectionDetails, constructor.new(_2220.ConnectionSystemDeflection))
        return value

    @property
    def component_details(self) -> 'List[_2208.ComponentSystemDeflection]':
        '''List[ComponentSystemDeflection]: 'ComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentDetails, constructor.new(_2208.ComponentSystemDeflection))
        return value

    @property
    def mountable_component_details(self) -> 'List[_2267.MountableComponentSystemDeflection]':
        '''List[MountableComponentSystemDeflection]: 'MountableComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MountableComponentDetails, constructor.new(_2267.MountableComponentSystemDeflection))
        return value

    @property
    def sorted_converged_component_details(self) -> 'List[_2208.ComponentSystemDeflection]':
        '''List[ComponentSystemDeflection]: 'SortedConvergedComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SortedConvergedComponentDetails, constructor.new(_2208.ComponentSystemDeflection))
        return value

    @property
    def sorted_unconverged_component_details(self) -> 'List[_2208.ComponentSystemDeflection]':
        '''List[ComponentSystemDeflection]: 'SortedUnconvergedComponentDetails' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SortedUnconvergedComponentDetails, constructor.new(_2208.ComponentSystemDeflection))
        return value

    @property
    def unconverged_bearings_sorted_by_load(self) -> 'List[_2191.BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'UnconvergedBearingsSortedByLoad' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnconvergedBearingsSortedByLoad, constructor.new(_2191.BearingSystemDeflection))
        return value

    @property
    def unconverged_gear_meshes_sorted_by_power(self) -> 'List[_2245.GearMeshSystemDeflection]':
        '''List[GearMeshSystemDeflection]: 'UnconvergedGearMeshesSortedByPower' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnconvergedGearMeshesSortedByPower, constructor.new(_2245.GearMeshSystemDeflection))
        return value
