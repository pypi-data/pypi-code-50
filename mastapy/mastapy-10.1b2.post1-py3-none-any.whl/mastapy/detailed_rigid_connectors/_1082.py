'''_1082.py

DetailedRigidConnectorDesign
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.scripting import _6321
from mastapy.detailed_rigid_connectors import _1083
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_DETAILED_RIGID_CONNECTOR_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors', 'DetailedRigidConnectorDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('DetailedRigidConnectorDesign',)


class DetailedRigidConnectorDesign(_1.APIBase):
    '''DetailedRigidConnectorDesign

    This is a mastapy class.
    '''

    TYPE = _DETAILED_RIGID_CONNECTOR_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DetailedRigidConnectorDesign.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def length_of_engagement(self) -> 'float':
        '''float: 'LengthOfEngagement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.LengthOfEngagement

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def twod_spline_drawing(self) -> '_6321.SMTBitmap':
        '''SMTBitmap: 'TwoDSplineDrawing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6321.SMTBitmap)(self.wrapped.TwoDSplineDrawing) if self.wrapped.TwoDSplineDrawing else None

    @property
    def halves(self) -> 'List[_1083.DetailedRigidConnectorHalfDesign]':
        '''List[DetailedRigidConnectorHalfDesign]: 'Halves' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Halves, constructor.new(_1083.DetailedRigidConnectorHalfDesign))
        return value
