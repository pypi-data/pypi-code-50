# coding=utf-8
from __future__ import unicode_literals, print_function, absolute_import
import traceback
import pandas as pd
import six

from bw import utils
from bw.constant import DATA_TYPE_TICK

from bw.model.fundamental import FundamentalApi

from bw.model.history import HistoryApi

from bw.retrying import retry
from bw.utils import load_to_datetime_str, standard_fields, bwsdklogger

from bw.enum import ADJUST_NONE,ADJUST_PREV,ADJUST_POST


fundamentalapi = FundamentalApi()

historyapi = HistoryApi()

pd.set_option('precision', 4)


def reset_historyapi():
    # historyapi.reset_addr()
    pass


def reset_fundamentalapi():
    fundamentalapi.reset_addr()


def condune_error(func):
    """
    调用尝试
    """

    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            # print('--'*20,e)
            func_name = func.__name__
            bwsdklogger.exception(e)
            dfval = kw.get('df', None)
            if dfval:  # df 参数为true
                return pd.DataFrame([])
            else:
                if func_name in {'get_previous_trading_date', 'get_next_trading_date', }:  # 这两个函数比较特殊
                    return ""
                return []

    return wrapper



def get_fundmental_set():
    
    fset = [
        {"name":"每股经营活动产生的现金流量净额","db":"SHSZADB","collections":"MEIGUJINGYINGHUODONGCHANSHENGDEXIANJINLIULIANGJINE",
"field":"MEIGUJINGYINGHUODONGCHANSHENGDEXIANJINLIULIANGJINE","date1":"10/23/2019 11:21:03","date2":"10/23/2019 11:21:12"},

{"name":"最新户均持股比例","db":"SHSZADB","collections":"ZUIXINGUDONGHUSHU",
"field":"ZUIXINHUJUNCHIGUBILI","date1":"10/23/2019 11:21:15","date2":"10/23/2019 11:21:18"},

{"name":"最新户均持股市值","db":"SHSZADB","collections":"ZUIXINGUDONGHUSHU",
"field":"ZUIXINHUJUNCHIGUSHIZHI","date1":"10/23/2019 11:21:21","date2":"10/23/2019 11:21:24"},

{"name":"上市日期","db":"SHSZADB","collections":"SHANGSHIRIQI",
"field":"SHANGSHIRIQI","date1":"10/23/2019 11:21:48","date2":"10/23/2019 11:21:51"},

{"name":"归属于母公司股东净利润同比增长率","db":"SHSZADB","collections":"GUISHUYUMUGONGSIGUDONGJINGLIRUN",
"field":"GUISHUYUMUGONGSIGUDONGJINGLIRUNZENGZHANGLV","date1":"10/23/2019 11:21:57","date2":"10/23/2019 11:21:54"},

{"name":"上市天数","db":"SHSZADB","collections":"SHANGSHITIANSHU",
"field":"SHANGSHITIANSHU","date1":"10/23/2019 11:22:01","date2":"10/23/2019 11:22:04"},

{"name":"申万三级行业","db":"SHSZADB","collections":"SHENWANHANGYE",
"field":"SHENWANSANJIHANGYE","date1":"10/23/2019 11:22:11","date2":"10/23/2019 11:22:08"},

{"name":"申万一级行业","db":"SHSZADB","collections":"SHENWANHANGYE",
"field":"SHENWANYIJIHANGYE","date1":"10/23/2019 11:22:13","date2":"10/23/2019 11:23:02"},

{"name":"申万行业","db":"SHSZADB","collections":"SHENWANHANGYE",
"field":"SHENWANHANGYE","date1":"10/23/2019 11:22:16","date2":"10/23/2019 11:23:05"},

{"name":"股票市场","db":"SHSZADB","collections":"GUPIAOSHICHANG",
"field":"GUPIAOSHICHANG","date1":"10/23/2019 11:22:18","date2":"10/23/2019 11:23:07"},

{"name":"大宗交易成交价格","db":"SHSZADB","collections":"DAZHONGJIAOYICHENGJIAOJUNXIA",
"field":"DAZHONGJIAOYICHENGJIAOJUNXIA","date1":"10/23/2019 11:22:22","date2":"10/23/2019 11:23:09"},

{"name":"流通B股","db":"SHSZADB","collections":"LIUTONGBGU",
"field":"LIUTONGBGU","date1":"10/23/2019 11:22:24","date2":"10/23/2019 11:23:12"},

{"name":"流通A股","db":"SHSZADB","collections":"LIUTONGAGU",
"field":"LIUTONGAGU","date1":"10/23/2019 11:22:27","date2":"10/23/2019 11:23:14"},

{"name":"申万二级行业","db":"SHSZADB","collections":"SHENWANHANGYE",
"field":"SHENWANERJIHANGYE","date1":"10/23/2019 11:22:30","date2":"10/23/2019 11:23:17"},

{"name":"所属概念","db":"SHSZADB","collections":"SUOSHUGAINIAN",
"field":"SUOSHUGAINIAN","date1":"10/23/2019 11:22:32","date2":"10/23/2019 11:23:21"},

{"name":"预告日期","db":"SHSZADB","collections":"YEJIYUGAORIQI",
"field":"YEJIYUGAORIQI","date1":"10/23/2019 11:22:35","date2":"10/23/2019 11:23:24"},

{"name":"业绩变脸","db":"SHSZADB","collections":"YEJIBIANLIAN",
"field":"YEJIBIANLIAN","date1":"10/23/2019 11:22:37","date2":"10/23/2019 11:23:26"},

{"name":"大宗交易日期","db":"SHSZADB","collections":"DAZONGJIAOYIRIQI",
"field":"DAZONGJIAOYIRIQI","date1":"10/23/2019 11:22:40","date2":"10/23/2019 11:23:29"},

{"name":"市盈率TTM","db":"SHSZADB","collections":"SHIYINGLVTTM",
"field":"SHIYINGLVTTM","date1":"10/23/2019 11:22:43","date2":"10/23/2019 11:23:31"},

{"name":"停牌截止时间","db":"SHSZADB","collections":"TINGPAIRIQIZHUANGTAI",
"field":"TINGPAIJIEZHISHIJIAN","date1":"10/23/2019 11:22:46","date2":"10/23/2019 11:23:38"},

{"name":"停牌开始时间","db":"SHSZADB","collections":"TINGPAIRIQIZHUANGTAI",
"field":"TINGPAIKAISHISHIJIAN","date1":"10/23/2019 11:22:48","date2":"10/23/2019 11:23:35"},

{"name":"停牌日期","db":"SHSZADB","collections":"TINGPAIRIQIZHUANGTAI",
"field":"TINGPAIRIQI","date1":"10/23/2019 11:22:54","date2":"10/23/2019 11:23:41"},

{"name":"上榜原因","db":"SHSZADB","collections":"LONGHUBANGRIQIYUANYIN",
"field":"LONGHUBANGSHANGBANYUANYIN","date1":"10/23/2019 11:22:56","date2":"10/23/2019 11:23:44"},

{"name":"上榜日期","db":"SHSZADB","collections":"LONGHUBANGRIQIYUANYIN",
"field":"LONGHUBANGSHANGBANRIQI","date1":"10/23/2019 11:22:59","date2":"10/23/2019 11:23:46"},

{"name":"存货周转天数","db":"SHSZADB","collections":"CUNHUOZHOUZHUANTIANSHU",
"field":"CUNHUOZHOUZHUANTIANSHU","date1":"11/4/2019 14:09:43","date2":"11/4/2019 14:09:43"},

{"name":"业绩预告净利润变动幅度下限","db":"SHSZADB","collections":"YEJIYUGAOJINESHUJU",
"field":"YEJIYUGAOJINGLIRUNBIANDONGFUDUXIAXIAN","date1":"11/4/2019 14:13:00","date2":"11/4/2019 14:13:00"},

{"name":"业绩预告净利润变动幅度上限","db":"SHSZADB","collections":"YEJIYUGAOJINESHUJU",
"field":"YEJIYUGAOJINGLIRUNBIANDONGFUDUSHANGXIAN","date1":"11/4/2019 14:16:26","date2":"11/4/2019 14:16:26"},

{"name":"业绩预告净利润","db":"SHSZADB","collections":"YEJIYUGAOJINESHUJU",
"field":"YEJIYUGAOJINGLIRUN","date1":"11/4/2019 14:19:04","date2":"11/4/2019 14:19:04"},

{"name":"净资产收益率ROE(摊薄|公布值)","db":"SHSZADB","collections":"JINGZICHANSHOUYILV",
"field":"TANBOJINGZICHANSHOUYILV","date1":"11/4/2019 15:28:03","date2":"11/4/2019 15:28:03"},

{"name":"每股收益EPS(扣除/基本)","db":"SHSZADB","collections":"KOUCHUHOUJIBENMEIGUSHOUYI",
"field":"KOUCHUHOUJIBENMEIGUSHOUYI","date1":"11/4/2019 16:02:06","date2":"11/4/2019 16:02:06"},

{"name":"净利润","db":"SHSZADB","collections":"JINGLIRUN",
"field":"JINGLIRUN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"拆出资金","db":"SHSZADB","collections":"CHAICHUZIJIN",
"field":"CHAICHUZIJIN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"存货","db":"SHSZADB","collections":"CUNHUO",
"field":"CUNHUO","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"非流动资产合计","db":"SHSZADB","collections":"FEILIUDONGZICHANHEJI",
"field":"FEILIUDONGZICHANHEJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"负债合计","db":"SHSZADB","collections":"FUZHAIHEJI",
"field":"FUZHAIHEJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"负债和股东权益合计","db":"SHSZADB","collections":"FUZHAIHEGUDONGQUANYIHEJI",
"field":"FUZHAIHEGUDONGQUANYIHEJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"股东权益合计","db":"SHSZADB","collections":"GUDONGQUANYIHEJI",
"field":"GUDONGQUANYIHEJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"归属于母公司股东净利润","db":"SHSZADB","collections":"GUISHUYUMUGONGSIGUDONGJINGLIRUN",
"field":"GUISHUYUMUGONGSIGUDONGJINGLIRUN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"归属于母公司股东权益合计","db":"SHSZADB","collections":"GUISHUYUMUGONGSIGUDONGQUANYIHEJI",
"field":"GUISHUYUMUGONGSIGUDONGQUANYIHEJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"货币资金","db":"SHSZADB","collections":"HUOBIZIJIN",
"field":"HUOBIZIJIN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"交易性金融资产","db":"SHSZADB","collections":"JIAOYIXINGZIRONGZICHAN",
"field":"JIAOYIXINGZIRONGZICHAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"结算备付金","db":"SHSZADB","collections":"JIESUANBEIFUJIN",
"field":"JIESUANBEIFUJIN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"净资产收益率","db":"SHSZADB","collections":"JINGZICHANSHOUYILV",
"field":"JIAQUANJINGZICHANSHOUYILV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"利润总额","db":"SHSZADB","collections":"LIRUNZONGE",
"field":"LIRUNZONGE","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"利润总额同比增长率","db":"SHSZADB","collections":"LIRUNZONGE",
"field":"LIRUNZONGEZENGZHANGLV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"流动资产合计","db":"SHSZADB","collections":"LIUDONGZICHANHEJI",
"field":"LIUDONGZICHANHEJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"买入返售金融资产","db":"SHSZADB","collections":"MAIRUFANSHOUJINEZICHAN",
"field":"MAIRUFANSHOUJINEZICHAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"每股净资产","db":"SHSZADB","collections":"MEIGUJINGZICHAN",
"field":"MEIGUJINGZICHAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"每股收益","db":"SHSZADB","collections":"JIBENMEIGUSHOUYI",
"field":"JIBENMEIGUSHOUYI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"每股收益增长率","db":"SHSZADB","collections":"JIBENMEIGUSHOUYI",
"field":"JIBENMEIGUSHOUYIZENGZHANGLV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"每股未分配利润","db":"SHSZADB","collections":"MEIGUZIBENYINGYUWEIFENPEILIRUN",
"field":"MEIGUWEIFENPEILIRUN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"每股现金流","db":"SHSZADB","collections":"MEIGUJINGYINGHUODONGCHANSHENGDEXIANJINLIULIANGJINE",
"field":"MEIGUJINGYINGHUODONGCHANSHENGDEXIANJINLIULIANGJINE","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"每股资本公积","db":"SHSZADB","collections":"MEIGUZIBENYINGYUWEIFENPEILIRUN",
"field":"MEIGUZIBENGONGJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"内部应收款","db":"SHSZADB","collections":"NEIBUYINGSHOUKUAN",
"field":"NEIBUYINGSHOUKUAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"其他应收款","db":"SHSZADB","collections":"QITAYINGSHOUKUAN",
"field":"QITAYINGSHOUKUAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"上年同期净利润","db":"SHSZADB","collections":"SHANGNIANTONGQIJINGLIRUN",
"field":"SHANGNIANTONGQIJINGLIRUN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"未分配利润","db":"SHSZADB","collections":"WEIFENPEILIRUN",
"field":"WEIFENPEILIRUN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"销售毛利率","db":"SHSZADB","collections":"XIAOSHOUMAOLILV",
"field":"XIAOSHOUMAOLILV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"业绩预告类型","db":"SHSZADB","collections":"YEJIYUGAOLEIXINGNEIRONGYUANYIN",
"field":"YEJIYUZENGYUJIAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"一般风险准备","db":"SHSZADB","collections":"YIBANFENGXIANZHUNBEI",
"field":"YIBANFENGXIANZHUNBEI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"盈余公积","db":"SHSZADB","collections":"YINGYUGONGJI",
"field":"YINGYUGONGJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业成本","db":"SHSZADB","collections":"YINGYECHENGBEN",
"field":"YINGYECHENGBEN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业成本同比增长率","db":"SHSZADB","collections":"YINGYECHENGBEN",
"field":"YINGYECHENGBENZENGZHANGLV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业收入","db":"SHSZADB","collections":"YINGYESHOURU",
"field":"YINGYESHOURU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业收入同比增长率","db":"SHSZADB","collections":"YINGYESHOURU",
"field":"YINGYESHOURUZENGZHANGLV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业外收入","db":"SHSZADB","collections":"YINGYEWAISHOURU",
"field":"YINGYEWAISHOURU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业外支出","db":"SHSZADB","collections":"YINGYEWAISHOURU",
"field":"YINGYEWAIZHICHU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业总成本","db":"SHSZADB","collections":"YINGYEZONGCHENGBEN",
"field":"YINGYEZONGCHENGBEN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业总成本同比增长率","db":"SHSZADB","collections":"YINGYEZONGCHENGBEN",
"field":"YINGYEZONGCHENGBENZENGZHANGLV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业总收入","db":"SHSZADB","collections":"YINGYEZONGSHOURU",
"field":"YINGYEZONGSHOURU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"营业总收入同比增长率","db":"SHSZADB","collections":"YINGYEZONGSHOURU",
"field":"YINGYEZONGSHOURUZENGZHANGLV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收保费","db":"SHSZADB","collections":"YINGSHOUBAOFEI",
"field":"YINGSHOUBAOFEI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收补贴款","db":"SHSZADB","collections":"YINGSHOUBUTIEKUAN",
"field":"YINGSHOUBUTIEKUAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收出口退税","db":"SHSZADB","collections":"YINGSHOUCHUKOUTUISUI",
"field":"YINGSHOUCHUKOUTUISUI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收分保合同准备金","db":"SHSZADB","collections":"YINGSHOUFENBAOHETONGZHUNBEIJIN",
"field":"YINGSHOUFENBAOHETONGZHUNBEIJIN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收分保账款","db":"SHSZADB","collections":"YINGSHOUFENBAOKUAN",
"field":"YINGSHOUFENBAOKUAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收股利","db":"SHSZADB","collections":"YINGSHOUGULI",
"field":"YINGSHOUGULI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收利息","db":"SHSZADB","collections":"YINGSHOULIXI",
"field":"YINGSHOULIXI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收票据","db":"SHSZADB","collections":"YINGSHOUPIAOJU",
"field":"YINGSHOUPIAOJU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"应收账款","db":"SHSZADB","collections":"YINGSHOUZHANGKUAN",
"field":"YINGSHOUZHANGKUAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预付款项","db":"SHSZADB","collections":"YUFUKUANXIANG",
"field":"YUFUKUANXIANG","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预告净利润","db":"SHSZADB","collections":"YEJIYUGAOJINGLIRUN",
"field":"YEJIYUGAOJINGLIRUN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预告净利润变动幅度","db":"SHSZADB","collections":"YEJIYUGAOJINGLIRUNBIANDONGFUDU",
"field":"YEJIYUGAOJINGLIRUNBIANDONGFUDU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预告净利润上限","db":"SHSZADB","collections":"YEJIYUGAOJINGLIRUNSHANGXIAN",
"field":"YEJIYUGAOJINGLIRUNSHANGXIAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预告净利润下限","db":"SHSZADB","collections":"YEJIYUGAOJINGLIRUNXIAXIAN",
"field":"YEJIYUGAOJINGLIRUNXIAXIAN","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预告每股收益","db":"SHSZADB","collections":"YEJIYUGAOMEIGUSHOUYI",
"field":"YEJIYUGAOMEIGUSHOUYI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"预告每股收益变动幅度","db":"SHSZADB","collections":"YEJIYUGAOMEIGUSHOUYI",
"field":"YEJIYUGAOMEIGUSHOUYIBIANDONGFUDU","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"资本公积","db":"SHSZADB","collections":"ZIBENGONGJI",
"field":"ZIBENGONGJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"资产负债率","db":"SHSZADB","collections":"ZICHANFUZHAILIUDONGLV",
"field":"ZICHANFUZHAILV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"资产总计","db":"SHSZADB","collections":"ZICHANZONGJI",
"field":"ZICHANZONGJI","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"总资产报酬率","db":"SHSZADB","collections":"ZONGZICHANBAOCHOULV",
"field":"ZONGZICHANBAOCHOULV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"总资产净利率","db":"SHSZADB","collections":"ZONGZICHANJINGLILV",
"field":"ZONGZICHANJINGLILV","date1":"11/15/2019 15:10:23","date2":"11/15/2019 15:10:23"},

{"name":"保户储金及投资款净增加额","db":"SHSZADB","collections":"BHCJJTZKJZJE",
"field":"BHCJJTZKJZJE","date1":"12/17/2019 11:11:20","date2":"12/17/2019 11:11:20"},

{"name":"股权激励股东大会公告日期","db":"SHSZADB","collections":"GUQUANJILIGUDONGDAHUIGONGGAORI",
"field":"GUQUANJILIGUDONGDAHUIGONGGAORI","date1":"12/17/2019 11:21:12","date2":"12/17/2019 11:21:12"},

{"name":"营业利润","db":"SHSZADB","collections":"YINGYELIRUN",
"field":"YINGYELIRUN","date1":"12/17/2019 14:34:06","date2":"12/17/2019 14:34:06"},

{"name":"收取利息、手续费及佣金的现金","db":"SHSZADB","collections":"SHOUQULIXICESHI",
"field":"SHOUQULIXICESHI","date1":"12/19/2019 14:15:43","date2":"12/19/2019 14:15:43"},

{"name":"收取利息测试顿号","db":"SHSZADB","collections":"SHOUQULIXICESHI",
"field":"SHOUQULIXICESHI","date1":"12/19/2019 14:37:28","date2":"12/19/2019 14:37:28"}


    ]

    return fset



