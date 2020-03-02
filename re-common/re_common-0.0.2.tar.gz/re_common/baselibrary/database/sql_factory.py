from re_common.baselibrary import BaseAbs


class SqlFactory(BaseAbs):
    @staticmethod
    def mysql_factory(type='mysql'):
        from re_common.baselibrary import Mysql
        if type == 'mysql':
            return Mysql()
        assert 0, "err sql type please check: %s" % type

    @staticmethod
    def sqlite_factory(type='sqlite3'):
        from re_common.baselibrary import Sqlite3
        if type == 'sqlite3':
            return Sqlite3()
        assert 0, "err sqllite type please check: %s" % type
