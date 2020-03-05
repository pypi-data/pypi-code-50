'''_2063.py

ActiveShaftDesignSelectionGroup
'''


from mastapy.system_model.part_model.configurations import _2074, _2087
from mastapy.system_model.part_model.shaft_model import _1952
from mastapy.shafts import _70
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveShaftDesignSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveShaftDesignSelectionGroup',)


class ActiveShaftDesignSelectionGroup(_2074.PartDetailConfiguration['_2087.ActiveShaftDesignSelection', '_1952.Shaft', '_70.SimpleShaftDefinition']):
    '''ActiveShaftDesignSelectionGroup

    This is a mastapy class.
    '''

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION_GROUP
    __hash__ = None

    def __init__(self, instance_to_wrap: 'ActiveShaftDesignSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
