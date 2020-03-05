'''_1549.py

LoadedBearingDutyCycle
'''


from typing import List

from mastapy._internal import constructor, conversion
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
from mastapy.utility.property import _1329
from mastapy.bearings import _1490
from mastapy.bearings.bearing_results import _1550
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingDutyCycle',)


class LoadedBearingDutyCycle(_1.APIBase):
    '''LoadedBearingDutyCycle

    This is a mastapy class.
    '''

    TYPE = _LOADED_BEARING_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def duty_cycle_name(self) -> 'str':
        '''str: 'DutyCycleName' is the original name of this property.'''

        return self.wrapped.DutyCycleName

    @duty_cycle_name.setter
    def duty_cycle_name(self, value: 'str'):
        self.wrapped.DutyCycleName = str(value) if value else None

    @property
    def duration(self) -> 'float':
        '''float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Duration

    @property
    def bearing_design(self) -> '_1709.BearingDesign':
        '''BearingDesign: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1709.BearingDesign)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_detailed_bearing(self) -> '_1710.DetailedBearing':
        '''DetailedBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1710.DetailedBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DetailedBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1710.DetailedBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_dummy_rolling_bearing(self) -> '_1711.DummyRollingBearing':
        '''DummyRollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1711.DummyRollingBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DummyRollingBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1711.DummyRollingBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_linear_bearing(self) -> '_1712.LinearBearing':
        '''LinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1712.LinearBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to LinearBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1712.LinearBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_non_linear_bearing(self) -> '_1713.NonLinearBearing':
        '''NonLinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1713.NonLinearBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonLinearBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1713.NonLinearBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_angular_contact_ball_bearing(self) -> '_1714.AngularContactBallBearing':
        '''AngularContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1714.AngularContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1714.AngularContactBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_angular_contact_thrust_ball_bearing(self) -> '_1715.AngularContactThrustBallBearing':
        '''AngularContactThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1715.AngularContactThrustBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactThrustBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1715.AngularContactThrustBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_asymmetric_spherical_roller_bearing(self) -> '_1716.AsymmetricSphericalRollerBearing':
        '''AsymmetricSphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1716.AsymmetricSphericalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AsymmetricSphericalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1716.AsymmetricSphericalRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_1717.AxialThrustCylindricalRollerBearing':
        '''AxialThrustCylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1717.AxialThrustCylindricalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1717.AxialThrustCylindricalRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_axial_thrust_needle_roller_bearing(self) -> '_1718.AxialThrustNeedleRollerBearing':
        '''AxialThrustNeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1718.AxialThrustNeedleRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustNeedleRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1718.AxialThrustNeedleRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_ball_bearing(self) -> '_1719.BallBearing':
        '''BallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1719.BallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1719.BallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_barrel_roller_bearing(self) -> '_1721.BarrelRollerBearing':
        '''BarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1721.BarrelRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BarrelRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1721.BarrelRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_cylindrical_roller_bearing(self) -> '_1726.CylindricalRollerBearing':
        '''CylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1726.CylindricalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CylindricalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1726.CylindricalRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_deep_groove_ball_bearing(self) -> '_1727.DeepGrooveBallBearing':
        '''DeepGrooveBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1727.DeepGrooveBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DeepGrooveBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1727.DeepGrooveBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_four_point_contact_ball_bearing(self) -> '_1729.FourPointContactBallBearing':
        '''FourPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1729.FourPointContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to FourPointContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1729.FourPointContactBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_multi_point_contact_ball_bearing(self) -> '_1731.MultiPointContactBallBearing':
        '''MultiPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1731.MultiPointContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to MultiPointContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1731.MultiPointContactBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_needle_roller_bearing(self) -> '_1732.NeedleRollerBearing':
        '''NeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1732.NeedleRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NeedleRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1732.NeedleRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_non_barrel_roller_bearing(self) -> '_1733.NonBarrelRollerBearing':
        '''NonBarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1733.NonBarrelRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonBarrelRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1733.NonBarrelRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_roller_bearing(self) -> '_1734.RollerBearing':
        '''RollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1734.RollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1734.RollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_rolling_bearing(self) -> '_1737.RollingBearing':
        '''RollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1737.RollingBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollingBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1737.RollingBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_self_aligning_ball_bearing(self) -> '_1738.SelfAligningBallBearing':
        '''SelfAligningBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1738.SelfAligningBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SelfAligningBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1738.SelfAligningBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_spherical_roller_bearing(self) -> '_1740.SphericalRollerBearing':
        '''SphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1740.SphericalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1740.SphericalRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_spherical_roller_thrust_bearing(self) -> '_1741.SphericalRollerThrustBearing':
        '''SphericalRollerThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1741.SphericalRollerThrustBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerThrustBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1741.SphericalRollerThrustBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_taper_roller_bearing(self) -> '_1742.TaperRollerBearing':
        '''TaperRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1742.TaperRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TaperRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1742.TaperRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_three_point_contact_ball_bearing(self) -> '_1743.ThreePointContactBallBearing':
        '''ThreePointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1743.ThreePointContactBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThreePointContactBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1743.ThreePointContactBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_thrust_ball_bearing(self) -> '_1744.ThrustBallBearing':
        '''ThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1744.ThrustBallBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThrustBallBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1744.ThrustBallBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_toroidal_roller_bearing(self) -> '_1745.ToroidalRollerBearing':
        '''ToroidalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1745.ToroidalRollerBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ToroidalRollerBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1745.ToroidalRollerBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_pad_fluid_film_bearing(self) -> '_1758.PadFluidFilmBearing':
        '''PadFluidFilmBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1758.PadFluidFilmBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PadFluidFilmBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1758.PadFluidFilmBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_plain_grease_filled_journal_bearing(self) -> '_1760.PlainGreaseFilledJournalBearing':
        '''PlainGreaseFilledJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1760.PlainGreaseFilledJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainGreaseFilledJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1760.PlainGreaseFilledJournalBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_plain_journal_bearing(self) -> '_1762.PlainJournalBearing':
        '''PlainJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1762.PlainJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1762.PlainJournalBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_plain_oil_fed_journal_bearing(self) -> '_1764.PlainOilFedJournalBearing':
        '''PlainOilFedJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1764.PlainOilFedJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainOilFedJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1764.PlainOilFedJournalBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_tilting_pad_journal_bearing(self) -> '_1765.TiltingPadJournalBearing':
        '''TiltingPadJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1765.TiltingPadJournalBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadJournalBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1765.TiltingPadJournalBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_tilting_pad_thrust_bearing(self) -> '_1766.TiltingPadThrustBearing':
        '''TiltingPadThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1766.TiltingPadThrustBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadThrustBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1766.TiltingPadThrustBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_concept_axial_clearance_bearing(self) -> '_1768.ConceptAxialClearanceBearing':
        '''ConceptAxialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1768.ConceptAxialClearanceBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptAxialClearanceBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1768.ConceptAxialClearanceBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_concept_clearance_bearing(self) -> '_1769.ConceptClearanceBearing':
        '''ConceptClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1769.ConceptClearanceBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptClearanceBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1769.ConceptClearanceBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def bearing_design_of_type_concept_radial_clearance_bearing(self) -> '_1770.ConceptRadialClearanceBearing':
        '''ConceptRadialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1770.ConceptRadialClearanceBearing.TYPE not in self.wrapped.BearingDesign.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptRadialClearanceBearing. Expected: {}.'.format(self.wrapped.BearingDesign.__class__.__qualname__))

        return constructor.new(_1770.ConceptRadialClearanceBearing)(self.wrapped.BearingDesign) if self.wrapped.BearingDesign else None

    @property
    def radial_load_summary(self) -> '_1329.DutyCyclePropertySummaryForce[_1490.BearingLoadCaseResultsLightweight]':
        '''DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'RadialLoadSummary' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1329.DutyCyclePropertySummaryForce)[_1490.BearingLoadCaseResultsLightweight](self.wrapped.RadialLoadSummary) if self.wrapped.RadialLoadSummary else None

    @property
    def z_thrust_reaction_summary(self) -> '_1329.DutyCyclePropertySummaryForce[_1490.BearingLoadCaseResultsLightweight]':
        '''DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'ZThrustReactionSummary' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1329.DutyCyclePropertySummaryForce)[_1490.BearingLoadCaseResultsLightweight](self.wrapped.ZThrustReactionSummary) if self.wrapped.ZThrustReactionSummary else None

    @property
    def bearing_load_case_results(self) -> 'List[_1550.LoadedBearingResults]':
        '''List[LoadedBearingResults]: 'BearingLoadCaseResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BearingLoadCaseResults, constructor.new(_1550.LoadedBearingResults))
        return value
