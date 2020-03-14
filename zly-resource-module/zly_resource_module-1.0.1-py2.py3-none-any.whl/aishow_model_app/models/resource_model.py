# -*- coding: utf-8 -*-
from sqlalchemy import String, Integer, Column, ForeignKey, BigInteger, Float, Boolean

from aishow_model_app.ext import db
from aishow_model_app.models import BaseDef
from config import USE



# 资源总表
class ResourceTable(db.Model,BaseDef):

    # 资源总表

        __tablename__ = 'resource_table'
        __bind_key__ = USE
        id = Column(BigInteger, primary_key=True)
        kol_name = Column(String(128),nullable=False,unique=True)     #达人昵称
        kol_id = Column(String(128),nullable=False,unique=True)        #达人平台ID
        platform = Column(String(128),nullable=False)       #平台
        avatar = Column(String(128),nullable=True)       #头像
        type_datil = Column(String(128),nullable=False)    #合作模式（专场直播，单链直播，直播，短视频，图文链接）
        company = Column(String(128),nullable=True)         #所属公司        BD不可见
        contact_name = Column(String(128),nullable=True)     #联系人         BD不可见
        contact_phone = Column(String(128),nullable=True)     #电话          BD不可见
        fans = Column(Float,nullable=False)                    #粉丝数(万）
        total_sell_money = Column(String(255),nullable=True)   #与麒腾累计带货合作金额
        cooperation_times = Column(Integer,nullable=True)                #合作次数
        # cooperation_times1 = Column(Integer,nullable=True)                #合作次数


        redbook_image_text_links = db.relationship('RedbookImageTextLink', backref='resource_tables')
        douyin_view_exports = db.relationship("DouyinViewExport", backref='resource_tables')
        douyin_special_lives = db.relationship("DouyinSpecialLive", backref='resource_tables')
        douyin_single_chain_lives = db.relationship("DouyinSingleChainLive", backref='resource_tables')
        taobao_lives = db.relationship("TaobaoLive", backref='resource_tables')
        kuai_show_lives = db.relationship("KuaiShouLive", backref='resource_tables')

#抖音达人分类
class DouyinExportClassification(db.Model, BaseDef):

    __tablename__ = 'douyin_export_classification'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    classification_description = Column(String(64),unique=True,)  # 分类描述


#小红书图文链接
class RedbookImageTextLink(db.Model, BaseDef):

    __tablename__ = 'redbook_image_text_link'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True)
    resource_table_id = Column(BigInteger, ForeignKey('resource_table.id',ondelete='CASCADE', onupdate='CASCADE'))  # 资源表ID
    dianzan = Column(Integer, default=0)  # 点赞量级(万）
    redbook_link = Column(String(255), nullable=False, unique=True)  # 链接
    export_city = Column(String(255), nullable=True)  # 达人所在城市
    export_tag = Column(String(128), default=0)  # 达人标签
    brand_partner = Column(Boolean, default=False)  # 是否品牌合作人
    redbook_cost_price = Column(Integer, default=0)  # 成本价   BD不可见


# 麒腾小红书3月报价
class QitengRedbookPrice(db.Model,BaseDef):

    __tablename__ = 'qiteng_redbook_price'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True,autoincrement=True)
    fans_less = Column(Integer, default=0)     #粉丝量级区间最低(万）
    fans_more = Column(Integer, default=0)        #粉丝量级区间最高(万）
    offer_less = Column(Integer, default=0)  # 报价区间最低值      630
    offer_more = Column(Integer, default=0)  # 报价区间最高值      900
    cost_price = Column(Integer, default=0)     #成本价
    remarks = Column(String(255),nullable=True)         #备注
    brand_partner= Column(Boolean, default=False)     #是否品牌合作人
    redbook_image_text_link_id = Column(BigInteger, ForeignKey('redbook_image_text_link.id', ondelete='CASCADE',onupdate='CASCADE'))  # 资源表ID
    redbook_image_text_linkid = db.relationship('RedbookImageTextLink', backref='redbook_image_text_links',uselist=False)


#抖音短视频达人表
class DouyinViewExport(db.Model, BaseDef):

    __tablename__ = 'douyin_view_export'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True,autoincrement=True)
    resource_table_id = Column(BigInteger, ForeignKey('resource_table.id',ondelete='CASCADE', onupdate='CASCADE'))  # 资源表ID
    douyin_export_classification_id = Column(BigInteger,ForeignKey('douyin_export_classification.id',ondelete='CASCADE', onupdate='CASCADE'))  # 类目属性
    export_tag = Column(String(255),nullable=True)  # 达人标签
    introduction = Column(String(255),nullable=True)  # 简介 可能是多个tag标签
    douyin_home_page = Column(String(255),nullable=False,unique=True)  # 抖音主页url
    export_city = Column(String(255),nullable=True)  # 达人所在城市
    cooperation_case = Column(String(255),nullable=True)  # 达人合作过的品牌
    better_sell_goods = Column(String(255),nullable=True)  # 可能是空值，达人销售过较好的商品
    douyin_export_classification = Column(String(255))  # 抖音达人分类
    cooperation_mode = Column(String(255),nullable=False)  # 合作模式
    offer_less = Column(Integer, default=0)  # 报价区间最低值      630
    offer_more = Column(Integer, default=0)  # 报价区间最高值      900
    star_offer = Column(Integer, default=0)  # 星图参考报价最高   3000
    douyin_view_cost_price = Column(Integer, default=0)  # 成本价   BD不可见


