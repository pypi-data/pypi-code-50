'''_479.py

WormGrindingProcessSimulationNew
'''


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _472, _477, _474, _475,
    _471, _481, _476, _465,
    _478
)
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessSimulationNew',)


class WormGrindingProcessSimulationNew(_465.ProcessSimulationNew['_478.WormGrindingProcessSimulationInput']):
    '''WormGrindingProcessSimulationNew

    This is a mastapy class.
    '''

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_NEW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def worm_grinding_process_lead_calculation(self) -> '_472.WormGrindingLeadCalculation':
        '''WormGrindingLeadCalculation: 'WormGrindingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_472.WormGrindingLeadCalculation)(self.wrapped.WormGrindingProcessLeadCalculation) if self.wrapped.WormGrindingProcessLeadCalculation else None

    @property
    def worm_grinding_process_profile_calculation(self) -> '_477.WormGrindingProcessProfileCalculation':
        '''WormGrindingProcessProfileCalculation: 'WormGrindingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_477.WormGrindingProcessProfileCalculation)(self.wrapped.WormGrindingProcessProfileCalculation) if self.wrapped.WormGrindingProcessProfileCalculation else None

    @property
    def worm_grinding_process_gear_shape_calculation(self) -> '_474.WormGrindingProcessGearShape':
        '''WormGrindingProcessGearShape: 'WormGrindingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_474.WormGrindingProcessGearShape)(self.wrapped.WormGrindingProcessGearShapeCalculation) if self.wrapped.WormGrindingProcessGearShapeCalculation else None

    @property
    def worm_grinding_process_mark_on_shaft_calculation(self) -> '_475.WormGrindingProcessMarkOnShaft':
        '''WormGrindingProcessMarkOnShaft: 'WormGrindingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_475.WormGrindingProcessMarkOnShaft)(self.wrapped.WormGrindingProcessMarkOnShaftCalculation) if self.wrapped.WormGrindingProcessMarkOnShaftCalculation else None

    @property
    def worm_grinding_cutter_calculation(self) -> '_471.WormGrindingCutterCalculation':
        '''WormGrindingCutterCalculation: 'WormGrindingCutterCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_471.WormGrindingCutterCalculation)(self.wrapped.WormGrindingCutterCalculation) if self.wrapped.WormGrindingCutterCalculation else None

    @property
    def worm_grinding_process_total_modification_calculation(self) -> '_481.WormGrindingProcessTotalModificationCalculation':
        '''WormGrindingProcessTotalModificationCalculation: 'WormGrindingProcessTotalModificationCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_481.WormGrindingProcessTotalModificationCalculation)(self.wrapped.WormGrindingProcessTotalModificationCalculation) if self.wrapped.WormGrindingProcessTotalModificationCalculation else None

    @property
    def worm_grinding_process_pitch_calculation(self) -> '_476.WormGrindingProcessPitchCalculation':
        '''WormGrindingProcessPitchCalculation: 'WormGrindingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_476.WormGrindingProcessPitchCalculation)(self.wrapped.WormGrindingProcessPitchCalculation) if self.wrapped.WormGrindingProcessPitchCalculation else None
