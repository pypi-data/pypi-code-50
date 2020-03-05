'''_61.py

FEStiffnessTester
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis import _59
from mastapy.gears.ltca import _731, _733, _741
from mastapy._internal.cast_exception import CastException
from mastapy.gears.ltca.cylindrical import _744, _746
from mastapy.gears.ltca.conical import _756, _758
from mastapy.system_model.imported_fes import _1861
from mastapy.math_utility.measured_vectors import _1222
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_FE_STIFFNESS_TESTER = python_net_import('SMT.MastaAPI.NodalAnalysis', 'FEStiffnessTester')


__docformat__ = 'restructuredtext en'
__all__ = ('FEStiffnessTester',)


class FEStiffnessTester(_1.APIBase):
    '''FEStiffnessTester

    This is a mastapy class.
    '''

    TYPE = _FE_STIFFNESS_TESTER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEStiffnessTester.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def force_scaling_factor(self) -> 'float':
        '''float: 'ForceScalingFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ForceScalingFactor

    @property
    def displacement_scaling_factor(self) -> 'float':
        '''float: 'DisplacementScalingFactor' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.DisplacementScalingFactor

    @property
    def fe_stiffness(self) -> '_59.FEStiffness':
        '''FEStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_59.FEStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_gear_bending_stiffness(self) -> '_731.GearBendingStiffness':
        '''GearBendingStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _731.GearBendingStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to GearBendingStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_731.GearBendingStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_gear_contact_stiffness(self) -> '_733.GearContactStiffness':
        '''GearContactStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _733.GearContactStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to GearContactStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_733.GearContactStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_gear_stiffness(self) -> '_741.GearStiffness':
        '''GearStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _741.GearStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to GearStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_741.GearStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_cylindrical_gear_bending_stiffness(self) -> '_744.CylindricalGearBendingStiffness':
        '''CylindricalGearBendingStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _744.CylindricalGearBendingStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to CylindricalGearBendingStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_744.CylindricalGearBendingStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_cylindrical_gear_contact_stiffness(self) -> '_746.CylindricalGearContactStiffness':
        '''CylindricalGearContactStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _746.CylindricalGearContactStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to CylindricalGearContactStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_746.CylindricalGearContactStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_conical_gear_bending_stiffness(self) -> '_756.ConicalGearBendingStiffness':
        '''ConicalGearBendingStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _756.ConicalGearBendingStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to ConicalGearBendingStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_756.ConicalGearBendingStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_conical_gear_contact_stiffness(self) -> '_758.ConicalGearContactStiffness':
        '''ConicalGearContactStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _758.ConicalGearContactStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to ConicalGearContactStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_758.ConicalGearContactStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_imported_fe(self) -> '_1861.ImportedFE':
        '''ImportedFE: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1861.ImportedFE.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to ImportedFE. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_1861.ImportedFE)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def force_and_displacement_results(self) -> 'List[_1222.ForceAndDisplacementResults]':
        '''List[ForceAndDisplacementResults]: 'ForceAndDisplacementResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ForceAndDisplacementResults, constructor.new(_1222.ForceAndDisplacementResults))
        return value
