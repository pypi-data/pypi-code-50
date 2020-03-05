'''_92.py

FEStiffnessTester
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.nodal_analysis import _90
from mastapy.gears.ltca import _106, _107, _108
from mastapy._internal.cast_exception import CastException
from mastapy.gears.ltca.cylindrical import _109, _110
from mastapy.gears.ltca.conical import _111, _112
from mastapy.system_model.imported_fes import _113
from mastapy.math_utility.measured_vectors import _114
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
    def fe_stiffness(self) -> '_90.FEStiffness':
        '''FEStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_90.FEStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_gear_bending_stiffness(self) -> '_106.GearBendingStiffness':
        '''GearBendingStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _106.GearBendingStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to GearBendingStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_106.GearBendingStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_gear_contact_stiffness(self) -> '_107.GearContactStiffness':
        '''GearContactStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _107.GearContactStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to GearContactStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_107.GearContactStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_gear_stiffness(self) -> '_108.GearStiffness':
        '''GearStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _108.GearStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to GearStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_108.GearStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_cylindrical_gear_bending_stiffness(self) -> '_109.CylindricalGearBendingStiffness':
        '''CylindricalGearBendingStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _109.CylindricalGearBendingStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to CylindricalGearBendingStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_109.CylindricalGearBendingStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_cylindrical_gear_contact_stiffness(self) -> '_110.CylindricalGearContactStiffness':
        '''CylindricalGearContactStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _110.CylindricalGearContactStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to CylindricalGearContactStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_110.CylindricalGearContactStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_conical_gear_bending_stiffness(self) -> '_111.ConicalGearBendingStiffness':
        '''ConicalGearBendingStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _111.ConicalGearBendingStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to ConicalGearBendingStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_111.ConicalGearBendingStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_conical_gear_contact_stiffness(self) -> '_112.ConicalGearContactStiffness':
        '''ConicalGearContactStiffness: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _112.ConicalGearContactStiffness.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to ConicalGearContactStiffness. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_112.ConicalGearContactStiffness)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def fe_stiffness_of_type_imported_fe(self) -> '_113.ImportedFE':
        '''ImportedFE: 'FEStiffness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _113.ImportedFE.TYPE not in self.wrapped.FEStiffness.__class__.__mro__:
            raise CastException('Failed to cast fe_stiffness to ImportedFE. Expected: {}.'.format(self.wrapped.FEStiffness.__class__.__qualname__))

        return constructor.new(_113.ImportedFE)(self.wrapped.FEStiffness) if self.wrapped.FEStiffness else None

    @property
    def force_and_displacement_results(self) -> 'List[_114.ForceAndDisplacementResults]':
        '''List[ForceAndDisplacementResults]: 'ForceAndDisplacementResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ForceAndDisplacementResults, constructor.new(_114.ForceAndDisplacementResults))
        return value
