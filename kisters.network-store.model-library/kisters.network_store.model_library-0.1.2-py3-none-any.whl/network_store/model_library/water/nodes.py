from typing import List

from pydantic import Field

from kisters.network_store.model_library.base import BaseNode as _BaseNode
from kisters.network_store.model_library.base import Model as _Model


class _Node(_BaseNode):
    domain: str = Field("water", const=True)


class Junction(_Node):
    element_class: str = Field("Junction", const=True)


class LevelBoundary(_Node):
    element_class: str = Field("LevelBoundary", const=True)


class FlowBoundary(_Node):
    element_class: str = Field("FlowBoundary", const=True)


class _StorageLevelVolume(_Model):
    level: float
    volume: float = Field(..., ge=0.0)


class Storage(_Node):
    element_class: str = Field("Storage", const=True)
    level_volume: List[_StorageLevelVolume] = Field(..., min_items=2)
