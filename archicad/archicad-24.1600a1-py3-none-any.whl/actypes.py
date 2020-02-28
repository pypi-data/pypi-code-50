"""GRAPHISOFT
"""
from uuid import UUID
from typing import List, Optional
from enum import Enum
from .acbasetype import ACBaseType
from .validators import value_set

# Navigator

VIEWMAP = 'ViewMap'
PROJECTMAP = 'ProjectMap'
LAYOUTBOOK = 'LayoutBook'

class NavigatorTreeId(ACBaseType):
    def __init__(self, type):
        self.type: str = type

NavigatorTreeId.get_classinfo().add_field('type', str, value_set(VIEWMAP, PROJECTMAP, LAYOUTBOOK))


class NavigatorItemId(ACBaseType):
    def __init__(self, guid):
        self.guid: UUID = guid

NavigatorItemId.get_classinfo().add_field('guid', UUID)


class NavigatorItem(ACBaseType):
    '''Navigátor item
    '''
    def __init__(self, navigatorItemId, prefix, name, type, sourceNavigatorItemId=None, children=None):
        self.navigatorItemId: NavigatorItemId = navigatorItemId
        self.prefix: str = prefix
        self.name: str = name
        self.type: str = type
        self.sourceNavigatorItemId: Optional[NavigatorItemId] = sourceNavigatorItemId
        self.children: Optional[List[NavigatorItem]] = children

NavigatorItem.get_classinfo().add_field('navigatorItemId', NavigatorItemId)
NavigatorItem.get_classinfo().add_field('prefix', str)
NavigatorItem.get_classinfo().add_field('name', str)
NavigatorItem.get_classinfo().add_field('type', str)
NavigatorItem.get_classinfo().add_field('sourceNavigatorItemId', Optional[NavigatorItemId])
NavigatorItem.get_classinfo().add_field('children', Optional[List[NavigatorItem]])
