'''_4650.py

PartCompoundAnalysis
'''


from mastapy.scripting import _744
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _3383
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'PartCompoundAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PartCompoundAnalysis',)


class PartCompoundAnalysis(_3383.DesignEntityCompoundAnalysis):
    '''PartCompoundAnalysis

    This is a mastapy class.
    '''

    TYPE = _PART_COMPOUND_ANALYSIS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartCompoundAnalysis.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def twod_drawing(self) -> '_744.SMTBitmap':
        '''SMTBitmap: 'TwoDDrawing' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_744.SMTBitmap)(self.wrapped.TwoDDrawing) if self.wrapped.TwoDDrawing else None
