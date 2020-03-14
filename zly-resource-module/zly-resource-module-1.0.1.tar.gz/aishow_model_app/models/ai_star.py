# -*- coding: utf-8 -*-
from sqlalchemy import String, Integer, Date, Column, ForeignKey, BigInteger, Float

from aishowapp.ext import db
from aishowapp.models import BaseDef

# 达人列表
class KolList(db.Model, BaseDef):

    __tablename__ = 'kol_list'

    userid = Column(BigInteger, primary_key=True)
    nickname = Column(String(255))
    follower_num = Column(Integer)
    tag = Column(String(255))
    video_count = Column(Integer)
    avg_interaction_15 = Column(Integer)
    age = Column(Integer)
    sex = Column(String(255))

    # 服务器
    Fans_description = Column(String(255))

    #需要增加
    view_link = Column(String(255))
    # 自己

    #页面访问量
    pv = Column(Integer)
    #独立访客
    uv = Column(Integer)
    #
    # tv = Column(String(255))
    #热度
    heat = Column(Integer)

    # word_cloud = Column(String(255))

    c_time = Column(Date)

    ebusines_id = db.relationship("Ebusines", backref='kolList')
    fansattribute_id = db.relationship("FansAttribute", backref='kolList')
    shoppingcart_id = db.relationship("ShoppingCart", backref='kolList')
    phoneageinfo_id = db.relationship("PhoneAgeInfo", backref='kolList')
    region_id = db.relationship("Region", backref='kolList')

# 电商表
class Ebusines(db.Model, BaseDef):
    __tablename__ = 'ebusiness'

    userid = Column(ForeignKey('kol_list.userid', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    datatime = Column(Date)
    goods_category = Column(String(255))
    Commodity_classification = Column(String(255))
    Video_likes = Column(Integer)
    Video_count = Column(Integer)
    Total_browsing = Column(Integer)
    Sales_volume = Column(Integer)
    sell_price = Column(Integer)
    Cargo_link = Column(String(255))

# 粉丝属性
class FansAttribute(db.Model, BaseDef):
    __tablename__ = 'fans_attributes'

    userid = Column(ForeignKey('kol_list.userid', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    avg_play = Column(Float(asdecimal=True))
    avg_like = Column(Float(asdecimal=True))
    avg_comment = Column(Float(asdecimal=True))
    total_video_count = Column(Integer)
    video_count_15 = Column(Integer)
    video_count_30 = Column(Integer)
    total_video_avg_interaction = Column(Float(asdecimal=True))
    avg_interaction_15 = Column(Float(asdecimal=True))
    avg_interaction_30 = Column(Float(asdecimal=True))

# 商品购物车
class ShoppingCart(db.Model, BaseDef):
    __tablename__ = 'shopping_cart'

    userid = Column(ForeignKey('kol_list.userid', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    LE10 = Column(BigInteger)
    GT10LE50 = Column(BigInteger)
    GT50LE100 = Column(BigInteger)
    GT100LE150 = Column(BigInteger)
    GT150LE200 = Column(BigInteger)
    GT200LE300 = Column(BigInteger)
    GT300LE400 = Column(BigInteger)
    GT400LE500 = Column(BigInteger)
    GT500 = Column(BigInteger)

# 手机年龄信息
class PhoneAgeInfo(db.Model, BaseDef):
    __tablename__ = 'phone_age_info'

    userid = Column(ForeignKey('kol_list.userid', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    iPhone = Column(BigInteger)
    OPPO = Column(BigInteger)
    vivo = Column(BigInteger)
    others = Column(BigInteger)
    huawei = Column(BigInteger)
    xiaomi = Column(BigInteger)
    less_18 = Column(BigInteger)
    age_18_25 = Column(BigInteger)
    age_26_32 = Column(BigInteger)
    age_33_39 = Column(BigInteger)
    age_40_46 = Column(BigInteger)
    greater_46 = Column(BigInteger)
    male = Column(BigInteger)
    female = Column(BigInteger)
    one_city = Column(Float(asdecimal=True))
    two_city = Column(Float(asdecimal=True))
    three_city = Column(Float(asdecimal=True))

# 地域
class Region(db.Model, BaseDef):
    __tablename__ = 'region'

    userid = Column(ForeignKey('kol_list.userid', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    qingh = Column(BigInteger)
    heil = Column(BigInteger)
    shangd = Column(BigInteger)
    sic = Column(BigInteger)
    jiangs = Column(BigInteger)
    guiz = Column(BigInteger)
    xingj = Column(BigInteger)
    fuj = Column(BigInteger)
    zhej = Column(BigInteger)
    hub = Column(BigInteger)
    tianj = Column(BigInteger)
    jiangx = Column(BigInteger)
    xiz = Column(BigInteger)
    heilj = Column(BigInteger)
    guangd = Column(BigInteger)
    yunn = Column(BigInteger)
    beij = Column(BigInteger)
    taiw = Column(BigInteger)
    aom = Column(BigInteger)
    guangx = Column(BigInteger)
    shan3x = Column(BigInteger)
    gans = Column(BigInteger)
    heb = Column(BigInteger)
    ningx = Column(BigInteger)
    chongq = Column(BigInteger)
    jil = Column(BigInteger)
    hun = Column(BigInteger)
    neimg = Column(BigInteger)
    anh = Column(BigInteger)
    xiangg = Column(BigInteger)
    shangh = Column(BigInteger)
    shan1x = Column(BigInteger)
    hain = Column(BigInteger)
    liaon = Column(BigInteger)