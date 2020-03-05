'''_5875.py

LoadCase
'''


from typing import List

from mastapy.system_model.analyses_and_results import (
    _2097, _2092, _2075, _2083,
    _2090, _2091, _2077, _2094,
    _2095, _2096, _2088, _2078,
    _2087, _2086, _2084, _2085,
    _2098, _2093, _2076, _2081,
    _2080, _2079, _2082, _2089,
    _2074, _2101
)
from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy.bearings.bearing_results.rolling import _1540
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.system_model import _1732, _1729, _1740
from mastapy.gears import _269
from mastapy.system_model.analyses_and_results.static_loads import (
    _5878, _5990, _6010, _5893,
    _5910, _5880, _5923, _5962,
    _5968, _5971, _5974, _6003,
    _6013, _6033, _6036, _5948,
    _5882, _5876, _5877, _5884,
    _5896, _5895, _5901, _5914,
    _5929, _5940, _5944, _5883,
    _5952, _5964, _5976, _5977,
    _5978, _5980, _5982, _5986,
    _5989, _5996, _6000, _6030,
    _6031, _5998, _5905, _5907,
    _5941, _5943, _5879, _5881,
    _5887, _5889, _5890, _5891,
    _5892, _5894, _5908, _5912,
    _5921, _5925, _5926, _5946,
    _5951, _5961, _5963, _5967,
    _5969, _5970, _5972, _5973,
    _5975, _5984, _6002, _6004,
    _6009, _6011, _6012, _6014,
    _6015, _6016, _6032, _6034,
    _6035, _6037, _5886, _5899,
    _5898, _5904, _5903, _5917,
    _5916, _5919, _5920, _5991,
    _5997, _5995, _5993, _6007,
    _6006, _6018, _6017, _6019,
    _6020, _6024, _6025, _6026,
    _5918, _5885, _5900, _5913,
    _5966, _5983, _5994, _5999,
    _5897, _5902, _5915, _6005,
    _6023, _5888, _5906, _5942
)
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3439
from mastapy.system_model.connections_and_sockets.gears import (
    _1815, _1793, _1797, _1789,
    _1799, _1805, _1808, _1809,
    _1810, _1813, _1817, _1819,
    _1821, _1803, _1791, _1795,
    _1801
)
from mastapy.system_model.part_model import (
    _1907, _1908, _1910, _1912,
    _1913, _1914, _1917, _1918,
    _1921, _1922, _1906, _1923,
    _1926, _1928, _1929, _1930,
    _1931, _1933, _1934, _1936,
    _1937, _1938, _1940, _1941,
    _1942
)
from mastapy.system_model.part_model.shaft_model import _1945
from mastapy.system_model.part_model.gears import (
    _1983, _1984, _1990, _1991,
    _1975, _1976, _1977, _1978,
    _1979, _1980, _1981, _1982,
    _1985, _1986, _1987, _1988,
    _1989, _1992, _1994, _1996,
    _1997, _1998, _1999, _2000,
    _2001, _2002, _2003, _2004,
    _2005, _2006, _2007, _2008,
    _2009, _2010, _2011, _2012,
    _2013, _2014, _2015, _2016
)
from mastapy.system_model.part_model.couplings import (
    _2034, _2036, _2037, _2039,
    _2040, _2041, _2042, _2043,
    _2044, _2045, _2053, _2051,
    _2052, _2054, _2055, _2056,
    _2058, _2059, _2060, _2061,
    _2062, _2064
)
from mastapy.system_model.connections_and_sockets import (
    _1766, _1761, _1762, _1765,
    _1774, _1777, _1781, _1785
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _1823, _1825, _1827, _1829,
    _1831
)
from mastapy._internal.python_net import python_net_import

_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'LoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadCase',)


