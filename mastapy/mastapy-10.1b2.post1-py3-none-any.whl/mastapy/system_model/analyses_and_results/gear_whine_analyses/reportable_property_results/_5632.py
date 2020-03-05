'''_5632.py

GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _5639, _5634
from mastapy.utility.units_and_measurements.measurements import (
    _1165, _1211, _1168, _1250,
    _1240, _1223
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic(_5634.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
    '''GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic

    This is a mastapy class.
    '''

    TYPE = _GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def component_name(self) -> 'str':
        '''str: 'ComponentName' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ComponentName

    @property
    def kinetic_energy(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1165.EnergySmall, _1211.PowerSmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[EnergySmall, PowerSmall]: 'KineticEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1165.EnergySmall, _1211.PowerSmall](self.wrapped.KineticEnergy) if self.wrapped.KineticEnergy else None

    @property
    def strain_energy(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1165.EnergySmall, _1211.PowerSmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[EnergySmall, PowerSmall]: 'StrainEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1165.EnergySmall, _1211.PowerSmall](self.wrapped.StrainEnergy) if self.wrapped.StrainEnergy else None

    @property
    def dynamic_mesh_force(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1168.Force, _1250.Yank]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Force, Yank]: 'DynamicMeshForce' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1168.Force, _1250.Yank](self.wrapped.DynamicMeshForce) if self.wrapped.DynamicMeshForce else None

    @property
    def dynamic_mesh_moment(self) -> '_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1240.Torque, _1223.Rotatum]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Torque, Rotatum]: 'DynamicMeshMoment' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5639.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1240.Torque, _1223.Rotatum](self.wrapped.DynamicMeshMoment) if self.wrapped.DynamicMeshMoment else None
