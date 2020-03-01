from requests import get
from json import loads

from .exceptions import (
    ActionNotFound, ActionNameNotSpecified
)
from .vars import (
    BREEDS_LIST_URL, ACTION_LIST_URL, ACTION_DETAIL_URL, ACTION_TYPES_URL,
    ACTION_TYPES_LIST
)
from ..model.action import (
    ActionDetailGeneralSchema, ActionListGeneralSchema, ActionTypeSchema
)
from ..model.breed import BreedSchema


class Loader(object):
    """
    Loading data and putting to structure
    """
    @staticmethod
    def _get(url):
        # loads and serialize to schema
        data = get(url)
        data = loads(data.text.encode("utf-8"))
        return data

    @classmethod
    def load_action_detail(cls, action_id):
        data = cls._get(ACTION_DETAIL_URL.format(action_id))
        if not data:
            raise ActionNotFound(action_id)
        return ActionDetailGeneralSchema().load(data)

    @classmethod
    def load_breeds(cls):
        data = cls._get(BREEDS_LIST_URL)
        return [BreedSchema().load(item) for item in data.get("items")]

    @classmethod
    def load_actions(cls):
        data = cls._get(ACTION_LIST_URL)
        return [ActionListGeneralSchema().load(item) for item in data]

    @classmethod
    def load_actions_by_date(cls, date_from, date_to):
        data = cls.load_actions()
        result = []
        for action in data:
            if action.date_from >= date_from and action.date_to <= date_to:
                result.append(action)
        return result

    @classmethod
    def load_actions_by_name(cls, name=None):
        if not name:
            raise ActionNameNotSpecified()
        data = cls.load_actions()
        result = []
        for action in data:
            if name.lower().strip() in action.name.lower().strip():
                result.append(action)
        return result

    @classmethod
    def load_types(cls):
        return [ActionTypeSchema().load(item) for item in ACTION_TYPES_LIST]