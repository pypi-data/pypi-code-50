import sense_core as sd
from django.db.utils import IntegrityError
from sense_push.common import *


class DjangoPushDataHandler(object):

    def __init__(self, model_map):
        self.model_map = model_map
        self.model_field_map = dict()

    def get_model_key(self, database, table):
        return "{0}_{1}".format(database, table)

    def get_model_fields(self, model):
        fields = self.model_field_map.get(model)
        if fields:
            return fields
        fields = set([field.name for field in model._meta.get_fields()])
        self.model_field_map[model] = fields
        return fields

    def _get_model(self, database, table):
        key = self.get_model_key(database, table)
        model = self.model_map.get(key)
        if model:
            return model
        return self.model_map.get(table)

    def insert(self, database, table, data):
        self._insert0(database, table, data, "insert")
        self.callback_handle(PUSH_ACTION_INSERT, database, table, data)

    def _insert0(self, database, table, data, action):
        try:
            model_item = self._get_model(database, table)
            if not model_item:
                return
            model = model_item['model']
            fields = model_item.get('fields')
            if not fields:
                fields = self.get_model_fields(model)
            data2 = self._build_update_data(data, model_item, fields)
            model.objects.update_or_create(**data2)
            sd.log_info(action + " data table={0} data={1}".format(table, data2))
        except IntegrityError as ex:
            sd.log_warn("IntegrityError for table={0} data={1}".format(table, data))
        except Exception as ex:
            sd.log_exception(ex)
            sd.log_error("execption for table={0} data={1}".format(table, data))
            raise ex

    def update(self, database, table, data):
        self._insert0(database, table, data, "update")
        self.callback_handle(PUSH_ACTION_UPDATE, database, table, data)

    def _build_update_data(self, data, model_item, fields):
        after = data.get('after')
        if after:
            data = after
        res = self.build_primary_keys(data, model_item['primary'])
        if not res:
            sd.log_error("build_primary_keys failed for data={0} primary={1}".format(data, model_item['primary']))
            return None
        data = self.build_field_keys(data, fields)
        res = self.build_update_params(res, data)
        return res

    def build_update_params(self, res, data):
        res['defaults'] = data
        return res

    def build_field_keys(self, data, fields):
        res = {}
        for key, val in data.items():
            if key not in fields:
                continue
            res[key] = val
        return res

    def build_primary_keys(self, data, primary_keys):
        res = {}
        for key in primary_keys:
            val = data.pop(key)
            if val is None:
                return None
            res[key] = val
        return res

    def delete(self, database, table, data):
        model_item = self._get_model(database, table)
        if not model_item:
            return
        model = model_item['model']
        res = self.build_primary_keys(data, model_item['primary'])
        if not res:
            sd.log_error("build_primary_keys failed for data={0} primary={1}".format(data, model_item['primary']))
            return
        model.objects.filter(**res).delete()
        self.callback_handle(PUSH_ACTION_DELETE, database, table, data)

    def callback_handle(self, action, database, table, data):
        pass
