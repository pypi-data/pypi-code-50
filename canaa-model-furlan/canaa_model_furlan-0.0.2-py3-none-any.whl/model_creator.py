import os
from collections import defaultdict
from datetime import datetime

import yaml

from .logging import get_logger
from .model_field import ModelField
from .model_info import ModelInfo
from .utils import camel_to_snake, snake_to_camel
from .imports import Imports


class ModelCreator:

    def __init__(self, file_name, ignore_field_errors, just_validate):
        if not os.path.exists(file_name):
            raise FileNotFoundError(file_name)
        self.log = get_logger()
        self.fields = []
        self.info: ModelInfo = None
        self.pks = []
        self._imports = Imports()
        self._ok = False
        self._ignore_field_errors = ignore_field_errors
        self._just_validate = just_validate
        ext = os.path.splitext(file_name)
        if len(ext) > 0:
            ext = ext[1].lower()
            self.log.info('ModelCreator: %s', file_name)
            if ext == '.csv':
                self._ok = self.load_from_csv(file_name)
            elif ext == '.yaml' or ext == '.yml':
                self._ok = self.load_from_yaml(file_name)
        else:
            raise ValueError('Invalid file type: {0}'.format(file_name))

    def __str__(self):
        if not self._ok:
            return "ModelCreator data is not loaded"

        return " - ".join([
            str(self.info),
            "{0} fields".format(len(self.fields))])

    @property
    def is_ok(self):
        return self._ok

    @property
    def promax_model_file_name(self):
        if self.info:
            return camel_to_snake(self.info.promax_model)+"_model.py"
        return "undefined_promax_model.py"

    @property
    def ms_model_file_name(self):
        if self.info:
            return camel_to_snake(self.info.ms_model)+'_model.py'
        return "undefined_ms_model.py"

    @property
    def dto_file_name(self):
        if self.info:
            return camel_to_snake(self.info.ms_model)+'_dto.py'
        return "undefined_dto_model.py"

    def load_from_csv(self, file_name):
        has_head = False

        with open(file_name, 'r', encoding='utf-8') as f:
            line_no = 0
            for linha in f.readlines():
                line_no += 1
                if not has_head:
                    self.info = ModelInfo(linha)
                    has_head = True
                else:
                    if not self._add_field(linha, line_no):
                        return False

        return True

    def load_from_yaml(self, file_name):
        with open(file_name) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            self.info = ModelInfo(data)
            if "fields" in data:
                for field_data in data['fields']:
                    if not self._add_field(field_data):
                        return False

        return True

    def _add_field(self, field_data, line_no: int = 0):
        try:
            field = ModelField(field_data)
        except Exception as exc:
            exc_msg = "".join([
                "" if line_no < 1 else "line #{0}: ".format(line_no),
                str(exc)])
            if self._ignore_field_errors:
                self.log.warning(exc_msg)
                return True
            else:
                self.log.error(exc_msg)
                return self._just_validate

        self.log.info(str(field))

        self.fields.append(field)
        if field.pk:
            self.pks.append(field)

        for datetime_type in ['datetime', 'time', 'date']:
            if datetime_type in [field.type_promax, field.type_ms]:
                self._imports.add('datetime', datetime_type)

        if not field.primitive_type:
            self._imports.add(self.info.namespace_ms, field.type_ms+'DTO')

        return True

    def imports(self):
        return self._imports.to_code().splitlines()
