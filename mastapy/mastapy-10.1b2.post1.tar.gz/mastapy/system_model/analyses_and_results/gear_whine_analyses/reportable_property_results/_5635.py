'''_5635.py

GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _5640, _5634
from mastapy.utility.units_and_measurements.measurements import (
    _1191, _1245, _1146, _1154,
    _1145, _1150, _1186, _1152,
    _1168, _1250, _1240, _1223
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic(_5634.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
    '''GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic

    This is a mastapy class.
    '''

    TYPE = _GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def node_name(self) -> 'str':
        '''str: 'NodeName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NodeName

    @property
    def displacement(self) -> '_5640.ResultsForResponseOfANodeOnAHarmonic[_1191.LengthShort, _1245.VelocitySmall, _1146.Angle, _1154.AngularVelocity]':
        '''ResultsForResponseOfANodeOnAHarmonic[LengthShort, VelocitySmall, Angle, AngularVelocity]: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5640.ResultsForResponseOfANodeOnAHarmonic)[_1191.LengthShort, _1245.VelocitySmall, _1146.Angle, _1154.AngularVelocity](self.wrapped.Displacement) if self.wrapped.Displacement else None

    @property
    def velocity(self) -> '_5640.ResultsForResponseOfANodeOnAHarmonic[_1245.VelocitySmall, _1145.Acceleration, _1154.AngularVelocity, _1150.AngularAcceleration]':
        '''ResultsForResponseOfANodeOnAHarmonic[VelocitySmall, Acceleration, AngularVelocity, AngularAcceleration]: 'Velocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5640.ResultsForResponseOfANodeOnAHarmonic)[_1245.VelocitySmall, _1145.Acceleration, _1154.AngularVelocity, _1150.AngularAcceleration](self.wrapped.Velocity) if self.wrapped.Velocity else None

    @property
    def acceleration(self) -> '_5640.ResultsForResponseOfANodeOnAHarmonic[_1145.Acceleration, _1186.Jerk, _1150.AngularAcceleration, _1152.AngularJerk]':
        '''ResultsForResponseOfANodeOnAHarmonic[Acceleration, Jerk, AngularAcceleration, AngularJerk]: 'Acceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5640.ResultsForResponseOfANodeOnAHarmonic)[_1145.Acceleration, _1186.Jerk, _1150.AngularAcceleration, _1152.AngularJerk](self.wrapped.Acceleration) if self.wrapped.Acceleration else None

    @property
    def force(self) -> '_5640.ResultsForResponseOfANodeOnAHarmonic[_1168.Force, _1250.Yank, _1240.Torque, _1223.Rotatum]':
        '''ResultsForResponseOfANodeOnAHarmonic[Force, Yank, Torque, Rotatum]: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5640.ResultsForResponseOfANodeOnAHarmonic)[_1168.Force, _1250.Yank, _1240.Torque, _1223.Rotatum](self.wrapped.Force) if self.wrapped.Force else None
