# -*- coding: utf-8 -*-
from .base import BaseSinkStreamOp, BaseSourceStreamOp
from ..base_db import makeJavaDb, makeDbOpParams, makeOpFromDbOp
from ..py4j_util import get_java_class


class DBSinkStreamOp(BaseSinkStreamOp):
    def __init__(self, j_op=None, *args, **kwargs):
        kwargs['CLS_NAME'] = 'com.alibaba.alink.operator.stream.sink.DBSinkStreamOp'
        super(DBSinkStreamOp, self).__init__(j_op=j_op, *args, **kwargs)
        pass


class DBSourceStreamOp(BaseSourceStreamOp):
    def __init__(self, j_op=None, *args, **kwargs):
        kwargs['CLS_NAME'] = 'com.alibaba.alink.operator.stream.source.DBSourceStreamOp'
        super(DBSourceStreamOp, self).__init__(j_op=j_op, *args, **kwargs)
        pass

    pass


def makeDBSourceStreamOp(db, *args, **kwargs):
    from .common import MySqlSourceStreamOp
    db_to_op_cls = {
        "MYSQL": MySqlSourceStreamOp
    }
    db_type = db._type
    if db_type not in db_to_op_cls:
        raise Exception("There is no sink stream op for %s", type)

    j_db = makeJavaDb(db)
    j_params = makeDbOpParams(db, *args, **kwargs)
    j_db_op = get_java_class("com.alibaba.alink.operator.stream.source.DBSourceStreamOp")(j_db, j_params)

    op_cls = db_to_op_cls.get(db_type)
    op = makeOpFromDbOp(op_cls, j_db_op)
    return op


def makeDBSinkStreamOp(db, *args, **kwargs):
    from .common import MySqlSinkStreamOp
    db_to_op_cls = {
        "MYSQL": MySqlSinkStreamOp
    }
    db_type = db._type
    if db_type not in db_to_op_cls:
        raise Exception("There is no sink stream op for %s", type)

    j_db = makeJavaDb(db)
    j_params = makeDbOpParams(db, *args, **kwargs)
    j_db_op = get_java_class("com.alibaba.alink.operator.stream.sink.DBSinkStreamOp")(j_db, j_params)

    op_cls = db_to_op_cls.get(db_type)
    op = makeOpFromDbOp(op_cls, j_db_op)
    return op
