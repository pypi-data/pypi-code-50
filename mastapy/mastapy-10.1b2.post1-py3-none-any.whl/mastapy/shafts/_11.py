'''_11.py

DesignShaftSectionEnd
'''


from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_DESIGN_SHAFT_SECTION_END = python_net_import('SMT.MastaAPI.Shafts', 'DesignShaftSectionEnd')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignShaftSectionEnd',)


class DesignShaftSectionEnd(_1.APIBase):
    '''DesignShaftSectionEnd

    This is a mastapy class.
    '''

    TYPE = _DESIGN_SHAFT_SECTION_END

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DesignShaftSectionEnd.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def offset(self) -> 'float':
        '''float: 'Offset' is the original name of this property.'''

        return self.wrapped.Offset

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value else 0.0

    @property
    def outer_diameter(self) -> 'float':
        '''float: 'OuterDiameter' is the original name of this property.'''

        return self.wrapped.OuterDiameter

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def inner_diameter(self) -> 'float':
        '''float: 'InnerDiameter' is the original name of this property.'''

        return self.wrapped.InnerDiameter

    @inner_diameter.setter
    def inner_diameter(self, value: 'float'):
        self.wrapped.InnerDiameter = float(value) if value else 0.0
