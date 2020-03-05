'''_1684.py

SKFCalculationResult
'''


from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SKF_CALCULATION_RESULT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'SKFCalculationResult')


__docformat__ = 'restructuredtext en'
__all__ = ('SKFCalculationResult',)


class SKFCalculationResult(_1.APIBase):
    '''SKFCalculationResult

    This is a mastapy class.
    '''

    TYPE = _SKF_CALCULATION_RESULT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SKFCalculationResult.TYPE'):
        super().__init__(instance_to_wrap)
