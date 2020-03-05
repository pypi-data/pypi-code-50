'''_737.py

CylindricalGearSpecification
'''


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _720, _721, _722
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SPECIFICATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'CylindricalGearSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSpecification',)


class CylindricalGearSpecification(_1.APIBase):
    '''CylindricalGearSpecification

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SPECIFICATION
    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSpecification.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def normal_module(self) -> 'float':
        '''float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NormalModule

    @property
    def helix_angle(self) -> 'float':
        '''float: 'HelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.HelixAngle

    @property
    def normal_pressure_angle(self) -> 'float':
        '''float: 'NormalPressureAngle' is the original name of this property.'''

        return self.wrapped.NormalPressureAngle

    @normal_pressure_angle.setter
    def normal_pressure_angle(self, value: 'float'):
        self.wrapped.NormalPressureAngle = float(value) if value else 0.0

    @property
    def number_of_teeth_unsigned(self) -> 'float':
        '''float: 'NumberOfTeethUnsigned' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.NumberOfTeethUnsigned

    @property
    def tooth_thickness_specification(self) -> '_720.ToothThicknessSpecificationBase':
        '''ToothThicknessSpecificationBase: 'ToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_720.ToothThicknessSpecificationBase)(self.wrapped.ToothThicknessSpecification) if self.wrapped.ToothThicknessSpecification else None

    @property
    def tooth_thickness_specification_of_type_finish_tooth_thickness_design_specification(self) -> '_721.FinishToothThicknessDesignSpecification':
        '''FinishToothThicknessDesignSpecification: 'ToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _721.FinishToothThicknessDesignSpecification.TYPE not in self.wrapped.ToothThicknessSpecification.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness_specification to FinishToothThicknessDesignSpecification. Expected: {}.'.format(self.wrapped.ToothThicknessSpecification.__class__.__qualname__))

        return constructor.new(_721.FinishToothThicknessDesignSpecification)(self.wrapped.ToothThicknessSpecification) if self.wrapped.ToothThicknessSpecification else None

    @property
    def tooth_thickness_specification_of_type_tooth_thickness_specification(self) -> '_722.ToothThicknessSpecification':
        '''ToothThicknessSpecification: 'ToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _722.ToothThicknessSpecification.TYPE not in self.wrapped.ToothThicknessSpecification.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness_specification to ToothThicknessSpecification. Expected: {}.'.format(self.wrapped.ToothThicknessSpecification.__class__.__qualname__))

        return constructor.new(_722.ToothThicknessSpecification)(self.wrapped.ToothThicknessSpecification) if self.wrapped.ToothThicknessSpecification else None
