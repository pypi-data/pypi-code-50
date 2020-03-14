# -*- coding: utf-8 -*-

from aishowapp.ext import db
from aishowapp.models import BaseDef

# 达人
class Mcn(db.Model,BaseDef):
    """
    达人
    """
    __tablename__ = 'mcn'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    mcn_id = db.Column(db.String(64))
    broker = db.Column(db.Integer, db.ForeignKey('users.id'))  #中间人
    nickname = db.Column(db.String(64))
    name = db.Column(db.String(64))
    # platform = db.Column(db.Enum(
    #     '快手', '抖音', '淘宝', '西瓜', 'bilibili', '美拍', '秒拍', '新浪微博'
    # ),  nullable=False,default=None)
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))  #平台
    way = db.Column(db.String(64))     #方式
    sex = db.Column(db.Boolean, default=False)
    fans = db.Column(db.Integer)    #粉丝
    viewers = db.Column(db.Integer)   #观看者
    Online = db.Column(db.Float) #在线时长
    region = db.Column(db.String(64)) #地区
    commission = db.Column(db.Float) # 佣金
    attributes = db.Column(db.String(64))   #属性
    price = db.Column(db.Float)     # 价格
    invoicing = db.Column(db.Boolean, default=False)  #是否开票
    live_url = db.Column(db.String(128))  #直播地址
    brand = db.Column(db.String(64))      #品牌
    data = db.Column(db.String(64))       #时间
    gent = db.Column(db.Integer, db.ForeignKey('users.id'))  # 经纪人


# 平台
class PlatForm(db.Model,BaseDef):
    """
    平台
    """
    __tablename__ = 'platform'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64))
    Mcns = db.relationship("Mcn", backref='platform')