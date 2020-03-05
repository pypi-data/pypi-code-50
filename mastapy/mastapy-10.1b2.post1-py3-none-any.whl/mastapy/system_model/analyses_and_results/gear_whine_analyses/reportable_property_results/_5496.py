'''_5496.py

GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _5501, _5495
from mastapy.utility.units_and_measurements.measurements import (
    _1312, _1363, _1267, _1275,
    _1266, _1271, _1307, _1273,
    _1289, _1368, _1358, _1341
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic(_5495.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
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
    def displacement(self) -> '_5501.ResultsForResponseOfANodeOnAHarmonic[_1312.LengthShort, _1363.VelocitySmall, _1267.Angle, _1275.AngularVelocity]':
        '''ResultsForResponseOfANodeOnAHarmonic[LengthShort, VelocitySmall, Angle, AngularVelocity]: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5501.ResultsForResponseOfANodeOnAHarmonic)[_1312.LengthShort, _1363.VelocitySmall, _1267.Angle, _1275.AngularVelocity](self.wrapped.Displacement) if self.wrapped.Displacement else None

    @property
    def velocity(self) -> '_5501.ResultsForResponseOfANodeOnAHarmonic[_1363.VelocitySmall, _1266.Acceleration, _1275.AngularVelocity, _1271.AngularAcceleration]':
        '''ResultsForResponseOfANodeOnAHarmonic[VelocitySmall, Acceleration, AngularVelocity, AngularAcceleration]: 'Velocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5501.ResultsForResponseOfANodeOnAHarmonic)[_1363.VelocitySmall, _1266.Acceleration, _1275.AngularVelocity, _1271.AngularAcceleration](self.wrapped.Velocity) if self.wrapped.Velocity else None

    @property
    def acceleration(self) -> '_5501.ResultsForResponseOfANodeOnAHarmonic[_1266.Acceleration, _1307.Jerk, _1271.AngularAcceleration, _1273.AngularJerk]':
        '''ResultsForResponseOfANodeOnAHarmonic[Acceleration, Jerk, AngularAcceleration, AngularJerk]: 'Acceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5501.ResultsForResponseOfANodeOnAHarmonic)[_1266.Acceleration, _1307.Jerk, _1271.AngularAcceleration, _1273.AngularJerk](self.wrapped.Acceleration) if self.wrapped.Acceleration else None

    @property
    def force(self) -> '_5501.ResultsForResponseOfANodeOnAHarmonic[_1289.Force, _1368.Yank, _1358.Torque, _1341.Rotatum]':
        '''ResultsForResponseOfANodeOnAHarmonic[Force, Yank, Torque, Rotatum]: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5501.ResultsForResponseOfANodeOnAHarmonic)[_1289.Force, _1368.Yank, _1358.Torque, _1341.Rotatum](self.wrapped.Force) if self.wrapped.Force else None
