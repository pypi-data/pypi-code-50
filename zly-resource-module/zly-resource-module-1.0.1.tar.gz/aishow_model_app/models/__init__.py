# -*- coding: utf-8 -*-
from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from datetime import date, time
from flask_sqlalchemy import Model
from sqlalchemy import DateTime, Numeric, Time, Date
from aishow_model_app.ext import db

class BaseDef(object):

    @classmethod
    def queryToDict(cls, models):
        if (isinstance(models, list)):
            if (isinstance(models[0], Model)):
                lst = []
                for model in models:
                    gen = cls.model_to_dict(model)
                    # print('gen',gen)
                    dit = dict((g[0], g[1]) for g in gen)
                    lst.append(dit)
                return lst
            else:
                res = cls.result_to_dict(models)
                return res
        else:
            if (isinstance(models, Model)):
                gen = cls.model_to_dict(models)
                dit = dict((g[0], g[1]) for g in gen)
                return dit
            else:
                res = dict(zip(models.keys(), models))
                cls.find_datetime(res)
                return res

    # 当结果为result对象列表时，result有key()方法
    @classmethod
    def result_to_dict(cls, results):
        res = [dict(zip(r.keys(), r)) for r in results]
        # 这里r为一个字典，对象传递直接改变字典属性
        for r in res:
            cls.find_datetime(r)
        return res

    @classmethod
    def model_to_dict(cls, model):  # 这段来自于参考资源
        for col in model.__table__.columns:
            # print('model_to_dict',)
            # print(col)
            if isinstance(col.type, DateTime):
                value = cls.convert_datetime(getattr(model, col.name))
            elif isinstance(col.type, Numeric):
                if getattr(model, col.name):
                    # print(getattr(model, col.name))
                    # print(type(getattr(model, col.name)))
                    value = float(getattr(model, col.name))
            else:
                value = getattr(model, col.name)
            yield (col.name, value)

    @classmethod
    def find_datetime(cls, value):
        for v in value:
            if (isinstance(value[v], cdatetime)):
                value[v] = cls.convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改

    @classmethod
    def convert_datetime(cls, value):
        if value:
            if (isinstance(value, (cdatetime, DateTime))):
                return value.strftime("%Y-%m-%d %H:%M:%S")
            elif (isinstance(value, (date, Date))):
                return value.strftime("%Y-%m-%d")
            elif (isinstance(value, (Time, time))):
                return value.strftime("%H:%M:%S")
        else:
            return ""

    def save(self,obj):
        try:
            db.session.add(obj)
            db.session.flush()
            db.session.commit()
        except Exception as e:
            print('save fail',e)


    # def delete(self,obj):
    #     try:
    #         db.session.delete(obj)
    #         db.session.commit()
    #     except Exception as e:
    #         print('save fail',e)

from . import resource_model