'''_1673.py

PreloadFactorLookupTable
'''


from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_PRELOAD_FACTOR_LOOKUP_TABLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'PreloadFactorLookupTable')


__docformat__ = 'restructuredtext en'
__all__ = ('PreloadFactorLookupTable',)


class PreloadFactorLookupTable(_1.APIBase):
    '''PreloadFactorLookupTable

    This is a mastapy class.
    '''

    TYPE = _PRELOAD_FACTOR_LOOKUP_TABLE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PreloadFactorLookupTable.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def high(self) -> 'float':
        '''float: 'High' is the original name of this property.'''

        return self.wrapped.High

    @high.setter
    def high(self, value: 'float'):
        self.wrapped.High = float(value) if value else 0.0

    @property
    def medium(self) -> 'float':
        '''float: 'Medium' is the original name of this property.'''

        return self.wrapped.Medium

    @medium.setter
    def medium(self, value: 'float'):
        self.wrapped.Medium = float(value) if value else 0.0

    @property
    def low(self) -> 'float':
        '''float: 'Low' is the original name of this property.'''

        return self.wrapped.Low

    @low.setter
    def low(self, value: 'float'):
        self.wrapped.Low = float(value) if value else 0.0

    @property
    def zero(self) -> 'float':
        '''float: 'Zero' is the original name of this property.'''

        return self.wrapped.Zero

    @zero.setter
    def zero(self, value: 'float'):
        self.wrapped.Zero = float(value) if value else 0.0
