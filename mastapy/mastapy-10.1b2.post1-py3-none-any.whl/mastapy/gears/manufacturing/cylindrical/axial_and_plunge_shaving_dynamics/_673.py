'''_673.py

ShavingDynamicsConfiguration
'''


from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _670, _655, _656, _657,
    _662, _663, _659
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_CONFIGURATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsConfiguration',)


class ShavingDynamicsConfiguration(_1.APIBase):
    '''ShavingDynamicsConfiguration

    This is a mastapy class.
    '''

    TYPE = _SHAVING_DYNAMICS_CONFIGURATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsConfiguration.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def conventional_shaving_dynamics(self) -> '_670.ShavingDynamicsCalculation[_655.ConventionalShavingDynamics]':
        '''ShavingDynamicsCalculation[ConventionalShavingDynamics]: 'ConventionalShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_670.ShavingDynamicsCalculation)[_655.ConventionalShavingDynamics](self.wrapped.ConventionalShavingDynamics) if self.wrapped.ConventionalShavingDynamics else None

    @property
    def conventional_shaving_dynamics_of_type_conventional_shaving_dynamics_calculation_for_designed_gears(self) -> '_656.ConventionalShavingDynamicsCalculationForDesignedGears':
        '''ConventionalShavingDynamicsCalculationForDesignedGears: 'ConventionalShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _656.ConventionalShavingDynamicsCalculationForDesignedGears.TYPE not in self.wrapped.ConventionalShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast conventional_shaving_dynamics to ConventionalShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(self.wrapped.ConventionalShavingDynamics.__class__.__qualname__))

        return constructor.new(_656.ConventionalShavingDynamicsCalculationForDesignedGears)(self.wrapped.ConventionalShavingDynamics) if self.wrapped.ConventionalShavingDynamics else None

    @property
    def conventional_shaving_dynamics_of_type_conventional_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_657.ConventionalShavingDynamicsCalculationForHobbedGears':
        '''ConventionalShavingDynamicsCalculationForHobbedGears: 'ConventionalShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _657.ConventionalShavingDynamicsCalculationForHobbedGears.TYPE not in self.wrapped.ConventionalShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast conventional_shaving_dynamics to ConventionalShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(self.wrapped.ConventionalShavingDynamics.__class__.__qualname__))

        return constructor.new(_657.ConventionalShavingDynamicsCalculationForHobbedGears)(self.wrapped.ConventionalShavingDynamics) if self.wrapped.ConventionalShavingDynamics else None

    @property
    def conventional_shaving_dynamics_of_type_plunge_shaving_dynamics_calculation_for_designed_gears(self) -> '_662.PlungeShavingDynamicsCalculationForDesignedGears':
        '''PlungeShavingDynamicsCalculationForDesignedGears: 'ConventionalShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _662.PlungeShavingDynamicsCalculationForDesignedGears.TYPE not in self.wrapped.ConventionalShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast conventional_shaving_dynamics to PlungeShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(self.wrapped.ConventionalShavingDynamics.__class__.__qualname__))

        return constructor.new(_662.PlungeShavingDynamicsCalculationForDesignedGears)(self.wrapped.ConventionalShavingDynamics) if self.wrapped.ConventionalShavingDynamics else None

    @property
    def conventional_shaving_dynamics_of_type_plunge_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_663.PlungeShavingDynamicsCalculationForHobbedGears':
        '''PlungeShavingDynamicsCalculationForHobbedGears: 'ConventionalShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _663.PlungeShavingDynamicsCalculationForHobbedGears.TYPE not in self.wrapped.ConventionalShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast conventional_shaving_dynamics to PlungeShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(self.wrapped.ConventionalShavingDynamics.__class__.__qualname__))

        return constructor.new(_663.PlungeShavingDynamicsCalculationForHobbedGears)(self.wrapped.ConventionalShavingDynamics) if self.wrapped.ConventionalShavingDynamics else None

    @property
    def plunge_shaving_dynamics(self) -> '_670.ShavingDynamicsCalculation[_659.PlungeShaverDynamics]':
        '''ShavingDynamicsCalculation[PlungeShaverDynamics]: 'PlungeShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_670.ShavingDynamicsCalculation)[_659.PlungeShaverDynamics](self.wrapped.PlungeShavingDynamics) if self.wrapped.PlungeShavingDynamics else None

    @property
    def plunge_shaving_dynamics_of_type_conventional_shaving_dynamics_calculation_for_designed_gears(self) -> '_656.ConventionalShavingDynamicsCalculationForDesignedGears':
        '''ConventionalShavingDynamicsCalculationForDesignedGears: 'PlungeShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _656.ConventionalShavingDynamicsCalculationForDesignedGears.TYPE not in self.wrapped.PlungeShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast plunge_shaving_dynamics to ConventionalShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(self.wrapped.PlungeShavingDynamics.__class__.__qualname__))

        return constructor.new(_656.ConventionalShavingDynamicsCalculationForDesignedGears)(self.wrapped.PlungeShavingDynamics) if self.wrapped.PlungeShavingDynamics else None

    @property
    def plunge_shaving_dynamics_of_type_conventional_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_657.ConventionalShavingDynamicsCalculationForHobbedGears':
        '''ConventionalShavingDynamicsCalculationForHobbedGears: 'PlungeShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _657.ConventionalShavingDynamicsCalculationForHobbedGears.TYPE not in self.wrapped.PlungeShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast plunge_shaving_dynamics to ConventionalShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(self.wrapped.PlungeShavingDynamics.__class__.__qualname__))

        return constructor.new(_657.ConventionalShavingDynamicsCalculationForHobbedGears)(self.wrapped.PlungeShavingDynamics) if self.wrapped.PlungeShavingDynamics else None

    @property
    def plunge_shaving_dynamics_of_type_plunge_shaving_dynamics_calculation_for_designed_gears(self) -> '_662.PlungeShavingDynamicsCalculationForDesignedGears':
        '''PlungeShavingDynamicsCalculationForDesignedGears: 'PlungeShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _662.PlungeShavingDynamicsCalculationForDesignedGears.TYPE not in self.wrapped.PlungeShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast plunge_shaving_dynamics to PlungeShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(self.wrapped.PlungeShavingDynamics.__class__.__qualname__))

        return constructor.new(_662.PlungeShavingDynamicsCalculationForDesignedGears)(self.wrapped.PlungeShavingDynamics) if self.wrapped.PlungeShavingDynamics else None

    @property
    def plunge_shaving_dynamics_of_type_plunge_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_663.PlungeShavingDynamicsCalculationForHobbedGears':
        '''PlungeShavingDynamicsCalculationForHobbedGears: 'PlungeShavingDynamics' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _663.PlungeShavingDynamicsCalculationForHobbedGears.TYPE not in self.wrapped.PlungeShavingDynamics.__class__.__mro__:
            raise CastException('Failed to cast plunge_shaving_dynamics to PlungeShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(self.wrapped.PlungeShavingDynamics.__class__.__qualname__))

        return constructor.new(_663.PlungeShavingDynamicsCalculationForHobbedGears)(self.wrapped.PlungeShavingDynamics) if self.wrapped.PlungeShavingDynamics else None
