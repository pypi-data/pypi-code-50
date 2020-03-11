import json
import pathlib

from typing import List

import marshmallow
from marshmallow import Schema, fields, post_load


class ConfigDamage(Exception):
    pass


class Feature(object):
    def __init__(self, name: str, url: str, save_dir: str, temp_dir: str):
        self.name = name
        self.url = url
        self.save_dir = save_dir
        self.temp_dir = temp_dir


class FeatureSchema(Schema):
    name = fields.String(required=True)
    url = fields.String(required=True)
    save_dir = fields.String(required=True)
    temp_dir = fields.String(required=True)

    @post_load
    def make_feature(self, data, *args, **kwargs) -> Feature:
        return Feature(**data)


class Origin(object):
    def __init__(self, name, url):
        self.name = name
        self.url = url


class OriginSchema(Schema):
    name = fields.String(required=True)
    url = fields.String(required=True)

    @post_load
    def make_config(self, data, *args, **kwargs):
        return Origin(**data)


class Config(object):
    def __init__(self, features: List[Feature], origins: List[Origin]):
        self.features = features
        self.origins = origins


class ConfigSchema(Schema):
    origins = fields.Nested(OriginSchema, many=True, required=True)
    features = fields.Nested(FeatureSchema, many=True, required=True)

    @post_load
    def make_config(self, data, *args, **kwargs):
        return Config(**data)


def read_conf(conf_path: str) -> Config:
    """
    负责读取配置文件
    :param conf_path:配置文件的路径
    :return:
    :raise
    """
    with open(conf_path) as file:
        try:
            conf_json = json.load(file)
        except json.decoder.JSONDecodeError:
            raise ConfigDamage("ddcmaker损坏，请执行ddcmaker更新")

    schema = ConfigSchema()
    try:
        conf = schema.load(conf_json)
    except marshmallow.exceptions.ValidationError:
        raise ConfigDamage("ddcmaker损坏，请执行ddcmaker更新")
    return conf


def get_conf() -> Config:
    """读取配置文件"""
    local_path = pathlib.Path(__file__).absolute()
    config_path = local_path.parent.joinpath('conf.json')
    if not config_path.exists():
        raise ConfigDamage("ddcmaker损坏，请执行ddcmaker更新")
    return read_conf(config_path.as_posix())
