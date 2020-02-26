""" Storage-friendly internal data classes. """
import numbers

from collections import Mapping, defaultdict
from base64 import urlsafe_b64decode, urlsafe_b64encode
from uuid import UUID, uuid4

from datetime import datetime
from dataclasses import dataclass, fields, _MISSING_TYPE, MISSING, field, asdict
from typing import Union, List

from .base import (
    BaseDataClass, 
    register_type, 
    _fields_cache,
    model_dataclass
)

from .view import ComplexPrimitiveView

NAME_SEPARATOR = ':'
NO_VERSION = '0'

def create_uuid():
    return uuid4()

def uuid_to_slug(uuidstring):
    try:
        uuid = UUID(uuidstring)
    except AttributeError:
        uuid = uuidstring
    
    return urlsafe_b64encode(uuid.bytes).rstrip(b'=').decode('ascii')

def slug_to_uuid(slug):
    return str(UUID(bytes=urlsafe_b64decode(slug + '==')))

def is_type_of(cls, base_cls):
    return cls._type == base_cls._type

def compute_stats(features):
    name_tuple_to_count_map = defaultdict(int)

    for feature in features:
        # For feature ('x', 'y', 'z'), increment ('x',), ('x', 'y') and ('x', 'y', 'z')
        name_tuple = feature.name_tuple

        for i in range(1, len(name_tuple)):
            sub_name = name_tuple[:i]
            name_tuple_to_count_map[sub_name] += 1

    for feature in features:
        feature.feature_count = name_tuple_to_count_map[feature.name_tuple]


@model_dataclass()
@register_type('dut')
class DutIDRecord(BaseDataClass):
    id: str
    version: str
    
    @classmethod
    def create(cls, id_or_dict, version=None):
        if isinstance(id_or_dict, Mapping):
            id = id_or_dict.get('id', None)
            version = id_or_dict.get('version', None)
        else:
            id = id_or_dict
            
        if version is None:
            version = NO_VERSION
            
        return cls(
            id=id,
            version=version
        )
        
    def match(self, other):
        id_match = self.id == other.id if self.id is not None else True
        version_match = self.version == other.version if self.version is not None else True
        return id_match and version_match

@model_dataclass()
@register_type('test_id')
class TestIDRecord(BaseDataClass):
    testbench_name: str
    dut: DutIDRecord
    test_uuid: str
    tags: dict
    start_datetime: datetime
    
    @classmethod
    def create(cls, testbench_name, dut, start_datetime, tags=None):
        return cls(
            testbench_name=testbench_name,
            dut=DutIDRecord.create(dut),
            test_uuid=uuid_to_slug(create_uuid()),
            start_datetime=start_datetime,
            tags= tags if tags else {}
        )
        
    
    def add_tag(self, key, value=True):
        self.tags[key] = value
        
    def remove_tag(self, key):
        del self.tags[key]

@model_dataclass()
@register_type('features_no_data')
class FeatureRecordNoData(BaseDataClass):
    oid: str
    test_id: TestIDRecord
    name: str
    description: str
    version: int
    depth: int
    index: int
    feature_count: int # Number of children
    ancestors: List[str]
    original: bool
    
    @classmethod
    def get_data_fields(cls):
        """ The data fields are all fields except the ones declare up to this cls
        in the cls MRO.
        
        If a subclass defines only a dataclass field 'foo', this method will return
        foo only as a data field.
        """
        return set(_fields_cache.retrieve(cls)) - set(_fields_cache.retrieve(FeatureRecordNoData))
    
    @property
    def name_tuple(self):
        return tuple(self.ancestors) + (self.name,)

    @property
    def complete_name(self):
        return NAME_SEPARATOR.join(self.name_tuple)
        
    def as_dict(self):
        """ Transforms this object recursively into a dict. Adds the static
        _type field to the data.."""
        data = super(FeatureRecordNoData, self).as_dict()
        return data
    
@model_dataclass()
@register_type('outcome')
class OutcomeData(BaseDataClass):
    is_pass: bool
    is_skip: bool = False
    is_abort: bool = False
    
    def __bool__(self):
        return self.is_pass and not self.is_abort


@model_dataclass()
@register_type('features')
class FeatureRecord(FeatureRecordNoData):
    user_data: dict # TODO Replace with data_view with descriptor protocol
    outcome: OutcomeData
    
    @classmethod
    def defaults(cls, **others):
        others['user_data'] = others.get('user_data', {})
        others['feature_count'] = others.get('feature_count', None)
        return super(FeatureRecord, cls).defaults(**others)
    
@model_dataclass()
@register_type('phases')
class PhaseFeatureRecord(FeatureRecord):
    duration: float
    
@model_dataclass()
@register_type('measures')
class MeasureFeatureRecord(FeatureRecord):
    value_f: float
    value_s: str

    @property
    def value(self):
        if self.value_f is not None:
            return self.value_f
        else:
            return self.value_s

    @value.setter
    def value(self, value):
        if value is None or isinstance(value, str):
            self.value_f = None
            self.value_s = value
        elif isinstance(value, numbers.Number):
            self.value_f = value
            self.value_s = None
        else:
            raise ValueError('Only string or numeric types are supported. Received {!r} of type {}'.format(value, type(value)))
    
@model_dataclass()
@register_type('template')
class FeatureRecordTemplate(FeatureRecord):
    source: FeatureRecord
    records_count: int = 0
    
    def increment_records_count(self):
        self.records_count = self.records_count + 1
    
    
@model_dataclass()
@register_type('top_level')
class TestRecordSummary(PhaseFeatureRecord):

    @property
    def total_feature_count(self):
        return self.feature_count

    @classmethod
    def get_data_fields(cls):
        base = super(TestRecordSummary, cls).get_data_fields()
        return list(base) + [FeatureRecord.test_id]
    
@model_dataclass()
class DutOp(BaseDataClass):
    dut_match: DutIDRecord
    dut_after: DutIDRecord
    op_datetime: datetime
    
    @classmethod
    def create(cls, dut_match, dut_after, op_datetime):
        return cls(
            dut_match=DutIDRecord.create(dut_match),
            dut_after=DutIDRecord.create(dut_after),
            op_datetime=op_datetime
        )
    
    def does_applies_to(self, dut, on_datetime):
        return self.dut_match.match(dut) and self.op_datetime < on_datetime
    
    def apply_or_return(self, dut, on_datetime):
        if self.does_applies_to(dut, on_datetime):
            return self.apply(dut)
        else:
            return dut
        
    def apply(self, dut):
        """Apply op to dut. Does not check for datetime. """
        new_dut = self.dut_after.copy()
        if new_dut.id is None:
            new_dut.id = dut.id
        return new_dut
        
        
def default_cls_missing_view_fn(cls):
    return cls.get_default_view()
        
class DefaultPrimitiveView(ComplexPrimitiveView):
    def __init__(self):
        super(DefaultPrimitiveView, self).__init__(
            BaseDataClass, 
            cls_missing_view_fn=default_cls_missing_view_fn
        )
        
        # summary_mapping = TestRecordSummary.get_default_view_mapping()
        
        # self.add_view(
        #     TestRecordSummary,
        #     summary_mapping
        # )