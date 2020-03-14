class TableBase(object):
    _instance = None
    table = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(cls.__class__, cls).__new__(cls)
        return cls._instance


class TableAccount(TableBase):
    pass


class TableTransactionCategory(TableBase):
    pass


class TableTransactionSubcategory(TableBase):
    pass


class TableTransaction(TableBase):
    pass
