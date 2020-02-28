#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from .converters import dict_to_j_params
from .py4j_util import get_java_class
from .session import Session


class BaseDB(object):
    def __init__(self, db_type, **kwargs):
        self._type = db_type
        self.params = dict()
        for k, v in kwargs.items():
            self.params[k] = v
        self._config = json.dumps(self.params)
        self._ds = None

    def get_params(self):
        return self.params

    def close(self):
        pass

    def _get_ds(self):
        if self._ds is None:
            self._ds = Session.inst()._jvm_bridge.get_datasource(
                self._type, self._config)
        return self._ds

    def _jvm(self):
        return Session.inst()._jvm_bridge

    def listTableNames(self, name_prefix='', max_size=100):
        return self._get_ds().list_tables(name_prefix, max_size)

    def hasTable(self, table_name):
        return self._get_ds().has_table(table_name)

    def dropTable(self, table_name):
        return self._get_ds().drop_table(table_name)

    def getColNames(self, table_name):
        return self._get_ds().get_column_names(table_name)

    def getColTypes(self, table_name):
        return Session.inst()._jvm_bridge.get_column_types(
            self._type, self._config, table_name)

    def execute(self, sql):
        return self._get_ds().execute(sql)

    def show(self, table_name, max_size=100):
        return self._get_ds().get_table_data(table_name, max_size)

    def readTable(self, tableName):
        pass

    def getName(self):
        return self._get_ds().name()

    def theTableParamKey(self):
        return 'tableName'

    def theProjectParamKey(self):
        return 'project'

    def theOpClsName(self, batchOrStream, sourceOrSink):
        raise RuntimeError('Not implemented yet')

    
class MysqlDB(BaseDB):
    def __init__(self, dbName, ip, port, userName, password, **kwargs):
        super(MysqlDB, self).__init__(
            db_type='MYSQL',
            dbName=dbName,
            ip=ip,
            port=port,
            userName=userName,
            password=password, **kwargs)
        self.dbName = dbName


def makeJavaDb(db, *args):
    j_base_db_cls = get_java_class("com.alibaba.alink.common.io.BaseDB")
    db.params.update({"ioName": db._type.lower()})
    j_db = j_base_db_cls.of(dict_to_j_params(db.params))
    return j_db


def makeDbOpParams(db, *args, **kwargs):
    table_name = kwargs.pop(db.theTableParamKey(), None)
    if len(args) > 0 and isinstance(args[0], (str,)):
        table_name = args[0]

    if table_name is not None:
        kwargs[db.theTableParamKey()] = table_name
    else:
        raise RuntimeError('Missing Parameter: {}'.format(db.theTableParamKey()))
    kwargs["tableName"] = kwargs[db.theTableParamKey()]
    return dict_to_j_params(kwargs)


def makeOpFromDbOp(op_cls, j_db_op):
    j_op_cls = get_java_class(op_cls.CLS_NAME)
    j_op = j_op_cls(j_db_op.getParams())

    op = op_cls(j_op=j_op)
    for key in j_op.getParams().listParamNames():
        op.params.set(key, j_op.getParams().getString(key))
    return op
