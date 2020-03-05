'''_4908.py

SubGroupInSingleDesignState
'''


from mastapy.system_model.analyses_and_results.static_loads import _1849
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.load_case_groups import _4907
from mastapy._internal.python_net import python_net_import

_SUB_GROUP_IN_SINGLE_DESIGN_STATE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'SubGroupInSingleDesignState')


__docformat__ = 'restructuredtext en'
__all__ = ('SubGroupInSingleDesignState',)


class SubGroupInSingleDesignState(_4907.AbstractDesignStateLoadCaseGroup):
    '''SubGroupInSingleDesignState

    This is a mastapy class.
    '''

    TYPE = _SUB_GROUP_IN_SINGLE_DESIGN_STATE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'SubGroupInSingleDesignState.TYPE'):
        super().__init__(instance_to_wrap)

    def remove_static_load(self, static_load: '_1849.StaticLoadCase'):
        ''' 'RemoveStaticLoad' is the original name of this method.

        Args:
            static_load (mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase)
        '''

        self.wrapped.RemoveStaticLoad(static_load.wrapped if static_load else None)
