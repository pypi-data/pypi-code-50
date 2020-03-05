'''_6236.py

GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _6241, _6235
from mastapy.utility.units_and_measurements.measurements import (
    _1078, _1375, _1281, _1289,
    _1280, _1285, _1321, _1287,
    _1303, _1380, _1370, _1353
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_NODE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownByNodeWithinAHarmonic(_6235.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
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
    def displacement(self) -> '_6241.ResultsForResponseOfANodeOnAHarmonic[_1078.LengthShort, _1375.VelocitySmall, _1281.Angle, _1289.AngularVelocity]':
        '''ResultsForResponseOfANodeOnAHarmonic[LengthShort, VelocitySmall, Angle, AngularVelocity]: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6241.ResultsForResponseOfANodeOnAHarmonic)[_1078.LengthShort, _1375.VelocitySmall, _1281.Angle, _1289.AngularVelocity](self.wrapped.Displacement) if self.wrapped.Displacement else None

    @property
    def velocity(self) -> '_6241.ResultsForResponseOfANodeOnAHarmonic[_1375.VelocitySmall, _1280.Acceleration, _1289.AngularVelocity, _1285.AngularAcceleration]':
        '''ResultsForResponseOfANodeOnAHarmonic[VelocitySmall, Acceleration, AngularVelocity, AngularAcceleration]: 'Velocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6241.ResultsForResponseOfANodeOnAHarmonic)[_1375.VelocitySmall, _1280.Acceleration, _1289.AngularVelocity, _1285.AngularAcceleration](self.wrapped.Velocity) if self.wrapped.Velocity else None

    @property
    def acceleration(self) -> '_6241.ResultsForResponseOfANodeOnAHarmonic[_1280.Acceleration, _1321.Jerk, _1285.AngularAcceleration, _1287.AngularJerk]':
        '''ResultsForResponseOfANodeOnAHarmonic[Acceleration, Jerk, AngularAcceleration, AngularJerk]: 'Acceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6241.ResultsForResponseOfANodeOnAHarmonic)[_1280.Acceleration, _1321.Jerk, _1285.AngularAcceleration, _1287.AngularJerk](self.wrapped.Acceleration) if self.wrapped.Acceleration else None

    @property
    def force(self) -> '_6241.ResultsForResponseOfANodeOnAHarmonic[_1303.Force, _1380.Yank, _1370.Torque, _1353.Rotatum]':
        '''ResultsForResponseOfANodeOnAHarmonic[Force, Yank, Torque, Rotatum]: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6241.ResultsForResponseOfANodeOnAHarmonic)[_1303.Force, _1380.Yank, _1370.Torque, _1353.Rotatum](self.wrapped.Force) if self.wrapped.Force else None
