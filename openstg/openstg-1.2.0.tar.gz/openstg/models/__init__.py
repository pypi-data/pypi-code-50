from collections import namedtuple

from backend.utils import unflatdot, normalize, flatdot, make_schema, recursive_crud
from backend.models import get_model

from openstg.serializers import *

SearchResult = namedtuple('SearchResult', ['items', 'n_items', 'limit', 'offset'])


class ModelException(Exception):
    pass


class Model(object):
    schema = unflatdot([])
    serializer = None
    model = None

    def get(self, search_params, limit, offset):
        model = get_model(self.model)
        try:
            n_items = model.search_count(search_params)
            res_ids = model.search(search_params, limit=limit, offset=offset)
        except Exception:
            raise ModelException
        if not res_ids:
            return SearchResult([], 0, limit, offset)
        items = []
        for values in model.read(res_ids, list(self.schema.keys())):
            obj = normalize(model, values, self.schema)
            items.append(self.serializer.dump(obj=obj).data)
        return SearchResult(items, n_items, limit, offset)


class ConcentratorModel(Model):
    model = 'tg.concentrator'
    schema = unflatdot([
        'name',
        'ip_address',
        'model',
        'type',
        'w_password',
        'r_password',
        'fw_version',
        'fw_comm_version',
        'protocol',
        'communication',
        'dc_ws_address',
        'stg_ws_ip_address',
        'stg_ws_password',
        'modem_user',
        'modem_password',
    ])
    serializer = ConcentratorSchema()


class RegisterModel(Model):
    model = 'giscedata.registrador'
    schema = unflatdot([
        'name',
        'cnc_id.id',
        'cnc_id.name',
        'cnc_id.ip_address',
        'cnc_id.dc_ws_address',
    ])
    serializer = RegisterSchema()
