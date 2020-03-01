from datetime import datetime, timedelta

from .lib.cache import Cacher
from .lib.exceptions import ActionNameNotSpecified, ActionDateIsNotDatetime, ActionDateNotSpecified
from .lib.loader import Loader


class CMKUClient(Cacher):
    """
    Client to enable access to data on CMKU
    """
    def load_actions(self):
        """
        Loads actions in the nearest half year
        :return: list instance of Action
        """
        params = ("load_actions",)
        cache = self._check_cache(params)
        if cache:
            return cache
        result = Loader.load_actions()
        self._store_cache(params, result)
        return result

    def load_action_detail(self, action_id=None):
        """
        Loads action detail based on ID
        :param action_id: id from url
        :return: instance of ActionDetail
        """
        params = ("load_action_detail", action_id,)
        cache = self._check_cache(params)
        if cache:
            return cache
        result = Loader.load_action_detail(action_id)
        self._store_cache(params, result)
        return result

    def load_breeds(self):
        """
          Loads action detail based on ID
          :return: list instances of Breeds
          """
        params = ("load_breeds",)
        cache = self._check_cache(params)
        if cache:
            return cache
        result = Loader.load_breeds()
        self._store_cache(params, result)
        return result

    def load_by_date(self, date_from=datetime.now(), date_to=(datetime.now() + timedelta(days=365))):
        """
        Loads actions in a wanted time interval
        :param date_from: datetime of start date
        :param date_to:  datetime of end date
        :return: list of instances ActionList
        """
        if not all((isinstance(date_from, datetime), isinstance(date_to, datetime))):
            raise ActionDateIsNotDatetime()
        if not all((date_to, date_from)):
            raise ActionDateNotSpecified()
        params = ("load_by_date", date_from, date_to)
        cache = self._check_cache(params)
        if cache:
            return cache
        result = Loader.load_actions_by_date(date_from, date_to)
        self._store_cache(params, result)
        return result

    def load_by_name(self, name=None):
        """
        Loads actions containing that string in name
        :param name: name or substr of name
        :return: list of instance ActionList
        """
        if not name:
            raise ActionNameNotSpecified()
        params = ("load_by_name", name)
        cache = self._check_cache(params)
        if cache:
            return cache
        result = Loader.load_actions_by_name(name)
        self._store_cache(params, result)
        return result

    def load_types(self):
        """
        Load all types of actions
        :return: list of instance ActionType
        """
        params = ("load_types",)
        cache = self._check_cache(params)
        if cache:
            return cache
        result = Loader.load_types()
        self._store_cache(params, result)
        return result

