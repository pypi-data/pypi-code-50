'''_5493.py

GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _5500, _5495
from mastapy.utility.units_and_measurements.measurements import (
    _1286, _1332, _1289, _1368
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic(_5495.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
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
    def kinetic_energy(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1286.EnergySmall, _1332.PowerSmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[EnergySmall, PowerSmall]: 'KineticEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1286.EnergySmall, _1332.PowerSmall](self.wrapped.KineticEnergy) if self.wrapped.KineticEnergy else None

    @property
    def strain_energy(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1286.EnergySmall, _1332.PowerSmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[EnergySmall, PowerSmall]: 'StrainEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1286.EnergySmall, _1332.PowerSmall](self.wrapped.StrainEnergy) if self.wrapped.StrainEnergy else None

    @property
    def dynamic_mesh_force(self) -> '_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1289.Force, _1368.Yank]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Force, Yank]: 'DynamicMeshForce' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_5500.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1289.Force, _1368.Yank](self.wrapped.DynamicMeshForce) if self.wrapped.DynamicMeshForce else None
