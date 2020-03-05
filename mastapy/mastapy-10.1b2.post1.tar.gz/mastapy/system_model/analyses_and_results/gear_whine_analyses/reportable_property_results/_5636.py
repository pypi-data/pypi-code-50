'''_5636.py

GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _5639, _5634
from mastapy.utility.units_and_measurements.measurements import (
    _1194, _1245, _1145, _1186,
    _1211, _1214, _1212, _1213,
    _1215, _1216
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_SURFACE_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownBySurfaceWithinAHarmonic(_5634.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
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
    def root_mean_squared_normal_displacement(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1194.LengthVeryShort, _1245.VelocitySmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[LengthVeryShort, VelocitySmall]: 'RootMeanSquaredNormalDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1194.LengthVeryShort, _1245.VelocitySmall](self.wrapped.RootMeanSquaredNormalDisplacement) if self.wrapped.RootMeanSquaredNormalDisplacement else None

    @property
    def root_mean_squared_normal_velocity(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1245.VelocitySmall, _1145.Acceleration]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[VelocitySmall, Acceleration]: 'RootMeanSquaredNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1245.VelocitySmall, _1145.Acceleration](self.wrapped.RootMeanSquaredNormalVelocity) if self.wrapped.RootMeanSquaredNormalVelocity else None

    @property
    def maximum_normal_velocity(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1245.VelocitySmall, _1145.Acceleration]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[VelocitySmall, Acceleration]: 'MaximumNormalVelocity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1245.VelocitySmall, _1145.Acceleration](self.wrapped.MaximumNormalVelocity) if self.wrapped.MaximumNormalVelocity else None

    @property
    def root_mean_squared_normal_acceleration(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1145.Acceleration, _1186.Jerk]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Acceleration, Jerk]: 'RootMeanSquaredNormalAcceleration' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1145.Acceleration, _1186.Jerk](self.wrapped.RootMeanSquaredNormalAcceleration) if self.wrapped.RootMeanSquaredNormalAcceleration else None

    @property
    def airborne_sound_power(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1211.PowerSmall, _1214.PowerSmallPerUnitTime]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[PowerSmall, PowerSmallPerUnitTime]: 'AirborneSoundPower' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1211.PowerSmall, _1214.PowerSmallPerUnitTime](self.wrapped.AirborneSoundPower) if self.wrapped.AirborneSoundPower else None

    @property
    def sound_intensity(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1212.PowerSmallPerArea, _1213.PowerSmallPerUnitAreaPerUnitTime]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[PowerSmallPerArea, PowerSmallPerUnitAreaPerUnitTime]: 'SoundIntensity' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1212.PowerSmallPerArea, _1213.PowerSmallPerUnitAreaPerUnitTime](self.wrapped.SoundIntensity) if self.wrapped.SoundIntensity else None

    @property
    def sound_pressure(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1215.Pressure, _1216.PressurePerUnitTime]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Pressure, PressurePerUnitTime]: 'SoundPressure' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1215.Pressure, _1216.PressurePerUnitTime](self.wrapped.SoundPressure) if self.wrapped.SoundPressure else None