class LoadCase(_2101.Context):
    '''LoadCase

    This is a mastapy class.
    '''

    TYPE = _LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadCase.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def system_deflection(self) -> '_2097.SystemDeflectionAnalysis':
        '''SystemDeflectionAnalysis: 'SystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2097.SystemDeflectionAnalysis)(self.wrapped.SystemDeflection) if self.wrapped.SystemDeflection else None

    @property
    def power_flow(self) -> '_2092.PowerFlowAnalysis':
        '''PowerFlowAnalysis: 'PowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2092.PowerFlowAnalysis)(self.wrapped.PowerFlow) if self.wrapped.PowerFlow else None

    @property
    def advanced_system_deflection(self) -> '_2075.AdvancedSystemDeflectionAnalysis':
        '''AdvancedSystemDeflectionAnalysis: 'AdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2075.AdvancedSystemDeflectionAnalysis)(self.wrapped.AdvancedSystemDeflection) if self.wrapped.AdvancedSystemDeflection else None

    @property
    def gear_whine_analysis(self) -> '_2083.GearWhineAnalysisAnalysis':
        '''GearWhineAnalysisAnalysis: 'GearWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2083.GearWhineAnalysisAnalysis)(self.wrapped.GearWhineAnalysis) if self.wrapped.GearWhineAnalysis else None

    @property
    def multibody_dynamics(self) -> '_2090.MultibodyDynamicsAnalysis':
        '''MultibodyDynamicsAnalysis: 'MultibodyDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2090.MultibodyDynamicsAnalysis)(self.wrapped.MultibodyDynamics) if self.wrapped.MultibodyDynamics else None

    @property
    def parametric_study_tool(self) -> '_2091.ParametricStudyToolAnalysis':
        '''ParametricStudyToolAnalysis: 'ParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2091.ParametricStudyToolAnalysis)(self.wrapped.ParametricStudyTool) if self.wrapped.ParametricStudyTool else None

    @property
    def compound_parametric_study_tool(self) -> '_2077.CompoundParametricStudyToolAnalysis':
        '''CompoundParametricStudyToolAnalysis: 'CompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2077.CompoundParametricStudyToolAnalysis)(self.wrapped.CompoundParametricStudyTool) if self.wrapped.CompoundParametricStudyTool else None

    @property
    def steady_state_synchronous_response(self) -> '_2094.SteadyStateSynchronousResponseAnalysis':
        '''SteadyStateSynchronousResponseAnalysis: 'SteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2094.SteadyStateSynchronousResponseAnalysis)(self.wrapped.SteadyStateSynchronousResponse) if self.wrapped.SteadyStateSynchronousResponse else None

    @property
    def steady_state_synchronous_responseata_speed(self) -> '_2095.SteadyStateSynchronousResponseataSpeedAnalysis':
        '''SteadyStateSynchronousResponseataSpeedAnalysis: 'SteadyStateSynchronousResponseataSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2095.SteadyStateSynchronousResponseataSpeedAnalysis)(self.wrapped.SteadyStateSynchronousResponseataSpeed) if self.wrapped.SteadyStateSynchronousResponseataSpeed else None

    @property
    def steady_state_synchronous_responseona_shaft(self) -> '_2096.SteadyStateSynchronousResponseonaShaftAnalysis':
        '''SteadyStateSynchronousResponseonaShaftAnalysis: 'SteadyStateSynchronousResponseonaShaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2096.SteadyStateSynchronousResponseonaShaftAnalysis)(self.wrapped.SteadyStateSynchronousResponseonaShaft) if self.wrapped.SteadyStateSynchronousResponseonaShaft else None

    @property
    def modal_analysis(self) -> '_2088.ModalAnalysisAnalysis':
        '''ModalAnalysisAnalysis: 'ModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2088.ModalAnalysisAnalysis)(self.wrapped.ModalAnalysis) if self.wrapped.ModalAnalysis else None

    @property
    def dynamic_analysis(self) -> '_2078.DynamicAnalysisAnalysis':
        '''DynamicAnalysisAnalysis: 'DynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2078.DynamicAnalysisAnalysis)(self.wrapped.DynamicAnalysis) if self.wrapped.DynamicAnalysis else None

    @property
    def modal_analysesat_stiffnesses(self) -> '_2087.ModalAnalysesatStiffnessesAnalysis':
        '''ModalAnalysesatStiffnessesAnalysis: 'ModalAnalysesatStiffnesses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2087.ModalAnalysesatStiffnessesAnalysis)(self.wrapped.ModalAnalysesatStiffnesses) if self.wrapped.ModalAnalysesatStiffnesses else None

    @property
    def modal_analysesat_speeds(self) -> '_2086.ModalAnalysesatSpeedsAnalysis':
        '''ModalAnalysesatSpeedsAnalysis: 'ModalAnalysesatSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2086.ModalAnalysesatSpeedsAnalysis)(self.wrapped.ModalAnalysesatSpeeds) if self.wrapped.ModalAnalysesatSpeeds else None

    @property
    def modal_analysesata_speed(self) -> '_2084.ModalAnalysesataSpeedAnalysis':
        '''ModalAnalysesataSpeedAnalysis: 'ModalAnalysesataSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2084.ModalAnalysesataSpeedAnalysis)(self.wrapped.ModalAnalysesataSpeed) if self.wrapped.ModalAnalysesataSpeed else None

    @property
    def modal_analysesata_stiffness(self) -> '_2085.ModalAnalysesataStiffnessAnalysis':
        '''ModalAnalysesataStiffnessAnalysis: 'ModalAnalysesataStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2085.ModalAnalysesataStiffnessAnalysis)(self.wrapped.ModalAnalysesataStiffness) if self.wrapped.ModalAnalysesataStiffness else None

    @property
    def torsional_system_deflection(self) -> '_2098.TorsionalSystemDeflectionAnalysis':
        '''TorsionalSystemDeflectionAnalysis: 'TorsionalSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2098.TorsionalSystemDeflectionAnalysis)(self.wrapped.TorsionalSystemDeflection) if self.wrapped.TorsionalSystemDeflection else None

    @property
    def single_mesh_whine_analysis(self) -> '_2093.SingleMeshWhineAnalysisAnalysis':
        '''SingleMeshWhineAnalysisAnalysis: 'SingleMeshWhineAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2093.SingleMeshWhineAnalysisAnalysis)(self.wrapped.SingleMeshWhineAnalysis) if self.wrapped.SingleMeshWhineAnalysis else None

    @property
    def advanced_system_deflection_sub_analysis(self) -> '_2076.AdvancedSystemDeflectionSubAnalysisAnalysis':
        '''AdvancedSystemDeflectionSubAnalysisAnalysis: 'AdvancedSystemDeflectionSubAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2076.AdvancedSystemDeflectionSubAnalysisAnalysis)(self.wrapped.AdvancedSystemDeflectionSubAnalysis) if self.wrapped.AdvancedSystemDeflectionSubAnalysis else None

    @property
    def dynamic_modelfor_gear_whine(self) -> '_2081.DynamicModelforGearWhineAnalysis':
        '''DynamicModelforGearWhineAnalysis: 'DynamicModelforGearWhine' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2081.DynamicModelforGearWhineAnalysis)(self.wrapped.DynamicModelforGearWhine) if self.wrapped.DynamicModelforGearWhine else None

    @property
    def dynamic_modelforat_speeds(self) -> '_2080.DynamicModelforatSpeedsAnalysis':
        '''DynamicModelforatSpeedsAnalysis: 'DynamicModelforatSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2080.DynamicModelforatSpeedsAnalysis)(self.wrapped.DynamicModelforatSpeeds) if self.wrapped.DynamicModelforatSpeeds else None

    @property
    def dynamic_modelata_stiffness(self) -> '_2079.DynamicModelataStiffnessAnalysis':
        '''DynamicModelataStiffnessAnalysis: 'DynamicModelataStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2079.DynamicModelataStiffnessAnalysis)(self.wrapped.DynamicModelataStiffness) if self.wrapped.DynamicModelataStiffness else None

    @property
    def dynamic_modelfor_steady_state_synchronous_response(self) -> '_2082.DynamicModelforSteadyStateSynchronousResponseAnalysis':
        '''DynamicModelforSteadyStateSynchronousResponseAnalysis: 'DynamicModelforSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2082.DynamicModelforSteadyStateSynchronousResponseAnalysis)(self.wrapped.DynamicModelforSteadyStateSynchronousResponse) if self.wrapped.DynamicModelforSteadyStateSynchronousResponse else None

    @property
    def modal_analysisfor_whine(self) -> '_2089.ModalAnalysisforWhineAnalysis':
        '''ModalAnalysisforWhineAnalysis: 'ModalAnalysisforWhine' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2089.ModalAnalysisforWhineAnalysis)(self.wrapped.ModalAnalysisforWhine) if self.wrapped.ModalAnalysisforWhine else None

    @property
    def include_shaft_and_gear_windage_loss(self) -> 'bool':
        '''bool: 'IncludeShaftAndGearWindageLoss' is the original name of this property.'''

        return self.wrapped.IncludeShaftAndGearWindageLoss

    @include_shaft_and_gear_windage_loss.setter
    def include_shaft_and_gear_windage_loss(self, value: 'bool'):
        self.wrapped.IncludeShaftAndGearWindageLoss = bool(value) if value else False

    @property
    def include_bearing_and_seal_loss(self) -> 'bool':
        '''bool: 'IncludeBearingAndSealLoss' is the original name of this property.'''

        return self.wrapped.IncludeBearingAndSealLoss

    @include_bearing_and_seal_loss.setter
    def include_bearing_and_seal_loss(self, value: 'bool'):
        self.wrapped.IncludeBearingAndSealLoss = bool(value) if value else False

    @property
    def include_clearance_bearing_loss(self) -> 'bool':
        '''bool: 'IncludeClearanceBearingLoss' is the original name of this property.'''

        return self.wrapped.IncludeClearanceBearingLoss

    @include_clearance_bearing_loss.setter
    def include_clearance_bearing_loss(self, value: 'bool'):
        self.wrapped.IncludeClearanceBearingLoss = bool(value) if value else False

    @property
    def use_advanced_needle_roller_bearing_power_loss_calculation(self) -> 'bool':
        '''bool: 'UseAdvancedNeedleRollerBearingPowerLossCalculation' is the original name of this property.'''

        return self.wrapped.UseAdvancedNeedleRollerBearingPowerLossCalculation

    @use_advanced_needle_roller_bearing_power_loss_calculation.setter
    def use_advanced_needle_roller_bearing_power_loss_calculation(self, value: 'bool'):
        self.wrapped.UseAdvancedNeedleRollerBearingPowerLossCalculation = bool(value) if value else False

    @property
    def include_gear_mesh_loss(self) -> 'bool':
        '''bool: 'IncludeGearMeshLoss' is the original name of this property.'''

        return self.wrapped.IncludeGearMeshLoss

    @include_gear_mesh_loss.setter
    def include_gear_mesh_loss(self, value: 'bool'):
        self.wrapped.IncludeGearMeshLoss = bool(value) if value else False

    @property
    def include_belt_loss(self) -> 'bool':
        '''bool: 'IncludeBeltLoss' is the original name of this property.'''

        return self.wrapped.IncludeBeltLoss

    @include_belt_loss.setter
    def include_belt_loss(self, value: 'bool'):
        self.wrapped.IncludeBeltLoss = bool(value) if value else False

    @property
    def include_bearing_centrifugal(self) -> 'bool':
        '''bool: 'IncludeBearingCentrifugal' is the original name of this property.'''

        return self.wrapped.IncludeBearingCentrifugal

    @include_bearing_centrifugal.setter
    def include_bearing_centrifugal(self, value: 'bool'):
        self.wrapped.IncludeBearingCentrifugal = bool(value) if value else False

    @property
    def include_efficiency(self) -> 'bool':
        '''bool: 'IncludeEfficiency' is the original name of this property.'''

        return self.wrapped.IncludeEfficiency

    @include_efficiency.setter
    def include_efficiency(self, value: 'bool'):
        self.wrapped.IncludeEfficiency = bool(value) if value else False

    @property
    def include_planetary_centrifugal(self) -> 'bool':
        '''bool: 'IncludePlanetaryCentrifugal' is the original name of this property.'''

        return self.wrapped.IncludePlanetaryCentrifugal

    @include_planetary_centrifugal.setter
    def include_planetary_centrifugal(self, value: 'bool'):
        self.wrapped.IncludePlanetaryCentrifugal = bool(value) if value else False

    @property
    def include_gravity(self) -> 'bool':
        '''bool: 'IncludeGravity' is the original name of this property.'''

        return self.wrapped.IncludeGravity

    @include_gravity.setter
    def include_gravity(self, value: 'bool'):
        self.wrapped.IncludeGravity = bool(value) if value else False

    @property
    def use_default_temperatures(self) -> 'bool':
        '''bool: 'UseDefaultTemperatures' is the original name of this property.'''

        return self.wrapped.UseDefaultTemperatures

    @use_default_temperatures.setter
    def use_default_temperatures(self, value: 'bool'):
        self.wrapped.UseDefaultTemperatures = bool(value) if value else False

    @property
    def include_fitting_effects(self) -> 'bool':
        '''bool: 'IncludeFittingEffects' is the original name of this property.'''

        return self.wrapped.IncludeFittingEffects

    @include_fitting_effects.setter
    def include_fitting_effects(self, value: 'bool'):
        self.wrapped.IncludeFittingEffects = bool(value) if value else False

    @property
    def include_thermal_expansion_effects(self) -> 'bool':
        '''bool: 'IncludeThermalExpansionEffects' is the original name of this property.'''

        return self.wrapped.IncludeThermalExpansionEffects

    @include_thermal_expansion_effects.setter
    def include_thermal_expansion_effects(self, value: 'bool'):
        self.wrapped.IncludeThermalExpansionEffects = bool(value) if value else False

    @property
    def include_ring_ovality(self) -> 'bool':
        '''bool: 'IncludeRingOvality' is the original name of this property.'''

        return self.wrapped.IncludeRingOvality

    @include_ring_ovality.setter
    def include_ring_ovality(self, value: 'bool'):
        self.wrapped.IncludeRingOvality = bool(value) if value else False

    @property
    def ring_ovality_scaling(self) -> 'float':
        '''float: 'RingOvalityScaling' is the original name of this property.'''

        return self.wrapped.RingOvalityScaling

    @ring_ovality_scaling.setter
    def ring_ovality_scaling(self, value: 'float'):
        self.wrapped.RingOvalityScaling = float(value) if value else 0.0

    @property
    def include_gear_blank_elastic_distortion(self) -> 'bool':
        '''bool: 'IncludeGearBlankElasticDistortion' is the original name of this property.'''

        return self.wrapped.IncludeGearBlankElasticDistortion

    @include_gear_blank_elastic_distortion.setter
    def include_gear_blank_elastic_distortion(self, value: 'bool'):
        self.wrapped.IncludeGearBlankElasticDistortion = bool(value) if value else False

    @property
    def include_inner_race_distortion_for_flexible_pin_spindle(self) -> 'bool':
        '''bool: 'IncludeInnerRaceDistortionForFlexiblePinSpindle' is the original name of this property.'''

        return self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle

    @include_inner_race_distortion_for_flexible_pin_spindle.setter
    def include_inner_race_distortion_for_flexible_pin_spindle(self, value: 'bool'):
        self.wrapped.IncludeInnerRaceDistortionForFlexiblePinSpindle = bool(value) if value else False

    @property
    def ball_bearing_contact_calculation(self) -> '_1540.BallBearingContactCalculation':
        '''BallBearingContactCalculation: 'BallBearingContactCalculation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.BallBearingContactCalculation)
        return constructor.new(_1540.BallBearingContactCalculation)(value) if value else None

    @ball_bearing_contact_calculation.setter
    def ball_bearing_contact_calculation(self, value: '_1540.BallBearingContactCalculation'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BallBearingContactCalculation = value

    @property
    def model_bearing_mounting_clearances_automatically(self) -> 'bool':
        '''bool: 'ModelBearingMountingClearancesAutomatically' is the original name of this property.'''

        return self.wrapped.ModelBearingMountingClearancesAutomatically

    @model_bearing_mounting_clearances_automatically.setter
    def model_bearing_mounting_clearances_automatically(self, value: 'bool'):
        self.wrapped.ModelBearingMountingClearancesAutomatically = bool(value) if value else False

    @property
    def maximum_shaft_section_length_to_diameter_ratio(self) -> 'float':
        '''float: 'MaximumShaftSectionLengthToDiameterRatio' is the original name of this property.'''

        return self.wrapped.MaximumShaftSectionLengthToDiameterRatio

    @maximum_shaft_section_length_to_diameter_ratio.setter
    def maximum_shaft_section_length_to_diameter_ratio(self, value: 'float'):
        self.wrapped.MaximumShaftSectionLengthToDiameterRatio = float(value) if value else 0.0

    @property
    def maximum_shaft_section_cross_sectional_area_ratio(self) -> 'float':
        '''float: 'MaximumShaftSectionCrossSectionalAreaRatio' is the original name of this property.'''

        return self.wrapped.MaximumShaftSectionCrossSectionalAreaRatio

    @maximum_shaft_section_cross_sectional_area_ratio.setter
    def maximum_shaft_section_cross_sectional_area_ratio(self, value: 'float'):
        self.wrapped.MaximumShaftSectionCrossSectionalAreaRatio = float(value) if value else 0.0

    @property
    def maximum_shaft_section_polar_area_moment_of_inertia_ratio(self) -> 'float':
        '''float: 'MaximumShaftSectionPolarAreaMomentOfInertiaRatio' is the original name of this property.'''

        return self.wrapped.MaximumShaftSectionPolarAreaMomentOfInertiaRatio

    @maximum_shaft_section_polar_area_moment_of_inertia_ratio.setter
    def maximum_shaft_section_polar_area_moment_of_inertia_ratio(self, value: 'float'):
        self.wrapped.MaximumShaftSectionPolarAreaMomentOfInertiaRatio = float(value) if value else 0.0

    @property
    def use_single_node_for_spline_rigid_bond_detailed_connection_connections(self) -> 'bool':
        '''bool: 'UseSingleNodeForSplineRigidBondDetailedConnectionConnections' is the original name of this property.'''

        return self.wrapped.UseSingleNodeForSplineRigidBondDetailedConnectionConnections

    @use_single_node_for_spline_rigid_bond_detailed_connection_connections.setter
    def use_single_node_for_spline_rigid_bond_detailed_connection_connections(self, value: 'bool'):
        self.wrapped.UseSingleNodeForSplineRigidBondDetailedConnectionConnections = bool(value) if value else False

    @property
    def spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio(self) -> 'float':
        '''float: 'SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio' is the original name of this property.'''

        return self.wrapped.SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio

    @spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio.setter
    def spline_rigid_bond_detailed_connection_nodes_per_unit_length_to_diameter_ratio(self, value: 'float'):
        self.wrapped.SplineRigidBondDetailedConnectionNodesPerUnitLengthToDiameterRatio = float(value) if value else 0.0

    @property
    def use_single_node_for_cylindrical_gear_meshes(self) -> 'bool':
        '''bool: 'UseSingleNodeForCylindricalGearMeshes' is the original name of this property.'''

        return self.wrapped.UseSingleNodeForCylindricalGearMeshes

    @use_single_node_for_cylindrical_gear_meshes.setter
    def use_single_node_for_cylindrical_gear_meshes(self, value: 'bool'):
        self.wrapped.UseSingleNodeForCylindricalGearMeshes = bool(value) if value else False

    @property
    def force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes(self) -> 'bool':
        '''bool: 'ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes' is the original name of this property.'''

        return self.wrapped.ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes

    @force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes.setter
    def force_multiple_mesh_nodes_for_unloaded_cylindrical_gear_meshes(self, value: 'bool'):
        self.wrapped.ForceMultipleMeshNodesForUnloadedCylindricalGearMeshes = bool(value) if value else False

    @property
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(self) -> 'float':
        '''float: 'GearMeshNodesPerUnitLengthToDiameterRatio' is the original name of this property.'''

        return self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio

    @gear_mesh_nodes_per_unit_length_to_diameter_ratio.setter
    def gear_mesh_nodes_per_unit_length_to_diameter_ratio(self, value: 'float'):
        self.wrapped.GearMeshNodesPerUnitLengthToDiameterRatio = float(value) if value else 0.0

    @property
    def minimum_number_of_gear_mesh_nodes(self) -> 'int':
        '''int: 'MinimumNumberOfGearMeshNodes' is the original name of this property.'''

        return self.wrapped.MinimumNumberOfGearMeshNodes

    @minimum_number_of_gear_mesh_nodes.setter
    def minimum_number_of_gear_mesh_nodes(self, value: 'int'):
        self.wrapped.MinimumNumberOfGearMeshNodes = int(value) if value else 0

    @property
    def peak_load_factor_for_shafts(self) -> 'float':
        '''float: 'PeakLoadFactorForShafts' is the original name of this property.'''

        return self.wrapped.PeakLoadFactorForShafts

    @peak_load_factor_for_shafts.setter
    def peak_load_factor_for_shafts(self, value: 'float'):
        self.wrapped.PeakLoadFactorForShafts = float(value) if value else 0.0

    @property
    def mesh_stiffness_model(self) -> 'enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel':
        '''enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel: 'MeshStiffnessModel' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.implicit_type()
        return enum_with_selected_value_runtime.create(self.wrapped.MeshStiffnessModel, value) if self.wrapped.MeshStiffnessModel else None

    @mesh_stiffness_model.setter
    def mesh_stiffness_model(self, value: 'enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_MeshStiffnessModel.implicit_type().type_()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value else None)
        self.wrapped.MeshStiffnessModel = value

    @property
    def micro_geometry_model_in_system_deflection(self) -> 'overridable.Overridable_MicroGeometryModel':
        '''overridable.Overridable_MicroGeometryModel: 'MicroGeometryModelInSystemDeflection' is the original name of this property.'''

        return constructor.new(overridable.Overridable_MicroGeometryModel)(self.wrapped.MicroGeometryModelInSystemDeflection) if self.wrapped.MicroGeometryModelInSystemDeflection else None

    @micro_geometry_model_in_system_deflection.setter
    def micro_geometry_model_in_system_deflection(self, value: 'overridable.Overridable_MicroGeometryModel.implicit_type()'):
        wrapper_type = overridable.Overridable_MicroGeometryModel.TYPE
        enclosed_type = overridable.Overridable_MicroGeometryModel.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value else None)
        self.wrapped.MicroGeometryModelInSystemDeflection = value

    @property
    def minimum_force_for_bearing_to_be_considered_loaded(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MinimumForceForBearingToBeConsideredLoaded' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MinimumForceForBearingToBeConsideredLoaded) if self.wrapped.MinimumForceForBearingToBeConsideredLoaded else None

    @minimum_force_for_bearing_to_be_considered_loaded.setter
    def minimum_force_for_bearing_to_be_considered_loaded(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MinimumForceForBearingToBeConsideredLoaded = value

    @property
    def minimum_moment_for_bearing_to_be_considered_loaded(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MinimumMomentForBearingToBeConsideredLoaded' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MinimumMomentForBearingToBeConsideredLoaded) if self.wrapped.MinimumMomentForBearingToBeConsideredLoaded else None

    @minimum_moment_for_bearing_to_be_considered_loaded.setter
    def minimum_moment_for_bearing_to_be_considered_loaded(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MinimumMomentForBearingToBeConsideredLoaded = value

    @property
    def energy_convergence_absolute_tolerance(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'EnergyConvergenceAbsoluteTolerance' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.EnergyConvergenceAbsoluteTolerance) if self.wrapped.EnergyConvergenceAbsoluteTolerance else None

    @energy_convergence_absolute_tolerance.setter
    def energy_convergence_absolute_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.EnergyConvergenceAbsoluteTolerance = value

    @property
    def hypoid_gear_wind_up_removal_method_for_misalignments(self) -> '_1729.HypoidWindUpRemovalMethod':
        '''HypoidWindUpRemovalMethod: 'HypoidGearWindUpRemovalMethodForMisalignments' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.HypoidGearWindUpRemovalMethodForMisalignments)
        return constructor.new(_1729.HypoidWindUpRemovalMethod)(value) if value else None

    @hypoid_gear_wind_up_removal_method_for_misalignments.setter
    def hypoid_gear_wind_up_removal_method_for_misalignments(self, value: '_1729.HypoidWindUpRemovalMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HypoidGearWindUpRemovalMethodForMisalignments = value

    @property
    def include_tilt_stiffness_for_bevel_hypoid_gears(self) -> 'bool':
        '''bool: 'IncludeTiltStiffnessForBevelHypoidGears' is the original name of this property.'''

        return self.wrapped.IncludeTiltStiffnessForBevelHypoidGears

    @include_tilt_stiffness_for_bevel_hypoid_gears.setter
    def include_tilt_stiffness_for_bevel_hypoid_gears(self, value: 'bool'):
        self.wrapped.IncludeTiltStiffnessForBevelHypoidGears = bool(value) if value else False

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MinimumPowerForGearMeshToBeLoaded' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MinimumPowerForGearMeshToBeLoaded) if self.wrapped.MinimumPowerForGearMeshToBeLoaded else None

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    def minimum_power_for_gear_mesh_to_be_loaded(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = value

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'MinimumTorqueForGearMeshToBeLoaded' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.MinimumTorqueForGearMeshToBeLoaded) if self.wrapped.MinimumTorqueForGearMeshToBeLoaded else None

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    def minimum_torque_for_gear_mesh_to_be_loaded(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = value

    @property
    def tolerance_factor_for_outer_fit(self) -> 'float':
        '''float: 'ToleranceFactorForOuterFit' is the original name of this property.'''

        return self.wrapped.ToleranceFactorForOuterFit

    @tolerance_factor_for_outer_fit.setter
    def tolerance_factor_for_outer_fit(self, value: 'float'):
        self.wrapped.ToleranceFactorForOuterFit = float(value) if value else 0.0

    @property
    def tolerance_factor_for_inner_fit(self) -> 'float':
        '''float: 'ToleranceFactorForInnerFit' is the original name of this property.'''

        return self.wrapped.ToleranceFactorForInnerFit

    @tolerance_factor_for_inner_fit.setter
    def tolerance_factor_for_inner_fit(self, value: 'float'):
        self.wrapped.ToleranceFactorForInnerFit = float(value) if value else 0.0

    @property
    def tolerance_factor_for_outer_support(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'ToleranceFactorForOuterSupport' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.ToleranceFactorForOuterSupport) if self.wrapped.ToleranceFactorForOuterSupport else None

    @tolerance_factor_for_outer_support.setter
    def tolerance_factor_for_outer_support(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.ToleranceFactorForOuterSupport = value

    @property
    def tolerance_factor_for_outer_ring(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'ToleranceFactorForOuterRing' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.ToleranceFactorForOuterRing) if self.wrapped.ToleranceFactorForOuterRing else None

    @tolerance_factor_for_outer_ring.setter
    def tolerance_factor_for_outer_ring(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.ToleranceFactorForOuterRing = value

    @property
    def tolerance_factor_for_inner_support(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'ToleranceFactorForInnerSupport' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.ToleranceFactorForInnerSupport) if self.wrapped.ToleranceFactorForInnerSupport else None

    @tolerance_factor_for_inner_support.setter
    def tolerance_factor_for_inner_support(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.ToleranceFactorForInnerSupport = value

    @property
    def tolerance_factor_for_inner_ring(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'ToleranceFactorForInnerRing' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.ToleranceFactorForInnerRing) if self.wrapped.ToleranceFactorForInnerRing else None

    @tolerance_factor_for_inner_ring.setter
    def tolerance_factor_for_inner_ring(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.ToleranceFactorForInnerRing = value

    @property
    def relative_tolerance_for_convergence(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'RelativeToleranceForConvergence' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.RelativeToleranceForConvergence) if self.wrapped.RelativeToleranceForConvergence else None

    @relative_tolerance_for_convergence.setter
    def relative_tolerance_for_convergence(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.RelativeToleranceForConvergence = value

    @property
    def air_density(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'AirDensity' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.AirDensity) if self.wrapped.AirDensity else None

    @air_density.setter
    def air_density(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.AirDensity = value

    @property
    def speed_of_sound(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'SpeedOfSound' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.SpeedOfSound) if self.wrapped.SpeedOfSound else None

    @speed_of_sound.setter
    def speed_of_sound(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.SpeedOfSound = value

    @property
    def characteristic_specific_acoustic_impedance(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'CharacteristicSpecificAcousticImpedance' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.CharacteristicSpecificAcousticImpedance) if self.wrapped.CharacteristicSpecificAcousticImpedance else None

    @characteristic_specific_acoustic_impedance.setter
    def characteristic_specific_acoustic_impedance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.CharacteristicSpecificAcousticImpedance = value

    @property
    def additional_acceleration(self) -> '_5878.AdditionalAccelerationOptions':
        '''AdditionalAccelerationOptions: 'AdditionalAcceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5878.AdditionalAccelerationOptions)(self.wrapped.AdditionalAcceleration) if self.wrapped.AdditionalAcceleration else None

    @property
    def temperatures(self) -> '_1740.TransmissionTemperatureSet':
        '''TransmissionTemperatureSet: 'Temperatures' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1740.TransmissionTemperatureSet)(self.wrapped.Temperatures) if self.wrapped.Temperatures else None

    @property
    def input_power_load(self) -> '_5990.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'InputPowerLoad' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5990.PowerLoadLoadCase)(self.wrapped.InputPowerLoad) if self.wrapped.InputPowerLoad else None

    @property
    def output_power_load(self) -> '_5990.PowerLoadLoadCase':
        '''PowerLoadLoadCase: 'OutputPowerLoad' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5990.PowerLoadLoadCase)(self.wrapped.OutputPowerLoad) if self.wrapped.OutputPowerLoad else None

    @property
    def parametric_study_tool_options(self) -> '_3439.ParametricStudyToolOptions':
        '''ParametricStudyToolOptions: 'ParametricStudyToolOptions' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3439.ParametricStudyToolOptions)(self.wrapped.ParametricStudyToolOptions) if self.wrapped.ParametricStudyToolOptions else None

    @property
    def power_loads(self) -> 'List[_5990.PowerLoadLoadCase]':
        '''List[PowerLoadLoadCase]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_5990.PowerLoadLoadCase))
        return value

    def inputs_for_straight_bevel_diff_gear_mesh(self, design_entity: '_1815.StraightBevelDiffGearMesh') -> '_6010.StraightBevelDiffGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6010.StraightBevelDiffGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_gear_mesh(self, design_entity: '_1793.BevelGearMesh') -> '_5893.BevelGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5893.BevelGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_conical_gear_mesh(self, design_entity: '_1797.ConicalGearMesh') -> '_5910.ConicalGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5910.ConicalGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_agma_gleason_conical_gear_mesh(self, design_entity: '_1789.AGMAGleasonConicalGearMesh') -> '_5880.AGMAGleasonConicalGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5880.AGMAGleasonConicalGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_cylindrical_gear_mesh(self, design_entity: '_1799.CylindricalGearMesh') -> '_5923.CylindricalGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5923.CylindricalGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_hypoid_gear_mesh(self, design_entity: '_1805.HypoidGearMesh') -> '_5962.HypoidGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5962.HypoidGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_conical_gear_mesh(self, design_entity: '_1808.KlingelnbergCycloPalloidConicalGearMesh') -> '_5968.KlingelnbergCycloPalloidConicalGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidConicalGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5968.KlingelnbergCycloPalloidConicalGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, design_entity: '_1809.KlingelnbergCycloPalloidHypoidGearMesh') -> '_5971.KlingelnbergCycloPalloidHypoidGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5971.KlingelnbergCycloPalloidHypoidGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, design_entity: '_1810.KlingelnbergCycloPalloidSpiralBevelGearMesh') -> '_5974.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidSpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5974.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_spiral_bevel_gear_mesh(self, design_entity: '_1813.SpiralBevelGearMesh') -> '_6003.SpiralBevelGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6003.SpiralBevelGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_gear_mesh(self, design_entity: '_1817.StraightBevelGearMesh') -> '_6013.StraightBevelGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6013.StraightBevelGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_worm_gear_mesh(self, design_entity: '_1819.WormGearMesh') -> '_6033.WormGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.WormGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6033.WormGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_zerol_bevel_gear_mesh(self, design_entity: '_1821.ZerolBevelGearMesh') -> '_6036.ZerolBevelGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6036.ZerolBevelGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_gear_mesh(self, design_entity: '_1803.GearMesh') -> '_5948.GearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.GearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5948.GearMeshLoadCase)(method_result) if method_result else None

    def analysis_of(self, analysis_type: '_5882.AnalysisType') -> '_2074.SingleAnalysis':
        ''' 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.SingleAnalysis
        '''

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        return constructor.new(_2074.SingleAnalysis)(method_result) if method_result else None

    def delete(self):
        ''' 'Delete' is the original name of this method.'''

        self.wrapped.Delete()

    def inputs_for_abstract_assembly(self, design_entity: '_1907.AbstractAssembly') -> '_5876.AbstractAssemblyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.AbstractAssemblyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5876.AbstractAssemblyLoadCase)(method_result) if method_result else None

    def inputs_for_abstract_shaft_or_housing(self, design_entity: '_1908.AbstractShaftOrHousing') -> '_5877.AbstractShaftOrHousingLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.AbstractShaftOrHousing)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.AbstractShaftOrHousingLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5877.AbstractShaftOrHousingLoadCase)(method_result) if method_result else None

    def inputs_for_bearing(self, design_entity: '_1910.Bearing') -> '_5884.BearingLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bearing)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BearingLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5884.BearingLoadCase)(method_result) if method_result else None

    def inputs_for_bolt(self, design_entity: '_1912.Bolt') -> '_5896.BoltLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Bolt)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BoltLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5896.BoltLoadCase)(method_result) if method_result else None

    def inputs_for_bolted_joint(self, design_entity: '_1913.BoltedJoint') -> '_5895.BoltedJointLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.BoltedJoint)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5895.BoltedJointLoadCase)(method_result) if method_result else None

    def inputs_for_component(self, design_entity: '_1914.Component') -> '_5901.ComponentLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ComponentLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5901.ComponentLoadCase)(method_result) if method_result else None

    def inputs_for_connector(self, design_entity: '_1917.Connector') -> '_5914.ConnectorLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Connector)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConnectorLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5914.ConnectorLoadCase)(method_result) if method_result else None

    def inputs_for_datum(self, design_entity: '_1918.Datum') -> '_5929.DatumLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Datum)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5929.DatumLoadCase)(method_result) if method_result else None

    def inputs_for_external_cad_model(self, design_entity: '_1921.ExternalCADModel') -> '_5940.ExternalCADModelLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ExternalCADModel)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5940.ExternalCADModelLoadCase)(method_result) if method_result else None

    def inputs_for_flexible_pin_assembly(self, design_entity: '_1922.FlexiblePinAssembly') -> '_5944.FlexiblePinAssemblyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.FlexiblePinAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.FlexiblePinAssemblyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5944.FlexiblePinAssemblyLoadCase)(method_result) if method_result else None

    def inputs_for_assembly(self, design_entity: '_1906.Assembly') -> '_5883.AssemblyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Assembly)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.AssemblyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5883.AssemblyLoadCase)(method_result) if method_result else None

    def inputs_for_guide_dxf_model(self, design_entity: '_1923.GuideDxfModel') -> '_5952.GuideDxfModelLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.GuideDxfModel)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5952.GuideDxfModelLoadCase)(method_result) if method_result else None

    def inputs_for_imported_fe_component(self, design_entity: '_1926.ImportedFEComponent') -> '_5964.ImportedFEComponentLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.ImportedFEComponent)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ImportedFEComponentLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5964.ImportedFEComponentLoadCase)(method_result) if method_result else None

    def inputs_for_mass_disc(self, design_entity: '_1928.MassDisc') -> '_5976.MassDiscLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MassDisc)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5976.MassDiscLoadCase)(method_result) if method_result else None

    def inputs_for_measurement_component(self, design_entity: '_1929.MeasurementComponent') -> '_5977.MeasurementComponentLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MeasurementComponent)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5977.MeasurementComponentLoadCase)(method_result) if method_result else None

    def inputs_for_mountable_component(self, design_entity: '_1930.MountableComponent') -> '_5978.MountableComponentLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.MountableComponent)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.MountableComponentLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5978.MountableComponentLoadCase)(method_result) if method_result else None

    def inputs_for_oil_seal(self, design_entity: '_1931.OilSeal') -> '_5980.OilSealLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.OilSeal)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5980.OilSealLoadCase)(method_result) if method_result else None

    def inputs_for_part(self, design_entity: '_1933.Part') -> '_5982.PartLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.Part)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PartLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5982.PartLoadCase)(method_result) if method_result else None

    def inputs_for_planet_carrier(self, design_entity: '_1934.PlanetCarrier') -> '_5986.PlanetCarrierLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PlanetCarrier)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5986.PlanetCarrierLoadCase)(method_result) if method_result else None

    def inputs_for_point_load(self, design_entity: '_1936.PointLoad') -> '_5989.PointLoadLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PointLoad)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PointLoadLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5989.PointLoadLoadCase)(method_result) if method_result else None

    def inputs_for_power_load(self, design_entity: '_1937.PowerLoad') -> '_5990.PowerLoadLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.PowerLoad)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PowerLoadLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5990.PowerLoadLoadCase)(method_result) if method_result else None

    def inputs_for_root_assembly(self, design_entity: '_1938.RootAssembly') -> '_5996.RootAssemblyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.RootAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.RootAssemblyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5996.RootAssemblyLoadCase)(method_result) if method_result else None

    def inputs_for_specialised_assembly(self, design_entity: '_1940.SpecialisedAssembly') -> '_6000.SpecialisedAssemblyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.SpecialisedAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpecialisedAssemblyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6000.SpecialisedAssemblyLoadCase)(method_result) if method_result else None

    def inputs_for_unbalanced_mass(self, design_entity: '_1941.UnbalancedMass') -> '_6030.UnbalancedMassLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.UnbalancedMass)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6030.UnbalancedMassLoadCase)(method_result) if method_result else None

    def inputs_for_virtual_component(self, design_entity: '_1942.VirtualComponent') -> '_6031.VirtualComponentLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.VirtualComponent)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.VirtualComponentLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6031.VirtualComponentLoadCase)(method_result) if method_result else None

    def inputs_for_shaft(self, design_entity: '_1945.Shaft') -> '_5998.ShaftLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.shaft_model.Shaft)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5998.ShaftLoadCase)(method_result) if method_result else None

    def inputs_for_concept_gear(self, design_entity: '_1983.ConceptGear') -> '_5905.ConceptGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConceptGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5905.ConceptGearLoadCase)(method_result) if method_result else None

    def inputs_for_concept_gear_set(self, design_entity: '_1984.ConceptGearSet') -> '_5907.ConceptGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConceptGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5907.ConceptGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_face_gear(self, design_entity: '_1990.FaceGear') -> '_5941.FaceGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5941.FaceGearLoadCase)(method_result) if method_result else None

    def inputs_for_face_gear_set(self, design_entity: '_1991.FaceGearSet') -> '_5943.FaceGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.FaceGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5943.FaceGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_agma_gleason_conical_gear(self, design_entity: '_1975.AGMAGleasonConicalGear') -> '_5879.AGMAGleasonConicalGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5879.AGMAGleasonConicalGearLoadCase)(method_result) if method_result else None

    def inputs_for_agma_gleason_conical_gear_set(self, design_entity: '_1976.AGMAGleasonConicalGearSet') -> '_5881.AGMAGleasonConicalGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.AGMAGleasonConicalGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5881.AGMAGleasonConicalGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_differential_gear(self, design_entity: '_1977.BevelDifferentialGear') -> '_5887.BevelDifferentialGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5887.BevelDifferentialGearLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_differential_gear_set(self, design_entity: '_1978.BevelDifferentialGearSet') -> '_5889.BevelDifferentialGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5889.BevelDifferentialGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_differential_planet_gear(self, design_entity: '_1979.BevelDifferentialPlanetGear') -> '_5890.BevelDifferentialPlanetGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialPlanetGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5890.BevelDifferentialPlanetGearLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_differential_sun_gear(self, design_entity: '_1980.BevelDifferentialSunGear') -> '_5891.BevelDifferentialSunGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelDifferentialSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialSunGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5891.BevelDifferentialSunGearLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_gear(self, design_entity: '_1981.BevelGear') -> '_5892.BevelGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5892.BevelGearLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_gear_set(self, design_entity: '_1982.BevelGearSet') -> '_5894.BevelGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.BevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5894.BevelGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_conical_gear(self, design_entity: '_1985.ConicalGear') -> '_5908.ConicalGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5908.ConicalGearLoadCase)(method_result) if method_result else None

    def inputs_for_conical_gear_set(self, design_entity: '_1986.ConicalGearSet') -> '_5912.ConicalGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5912.ConicalGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_cylindrical_gear(self, design_entity: '_1987.CylindricalGear') -> '_5921.CylindricalGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5921.CylindricalGearLoadCase)(method_result) if method_result else None

    def inputs_for_cylindrical_gear_set(self, design_entity: '_1988.CylindricalGearSet') -> '_5925.CylindricalGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5925.CylindricalGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_cylindrical_planet_gear(self, design_entity: '_1989.CylindricalPlanetGear') -> '_5926.CylindricalPlanetGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.CylindricalPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CylindricalPlanetGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5926.CylindricalPlanetGearLoadCase)(method_result) if method_result else None

    def inputs_for_gear(self, design_entity: '_1992.Gear') -> '_5946.GearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.Gear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.GearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5946.GearLoadCase)(method_result) if method_result else None

    def inputs_for_gear_set(self, design_entity: '_1994.GearSet') -> '_5951.GearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.GearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.GearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5951.GearSetLoadCase)(method_result) if method_result else None

    def inputs_for_hypoid_gear(self, design_entity: '_1996.HypoidGear') -> '_5961.HypoidGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5961.HypoidGearLoadCase)(method_result) if method_result else None

    def inputs_for_hypoid_gear_set(self, design_entity: '_1997.HypoidGearSet') -> '_5963.HypoidGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.HypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.HypoidGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5963.HypoidGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_conical_gear(self, design_entity: '_1998.KlingelnbergCycloPalloidConicalGear') -> '_5967.KlingelnbergCycloPalloidConicalGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5967.KlingelnbergCycloPalloidConicalGearLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_conical_gear_set(self, design_entity: '_1999.KlingelnbergCycloPalloidConicalGearSet') -> '_5969.KlingelnbergCycloPalloidConicalGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidConicalGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5969.KlingelnbergCycloPalloidConicalGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear(self, design_entity: '_2000.KlingelnbergCycloPalloidHypoidGear') -> '_5970.KlingelnbergCycloPalloidHypoidGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5970.KlingelnbergCycloPalloidHypoidGearLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_hypoid_gear_set(self, design_entity: '_2001.KlingelnbergCycloPalloidHypoidGearSet') -> '_5972.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5972.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, design_entity: '_2002.KlingelnbergCycloPalloidSpiralBevelGear') -> '_5973.KlingelnbergCycloPalloidSpiralBevelGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5973.KlingelnbergCycloPalloidSpiralBevelGearLoadCase)(method_result) if method_result else None

    def inputs_for_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, design_entity: '_2003.KlingelnbergCycloPalloidSpiralBevelGearSet') -> '_5975.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5975.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_planetary_gear_set(self, design_entity: '_2004.PlanetaryGearSet') -> '_5984.PlanetaryGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.PlanetaryGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PlanetaryGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5984.PlanetaryGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_spiral_bevel_gear(self, design_entity: '_2005.SpiralBevelGear') -> '_6002.SpiralBevelGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6002.SpiralBevelGearLoadCase)(method_result) if method_result else None

    def inputs_for_spiral_bevel_gear_set(self, design_entity: '_2006.SpiralBevelGearSet') -> '_6004.SpiralBevelGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.SpiralBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6004.SpiralBevelGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_diff_gear(self, design_entity: '_2007.StraightBevelDiffGear') -> '_6009.StraightBevelDiffGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6009.StraightBevelDiffGearLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_diff_gear_set(self, design_entity: '_2008.StraightBevelDiffGearSet') -> '_6011.StraightBevelDiffGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelDiffGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6011.StraightBevelDiffGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_gear(self, design_entity: '_2009.StraightBevelGear') -> '_6012.StraightBevelGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6012.StraightBevelGearLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_gear_set(self, design_entity: '_2010.StraightBevelGearSet') -> '_6014.StraightBevelGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6014.StraightBevelGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_planet_gear(self, design_entity: '_2011.StraightBevelPlanetGear') -> '_6015.StraightBevelPlanetGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelPlanetGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelPlanetGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6015.StraightBevelPlanetGearLoadCase)(method_result) if method_result else None

    def inputs_for_straight_bevel_sun_gear(self, design_entity: '_2012.StraightBevelSunGear') -> '_6016.StraightBevelSunGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.StraightBevelSunGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.StraightBevelSunGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6016.StraightBevelSunGearLoadCase)(method_result) if method_result else None

    def inputs_for_worm_gear(self, design_entity: '_2013.WormGear') -> '_6032.WormGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.WormGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6032.WormGearLoadCase)(method_result) if method_result else None

    def inputs_for_worm_gear_set(self, design_entity: '_2014.WormGearSet') -> '_6034.WormGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.WormGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.WormGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6034.WormGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_zerol_bevel_gear(self, design_entity: '_2015.ZerolBevelGear') -> '_6035.ZerolBevelGearLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGear)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6035.ZerolBevelGearLoadCase)(method_result) if method_result else None

    def inputs_for_zerol_bevel_gear_set(self, design_entity: '_2016.ZerolBevelGearSet') -> '_6037.ZerolBevelGearSetLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.gears.ZerolBevelGearSet)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6037.ZerolBevelGearSetLoadCase)(method_result) if method_result else None

    def inputs_for_belt_drive(self, design_entity: '_2034.BeltDrive') -> '_5886.BeltDriveLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.BeltDrive)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5886.BeltDriveLoadCase)(method_result) if method_result else None

    def inputs_for_clutch(self, design_entity: '_2036.Clutch') -> '_5899.ClutchLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Clutch)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5899.ClutchLoadCase)(method_result) if method_result else None

    def inputs_for_clutch_half(self, design_entity: '_2037.ClutchHalf') -> '_5898.ClutchHalfLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ClutchHalf)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5898.ClutchHalfLoadCase)(method_result) if method_result else None

    def inputs_for_concept_coupling(self, design_entity: '_2039.ConceptCoupling') -> '_5904.ConceptCouplingLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCoupling)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5904.ConceptCouplingLoadCase)(method_result) if method_result else None

    def inputs_for_concept_coupling_half(self, design_entity: '_2040.ConceptCouplingHalf') -> '_5903.ConceptCouplingHalfLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ConceptCouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingHalfLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5903.ConceptCouplingHalfLoadCase)(method_result) if method_result else None

    def inputs_for_coupling(self, design_entity: '_2041.Coupling') -> '_5917.CouplingLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Coupling)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CouplingLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5917.CouplingLoadCase)(method_result) if method_result else None

    def inputs_for_coupling_half(self, design_entity: '_2042.CouplingHalf') -> '_5916.CouplingHalfLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CouplingHalf)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CouplingHalfLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5916.CouplingHalfLoadCase)(method_result) if method_result else None

    def inputs_for_cvt(self, design_entity: '_2043.CVT') -> '_5919.CVTLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVT)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CVTLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5919.CVTLoadCase)(method_result) if method_result else None

    def inputs_for_cvt_pulley(self, design_entity: '_2044.CVTPulley') -> '_5920.CVTPulleyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.CVTPulley)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CVTPulleyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5920.CVTPulleyLoadCase)(method_result) if method_result else None

    def inputs_for_pulley(self, design_entity: '_2045.Pulley') -> '_5991.PulleyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Pulley)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5991.PulleyLoadCase)(method_result) if method_result else None

    def inputs_for_shaft_hub_connection(self, design_entity: '_2053.ShaftHubConnection') -> '_5997.ShaftHubConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.ShaftHubConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ShaftHubConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5997.ShaftHubConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_rolling_ring(self, design_entity: '_2051.RollingRing') -> '_5995.RollingRingLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRing)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5995.RollingRingLoadCase)(method_result) if method_result else None

    def inputs_for_rolling_ring_assembly(self, design_entity: '_2052.RollingRingAssembly') -> '_5993.RollingRingAssemblyLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.RollingRingAssembly)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5993.RollingRingAssemblyLoadCase)(method_result) if method_result else None

    def inputs_for_spring_damper(self, design_entity: '_2054.SpringDamper') -> '_6007.SpringDamperLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamper)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6007.SpringDamperLoadCase)(method_result) if method_result else None

    def inputs_for_spring_damper_half(self, design_entity: '_2055.SpringDamperHalf') -> '_6006.SpringDamperHalfLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SpringDamperHalf)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6006.SpringDamperHalfLoadCase)(method_result) if method_result else None

    def inputs_for_synchroniser(self, design_entity: '_2056.Synchroniser') -> '_6018.SynchroniserLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.Synchroniser)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6018.SynchroniserLoadCase)(method_result) if method_result else None

    def inputs_for_synchroniser_half(self, design_entity: '_2058.SynchroniserHalf') -> '_6017.SynchroniserHalfLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserHalf)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6017.SynchroniserHalfLoadCase)(method_result) if method_result else None

    def inputs_for_synchroniser_part(self, design_entity: '_2059.SynchroniserPart') -> '_6019.SynchroniserPartLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserPart)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SynchroniserPartLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6019.SynchroniserPartLoadCase)(method_result) if method_result else None

    def inputs_for_synchroniser_sleeve(self, design_entity: '_2060.SynchroniserSleeve') -> '_6020.SynchroniserSleeveLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.SynchroniserSleeve)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6020.SynchroniserSleeveLoadCase)(method_result) if method_result else None

    def inputs_for_torque_converter(self, design_entity: '_2061.TorqueConverter') -> '_6024.TorqueConverterLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverter)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.TorqueConverterLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6024.TorqueConverterLoadCase)(method_result) if method_result else None

    def inputs_for_torque_converter_pump(self, design_entity: '_2062.TorqueConverterPump') -> '_6025.TorqueConverterPumpLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterPump)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.TorqueConverterPumpLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6025.TorqueConverterPumpLoadCase)(method_result) if method_result else None

    def inputs_for_torque_converter_turbine(self, design_entity: '_2064.TorqueConverterTurbine') -> '_6026.TorqueConverterTurbineLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.part_model.couplings.TorqueConverterTurbine)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.TorqueConverterTurbineLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6026.TorqueConverterTurbineLoadCase)(method_result) if method_result else None

    def inputs_for_cvt_belt_connection(self, design_entity: '_1766.CVTBeltConnection') -> '_5918.CVTBeltConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CVTBeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CVTBeltConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5918.CVTBeltConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_belt_connection(self, design_entity: '_1761.BeltConnection') -> '_5885.BeltConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.BeltConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5885.BeltConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_coaxial_connection(self, design_entity: '_1762.CoaxialConnection') -> '_5900.CoaxialConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.CoaxialConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5900.CoaxialConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_connection(self, design_entity: '_1765.Connection') -> '_5913.ConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.Connection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5913.ConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_inter_mountable_component_connection(self, design_entity: '_1774.InterMountableComponentConnection') -> '_5966.InterMountableComponentConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.InterMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.InterMountableComponentConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5966.InterMountableComponentConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_planetary_connection(self, design_entity: '_1777.PlanetaryConnection') -> '_5983.PlanetaryConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.PlanetaryConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5983.PlanetaryConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_rolling_ring_connection(self, design_entity: '_1781.RollingRingConnection') -> '_5994.RollingRingConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.RollingRingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.RollingRingConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5994.RollingRingConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_shaft_to_mountable_component_connection(self, design_entity: '_1785.ShaftToMountableComponentConnection') -> '_5999.ShaftToMountableComponentConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ShaftToMountableComponentConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5999.ShaftToMountableComponentConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_clutch_connection(self, design_entity: '_1823.ClutchConnection') -> '_5897.ClutchConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ClutchConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5897.ClutchConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_concept_coupling_connection(self, design_entity: '_1825.ConceptCouplingConnection') -> '_5902.ConceptCouplingConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5902.ConceptCouplingConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_coupling_connection(self, design_entity: '_1827.CouplingConnection') -> '_5915.CouplingConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.CouplingConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CouplingConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5915.CouplingConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_spring_damper_connection(self, design_entity: '_1829.SpringDamperConnection') -> '_6005.SpringDamperConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6005.SpringDamperConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_torque_converter_connection(self, design_entity: '_1831.TorqueConverterConnection') -> '_6023.TorqueConverterConnectionLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_6023.TorqueConverterConnectionLoadCase)(method_result) if method_result else None

    def inputs_for_bevel_differential_gear_mesh(self, design_entity: '_1791.BevelDifferentialGearMesh') -> '_5888.BevelDifferentialGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5888.BevelDifferentialGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_concept_gear_mesh(self, design_entity: '_1795.ConceptGearMesh') -> '_5906.ConceptGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5906.ConceptGearMeshLoadCase)(method_result) if method_result else None

    def inputs_for_face_gear_mesh(self, design_entity: '_1801.FaceGearMesh') -> '_5942.FaceGearMeshLoadCase':
        ''' 'InputsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.connections_and_sockets.gears.FaceGearMesh)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase
        '''

        method_result = self.wrapped.InputsFor(design_entity.wrapped if design_entity else None)
        return constructor.new(_5942.FaceGearMeshLoadCase)(method_result) if method_result else None