@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_fundamentals(symbols,  collection ,field,start_date, 
    end_date,limit=1000,  table="SHSZADB", df=False):
    """
    查询基本面财务数据
    """
    fields_str, fields_list = standard_fields(field, letter_upper=True)
    start_date = utils.to_datestr(start_date)
    end_date = utils.to_datestr(end_date)
    data = fundamentalapi.get_fundamentals(symbols=symbols,
                                           start_date=start_date,end_date=end_date, 
                                           field=fields_str,collection=collection,table=table, 
                                           limit=limit)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            fields_list = ['symbol', 'date', 'name','value'] + fields_list
            columns = [x for x in fields_list if x in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_fundamentals_n(table, symbols, end_date, fields=None, filter=None,
                       order_by=None, count=1, df=False):
    """
    查询基本面财务数据,每个股票在end_date的前n条
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=True)
    data = fundamentalapi.get_fundamentals_n(table=table, symbols=symbols,
                                             end_date=end_date,
                                             fields=fields_str,
                                             filter=filter, order_by=order_by,
                                             count=count)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            fields_list = ['symbol', 'pub_date', 'end_date'] + fields_list
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_instruments(symbols=None, exchanges=None, sec_types=None, names=None,
                    skip_suspended=True, skip_st=True, fields=None, df=False):
    """
    查询最新交易标的信息,有基本数据及最新日频数据
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)
    data = fundamentalapi.get_instruments(symbols, exchanges, sec_types, names,
                                          skip_suspended, skip_st, fields_str)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_history_instruments(symbols, fields=None, start_date=None,
                            end_date=None, df=False):
    """
    返回指定的symbols的标的日指标数据
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)

    data = fundamentalapi.get_history_instruments(symbols, fields_str,
                                                  start_date, end_date)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_instrumentinfos(symbols=None, exchanges=None, sec_types=None,
                        names=None, fields=None, df=False):
    """
    查询交易标的基本信息
    如果没有数据的话,返回空列表. 有的话, 返回list[dict]这样的列表. 其中 listed_date, delisted_date 为 datetime 类型
    @:param fields: 可以是 'symbol, sec_type' 这样的字符串, 也可以是 ['symbol', 'sec_type'] 这样的字符list
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)
    data = fundamentalapi.get_instrumentinfos(symbols, exchanges, sec_types,
                                              names, fields)

    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_constituents(index, fields=None, df=False):
    """
    查询指数最新成分股
    返回的list每项是个字典,包含的key值有:
    symbol 股票symbol
    name 名字
    """
    fields_str, fields_list = standard_fields(fields, letter_upper=False)
    data = fundamentalapi.get_constituents(index, fields, df)
    if df:
        data = pd.DataFrame(data)
        if fields_list:
            columns = [field for field in fields_list if field in data.columns]
            data = data[columns]

    return data


