'''_1975.py

Coupling
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import (
    _2001, _2024, _2025, _2026,
    _2027, _2028, _2030, _2031,
    _2032, _2033, _2034
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model import _1938
from mastapy._internal.python_net import python_net_import

_COUPLING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'Coupling')


__docformat__ = 'restructuredtext en'
__all__ = ('Coupling',)


class Coupling(_1938.SpecialisedAssembly):
    '''Coupling

    This is a mastapy class.
    '''

    TYPE = _COUPLING
    __hash__ = None

    def __init__(self, instance_to_wrap: 'Coupling.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def torsional_stiffness(self) -> 'float':
        '''float: 'TorsionalStiffness' is the original name of this property.'''

        return self.wrapped.TorsionalStiffness

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: 'float'):
        self.wrapped.TorsionalStiffness = float(value) if value else 0.0

    @property
    def radial_stiffness(self) -> 'float':
        '''float: 'RadialStiffness' is the original name of this property.'''

        return self.wrapped.RadialStiffness

    @radial_stiffness.setter
    def radial_stiffness(self, value: 'float'):
        self.wrapped.RadialStiffness = float(value) if value else 0.0

    @property
    def axial_stiffness(self) -> 'float':
        '''float: 'AxialStiffness' is the original name of this property.'''

        return self.wrapped.AxialStiffness

    @axial_stiffness.setter
    def axial_stiffness(self, value: 'float'):
        self.wrapped.AxialStiffness = float(value) if value else 0.0

    @property
    def tilt_stiffness(self) -> 'float':
        '''float: 'TiltStiffness' is the original name of this property.'''

        return self.wrapped.TiltStiffness

    @tilt_stiffness.setter
    def tilt_stiffness(self, value: 'float'):
        self.wrapped.TiltStiffness = float(value) if value else 0.0

    @property
    def halves(self) -> 'List[_2001.CouplingHalf]':
        '''List[CouplingHalf]: 'Halves' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Halves, constructor.new(_2001.CouplingHalf))
        return value

    @property
    def half_a(self) -> '_2001.CouplingHalf':
        '''CouplingHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2001.CouplingHalf)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_clutch_half(self) -> '_2024.ClutchHalf':
        '''ClutchHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'ClutchHalf':
            raise CastException('Failed to cast half_a to ClutchHalf. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2024.ClutchHalf)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_concept_coupling_half(self) -> '_2025.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'ConceptCouplingHalf':
            raise CastException('Failed to cast half_a to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2025.ConceptCouplingHalf)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_pulley(self) -> '_2026.Pulley':
        '''Pulley: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'Pulley':
            raise CastException('Failed to cast half_a to Pulley. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2026.Pulley)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_rolling_ring(self) -> '_2027.RollingRing':
        '''RollingRing: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'RollingRing':
            raise CastException('Failed to cast half_a to RollingRing. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2027.RollingRing)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_spring_damper_half(self) -> '_2028.SpringDamperHalf':
        '''SpringDamperHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'SpringDamperHalf':
            raise CastException('Failed to cast half_a to SpringDamperHalf. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2028.SpringDamperHalf)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_torque_converter_pump(self) -> '_2030.TorqueConverterPump':
        '''TorqueConverterPump: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'TorqueConverterPump':
            raise CastException('Failed to cast half_a to TorqueConverterPump. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2030.TorqueConverterPump)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_torque_converter_turbine(self) -> '_2031.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'TorqueConverterTurbine':
            raise CastException('Failed to cast half_a to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2031.TorqueConverterTurbine)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_cvt_pulley(self) -> '_2032.CVTPulley':
        '''CVTPulley: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'CVTPulley':
            raise CastException('Failed to cast half_a to CVTPulley. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2032.CVTPulley)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_synchroniser_half(self) -> '_2033.SynchroniserHalf':
        '''SynchroniserHalf: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'SynchroniserHalf':
            raise CastException('Failed to cast half_a to SynchroniserHalf. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2033.SynchroniserHalf)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_a_of_type_synchroniser_sleeve(self) -> '_2034.SynchroniserSleeve':
        '''SynchroniserSleeve: 'HalfA' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfA.__class__.__qualname__ != 'SynchroniserSleeve':
            raise CastException('Failed to cast half_a to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.HalfA.__class__.__qualname__))

        return constructor.new(_2034.SynchroniserSleeve)(self.wrapped.HalfA) if self.wrapped.HalfA else None

    @property
    def half_b(self) -> '_2001.CouplingHalf':
        '''CouplingHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2001.CouplingHalf)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_clutch_half(self) -> '_2024.ClutchHalf':
        '''ClutchHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'ClutchHalf':
            raise CastException('Failed to cast half_b to ClutchHalf. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2024.ClutchHalf)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_concept_coupling_half(self) -> '_2025.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'ConceptCouplingHalf':
            raise CastException('Failed to cast half_b to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2025.ConceptCouplingHalf)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_pulley(self) -> '_2026.Pulley':
        '''Pulley: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'Pulley':
            raise CastException('Failed to cast half_b to Pulley. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2026.Pulley)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_rolling_ring(self) -> '_2027.RollingRing':
        '''RollingRing: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'RollingRing':
            raise CastException('Failed to cast half_b to RollingRing. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2027.RollingRing)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_spring_damper_half(self) -> '_2028.SpringDamperHalf':
        '''SpringDamperHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'SpringDamperHalf':
            raise CastException('Failed to cast half_b to SpringDamperHalf. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2028.SpringDamperHalf)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_torque_converter_pump(self) -> '_2030.TorqueConverterPump':
        '''TorqueConverterPump: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'TorqueConverterPump':
            raise CastException('Failed to cast half_b to TorqueConverterPump. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2030.TorqueConverterPump)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_torque_converter_turbine(self) -> '_2031.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'TorqueConverterTurbine':
            raise CastException('Failed to cast half_b to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2031.TorqueConverterTurbine)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_cvt_pulley(self) -> '_2032.CVTPulley':
        '''CVTPulley: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'CVTPulley':
            raise CastException('Failed to cast half_b to CVTPulley. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2032.CVTPulley)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_synchroniser_half(self) -> '_2033.SynchroniserHalf':
        '''SynchroniserHalf: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'SynchroniserHalf':
            raise CastException('Failed to cast half_b to SynchroniserHalf. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2033.SynchroniserHalf)(self.wrapped.HalfB) if self.wrapped.HalfB else None

    @property
    def half_b_of_type_synchroniser_sleeve(self) -> '_2034.SynchroniserSleeve':
        '''SynchroniserSleeve: 'HalfB' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if self.wrapped.HalfB.__class__.__qualname__ != 'SynchroniserSleeve':
            raise CastException('Failed to cast half_b to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.HalfB.__class__.__qualname__))

        return constructor.new(_2034.SynchroniserSleeve)(self.wrapped.HalfB) if self.wrapped.HalfB else None
