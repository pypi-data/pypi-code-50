'''_1494.py

OuterRaceTolerance
'''


from mastapy.bearings.tolerances import _1498
from mastapy._internal.python_net import python_net_import

_OUTER_RACE_TOLERANCE = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'OuterRaceTolerance')


__docformat__ = 'restructuredtext en'
__all__ = ('OuterRaceTolerance',)


class OuterRaceTolerance(_1498.RaceTolerance):
    '''OuterRaceTolerance

    This is a mastapy class.
    '''

    TYPE = _OUTER_RACE_TOLERANCE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OuterRaceTolerance.TYPE'):
        super().__init__(instance_to_wrap)
