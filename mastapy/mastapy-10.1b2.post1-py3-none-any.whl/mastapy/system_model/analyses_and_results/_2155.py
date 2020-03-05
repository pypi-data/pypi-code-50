'''_2155.py

TorsionalSystemDeflectionAnalysis
'''


from mastapy.system_model.analyses_and_results import _2131
from mastapy._internal.python_net import python_net_import

_TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults', 'TorsionalSystemDeflectionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorsionalSystemDeflectionAnalysis',)


class TorsionalSystemDeflectionAnalysis(_2131.SingleAnalysis):
    '''TorsionalSystemDeflectionAnalysis

    This is a mastapy class.
    '''

    TYPE = _TORSIONAL_SYSTEM_DEFLECTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorsionalSystemDeflectionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
