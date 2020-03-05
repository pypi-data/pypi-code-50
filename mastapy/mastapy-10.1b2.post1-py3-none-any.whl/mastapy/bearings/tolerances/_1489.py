'''_1489.py

InnerRaceTolerance
'''


from mastapy.bearings.tolerances import _1498
from mastapy._internal.python_net import python_net_import

_INNER_RACE_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InnerRaceTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('InnerRaceTolerance',)


class InnerRaceTolerance(_1498.RaceTolerance):
    '''InnerRaceTolerance

    This is a mastapy class.
    '''

    TYPE = _INNER_RACE_TOLERANCE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InnerRaceTolerance.TYPE'):
        super().__init__(instance_to_wrap)
