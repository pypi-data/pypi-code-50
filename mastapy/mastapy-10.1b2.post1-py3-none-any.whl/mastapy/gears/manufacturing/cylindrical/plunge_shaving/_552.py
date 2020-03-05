'''_552.py

PlungeShaverCalculation
'''


from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _553, _562
from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_PLUNGE_SHAVER_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving', 'PlungeShaverCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('PlungeShaverCalculation',)


class PlungeShaverCalculation(_1.APIBase):
    '''PlungeShaverCalculation

    This is a mastapy class.
    '''

    TYPE = _PLUNGE_SHAVER_CALCULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlungeShaverCalculation.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def inputs(self) -> '_553.PlungeShaverCalculationInputs':
        '''PlungeShaverCalculationInputs: 'Inputs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_553.PlungeShaverCalculationInputs)(self.wrapped.Inputs) if self.wrapped.Inputs else None

    @property
    def simulation_of_ideal_shaver_conjugate_to_the_designed_gear(self) -> '_562.VirtualPlungeShaverOutputs':
        '''VirtualPlungeShaverOutputs: 'SimulationOfIdealShaverConjugateToTheDesignedGear' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_562.VirtualPlungeShaverOutputs)(self.wrapped.SimulationOfIdealShaverConjugateToTheDesignedGear) if self.wrapped.SimulationOfIdealShaverConjugateToTheDesignedGear else None
