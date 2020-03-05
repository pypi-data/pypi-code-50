'''_5497.py

GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _5500, _5495
from mastapy.utility.units_and_measurements.measurements import (
    _1315, _1363, _1266, _1307,
    _1332, _1333
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(_5495.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
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
    def root_mean_squared_normal_displacement(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1315.LengthVeryShort, _1363.VelocitySmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[LengthVeryShort, VelocitySmall]: 'RootMeanSquaredNormalDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1315.LengthVeryShort, _1363.VelocitySmall](self.wrapped.RootMeanSquaredNormalDisplacement) if self.wrapped.RootMeanSquaredNormalDisplacement else None

    @property
    def root_mean_squared_normal_velocity(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1363.VelocitySmall, _1266.Acceleration]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[VelocitySmall, Acceleration]: 'RootMeanSquaredNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1363.VelocitySmall, _1266.Acceleration](self.wrapped.RootMeanSquaredNormalVelocity) if self.wrapped.RootMeanSquaredNormalVelocity else None

    @property
    def maximum_normal_velocity(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1363.VelocitySmall, _1266.Acceleration]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[VelocitySmall, Acceleration]: 'MaximumNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1363.VelocitySmall, _1266.Acceleration](self.wrapped.MaximumNormalVelocity) if self.wrapped.MaximumNormalVelocity else None

    @property
    def root_mean_squared_normal_acceleration(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1266.Acceleration, _1307.Jerk]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Acceleration, Jerk]: 'RootMeanSquaredNormalAcceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1266.Acceleration, _1307.Jerk](self.wrapped.RootMeanSquaredNormalAcceleration) if self.wrapped.RootMeanSquaredNormalAcceleration else None

    @property
    def airborne_sound_power(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1332.PowerSmall, _1333.PowerSmallPerUnitTime]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[PowerSmall, PowerSmallPerUnitTime]: 'AirborneSoundPower' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1332.PowerSmall, _1333.PowerSmallPerUnitTime](self.wrapped.AirborneSoundPower) if self.wrapped.AirborneSoundPower else None
