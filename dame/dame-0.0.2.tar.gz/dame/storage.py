from datetime import datetime
from io import BytesIO
import pickle

import numpy as np
from peewee import (
    Model,
    FixedCharField,
    ForeignKeyField,
    DateTimeField,
    BlobField,
    IntegerField,
    SqliteDatabase,
)


class TransformModel(Model):
    name = FixedCharField(max_length=128)
    digest = FixedCharField(max_length=128)
    version = DateTimeField(default=datetime.now)


class Result(Model):
    origin = ForeignKeyField(TransformModel, backref="results")
    dataset_index = IntegerField()
    pickled_data = BlobField()
    numpy_data = BlobField(null=True)


class NumpyPlaceholder:
    def __init__(self, num):
        self.num = num


class PeeWeeStore:
    def __init__(
        self, db_cls=SqliteDatabase, src_id=None, db_kwargs=None, db_name=None
    ):
        self.db_cls = db_cls
        self.db_name = db_name if db_name is not None else src_id
        self.db_kwargs = db_kwargs or dict({"pragmas": {"foreign_keys": 1}})

    def open(self, db_name=None, **kwargs):
        if db_name is None:
            db_name = self.db_name
        if not kwargs:
            kwargs = self.db_kwargs
        self.db = self.db_cls(db_name, **kwargs)
        # Models in relation are automatically bound
        TransformModel.bind(self.db)
        self.db.connect()
        self.db.create_tables([TransformModel, Result])

    def close(self):
        self.db.close()

    def transform_id(self, t):
        t_name = t.__class__.__name__
        if not hasattr(self, "_transform_ids"):
            self._transform_ids = {}
        if t_name not in self._transform_ids:
            self._transform_ids[t_name] = TransformModel.get_or_create(
                digest=t.version(), name=t_name
            )[0].id
        return self._transform_ids[t_name]

    @staticmethod
    def separate_numpy_data(data):
        np_data = []
        for key in sorted(data.keys()):
            if isinstance(data[key], np.ndarray):
                np_data.append(data[key])
                data[key] = NumpyPlaceholder(len(np_data) - 1)
        return data, np_data

    @staticmethod
    def get_blobs(data, np_data):
        out = pickle.dumps(data)
        if len(np_data) > 0:
            np_out = BytesIO()
            for arr in np_data:
                np.save(np_out, arr)
            return out, np_out.getvalue()
        return out, None

    @staticmethod
    def unpack_blobs(data_blob, np_data_blob):
        data = pickle.loads(data_blob)
        if np_data_blob is not None:
            ord_keys = [i for i in data.items() if isinstance(i[1], NumpyPlaceholder)]
            ord_keys = sorted(ord_keys, key=lambda item: item[1].num)
            ord_keys, _ = zip(*ord_keys)
            np_data_blob = BytesIO(np_data_blob)
            for key in ord_keys:
                data[key] = np.load(np_data_blob)
        return data

    def save(self, idx, transform, data):
        data = dict(data)
        out, np_out = self.get_blobs(*self.separate_numpy_data(data))
        trans = self.transform_id(transform)
        res = Result(
            origin_id=trans, dataset_index=idx, pickled_data=out, numpy_data=np_out,
        )
        res.save()

    def load(self, idx, transform):
        trans = self.transform_id(transform)
        res = Result.get_or_none(origin_id=trans, dataset_index=idx)
        if res is None:
            return None
        return self.unpack_blobs(res.pickled_data, res.numpy_data)
