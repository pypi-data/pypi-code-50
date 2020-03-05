'''_6228.py

GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _6234, _6230
from mastapy.utility.units_and_measurements.measurements import (
    _1309, _1353, _1312, _1389
)
from mastapy._internal.python_net import python_net_import

_GEAR_WHINE_ANALYSIS_RESULTS_BROKEN_DOWN_BY_COMPONENT_WITHIN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic',)


class GearWhineAnalysisResultsBrokenDownByComponentWithinAHarmonic(_6230.GearWhineAnalysisResultsBrokenDownByLocationWithinAHarmonic):
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
    def kinetic_energy(self) -> '_6234.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1309.EnergySmall, _1353.PowerSmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[EnergySmall, PowerSmall]: 'KineticEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6234.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1309.EnergySmall, _1353.PowerSmall](self.wrapped.KineticEnergy) if self.wrapped.KineticEnergy else None

    @property
    def strain_energy(self) -> '_6234.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1309.EnergySmall, _1353.PowerSmall]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[EnergySmall, PowerSmall]: 'StrainEnergy' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6234.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1309.EnergySmall, _1353.PowerSmall](self.wrapped.StrainEnergy) if self.wrapped.StrainEnergy else None

    @property
    def dynamic_mesh_force(self) -> '_6234.ResultsForResponseOfAComponentOrSurfaceInAHarmonic[_1312.Force, _1389.Yank]':
        '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic[Force, Yank]: 'DynamicMeshForce' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6234.ResultsForResponseOfAComponentOrSurfaceInAHarmonic)[_1312.Force, _1389.Yank](self.wrapped.DynamicMeshForce) if self.wrapped.DynamicMeshForce else None