# @condune_error
# @retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
# def get_history_constituents(index, start_date=None, end_date=None):
#     """
#     查询指数历史成分股
#     返回的list每项是个字典,包含的key值有:
#     trade_date: 交易日期(datetime类型)
#     constituents: 一个字典. 每个股票的sybol做为key值, weight做为value值
#     """
#     return fundamentalapi.get_history_constituents(index, start_date, end_date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_plates(code):
    """
    查询板块股票列表
    """
    return fundamentalapi.get_plates(code)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_industry(code):
    """
    查询行业股票列表
    """
    return fundamentalapi.get_industry(code)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_concept(code):
    """
    查询概念股票列表
    """

    return fundamentalapi.get_concept(code)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_trading_dates(exchange, start_date, end_date):
    """
    查询交易日列表
    如果指定的市场不存在, 返回空列表. 有值的话,返回 yyyy-mm-dd 格式的列表
    """
    return fundamentalapi.get_trading_dates(exchange, start_date, end_date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_previous_trading_date(exchange, date):
    """
    返回指定日期的上一个交易日
    @:param exchange: 交易市场
    @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
    @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
    """
    return fundamentalapi.get_previous_trading_date(exchange, date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_next_trading_date(exchange, date):
    """
    返回指定日期的下一个交易日
    @:param exchange: 交易市场
    @:param date: 指定日期, 可以是datetime.date 或者 datetime.datetime 类型. 或者是 yyyy-mm-dd 或 yyyymmdd 格式的字符串
    @:return 返回下一交易日, 为 yyyy-mm-dd 格式的字符串, 如果不存在则返回None
    """
    return fundamentalapi.get_next_trading_date(exchange, date)


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_dividend(symbol, start_date, end_date=None, df=False):
    """
    查询分红送配
    """
    data = fundamentalapi.get_dividend(symbol, start_date, end_date)

    if df:
        data = pd.DataFrame(data)

    return data


@condune_error
@retry(pre_func=reset_fundamentalapi, stop_max_attempt_number=5)
def get_continuous_contracts(csymbol, start_date=None, end_date=None):
    """
    获取连续合约
    """
    return fundamentalapi.get_continuous_contracts(csymbol, start_date,
                                                   end_date)


@condune_error
@retry(pre_func=reset_historyapi, stop_max_attempt_number=5)
def history(symbol, frequency, start_time, end_time, fields=None,
            skip_suspended=True, fill_missing=None, 
            adjust=1, df=False):
    """
    查询历史行情
    """
    start_time = load_to_datetime_str(start_time)
    end_time = load_to_datetime_str(end_time)
    # adjust_end_time = load_to_datetime_str(adjust_end_time)
    symbol = symbol.strip()
    frequency = frequency.strip()
    # print("&"*20,start_time,end_time,symbol,frequency)
    if frequency == DATA_TYPE_TICK:
        return historyapi.get_history_ticks(symbols=symbol,
                                            start_time=start_time,
                                            end_time=end_time, fields=fields,
                                            skip_suspended=skip_suspended,
                                            
                                            adjust=adjust,
                                            # adjust_end_time=adjust_end_time,
                                            df=df)

    else:
        return historyapi.get_history_bars(symbol=symbol, frequency=frequency,
                                           start_time=start_time,
                                           end_time=end_time, fields=fields,
                                          
                                           adjust=adjust,
                                        #    adjust_end_time=adjust_end_time,
                                           df=df)


@condune_error
@retry(pre_func=reset_historyapi, stop_max_attempt_number=5)
def history_n(symbol, frequency, count, end_time=None, fields=None,
              skip_suspended=True, fill_missing=None, adjust=ADJUST_PREV,
              adjust_end_time='', df=False):
    """
    查询历史行情
    """
    end_time = load_to_datetime_str(end_time)
    # adjust_end_time = load_to_datetime_str(adjust_end_time)
        
    try:
        symbol = symbol.strip()
        frequency = frequency.strip()

        if frequency == DATA_TYPE_TICK:
            return historyapi.get_history_n_ticks(symbol=symbol, count=count,
                                                end_time=end_time, fields=fields,
                                                
                                                fill_missing=fill_missing,
                                                adjust=adjust,
                                                df=df)

        else:
            return historyapi.get_history_n_bars(symbol=symbol, frequency=frequency,
                                                count=count, end_time=end_time,
                                                fields=fields,
                                                fill_missing=fill_missing,
                                                adjust=adjust,
                                                df=df)

        pass
    except Exception as identifier:
        print('Error occured :',identifier)
        # exit(0)
        pass
                                             
                                        
