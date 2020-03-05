'''_1550.py

LoadedBearingResults
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results import _1561
from mastapy.math_utility.measured_vectors import _1106
from mastapy.utility.units_and_measurements.measurements import _1168, _1240
from mastapy.bearings.bearing_designs import (
    _1709, _1710, _1711, _1712,
    _1713
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs.rolling import (
    _1714, _1715, _1716, _1717,
    _1718, _1719, _1721, _1726,
    _1727, _1729, _1731, _1732,
    _1733, _1734, _1737, _1738,
    _1740, _1741, _1742, _1743,
    _1744, _1745
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _1758, _1760, _1762, _1764,
    _1765, _1766
)
from mastapy.bearings.bearing_designs.concept import _1768, _1769, _1770
from mastapy.bearings.bearing_results.rolling import _1660
from mastapy.bearings import _1490
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingResults',)


class LoadedBearingResults(_1490.BearingLoadCaseResultsLightweight):
    '''LoadedBearingResults

    This is a mastapy class.
    '''

    TYPE = _LOADED_BEARING_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedBearingResults.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def angle_of_gravity_from_z_axis(self) -> 'float':
        '''float: 'AngleOfGravityFromZAxis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AngleOfGravityFromZAxis

    @property
    def signed_relative_speed(self) -> 'float':
        '''float: 'SignedRelativeSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SignedRelativeSpeed

    @property
    def relative_speed(self) -> 'float':
        '''float: 'RelativeSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeSpeed

    @property
    def inner_race_speed(self) -> 'float':
        '''float: 'InnerRaceSpeed' is the original name of this property.'''

        return self.wrapped.InnerRaceSpeed

    @inner_race_speed.setter
    def inner_race_speed(self, value: 'float'):
        self.wrapped.InnerRaceSpeed = float(value) if value else 0.0

    @property
    def outer_race_speed(self) -> 'float':
        '''float: 'OuterRaceSpeed' is the original name of this property.'''

        return self.wrapped.OuterRaceSpeed

    @outer_race_speed.setter
    def outer_race_speed(self, value: 'float'):
        self.wrapped.OuterRaceSpeed = float(value) if value else 0.0

    @property
    def duration(self) -> 'float':
        '''float: 'Duration' is the original name of this property.'''

        return self.wrapped.Duration

    @duration.setter
    def duration(self, value: 'float'):
        self.wrapped.Duration = float(value) if value else 0.0

    @property
    def orientation(self) -> '_1561.Orientations':
        '''Orientations: 'Orientation' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.Orientation)
        return constructor.new(_1561.Orientations)(value) if value else None

    @orientation.setter
    def orientation(self, value: '_1561.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def specified_radial_internal_clearance(self) -> 'float':
        '''float: 'SpecifiedRadialInternalClearance' is the original name of this property.'''

        return self.wrapped.SpecifiedRadialInternalClearance

    @specified_radial_internal_clearance.setter
    def specified_radial_internal_clearance(self, value: 'float'):
        self.wrapped.SpecifiedRadialInternalClearance = float(value) if value else 0.0

    @property
    def specified_axial_internal_clearance(self) -> 'float':
        '''float: 'SpecifiedAxialInternalClearance' is the original name of this property.'''

        return self.wrapped.SpecifiedAxialInternalClearance

    @specified_axial_internal_clearance.setter
    def specified_axial_internal_clearance(self, value: 'float'):
        self.wrapped.SpecifiedAxialInternalClearance = float(value) if value else 0.0

    @property
    def axial_displacement_preload(self) -> 'float':
        '''float: 'AxialDisplacementPreload' is the original name of this property.'''

        return self.wrapped.AxialDisplacementPreload

    @axial_displacement_preload.setter
    def axial_displacement_preload(self, value: 'float'):
        self.wrapped.AxialDisplacementPreload = float(value) if value else 0.0

    @property
    def pre_assembly_axial_force_preload(self) -> 'float':
        '''float: 'PreAssemblyAxialForcePreload' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.PreAssemblyAxialForcePreload

    @property
    def relative_displacement_x(self) -> 'float':
        '''float: 'RelativeDisplacementX' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeDisplacementX

    @property
    def relative_displacement_y(self) -> 'float':
        '''float: 'RelativeDisplacementY' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeDisplacementY

    @property
    def relative_displacement_z(self) -> 'float':
        '''float: 'RelativeDisplacementZ' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeDisplacementZ

    @property
    def relative_displacement_about_x(self) -> 'float':
        '''float: 'RelativeDisplacementAboutX' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeDisplacementAboutX

    @property
    def relative_displacement_about_y(self) -> 'float':
        '''float: 'RelativeDisplacementAboutY' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeDisplacementAboutY

    @property
    def relative_axial_displacement(self) -> 'float':
        '''float: 'RelativeAxialDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeAxialDisplacement

    @property
    def relative_radial_displacement(self) -> 'float':
        '''float: 'RelativeRadialDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeRadialDisplacement

    @property
    def relative_misalignment(self) -> 'float':
        '''float: 'RelativeMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.RelativeMisalignment

    @property
    def magnitude_of_misalignment_normal_to_load_direction(self) -> 'float':
        '''float: 'MagnitudeOfMisalignmentNormalToLoadDirection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MagnitudeOfMisalignmentNormalToLoadDirection

    @property
    def force_results_are_overridden(self) -> 'bool':
        '''bool: 'ForceResultsAreOverridden' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ForceResultsAreOverridden

    @property
    def force_on_inner_race(self) -> '_1106.VectorWithLinearAndAngularComponents[_1168.Force, _1240.Torque]':
        '''VectorWithLinearAndAngularComponents[Force, Torque]: 'ForceOnInnerRace' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1106.VectorWithLinearAndAngularComponents)[_1168.Force, _1240.Torque](self.wrapped.ForceOnInnerRace) if self.wrapped.ForceOnInnerRace else None

    @property
    def bearing(self) -> '_1709.BearingDesign':
        '''BearingDesign: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1709.BearingDesign)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_detailed_bearing(self) -> '_1710.DetailedBearing':
        '''DetailedBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1710.DetailedBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to DetailedBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1710.DetailedBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_dummy_rolling_bearing(self) -> '_1711.DummyRollingBearing':
        '''DummyRollingBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1711.DummyRollingBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to DummyRollingBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1711.DummyRollingBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_linear_bearing(self) -> '_1712.LinearBearing':
        '''LinearBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1712.LinearBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to LinearBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1712.LinearBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_non_linear_bearing(self) -> '_1713.NonLinearBearing':
        '''NonLinearBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1713.NonLinearBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to NonLinearBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1713.NonLinearBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_angular_contact_ball_bearing(self) -> '_1714.AngularContactBallBearing':
        '''AngularContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1714.AngularContactBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to AngularContactBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1714.AngularContactBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_angular_contact_thrust_ball_bearing(self) -> '_1715.AngularContactThrustBallBearing':
        '''AngularContactThrustBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1715.AngularContactThrustBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to AngularContactThrustBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1715.AngularContactThrustBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_asymmetric_spherical_roller_bearing(self) -> '_1716.AsymmetricSphericalRollerBearing':
        '''AsymmetricSphericalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1716.AsymmetricSphericalRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to AsymmetricSphericalRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1716.AsymmetricSphericalRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_1717.AxialThrustCylindricalRollerBearing':
        '''AxialThrustCylindricalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1717.AxialThrustCylindricalRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1717.AxialThrustCylindricalRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_axial_thrust_needle_roller_bearing(self) -> '_1718.AxialThrustNeedleRollerBearing':
        '''AxialThrustNeedleRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1718.AxialThrustNeedleRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to AxialThrustNeedleRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1718.AxialThrustNeedleRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_ball_bearing(self) -> '_1719.BallBearing':
        '''BallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1719.BallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to BallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1719.BallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_barrel_roller_bearing(self) -> '_1721.BarrelRollerBearing':
        '''BarrelRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1721.BarrelRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to BarrelRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1721.BarrelRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_cylindrical_roller_bearing(self) -> '_1726.CylindricalRollerBearing':
        '''CylindricalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1726.CylindricalRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to CylindricalRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1726.CylindricalRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_deep_groove_ball_bearing(self) -> '_1727.DeepGrooveBallBearing':
        '''DeepGrooveBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1727.DeepGrooveBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to DeepGrooveBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1727.DeepGrooveBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_four_point_contact_ball_bearing(self) -> '_1729.FourPointContactBallBearing':
        '''FourPointContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1729.FourPointContactBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to FourPointContactBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1729.FourPointContactBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_multi_point_contact_ball_bearing(self) -> '_1731.MultiPointContactBallBearing':
        '''MultiPointContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1731.MultiPointContactBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to MultiPointContactBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1731.MultiPointContactBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_needle_roller_bearing(self) -> '_1732.NeedleRollerBearing':
        '''NeedleRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1732.NeedleRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to NeedleRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1732.NeedleRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_non_barrel_roller_bearing(self) -> '_1733.NonBarrelRollerBearing':
        '''NonBarrelRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1733.NonBarrelRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to NonBarrelRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1733.NonBarrelRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_roller_bearing(self) -> '_1734.RollerBearing':
        '''RollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1734.RollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to RollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1734.RollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_rolling_bearing(self) -> '_1737.RollingBearing':
        '''RollingBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1737.RollingBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to RollingBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1737.RollingBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_self_aligning_ball_bearing(self) -> '_1738.SelfAligningBallBearing':
        '''SelfAligningBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1738.SelfAligningBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to SelfAligningBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1738.SelfAligningBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_spherical_roller_bearing(self) -> '_1740.SphericalRollerBearing':
        '''SphericalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1740.SphericalRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to SphericalRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1740.SphericalRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_spherical_roller_thrust_bearing(self) -> '_1741.SphericalRollerThrustBearing':
        '''SphericalRollerThrustBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1741.SphericalRollerThrustBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to SphericalRollerThrustBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1741.SphericalRollerThrustBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_taper_roller_bearing(self) -> '_1742.TaperRollerBearing':
        '''TaperRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1742.TaperRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to TaperRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1742.TaperRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_three_point_contact_ball_bearing(self) -> '_1743.ThreePointContactBallBearing':
        '''ThreePointContactBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1743.ThreePointContactBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to ThreePointContactBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1743.ThreePointContactBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_thrust_ball_bearing(self) -> '_1744.ThrustBallBearing':
        '''ThrustBallBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1744.ThrustBallBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to ThrustBallBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1744.ThrustBallBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_toroidal_roller_bearing(self) -> '_1745.ToroidalRollerBearing':
        '''ToroidalRollerBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.ToroidalRollerBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to ToroidalRollerBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1745.ToroidalRollerBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_pad_fluid_film_bearing(self) -> '_1758.PadFluidFilmBearing':
        '''PadFluidFilmBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1758.PadFluidFilmBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to PadFluidFilmBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1758.PadFluidFilmBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_plain_grease_filled_journal_bearing(self) -> '_1760.PlainGreaseFilledJournalBearing':
        '''PlainGreaseFilledJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1760.PlainGreaseFilledJournalBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to PlainGreaseFilledJournalBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1760.PlainGreaseFilledJournalBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_plain_journal_bearing(self) -> '_1762.PlainJournalBearing':
        '''PlainJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1762.PlainJournalBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to PlainJournalBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1762.PlainJournalBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_plain_oil_fed_journal_bearing(self) -> '_1764.PlainOilFedJournalBearing':
        '''PlainOilFedJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1764.PlainOilFedJournalBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to PlainOilFedJournalBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1764.PlainOilFedJournalBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_tilting_pad_journal_bearing(self) -> '_1765.TiltingPadJournalBearing':
        '''TiltingPadJournalBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1765.TiltingPadJournalBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to TiltingPadJournalBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1765.TiltingPadJournalBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_tilting_pad_thrust_bearing(self) -> '_1766.TiltingPadThrustBearing':
        '''TiltingPadThrustBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1766.TiltingPadThrustBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to TiltingPadThrustBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1766.TiltingPadThrustBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_concept_axial_clearance_bearing(self) -> '_1768.ConceptAxialClearanceBearing':
        '''ConceptAxialClearanceBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1768.ConceptAxialClearanceBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to ConceptAxialClearanceBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1768.ConceptAxialClearanceBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_concept_clearance_bearing(self) -> '_1769.ConceptClearanceBearing':
        '''ConceptClearanceBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1769.ConceptClearanceBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to ConceptClearanceBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1769.ConceptClearanceBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def bearing_of_type_concept_radial_clearance_bearing(self) -> '_1770.ConceptRadialClearanceBearing':
        '''ConceptRadialClearanceBearing: 'Bearing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1770.ConceptRadialClearanceBearing.TYPE not in self.wrapped.Bearing.__class__.__mro__:
            raise CastException('Failed to cast bearing to ConceptRadialClearanceBearing. Expected: {}.'.format(self.wrapped.Bearing.__class__.__qualname__))

        return constructor.new(_1770.ConceptRadialClearanceBearing)(self.wrapped.Bearing) if self.wrapped.Bearing else None

    @property
    def ring_results(self) -> 'List[_1660.RingForceAndDisplacement]':
        '''List[RingForceAndDisplacement]: 'RingResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingResults, constructor.new(_1660.RingForceAndDisplacement))
        return value
