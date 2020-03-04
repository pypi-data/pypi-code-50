import enum
from datetime import datetime
from typing import Optional, List

import attr


class AccountServiceException(Exception):
    pass


class UserSexEnum(enum.IntEnum):
    USER_SEX_UNKNOWN = 0
    USER_SEX_MALE = 1
    USER_SEX_FEMALE = 2


class UserStatusEnum(enum.IntEnum):
    USER_STATUS_DEACTIVATED = 0
    USER_STATUS_ACTIVATED = 1
    USER_STATUS_DISABLED = 2


class UserTypeEnum(enum.IntEnum):
    USER_TYPE_SYSTEM = 0
    USER_TYPE_GENERAL = 1
    USER_TYPE_PATIENT = 2
    USER_TYPE_ADMIN = 3


class UserSourceTypeEnum(enum.IntEnum):
    USER_SOURCE_TYPE_SERVICE = 0
    USER_SOURCE_TYPE_REGISTER = 1
    USER_SOURCE_TYPE_ADMIN = 2
    USER_SOURCE_TYPE_IMPORT = 3


class UserUpdatePasswordStrategyEnum(enum.IntEnum):
    USER_UPDATE_PASSWORD_STRATEGY_NONE = 0
    USER_UPDATE_PASSWORD_STRATEGY_EVERY_THREE_MONTHS = 1


@attr.s
class _Base(object):
    id: int = attr.ib()
    create_time: Optional[datetime] = attr.ib(default=None)
    # update_time: Optional[datetime] = attr.ib(default=None)


@attr.s
class User(_Base):
    username: str = attr.ib(default='')
    password: str = attr.ib(default='')
    password_old: str = attr.ib(default='')
    name: str = attr.ib(default='')
    sex: UserSexEnum = attr.ib(default=UserSexEnum.USER_SEX_UNKNOWN)
    birthday: Optional[datetime] = attr.ib(default='')
    avatar: str = attr.ib(default='')
    id_card_number = attr.ib(default='')
    id_card_is_verified: bool = attr.ib(default=False)
    company: str = attr.ib(default='')
    position: str = attr.ib(default='')
    email: str = attr.ib(default='')
    email_is_verified: bool = attr.ib(default=False)
    phone: str = attr.ib(default='')
    phone_is_verified: bool = attr.ib(default=False)
    status: UserStatusEnum = attr.ib(default=UserStatusEnum.USER_STATUS_DEACTIVATED)
    is_activated: bool = attr.ib(default=False)
    activation_time: str = attr.ib(default='')
    disabled_at: Optional[datetime] = attr.ib(default='')
    user_type: UserTypeEnum = attr.ib(default=UserTypeEnum.USER_TYPE_SYSTEM)
    source_type: UserSourceTypeEnum = attr.ib(default=UserSourceTypeEnum.USER_SOURCE_TYPE_SERVICE)
    update_password_strategy: UserUpdatePasswordStrategyEnum = attr.ib(
        default=UserUpdatePasswordStrategyEnum.USER_UPDATE_PASSWORD_STRATEGY_NONE)
    last_login_time: Optional[datetime] = attr.ib(default='')
    last_update_password_time: Optional[datetime] = attr.ib(default='')
    creator_id: int = attr.ib(default=0)


@attr.s
class UserPagination(object):
    page_total: int = attr.ib()
    total: int = attr.ib()
    current_page: int = attr.ib(default=1)
    page_size: int = attr.ib(default=10)
    list: Optional[List[User]] = attr.ib(default=[])
