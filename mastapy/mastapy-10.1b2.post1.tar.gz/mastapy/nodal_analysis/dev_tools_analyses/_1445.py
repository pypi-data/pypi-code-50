'''_1445.py

FEModelTabDrawStyle
'''


from mastapy.nodal_analysis.dev_tools_analyses import _1432
from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_FE_MODEL_TAB_DRAW_STYLE = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses', 'FEModelTabDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('FEModelTabDrawStyle',)


class FEModelTabDrawStyle(_1.APIBase):
    '''FEModelTabDrawStyle

    This is a mastapy class.
    '''

    TYPE = _FE_MODEL_TAB_DRAW_STYLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEModelTabDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def draw_style(self) -> '_1432.DrawStyleForImportedFE':
        '''DrawStyleForImportedFE: 'DrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1432.DrawStyleForImportedFE)(self.wrapped.DrawStyle) if self.wrapped.DrawStyle else None
