'''_2004.py

DesignResults
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.imported_fes.version_comparer import _2007
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_DESIGN_RESULTS = python_net_import('SMT.MastaAPI.SystemModel.ImportedFEs.VersionComparer', 'DesignResults')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignResults',)


class DesignResults(_1.APIBase):
    '''DesignResults

    This is a mastapy class.
    '''

    TYPE = _DESIGN_RESULTS
    __hash__ = None

    def __init__(self, instance_to_wrap: 'DesignResults.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def status(self) -> 'str':
        '''str: 'Status' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Status

    @property
    def load_cases(self) -> 'List[_2007.LoadCaseResults]':
        '''List[LoadCaseResults]: 'LoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.LoadCases, constructor.new(_2007.LoadCaseResults))
        return value
