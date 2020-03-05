'''_6240.py

ResultsForResponseOfAComponentOrSurfaceInAHarmonic
'''


from typing import List, Generic, TypeVar

from mastapy.system_model.analyses_and_results.gear_whine_analyses.reportable_property_results import _6242, _6231
from mastapy._internal import constructor, conversion
from mastapy import _1
from mastapy.utility.units_and_measurements import _1071
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.GearWhineAnalyses.ReportablePropertyResults', 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForResponseOfAComponentOrSurfaceInAHarmonic',)


TLinearMeasurement = TypeVar('TLinearMeasurement', bound='_1071.MeasurementBase')
TLinearDerivativeMeasurement = TypeVar('TLinearDerivativeMeasurement', bound='_1071.MeasurementBase')


class ResultsForResponseOfAComponentOrSurfaceInAHarmonic(_1.APIBase, Generic[TLinearMeasurement, TLinearDerivativeMeasurement]):
    '''ResultsForResponseOfAComponentOrSurfaceInAHarmonic

    This is a mastapy class.

    Generic Types:
        TLinearMeasurement
        TLinearDerivativeMeasurement
    '''

    TYPE = _RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def magnitude(self) -> '_6242.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic[TLinearMeasurement, TLinearDerivativeMeasurement]':
        '''ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic[TLinearMeasurement, TLinearDerivativeMeasurement]: 'Magnitude' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6242.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic)[TLinearMeasurement, TLinearDerivativeMeasurement](self.wrapped.Magnitude) if self.wrapped.Magnitude else None

    @property
    def data_points(self) -> 'List[_6231.DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic[TLinearMeasurement]]':
        '''List[DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic[TLinearMeasurement]]: 'DataPoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.DataPoints, constructor.new(_6231.DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic)[TLinearMeasurement])
        return value
