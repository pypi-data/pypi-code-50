# -*- coding: utf-8 -*-
import json

from marshmallow import fields, Schema, EXCLUDE, post_dump, post_load

from .models import UserPagination
from .models import User
from .models import UserSexEnum, UserStatusEnum, UserSourceTypeEnum, UserTypeEnum, UserUpdatePasswordStrategyEnum
from . import accountService_pb2 as a_pb


class DateTimeField(fields.DateTime):
    def _serialize(self, value, attr, obj, **kwargs):
        return super()._serialize(value, attr, obj, **kwargs)

    def _deserialize(self, value, attr, data, **kwargs):
        if not value:
            return None
        return super()._deserialize(value, attr, data, **kwargs)


class PbJsonString(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return {}

    def _deserialize(self, value, attr, data, **kwargs):
        return json.dumps(value)


class UserSexEnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        value = value if isinstance(value, int) else value.value
        return int(value) if value is not None else 0

    def _deserialize(self, value, attr, data, **kwargs):
        return UserSexEnum(value) if value is not None else UserSexEnum.USER_SEX_UNKNOWN


class UserStatusEnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        value = value if isinstance(value, int) else value.value
        return int(value) if value is not None else 0

    def _deserialize(self, value, attr, data, **kwargs):
        return UserStatusEnum(value) if value is not None else UserStatusEnum.USER_STATUS_DEACTIVATED


class UserSourceTypeEnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        value = value if isinstance(value, int) else value.value
        return int(value) if value is not None else 0

    def _deserialize(self, value, attr, data, **kwargs):
        return UserSourceTypeEnum(value) if value is not None else UserSourceTypeEnum.USER_SOURCE_TYPE_SERVICE


class UserTypeEnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        value = value if isinstance(value, int) else value.value
        return int(value) if value is not None else 0

    def _deserialize(self, value, attr, data, **kwargs):
        return UserTypeEnum(value) if value is not None else UserTypeEnum.USER_TYPE_SYSTEM


class UserUpdatePasswordStrategyEnumField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        value = value if isinstance(value, int) else value.value
        return int(value) if value is not None else 0

    def _deserialize(self, value, attr, data, **kwargs):
        return UserUpdatePasswordStrategyEnum(
            value) if value is not None else UserUpdatePasswordStrategyEnum.USER_UPDATE_PASSWORD_STRATEGY_NONE


# base object schema
class _OBSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Int(required=True)
    create_time = DateTimeField(default=None, missing=None, allow_none=True)

    # update_time = DateTimeField(default=None, missing=None, allow_none=True)

    @post_dump
    def clean_missing(self, data, **kwargs):
        ret = data.copy()
        for key in filter(lambda key: data[key] is None, data):
            del ret[key]
        return ret


# base pb schema
class _PbSchema(_OBSchema):
    create_time = fields.Str(default=None, missing=None)
    # update_time = fields.Str(default=None, missing=None)


# user schema
class UserBaseSchema(Schema):
    username = fields.Str(default='', missing='')
    password = fields.Str(default='', missing='')
    password_old = fields.Str(default='', missing='')
    name = fields.Str(default='', missing='')
    sex = UserSexEnumField(default=UserSexEnum.USER_SEX_UNKNOWN, missing=0)
    avatar = fields.Str(default='', missing='')
    id_card_number = fields.Str(default='', missing='')
    id_card_is_verified = fields.Bool(default=False, missing=False)
    company = fields.Str(default='', missing='')
    position = fields.Str(default='', missing='')
    email = fields.Str(default='', missing='')
    email_is_verified = fields.Bool(default=False, missing=False)
    phone = fields.Str(default='', missing='')
    phone_is_verified = fields.Bool(default='', missing='')
    status = UserStatusEnumField(default=UserStatusEnum.USER_STATUS_DEACTIVATED, missing=0)
    is_activated = fields.Bool(default=False, missing=False)
    user_type = UserTypeEnumField(default=UserTypeEnum.USER_TYPE_SYSTEM, missing=0)
    source_type = UserSourceTypeEnumField(default=UserSourceTypeEnum.USER_SOURCE_TYPE_SERVICE, missing=0)
    update_password_strategy = UserUpdatePasswordStrategyEnumField(
        default=UserUpdatePasswordStrategyEnum.USER_UPDATE_PASSWORD_STRATEGY_NONE, missing=0)
    creator_id = fields.Int(required=True)


class UserObjectSchema(_OBSchema, UserBaseSchema):
    birthday = DateTimeField(default=None, missing=None, allow_none=True)
    activation_time = DateTimeField(default=None, missing=None, allow_none=True)
    disabled_at = DateTimeField(default=None, missing=None, allow_none=True)
    last_login_time = DateTimeField(default=None, missing=None, allow_none=True)
    last_update_password_time = DateTimeField(default=None, missing=None, allow_none=True)

    @post_load
    def make_object(self, data, **kwargs):
        return User(**data)


class UserPbSchema(_PbSchema, UserBaseSchema):
    birthday = fields.Str(default=None, missing=None)
    activation_time = fields.Str(default=None, missing=None)
    disabled_at = fields.Str(default=None, missing=None)
    last_login_time = fields.Str(default=None, missing=None)
    last_update_password_time = fields.Str(default=None, missing=None)

    @post_load
    def make_object(self, data, **kwargs):
        return a_pb.UserMessage(**data)


# user pagination schema
class UserPaginationBaseSchema(Schema):
    current_page = fields.Int(default=1, missing=1)
    page_size = fields.Int(default=10, missing=10)
    page_total = fields.Int()
    total = fields.Int()

    @post_dump
    def clean_missing(self, data, **kwargs):
        ret = data.copy()
        for key in filter(lambda key: data[key] is None, data):
            del ret[key]
        return ret


class UserPaginationObjectSchema(UserPaginationBaseSchema):
    list = fields.List(fields.Nested(UserObjectSchema), default=[], missing=[])

    @post_load
    def make_object(self, data, **kwargs):
        return UserPagination(**data)


class UserPaginationPbSchema(UserPaginationBaseSchema):
    list = fields.List(fields.Nested(UserPbSchema), default=[], missing=[])

    @post_load
    def make_object(self, data, **kwargs):
        return a_pb.GetUserPageListResponse(**data)
