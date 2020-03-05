'''_700.py

ProcessLeadCalculation
'''


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _677
from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_PROCESS_LEAD_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'ProcessLeadCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('ProcessLeadCalculation',)


class ProcessLeadCalculation(_1.APIBase):
    '''ProcessLeadCalculation

    This is a mastapy class.
    '''

    TYPE = _PROCESS_LEAD_CALCULATION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ProcessLeadCalculation.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def right_flank_accuracy_calculation(self) -> '_677.CalculateLeadDeviationAccuracy':
        '''CalculateLeadDeviationAccuracy: 'RightFlankAccuracyCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_677.CalculateLeadDeviationAccuracy)(self.wrapped.RightFlankAccuracyCalculation) if self.wrapped.RightFlankAccuracyCalculation else None

    @property
    def left_flank_accuracy_calculation(self) -> '_677.CalculateLeadDeviationAccuracy':
        '''CalculateLeadDeviationAccuracy: 'LeftFlankAccuracyCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_677.CalculateLeadDeviationAccuracy)(self.wrapped.LeftFlankAccuracyCalculation) if self.wrapped.LeftFlankAccuracyCalculation else None
