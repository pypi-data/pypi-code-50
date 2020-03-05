'''_1296.py

StatusItem
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility.model_validation import _1294
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_STATUS_ITEM = python_net_import('SMT.MastaAPI.Utility.ModelValidation', 'StatusItem')


__docformat__ = 'restructuredtext en'
__all__ = ('StatusItem',)


class StatusItem(_1.APIBase):
    '''StatusItem

    This is a mastapy class.
    '''

    TYPE = _STATUS_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StatusItem.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def description(self) -> 'str':
        '''str: 'Description' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Description

    @property
    def can_fix(self) -> 'bool':
        '''bool: 'CanFix' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CanFix

    @property
    def fixes(self) -> 'List[_1294.Fix]':
        '''List[Fix]: 'Fixes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Fixes, constructor.new(_1294.Fix))
        return value

    def apply_first_fix(self):
        ''' 'ApplyFirstFix' is the original name of this method.'''

        self.wrapped.ApplyFirstFix()
