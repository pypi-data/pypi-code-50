'''_6237.py

GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _6240, _6235
from mastapy.utility.units_and_measurements.measurements import (
    _1328, _1375, _1280, _1321,
    _1344, _1345
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(_6235.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
    '''GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic

    This is a mastapy class.
    '''

    TYPE = _GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC
    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def surface_name(self) -> 'str':
        '''str: 'SurfaceName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SurfaceName

    @property
    def root_mean_squared_normal_displacement(self) -> '_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1328.LengthVeryShort, _1375.VelocitySmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[LengthVeryShort, VelocitySmall]: 'RootMeanSquaredNormalDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1328.LengthVeryShort, _1375.VelocitySmall](self.wrapped.RootMeanSquaredNormalDisplacement) if self.wrapped.RootMeanSquaredNormalDisplacement else None

    @property
    def root_mean_squared_normal_velocity(self) -> '_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1375.VelocitySmall, _1280.Acceleration]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[VelocitySmall, Acceleration]: 'RootMeanSquaredNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1375.VelocitySmall, _1280.Acceleration](self.wrapped.RootMeanSquaredNormalVelocity) if self.wrapped.RootMeanSquaredNormalVelocity else None

    @property
    def maximum_normal_velocity(self) -> '_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1375.VelocitySmall, _1280.Acceleration]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[VelocitySmall, Acceleration]: 'MaximumNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1375.VelocitySmall, _1280.Acceleration](self.wrapped.MaximumNormalVelocity) if self.wrapped.MaximumNormalVelocity else None

    @property
    def root_mean_squared_normal_acceleration(self) -> '_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1280.Acceleration, _1321.Jerk]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Acceleration, Jerk]: 'RootMeanSquaredNormalAcceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1280.Acceleration, _1321.Jerk](self.wrapped.RootMeanSquaredNormalAcceleration) if self.wrapped.RootMeanSquaredNormalAcceleration else None

    @property
    def airborne_sound_power(self) -> '_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1344.PowerSmall, _1345.PowerSmallPerUnitTime]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[PowerSmall, PowerSmallPerUnitTime]: 'AirborneSoundPower' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6240.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1344.PowerSmall, _1345.PowerSmallPerUnitTime](self.wrapped.AirborneSoundPower) if self.wrapped.AirborneSoundPower else None
