# -*- coding: utf-8 -*-

from .base import BaseSinkBatchOp, BaseSourceBatchOp
from ..base_db import makeJavaDb, makeDbOpParams, makeOpFromDbOp
from ..py4j_util import get_java_class


# TODO: not used now
class MemSourceBatchOp(BaseSourceBatchOp):
    def __init__(self, data, colNames=None, **kwargs):
        dim = self._calc_dimesion(data)
        import json
        data_json = json.dumps(data)
        if dim == 1:
            raise RuntimeError('the data should be in two dimension')
        if colNames is None:
            colNames = ['col' + str(x) for x in range(len(data[0]))]
        super(MemSourceBatchOp, self).__init__(
            CLS_NAME='com.alibaba.alink.executor.python.util.InMemorySourceBatchOp',
            colNames=colNames,
            data=data_json)
        pass

    def _calc_dimesion(self, data):
        if isinstance(data, (list, tuple)):
            if len(data) == 0:
                raise RuntimeError('empty list')
            if isinstance(data[0], (list, tuple)):
                return 2
            return 1
        raise RuntimeError('invalid data')

    pass


class DBSinkBatchOp(BaseSinkBatchOp):
    def __init__(self, j_op=None, *args, **kwargs):
        kwargs['CLS_NAME'] = 'com.alibaba.alink.operator.batch.sink.DBSinkBatchOp'
        super(DBSinkBatchOp, self).__init__(j_op=j_op, *args, **kwargs)
        pass


class DBSourceBatchOp(BaseSourceBatchOp):
    def __init__(self, j_op=None, *args, **kwargs):
        kwargs['CLS_NAME'] = 'com.alibaba.alink.operator.batch.source.DBSourceBatchOp'
        super(DBSourceBatchOp, self).__init__(j_op=j_op, *args, **kwargs)
        pass


def makeDBSourceBatchOp(db, *args, **kwargs):
    from .common import MySqlSourceBatchOp
    from .special_operators import MaxComputeSourceBatchOp
    db_to_op_cls = {
        "ODPS": MaxComputeSourceBatchOp,
        "MYSQL": MySqlSourceBatchOp
    }
    db_type = db._type
    if db_type not in db_to_op_cls:
        raise Exception("There is no source batch op for %s", type)

    j_db = makeJavaDb(db)
    j_params = makeDbOpParams(db, *args, **kwargs)
    j_db_op = get_java_class('com.alibaba.alink.operator.batch.source.DBSourceBatchOp')(j_db, j_params)

    op_cls = db_to_op_cls.get(db_type)
    op = makeOpFromDbOp(op_cls, j_db_op)
    return op


def makeDBSinkBatchOp(db, *args, **kwargs):
    from .common import MySqlSinkBatchOp
    from .special_operators import MaxComputeSinkBatchOp
    db_to_op_cls = {
        "ODPS": MaxComputeSinkBatchOp,
        "MYSQL": MySqlSinkBatchOp
    }
    db_type = db._type
    if db_type not in db_to_op_cls:
        raise Exception("There is no sink batch op for %s", type)

    j_db = makeJavaDb(db)
    j_params = makeDbOpParams(db, *args, **kwargs)
    j_db_op = get_java_class("com.alibaba.alink.operator.stream.sink.DBSinkStreamOp")(j_db, j_params)

    op_cls = db_to_op_cls.get(db_type)
    op = makeOpFromDbOp(op_cls, j_db_op)
    return op