#麒腾抖音短视频3月报价
class QitengDouyinViewPrice(db.Model, BaseDef):

    __tablename__ = 'qiteng_douyin_view_price'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    fans_less = Column(Float, default=0)   # 粉丝量级区间最低(万） 1w
    fans_more = Column(Float, default=0)   # 粉丝量级区间最高(万） 2w
    offer_less = Column(Integer, default=0)  # 报价区间最低值      630
    offer_more = Column(Integer, default=0)  # 报价区间最高值      900
    star_offer_less = Column(Integer, default=0)  # 星图参考报价最低   1700
    star_offer_more = Column(Integer, default=0)  # 星图参考报价最低   3000
    estimated_exposure = Column(Float, default=0)  # 预估曝光     100w
    remarks = Column(String(255),nullable=False)  # 备注       30条起作这个价格或下方粉丝量有数量可抵
    douyin_view_export_id = Column(BigInteger, ForeignKey('douyin_view_export.id', ondelete='CASCADE',
                                                               onupdate='CASCADE'))  # 资源表ID
    douyin_view_exportid = db.relationship('DouyinViewExport', backref='douyin_view_exports',uselist=False)


#抖音专场直播
class DouyinSpecialLive(db.Model, BaseDef):

    __tablename__ = 'douyin_special_live'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    resource_table_id = Column(BigInteger, ForeignKey('resource_table.id',ondelete='CASCADE', onupdate='CASCADE'))  # 资源表ID
    export_tag = Column(String(128),nullable=False)  # 达人标签
    special_offer = Column(Integer, default=0)  # 专场报价区间最低值      630
    export_city = Column(String(64),nullable=True)  # 达人所在城市
    cooperation_case = Column(String(255),nullable=True)  # 达人合作过的品牌
    douyin_special_cost_price = Column(Integer, default=0)  # 成本价   BD不可见


#抖音单链直播
class DouyinSingleChainLive(db.Model, BaseDef):

    __tablename__ = 'douyin_single_chain_live'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    resource_table_id = Column(BigInteger, ForeignKey('resource_table.id',ondelete='CASCADE', onupdate='CASCADE'))  # 资源表ID
    douyin_export_classification = Column(String(255),nullable=False)  # 达人适合的类目 抖音大类，可能多个
    Single_chain_offer = Column(Integer, default=0)  # 单链接报价区间      630
    introduction = Column(String(255),nullable=True)  # 简介
    selection_requirements = Column(String(255),nullable=False)  # 选品要求   颜值高，成分好的美妆产品
    live_time = Column(String(64))  # 直播时间,每天\每周N
    remarks = Column(String(255), nullable=True)  # 备注
    douyin_single_cost_price = Column(Integer, default=0)  # 成本价   BD不可见


#淘宝直播
class TaobaoLive(db.Model, BaseDef):

    __tablename__ = 'taobao_live'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    resource_table_id = Column(BigInteger, ForeignKey('resource_table.id',ondelete='CASCADE', onupdate='CASCADE'))  # 资源表ID
    avg_viewing_num = Column(Float,default=0)  # 场均观看/小时
    main_category = db.Column(db.String(64),nullable=False)  # 主营类目
    introduction = Column(String(255), nullable=True)  # 简介
    taobao_offer = Column(Integer,default=0)  #最高
    taobao_cost_price = Column(Integer, default=0)  # 成本价   BD不可见


#麒腾淘宝KOL直播报价
class QitengTaobaoExportLiveOffer(db.Model, BaseDef):

    __tablename__ = 'qiteng_taobao_export_live_offer'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    hierarchy = Column(String(64),nullable=False)  # 层级 优质、腰部、头部、超头部
    avg_viewing_num_less = Column(Float,default=0)  # 场均观看量级低区间最低万
    avg_viewing_num_more = Column(Float,default=0)  # 场均观看量级低 区间最高万
    offer_less = Column(Integer,default=0)  #最低报价
    offer_more = Column(Integer,default=0)  #最高报价
    remarks = Column(String(255), nullable=True)  # 备注
    cost_price = Column(Integer,default=0)  # 成本价   BD不可见
    taobao_live_id = Column(BigInteger, ForeignKey('taobao_live.id', ondelete='CASCADE',
                                                          onupdate='CASCADE'))  # 资源表ID
    taobao_liveid = db.relationship('TaobaoLive', backref='taobao_lives',uselist=False)


# 快手直播
class KuaiShouLive(db.Model, BaseDef):

    __tablename__ = 'kuai_show_live'
    __bind_key__ = USE

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    resource_table_id = Column(BigInteger, ForeignKey('resource_table.id',ondelete='CASCADE', onupdate='CASCADE'))  # 资源表ID
    avg_online_num = Column(Float, default=0)  #单位：平均在线人数(万)
    sell_classification = Column(String(255),nullable=False)  # 可售卖类目
    commission_less = Column(Integer, default=0)   # 佣金最低范围最低，例如10%
    commission_more = Column(Integer, default=0)   # 佣金最高范围最高，例如10%
    attributes = db.Column(db.String(64),nullable=False)  # 属性 带货、刷榜
    kuaishou_offer = db.Column(Integer, default=0)  # 快手报价（单链接）
    kuaishou_cost_price = Column(Integer, default=0)  # 快手成本价   BD不可见
    remarks = Column(String(255),nullable=True)  # 备注


#

    # douyin_view_exports = db.relationship("DouyinViewExport", backref='douyin_export_classification')
