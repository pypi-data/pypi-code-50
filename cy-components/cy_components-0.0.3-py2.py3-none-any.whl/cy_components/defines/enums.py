# -*- coding: utf-8 -*-

from enum import Enum
from datetime import datetime, timedelta


class RuleType(Enum):
    """ Pandas Resample 规则枚举 """

    Day_1 = '1D'

    Minute_5 = '5T'
    Minute_15 = '15T'
    Minute_30 = '30T'


class TimeFrame(Enum):
    """ CCXT 请求用的 K 线时间规则"""

    Minute_1 = '1m'
    Minute_3 = '3m'
    Minute_5 = '5m'
    Minute_15 = '15m'
    Minute_30 = '30m'
    Hour_1 = '1h'
    Hour_2 = '2h'
    Hour_4 = '4h'
    Hour_6 = '6h'
    Hour_8 = '8h'
    Hour_12 = '12h'
    Day_1 = '1d'
    Day_3 = '3d'
    Week_1 = '1w'
    Month_1 = '1M'

    @classmethod
    def all_values(cls):
        """ 所有枚举项的实际值数组 """
        return [e.value for e in cls]

    def time_interval(self, res_unit='ms'):
        """转为时间戳长度

        Parameters
        ----------
        res_unit : str, optional
            时间戳单位, by default 'ms'
        """
        amount = int(self.value[0:-1])
        unit = self.value[-1]
        if 'y' in unit:
            scale = 60 * 60 * 24 * 365
        elif 'M' in unit:
            scale = 60 * 60 * 24 * 30
        elif 'w' in unit:
            scale = 60 * 60 * 24 * 7
        elif 'd' in unit:
            scale = 60 * 60 * 24
        elif 'h' in unit:
            scale = 60 * 60
        else:
            scale = 60
        ti = amount * scale
        if res_unit == 'ms':
            ti *= 1000
        return ti

    def timestamp_backward_offset(self, timestamp, count, unit='ms'):
        """`timestamp` 回推 `count` 个 time_interval 后的时间戳
        ts -= count * time_interval"""
        ts = timestamp - count * self.time_interval(unit)
        return ts

    def next_date_time_point(self, ahead_time=1, debug=False):
        """计算下一个实际时间点

        Parameters
        ----------
        ahead_time : int, optional
            误差秒数，误差内忽略当前周期, by default 1
        debug : bool, optional
            调试模式，打开时设定 10s 后为下个周期, by default False

        Raises
        ------
        ValueError
            目前只支持 'm' 结尾的 Time Interval
        """

        if self.value.endswith('m'):
            time_interval = int(self.value.strip('m'))
            now_time = datetime.now()
            if debug:
                print(now_time)
                return now_time + timedelta(seconds=10)
            target_min = (int(now_time.minute / time_interval) + 1) * time_interval
            # 没到下一个小时
            if target_min < 60:
                target_time = now_time.replace(minute=target_min, second=0, microsecond=0)
            else:
                # 到第二天
                if now_time.hour == 23:
                    target_time = now_time.replace(hour=0, minute=0, second=0, microsecond=0)
                    target_time += timedelta(days=1)
                else:
                    # 下一个小时
                    target_time = now_time.replace(hour=now_time.hour + 1, minute=0, second=0, microsecond=0)

            # 离目标时间太近，再加一个周期
            if (target_time - datetime.now()).seconds < ahead_time + 1:
                target_time += timedelta(minutes=time_interval)
            return target_time
        else:
            # 暂时没支持其他单位
            raise ValueError('time_interval doesn\'t end with m')


class ErrorEnum(Enum):
    """错误处理"""

    # Global
    DATABASE_AUTH_FAILED = 100001  # auth database failed
    DATABASE_QUERY_FAILED = 100002  # query exec failed

    # Sp
    REQUEST_PARAM_INVALID = 200001  # param invalid

    def description_dict(self, desc=''):
        """格式化输出错误字典"""
        desc_dict = {'code': self.value}
        if self.value == ErrorEnum.DATABASE_AUTH_FAILED.value:
            desc_dict['message'] = 'Database authorization denied'
        else:
            desc_dict['message'] = desc
        return desc_dict
