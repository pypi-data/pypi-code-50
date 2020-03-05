'''_2134.py

BearingSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _1910, _1911
from mastapy.system_model.analyses_and_results.static_loads import _5884
from mastapy.math_utility.measured_vectors import _1227
from mastapy.utility.units_and_measurements.measurements import _1315, _1269
from mastapy.bearings.bearing_results import (
    _1519, _1524, _1526, _1527,
    _1528, _1529, _1530, _1532
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_results.rolling import (
    _1550, _1553, _1556, _1561,
    _1564, _1569, _1573, _1576,
    _1581, _1585, _1588, _1593,
    _1597, _1600, _1604, _1607,
    _1613, _1616, _1619, _1622
)
from mastapy.bearings.bearing_results.fluid_film import (
    _1649, _1650, _1651, _1653,
    _1656, _1657
)
from mastapy.system_model.analyses_and_results.system_deflections import _2164
from mastapy._internal.python_net import python_net_import

_BEARING_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSystemDeflection',)


class BearingSystemDeflection(_2164.ConnectorSystemDeflection):
    '''BearingSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _BEARING_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def element_radial_displacements(self) -> 'List[float]':
        '''List[float]: 'ElementRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ElementRadialDisplacements, float)
        return value

    @property
    def element_axial_displacements(self) -> 'List[float]':
        '''List[float]: 'ElementAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ElementAxialDisplacements, float)
        return value

    @property
    def element_tilts(self) -> 'List[float]':
        '''List[float]: 'ElementTilts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ElementTilts, float)
        return value

    @property
    def maximum_radial_stiffness(self) -> 'float':
        '''float: 'MaximumRadialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumRadialStiffness

    @property
    def maximum_tilt_stiffness(self) -> 'float':
        '''float: 'MaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumTiltStiffness

    @property
    def axial_stiffness(self) -> 'float':
        '''float: 'AxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AxialStiffness

    @property
    def inner_left_mounting_axial_stiffness(self) -> 'float':
        '''float: 'InnerLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InnerLeftMountingAxialStiffness

    @property
    def inner_right_mounting_axial_stiffness(self) -> 'float':
        '''float: 'InnerRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InnerRightMountingAxialStiffness

    @property
    def outer_left_mounting_axial_stiffness(self) -> 'float':
        '''float: 'OuterLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OuterLeftMountingAxialStiffness

    @property
    def outer_right_mounting_axial_stiffness(self) -> 'float':
        '''float: 'OuterRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OuterRightMountingAxialStiffness

    @property
    def inner_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        '''float: 'InnerLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InnerLeftMountingMaximumTiltStiffness

    @property
    def inner_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        '''float: 'InnerRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InnerRightMountingMaximumTiltStiffness

    @property
    def outer_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        '''float: 'OuterLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OuterLeftMountingMaximumTiltStiffness

    @property
    def outer_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        '''float: 'OuterRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OuterRightMountingMaximumTiltStiffness

    @property
    def outer_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        '''float: 'OuterRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OuterRadialMountingMaximumTiltStiffness

    @property
    def inner_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        '''float: 'InnerRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.InnerRadialMountingMaximumTiltStiffness

    @property
    def elements_in_contact(self) -> 'int':
        '''int: 'ElementsInContact' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ElementsInContact

    @property
    def is_loaded(self) -> 'bool':
        '''bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.IsLoaded

    @property
    def linear_displacement_axial_component(self) -> 'float':
        '''float: 'LinearDisplacementAxialComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LinearDisplacementAxialComponent

    @property
    def percentage_preload_spring_compression(self) -> 'float':
        '''float: 'PercentagePreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PercentagePreloadSpringCompression

    @property
    def preload_spring_compression(self) -> 'float':
        '''float: 'PreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PreloadSpringCompression

    @property
    def component_design(self) -> '_1910.Bearing':
        '''Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1910.Bearing)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign else None

    @property
    def component_load_case(self) -> '_5884.BearingLoadCase':
        '''BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5884.BearingLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase else None

    @property
    def relative_displacement_in_wcs(self) -> '_1227.VectorWithLinearAndAngularComponents[_1315.LengthVeryShort, _1269.AngleSmall]':
        '''VectorWithLinearAndAngularComponents[LengthVeryShort, AngleSmall]: 'RelativeDisplacementInWCS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1227.VectorWithLinearAndAngularComponents)[_1315.LengthVeryShort, _1269.AngleSmall](self.wrapped.RelativeDisplacementInWCS) if self.wrapped.RelativeDisplacementInWCS else None

    @property
    def relative_displacement_in_lcs(self) -> '_1227.VectorWithLinearAndAngularComponents[_1315.LengthVeryShort, _1269.AngleSmall]':
        '''VectorWithLinearAndAngularComponents[LengthVeryShort, AngleSmall]: 'RelativeDisplacementInLCS' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1227.VectorWithLinearAndAngularComponents)[_1315.LengthVeryShort, _1269.AngleSmall](self.wrapped.RelativeDisplacementInLCS) if self.wrapped.RelativeDisplacementInLCS else None

    @property
    def stiffness_between_rings(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'StiffnessBetweenRings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.StiffnessBetweenRings) if self.wrapped.StiffnessBetweenRings else None

    @property
    def stiffness_matrix(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'StiffnessMatrix' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.StiffnessMatrix) if self.wrapped.StiffnessMatrix else None

    @property
    def outer_left_mounting_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'OuterLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.OuterLeftMountingStiffness) if self.wrapped.OuterLeftMountingStiffness else None

    @property
    def outer_right_mounting_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'OuterRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.OuterRightMountingStiffness) if self.wrapped.OuterRightMountingStiffness else None

    @property
    def inner_left_mounting_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'InnerLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.InnerLeftMountingStiffness) if self.wrapped.InnerLeftMountingStiffness else None

    @property
    def inner_right_mounting_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'InnerRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.InnerRightMountingStiffness) if self.wrapped.InnerRightMountingStiffness else None

    @property
    def inner_radial_mounting_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'InnerRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.InnerRadialMountingStiffness) if self.wrapped.InnerRadialMountingStiffness else None

    @property
    def outer_radial_mounting_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'OuterRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.OuterRadialMountingStiffness) if self.wrapped.OuterRadialMountingStiffness else None

    @property
    def preload_spring_stiffness(self) -> '_1519.BearingStiffnessMatrixReporter':
        '''BearingStiffnessMatrixReporter: 'PreloadSpringStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1519.BearingStiffnessMatrixReporter)(self.wrapped.PreloadSpringStiffness) if self.wrapped.PreloadSpringStiffness else None

    @property
    def component_detailed_analysis(self) -> '_1524.LoadedBearingResults':
        '''LoadedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1524.LoadedBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_axial_clearance_bearing_results(self) -> '_1526.LoadedConceptAxialClearanceBearingResults':
        '''LoadedConceptAxialClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1526.LoadedConceptAxialClearanceBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptAxialClearanceBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1526.LoadedConceptAxialClearanceBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_clearance_bearing_results(self) -> '_1527.LoadedConceptClearanceBearingResults':
        '''LoadedConceptClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1527.LoadedConceptClearanceBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptClearanceBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1527.LoadedConceptClearanceBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_radial_clearance_bearing_results(self) -> '_1528.LoadedConceptRadialClearanceBearingResults':
        '''LoadedConceptRadialClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1528.LoadedConceptRadialClearanceBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptRadialClearanceBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1528.LoadedConceptRadialClearanceBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_detailed_bearing_results(self) -> '_1529.LoadedDetailedBearingResults':
        '''LoadedDetailedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1529.LoadedDetailedBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedDetailedBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1529.LoadedDetailedBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_linear_bearing_results(self) -> '_1530.LoadedLinearBearingResults':
        '''LoadedLinearBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1530.LoadedLinearBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedLinearBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1530.LoadedLinearBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_non_linear_bearing_results(self) -> '_1532.LoadedNonLinearBearingResults':
        '''LoadedNonLinearBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1532.LoadedNonLinearBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNonLinearBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1532.LoadedNonLinearBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_angular_contact_ball_bearing_results(self) -> '_1550.LoadedAngularContactBallBearingResults':
        '''LoadedAngularContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1550.LoadedAngularContactBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAngularContactBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1550.LoadedAngularContactBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_angular_contact_thrust_ball_bearing_results(self) -> '_1553.LoadedAngularContactThrustBallBearingResults':
        '''LoadedAngularContactThrustBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1553.LoadedAngularContactThrustBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAngularContactThrustBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1553.LoadedAngularContactThrustBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_asymmetric_spherical_roller_bearing_results(self) -> '_1556.LoadedAsymmetricSphericalRollerBearingResults':
        '''LoadedAsymmetricSphericalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1556.LoadedAsymmetricSphericalRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAsymmetricSphericalRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1556.LoadedAsymmetricSphericalRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_axial_thrust_cylindrical_roller_bearing_results(self) -> '_1561.LoadedAxialThrustCylindricalRollerBearingResults':
        '''LoadedAxialThrustCylindricalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1561.LoadedAxialThrustCylindricalRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAxialThrustCylindricalRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1561.LoadedAxialThrustCylindricalRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_axial_thrust_needle_roller_bearing_results(self) -> '_1564.LoadedAxialThrustNeedleRollerBearingResults':
        '''LoadedAxialThrustNeedleRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1564.LoadedAxialThrustNeedleRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAxialThrustNeedleRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1564.LoadedAxialThrustNeedleRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_ball_bearing_results(self) -> '_1569.LoadedBallBearingResults':
        '''LoadedBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1569.LoadedBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1569.LoadedBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_cylindrical_roller_bearing_results(self) -> '_1573.LoadedCylindricalRollerBearingResults':
        '''LoadedCylindricalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1573.LoadedCylindricalRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedCylindricalRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1573.LoadedCylindricalRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_deep_groove_ball_bearing_results(self) -> '_1576.LoadedDeepGrooveBallBearingResults':
        '''LoadedDeepGrooveBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1576.LoadedDeepGrooveBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedDeepGrooveBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1576.LoadedDeepGrooveBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_four_point_contact_ball_bearing_results(self) -> '_1581.LoadedFourPointContactBallBearingResults':
        '''LoadedFourPointContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1581.LoadedFourPointContactBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedFourPointContactBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1581.LoadedFourPointContactBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_needle_roller_bearing_results(self) -> '_1585.LoadedNeedleRollerBearingResults':
        '''LoadedNeedleRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1585.LoadedNeedleRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNeedleRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1585.LoadedNeedleRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_non_barrel_roller_bearing_results(self) -> '_1588.LoadedNonBarrelRollerBearingResults':
        '''LoadedNonBarrelRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1588.LoadedNonBarrelRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNonBarrelRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1588.LoadedNonBarrelRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_roller_bearing_results(self) -> '_1593.LoadedRollerBearingResults':
        '''LoadedRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1593.LoadedRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1593.LoadedRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_rolling_bearing_results(self) -> '_1597.LoadedRollingBearingResults':
        '''LoadedRollingBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1597.LoadedRollingBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedRollingBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1597.LoadedRollingBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_self_aligning_ball_bearing_results(self) -> '_1600.LoadedSelfAligningBallBearingResults':
        '''LoadedSelfAligningBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1600.LoadedSelfAligningBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSelfAligningBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1600.LoadedSelfAligningBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_spherical_roller_radial_bearing_results(self) -> '_1604.LoadedSphericalRollerRadialBearingResults':
        '''LoadedSphericalRollerRadialBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1604.LoadedSphericalRollerRadialBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSphericalRollerRadialBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1604.LoadedSphericalRollerRadialBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_spherical_roller_thrust_bearing_results(self) -> '_1607.LoadedSphericalRollerThrustBearingResults':
        '''LoadedSphericalRollerThrustBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1607.LoadedSphericalRollerThrustBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSphericalRollerThrustBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1607.LoadedSphericalRollerThrustBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_taper_roller_bearing_results(self) -> '_1613.LoadedTaperRollerBearingResults':
        '''LoadedTaperRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1613.LoadedTaperRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTaperRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1613.LoadedTaperRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_three_point_contact_ball_bearing_results(self) -> '_1616.LoadedThreePointContactBallBearingResults':
        '''LoadedThreePointContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1616.LoadedThreePointContactBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedThreePointContactBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1616.LoadedThreePointContactBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_thrust_ball_bearing_results(self) -> '_1619.LoadedThrustBallBearingResults':
        '''LoadedThrustBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1619.LoadedThrustBallBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedThrustBallBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1619.LoadedThrustBallBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_toroidal_roller_bearing_results(self) -> '_1622.LoadedToroidalRollerBearingResults':
        '''LoadedToroidalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1622.LoadedToroidalRollerBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedToroidalRollerBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1622.LoadedToroidalRollerBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_grease_filled_journal_bearing_results(self) -> '_1649.LoadedGreaseFilledJournalBearingResults':
        '''LoadedGreaseFilledJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1649.LoadedGreaseFilledJournalBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedGreaseFilledJournalBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1649.LoadedGreaseFilledJournalBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_pad_fluid_film_bearing_results(self) -> '_1650.LoadedPadFluidFilmBearingResults':
        '''LoadedPadFluidFilmBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1650.LoadedPadFluidFilmBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPadFluidFilmBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1650.LoadedPadFluidFilmBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_plain_journal_bearing_results(self) -> '_1651.LoadedPlainJournalBearingResults':
        '''LoadedPlainJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1651.LoadedPlainJournalBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPlainJournalBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1651.LoadedPlainJournalBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_plain_oil_fed_journal_bearing(self) -> '_1653.LoadedPlainOilFedJournalBearing':
        '''LoadedPlainOilFedJournalBearing: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1653.LoadedPlainOilFedJournalBearing.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPlainOilFedJournalBearing. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1653.LoadedPlainOilFedJournalBearing)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_tilting_pad_journal_bearing_results(self) -> '_1656.LoadedTiltingPadJournalBearingResults':
        '''LoadedTiltingPadJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1656.LoadedTiltingPadJournalBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTiltingPadJournalBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1656.LoadedTiltingPadJournalBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def component_detailed_analysis_of_type_loaded_tilting_pad_thrust_bearing_results(self) -> '_1657.LoadedTiltingPadThrustBearingResults':
        '''LoadedTiltingPadThrustBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1657.LoadedTiltingPadThrustBearingResults.TYPE not in self.wrapped.ComponentDetailedAnalysis.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTiltingPadThrustBearingResults. Expected: {}.'.format(self.wrapped.ComponentDetailedAnalysis.__class__.__qualname__))

        return constructor.new(_1657.LoadedTiltingPadThrustBearingResults)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis else None

    @property
    def planetaries(self) -> 'List[BearingSystemDeflection]':
        '''List[BearingSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(BearingSystemDeflection))
        return value

    @property
    def race_mounting_options_for_analysis(self) -> 'List[_1911.BearingRaceMountingOptions]':
        '''List[BearingRaceMountingOptions]: 'RaceMountingOptionsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RaceMountingOptionsForAnalysis, constructor.new(_1911.BearingRaceMountingOptions))
        return value
