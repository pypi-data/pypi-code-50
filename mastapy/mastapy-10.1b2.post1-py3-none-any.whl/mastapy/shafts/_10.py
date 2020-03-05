'''_10.py

DesignShaftSection
'''


from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy.shafts import _11
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_DESIGN_SHAFT_SECTION = python_net_import('SMT.MastaAPI.Shafts', 'DesignShaftSection')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignShaftSection',)


class DesignShaftSection(_1.APIBase):
    '''DesignShaftSection

    This is a mastapy class.
    '''

    TYPE = _DESIGN_SHAFT_SECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DesignShaftSection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def length(self) -> 'float':
        '''float: 'Length' is the original name of this property.'''

        return self.wrapped.Length

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def outer_diameter(self) -> 'float':
        '''float: 'OuterDiameter' is the original name of this property.'''

        return self.wrapped.OuterDiameter

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def bore(self) -> 'float':
        '''float: 'Bore' is the original name of this property.'''

        return self.wrapped.Bore

    @bore.setter
    def bore(self, value: 'float'):
        self.wrapped.Bore = float(value) if value else 0.0

    @property
    def torsional_stiffness(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'TorsionalStiffness' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.TorsionalStiffness) if self.wrapped.TorsionalStiffness else None

    @torsional_stiffness.setter
    def torsional_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.TorsionalStiffness = value

    @property
    def polar_inertia(self) -> 'overridable.Overridable_float':
        '''overridable.Overridable_float: 'PolarInertia' is the original name of this property.'''

        return constructor.new(overridable.Overridable_float)(self.wrapped.PolarInertia) if self.wrapped.PolarInertia else None

    @polar_inertia.setter
    def polar_inertia(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.TYPE
        enclosed_type = overridable.Overridable_float.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value else 0.0)
        self.wrapped.PolarInertia = value

    @property
    def left(self) -> '_11.DesignShaftSectionEnd':
        '''DesignShaftSectionEnd: 'Left' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_11.DesignShaftSectionEnd)(self.wrapped.Left) if self.wrapped.Left else None

    @property
    def right(self) -> '_11.DesignShaftSectionEnd':
        '''DesignShaftSectionEnd: 'Right' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_11.DesignShaftSectionEnd)(self.wrapped.Right) if self.wrapped.Right else None
