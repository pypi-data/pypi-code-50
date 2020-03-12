import pandas as pd


class DaoBase(object):

    def __init__(self, **kwargs):
        self._run_date = kwargs.get("run_date")
        self._pool_name = None

    def save(self, source_block):
        pass

    def save_to_csv(self, *args, **kwargs):
        pass

    def save_to_mongo(self, *args, **kwargs):
        pass

    def save_to_mysql(self, *args, **kwargs):
        pass

    def export_to_csv(self, *args, **kwargs):
        pass

    def export_to_mysql(self, *args, **kwargs):
        pass

