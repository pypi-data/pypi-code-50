'''_645.py

CutterShapeDefinition
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _635, _629, _630, _631,
    _632, _634, _636, _637,
    _640
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _651
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CUTTER_SHAPE_DEFINITION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CutterShapeDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('CutterShapeDefinition',)


class CutterShapeDefinition(_1.APIBase):
    '''CutterShapeDefinition

    This is a mastapy class.
    '''

    TYPE = _CUTTER_SHAPE_DEFINITION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CutterShapeDefinition.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def normal_module(self) -> 'float':
        '''float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalModule

    @property
    def normal_pressure_angle(self) -> 'float':
        '''float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalPressureAngle

    @property
    def design(self) -> '_635.CylindricalGearRealCutterDesign':
        '''CylindricalGearRealCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_635.CylindricalGearRealCutterDesign)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_629.CylindricalGearFormGrindingWheel':
        '''CylindricalGearFormGrindingWheel: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _629.CylindricalGearFormGrindingWheel.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearFormGrindingWheel. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_629.CylindricalGearFormGrindingWheel)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_grinding_worm(self) -> '_630.CylindricalGearGrindingWorm':
        '''CylindricalGearGrindingWorm: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _630.CylindricalGearGrindingWorm.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearGrindingWorm. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_630.CylindricalGearGrindingWorm)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_hob_design(self) -> '_631.CylindricalGearHobDesign':
        '''CylindricalGearHobDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _631.CylindricalGearHobDesign.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearHobDesign. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_631.CylindricalGearHobDesign)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_plunge_shaver(self) -> '_632.CylindricalGearPlungeShaver':
        '''CylindricalGearPlungeShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _632.CylindricalGearPlungeShaver.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearPlungeShaver. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_632.CylindricalGearPlungeShaver)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_rack_design(self) -> '_634.CylindricalGearRackDesign':
        '''CylindricalGearRackDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _634.CylindricalGearRackDesign.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearRackDesign. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_634.CylindricalGearRackDesign)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_shaper(self) -> '_636.CylindricalGearShaper':
        '''CylindricalGearShaper: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _636.CylindricalGearShaper.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearShaper. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_636.CylindricalGearShaper)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_cylindrical_gear_shaver(self) -> '_637.CylindricalGearShaver':
        '''CylindricalGearShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _637.CylindricalGearShaver.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearShaver. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_637.CylindricalGearShaver)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def design_of_type_involute_cutter_design(self) -> '_640.InvoluteCutterDesign':
        '''InvoluteCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _640.InvoluteCutterDesign.TYPE not in self.wrapped.Design.__class__.__mro__:
            raise CastException('Failed to cast design to InvoluteCutterDesign. Expected: {}.'.format(self.wrapped.Design.__class__.__qualname__))

        return constructor.new(_640.InvoluteCutterDesign)(self.wrapped.Design) if self.wrapped.Design else None

    @property
    def fillet_points(self) -> 'List[_651.NamedPoint]':
        '''List[NamedPoint]: 'FilletPoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FilletPoints, constructor.new(_651.NamedPoint))
        return value

    @property
    def main_blade_points(self) -> 'List[_651.NamedPoint]':
        '''List[NamedPoint]: 'MainBladePoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MainBladePoints, constructor.new(_651.NamedPoint))
        return value
