'''_817.py

ParetoOptimiserChartInformation
'''


from mastapy.gears.gear_set_pareto_optimiser import _792, _799
from mastapy.gears.rating import _284
from mastapy._internal.python_net import python_net_import

_PARETO_OPTIMISER_CHART_INFORMATION = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'ParetoOptimiserChartInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('ParetoOptimiserChartInformation',)


class ParetoOptimiserChartInformation(_792.ChartInfoBase['_284.AbstractGearSetRating', '_799.GearSetOptimiserCandidate']):
    '''ParetoOptimiserChartInformation

    This is a mastapy class.
    '''

    TYPE = _PARETO_OPTIMISER_CHART_INFORMATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ParetoOptimiserChartInformation.TYPE'):
        super().__init__(instance_to_wrap)
