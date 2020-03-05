'''_1846.py

ActiveImportedFESelectionGroup
'''


from mastapy.system_model.part_model.configurations import _2068, _2079
from mastapy.system_model.part_model import _1867
from mastapy.system_model.imported_fes import _104
from mastapy._internal.python_net import python_net_import

_ACTIVE_IMPORTED_FE_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveImportedFESelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveImportedFESelectionGroup',)


class ActiveImportedFESelectionGroup(_2068.PartDetailConfiguration['_2079.ActiveImportedFESelection', '_1867.ImportedFEComponent', '_104.ImportedFE']):
    '''ActiveImportedFESelectionGroup

    This is a mastapy class.
    '''

    TYPE = _ACTIVE_IMPORTED_FE_SELECTION_GROUP
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ActiveImportedFESelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
