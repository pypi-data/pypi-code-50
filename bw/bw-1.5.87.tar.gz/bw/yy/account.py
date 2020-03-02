# coding=utf-8
from typing import Text, Dict

from bw.yy.common import ConnectionStatus, ConnectionAddress,EnumTypeWrapper

from bw.csdk.cpp_sdk import CBar,CQuote,CTick,COrder,CExecRpt,CCash,CPosition,CAccount,CAccountStatus,CParameter,CIndicator

from bw.yy.data import *


ExecType_Unknown = 0
ExecType_New = 1                      #已报
ExecType_DoneForDay = 4               #
ExecType_Canceled = 5                 #已撤销
ExecType_PendingCancel = 6            #待撤销
ExecType_Stopped = 7                  #
ExecType_Rejected = 8                 #已拒绝
ExecType_Suspended = 9                #挂起
ExecType_PendingNew = 10              #待报
ExecType_Calculated = 11              #
ExecType_Expired = 12                 #过期
ExecType_Restated = 13                #
ExecType_PendingReplace = 14          #
ExecType_Trade = 15                   #成交
ExecType_TradeCorrect = 16            #
ExecType_TradeCancel = 17             #
ExecType_OrderStatus = 18             #委托状态
ExecType_CancelRejected = 19          #撤单被拒绝


OrderStatus_Unknown = 0
OrderStatus_New = 1                   #已报
OrderStatus_PartiallyFilled = 2       #部成
OrderStatus_Filled = 3                #已成
OrderStatus_DoneForDay = 4            #
OrderStatus_Canceled = 5              #已撤
OrderStatus_PendingCancel = 6         #待撤
OrderStatus_Stopped = 7               #
OrderStatus_Rejected = 8              #已拒绝
OrderStatus_Suspended = 9             #挂起
OrderStatus_PendingNew = 10           #待报
OrderStatus_Calculated = 11           #
OrderStatus_Expired = 12              #已过期
OrderStatus_AcceptedForBidding = 13   #
OrderStatus_PendingReplace = 14       #

OrderRejectReason_Unknown = 0                           #未知原因
OrderRejectReason_RiskRuleCheckFailed = 1               #不符合风控规则
OrderRejectReason_NoEnoughCash = 2                      #资金不足
OrderRejectReason_NoEnoughPosition = 3                  #仓位不足
OrderRejectReason_IllegalAccountId = 4                  #非法账户ID
OrderRejectReason_IllegalStrategyId = 5                 #非法策略ID
OrderRejectReason_IllegalSymbol = 6                     #非法交易代码
OrderRejectReason_IllegalVolume = 7                     #非法委托量
OrderRejectReason_IllegalPrice = 8                      #非法委托价
OrderRejectReason_AccountDisabled = 10                  #交易账号被禁止交易
OrderRejectReason_AccountDisconnected = 11              #交易账号未连接
OrderRejectReason_AccountLoggedout = 12                 #交易账号未登录
OrderRejectReason_NotInTradingSession = 13              #非交易时段
OrderRejectReason_OrderTypeNotSupported = 14            #委托类型不支持
OrderRejectReason_Throttle = 15                         #流控限制
OrderRejectReason_SymbolSusppended = 16                 #交易代码停牌
OrderRejectReason_Internal = 999                        #内部错误

CancelOrderRejectReason_OrderFinalized = 101            #委托已完成
CancelOrderRejectReason_UnknownOrder = 102              #未知委托
CancelOrderRejectReason_BrokerOption = 103              #柜台设置
CancelOrderRejectReason_AlreadyInPendingCancel = 104    #委托撤销中

OrderSide_Unknown = 0
OrderSide_Buy     = 1    #买入
OrderSide_Sell    = 2    #卖出


OrderType_Unknown = 0
OrderType_Limit   = 1    #限价委托
OrderType_Market  = 2    #市价委托
OrderType_Stop    = 3    #止损止盈委托

OrderDuration_Unknown = 0
OrderDuration_FAK     = 1  #即时成交剩余撤销(fill and kill)
OrderDuration_FOK     = 2  #即时全额成交或撤销(fill or kill)
OrderDuration_GFD     = 3  #当日有效(good for day)
OrderDuration_GFS     = 4  #本节有效(good for section)
OrderDuration_GTD     = 5  #指定日期前有效(goodl till date)
OrderDuration_GTC     = 6  #撤销前有效(good till cancel)
OrderDuration_GFA     = 7  #集合竞价前有效(good for auction)

OrderQualifier_Unknown = 0
OrderQualifier_BOC     = 1  #对方最优价格(best of counterparty)
OrderQualifier_BOP     = 2  #己方最优价格(best of party)
OrderQualifier_B5TC    = 3  #最优五档剩余撤销(best 5 then cancel)
OrderQualifier_B5TL    = 4  #最优五档剩余转限价(best 5 then limit)

OrderStyle_Unknown = 0
OrderStyle_Volume = 1
OrderStyle_Value = 2
OrderStyle_Percent = 3
OrderStyle_TargetVolume = 4
OrderStyle_TargetValue = 5
OrderStyle_TargetPercent = 6

PositionSide_Unknown  = 0
PositionSide_Long     = 1   #多方向
PositionSide_Short    = 2   #空方向

PositionEffect_Unknown        = 0
PositionEffect_Open           = 1     #开仓
PositionEffect_Close          = 2     #平仓,具体语义取决于对应的交易所
PositionEffect_CloseToday     = 3     #平今仓
PositionEffect_CloseYesterday = 4     #平昨仓

CashPositionChangeReason_Unknown = 0
CashPositionChangeReason_Trade   = 1  #交易
CashPositionChangeReason_Inout   = 2  #出入金/出入持仓


# nipasbc
class ExecType(EnumTypeWrapper):
    pass


# nipasbc
class OrderStatus(EnumTypeWrapper):
    pass


# nipasbc
class OrderRejectReason(EnumTypeWrapper):
    pass


# nipasbc
class OrderSide(EnumTypeWrapper):
    pass


# nipasbc
class OrderType(EnumTypeWrapper):
    pass


# nipasbc
class OrderDuration(EnumTypeWrapper):
    pass


# nipasbc
class OrderQualifier(EnumTypeWrapper):
    pass


# nipasbc
class OrderStyle(EnumTypeWrapper):
    pass


# nipasbc
class PositionSide(EnumTypeWrapper):
    pass


# nipasbc
class PositionEffect(EnumTypeWrapper):
    pass


# nipasbc
class CashPositionChangeReason(EnumTypeWrapper):
    pass


#  CBar,CQuote,CTick,COrder,CExecRpt,CCash,CPosition,CAccount,CAccountStatus,CParameter,CIndicator

# 委托定义
# nipasbc
class Order(object):
    # # 策略ID
    # strategy_id = ... # type: Text
    # # 账号ID
    # account_id = ... # type: Text
    # # 账户登录名
    # account_name = ... # type: Text

    # # 委托客户端ID
    # cl_ord_id = ... # type: Text
    # # 委托柜台ID
    # order_id = ... # type: Text
    # # 委托交易所ID
    # ex_ord_id = ... # type: Text

    # # symbol
    # symbol = ... # type: Text
    # # 买卖方向，取值参考enum OrderSide
    # side = ... # type: int
    # # 开平标志，取值参考enum PositionEffect
    # position_effect = ... # type: int
    # # 持仓方向，取值参考enum PositionSide
    # position_side = ... # type: int

    # # 委托类型，取值参考enum OrderType
    # order_type = ... # type: int
    # # 委托时间属性，取值参考enum OrderDuration
    # order_duration = ... # type: int
    # # 委托成交属性，取值参考enum OrderQualifier
    # order_qualifier = ... # type: int
    # # 委托来源，取值参考enum OrderSrc
    # order_src = ... # type: int

    # # 委托状态，取值参考enum OrderStatus
    # status = ... # type: int
    # # 委托拒绝原因，取值参考enum OrderRejectReason
    # ord_rej_reason = ... # type: int
    # # 委托拒绝原因描述
    # ord_rej_reason_detail = ... # type: int

    # # 委托价格
    # price = ... # type: float
    # # 委托止损/止盈触发价格
    # stop_price = ... # type: float

    # # 委托风格，取值参考 enum OrderStyle
    # order_style = ... # type: int
    # # 委托量
    # volume = ... # type: int
    # # 委托额
    # value = ... # type: float
    # # 委托百分比
    # percent = ... # type: float
    # # 委托目标量
    # target_volume = ... # type: int
    # # 委托目标额
    # target_value = ... # type: float
    # # 委托目标百分比
    # target_percent = ... # type: float

    # # 已成量
    # filled_volume = ... # type: int
    # # 已成均价
    # filled_vwap = ... # type: float
    # # 已成金额
    # filled_amount = ... # type: float
    # # 已成手续费
    # filled_commission = ... # type: float

    # # 委托创建时间
    # created_at = ... # type: int
    # # 委托更新时间
    # updated_at = ... # type: int
    
    def __init__(self,):
        pass

    # def __init__(self,ord):
    #     self.strategy_id =  ord.strategy_id #///策略ID  strategy_id #///策略ID  
    #     self.account_id = ord.account_id #///账号ID   account_id #///账号ID   
    #     self.account_name = ord.account_name #///账户登录account_name #///账户登录
    #     self.cl_ord_id = ord.cl_ord_id #///委托客户端cl_ord_id #///委托客户端
    #     self.order_id = ord.order_id #///委托柜台ID order_id #///委托柜台ID 
    #     self.ex_ord_id = ord.ex_ord_id #///委托交易所ex_ord_id #///委托交易所
    #     self.symbol = ord.symbol #///symbol       symbol #///symbol       
    #     self.side = ord.side #
    #     self.position_effect = ord.position_effect #
    #     self.position_side = ord.position_side #
    #     self.order_type = ord.order_type #
    #     self.order_duration = ord.order_duration #
    #     self.order_qualifier = ord.order_qualifier #
    #     self.order_src = ord.order_src #
    #     self.status = ord.status #
    #     self.ord_rej_reason = ord.ord_rej_reason #
    #     self.ord_rej_reason_detail = ord.ord_rej_reason_detail #
    #     self.price = ord.price #
    #     self.stop_price = ord.stop_price #
    #     self.order_style = ord.order_style #
    #     self.volume = ord.volume #
    #     self.value = ord.value #
    #     self.percent = ord.percent #
    #     self.target_volume = ord.target_volume #
    #     self.target_value = ord.target_value #
    #     self.target_percent = ord.target_percent #
    #     self.filled_volume = ord.filled_volume #
    #     self.filled_vwap = ord.filled_vwap #
    #     self.filled_amount = ord.filled_amount #
    #     self.filled_commission = ord.filled_commission #
    #     self.created_at = ord.created_at #
    #     self.updated_at = ord.updated_at #
    #     pass

    def FromFmt(self,ord):
        self.strategy_id =  ord.strategy_id #///策略ID  strategy_id #///策略ID  
        self.account_id = ord.account_id #///账号ID   account_id #///账号ID   
        self.account_name = ord.account_name #///账户登录account_name #///账户登录
        self.cl_ord_id = ord.cl_ord_id #///委托客户端cl_ord_id #///委托客户端
        self.order_id = ord.order_id #///委托柜台ID order_id #///委托柜台ID 
        self.ex_ord_id = ord.ex_ord_id #///委托交易所ex_ord_id #///委托交易所
        self.symbol = ord.symbol #///symbol       symbol #///symbol       
        self.side = ord.side #
        self.position_effect = ord.position_effect #
        self.position_side = ord.position_side #
        self.order_type = ord.order_type #
        self.order_duration = ord.order_duration #
        self.order_qualifier = ord.order_qualifier #
        self.order_src = ord.order_src #
        self.status = ord.status #
        self.ord_rej_reason = ord.ord_rej_reason #
        self.ord_rej_reason_detail = ord.ord_rej_reason_detail #
        self.price = ord.price #
        self.stop_price = ord.stop_price #
        self.order_style = ord.order_style #
        self.volume = ord.volume #
        self.value = ord.value #
        self.percent = ord.percent #
        self.target_volume = ord.target_volume #
        self.target_value = ord.target_value #
        self.target_percent = ord.target_percent #
        self.filled_volume = ord.filled_volume #
        self.filled_vwap = ord.filled_vwap #
        self.filled_amount = ord.filled_amount #
        self.filled_commission = ord.filled_commission #
        self.created_at = Timestamp(ord.created_at) #
        self.updated_at = Timestamp(ord.updated_at) #
        pass

# # 委托集合
# # nipasbc
# class Orders(object):
#     data = ... # type: List[Order]
#     is_combined = ... # type: int
#     properties = ... # type: Dict[Text, Text]


# 委托执行回报定义
# nipasbc
class ExecRpt(object):
    # # 策略ID
    # strategy_id = ... # type: Text
    # # 账号ID
    # account_id = ... # type: Text
    # # 账户登录名
    # account_name = ... # type: Text

    # # 委托客户端ID
    # cl_ord_id = ... # type: Text
    # # 委托柜台ID
    # order_id = ... # type: Text
    # # 委托回报ID
    # exec_id = ... # type: Text

    # symbol = ... # type: Text

    # # 开平标志，取值参考enum PositionEffect
    # position_effect = ... # type: int
    # # 买卖方向，取值参考enum OrderSide
    # side = ... # type: int
    # # 委托拒绝原因，取值参考enum OrderRejectReason
    # ord_rej_reason = ... # type: int
    # # 委托拒绝原因描述
    # ord_rej_reason_detail = ... # type: Text
    # # 执行回报类型, 取值参考enum ExecType
    # exec_type = ... # type: int

    # # 委托成交价格
    # price = ... # type: float
    # # 委托成交量
    # volume = ... # type: int
    # # 委托成交金额
    # amount = ... # type: float
    # # 委托成交手续费
    # commission = ... # type: float

    # const = ... # type: float

    # # 回报创建时间
    # created_at = ... # type: int

    def FromFmt(self,exerpt):
        self.strategy_id=exerpt.strategy_id#                  //策略ID                                                                                                        
        self.account_id=exerpt.account_id#                   //账号ID                                                       
        self.account_name=exerpt.account_name#               //账户登录名                                                                                                    
        self.cl_ord_id=exerpt.cl_ord_id#                    //委托客户端ID                                                                                                  
        self.order_id=exerpt.order_id#                     //委托柜台ID                                                                                                    
        self.exec_id=exerpt.exec_id#                      //委托回报ID                                                                                                    
        self.symbol=exerpt.symbol#                   //symbol                                                                                                        
        self.position_effect=exerpt.position_effect#                      //开平标志，取值参考enum PositionEffect                                                                         
        self.side=exerpt.side#                                 //买卖方向，取值参考enum OrderSide                                                                              
        self.ord_rej_reason=exerpt.ord_rej_reason#                       //委托拒绝原因，取值参考enum OrderRejectReason                                                                  
        self.ord_rej_reason_detail=exerpt.ord_rej_reason_detail#      //委托拒绝原因描述                                                                                              
        self.exec_type=exerpt.exec_type#                            //执行回报类型, 取值参考enum ExecType                                                                           
        self.price=exerpt.price#                                //委托成交价格                                                                                                  
        self.volume=exerpt.volume#                               //委托成交量                                                                                                    
        self.amount=exerpt.amount#                               //委托成交金额                                                                                                  
        self.commission=exerpt.commission#                           //委托成交手续费                                                                                                
        self.cost=exerpt.cost#                                 //委托成交成本金额  
        # self.created_at=exerpt.created_at#                           //回报创建时间
        self.created_at = Timestamp(exerpt.created_at) #
       
        pass




# 成交回报集合
# nipasbc
class ExecRpts(object):
    data = ... # type: List[ExecRpt]


# 资金定义
# nipasbc

class Cash(object):
    # account_id=...#                        //账号ID               
    # account_name=...#                    //账户登录名                                                                   
    # currency=...#                                  //币种                                                                         
    # nav=...#                                        //净值(const cum_inout + cum_pnl + fpnl - cum_commission)                            
    # pnl=...#                                        //净收益(const nav-cum_inout)                                                        
    # fpnl=...#                                       //浮动盈亏(const sum(each position fpnl))                                            
    # frozen=...#                                     //持仓占用资金                                                                 
    # order_frozen=...#                               //挂单冻结资金                                                                 
    # available=...#                                  //可用资金      
    # balance=...#                                    //资金余额                                                                     
    # cum_inout=...#                                  //累计出入金                                                                   
    # cum_trade=...#                                  //累计交易额                                                                   
    # cum_pnl=...#                                    //累计平仓收益(const 没扣除手续费)                                                   
    # cum_commission=...#                             //累计手续费                                                                   
    # last_trade=...#                                 //上一次交易额                                                                 
    # last_pnl=...#                                   //上一次收益                                                                   
    # last_commission=...#                            //上一次手续费                                                                 
    # last_inout=...#                                 //上一次出入金                                                                 
    # change_reason=...#                              //资金变更原因，取值参考enum CashPositionChangeReason                          
    # change_event_id=...#                    //触发资金变更事件的ID     
    # created_at=...#                                 //资金初始时间
    # updated_at=...#                                 //资金变更时间
    def __init__(self,c):
        self.account_id=c.account_id#                        //账号ID               
        self.account_name=c.account_name#                    //账户登录名                                                                   
        self.currency=c.currency#                                  //币种                                                                         
        self.nav=c.nav#                                        //净值(const cum_inout + cum_pnl + fpnl - cum_commission)                            
        self.pnl=c.pnl#                                        //净收益(const nav-cum_inout)                                                        
        self.fpnl=c.fpnl#                                       //浮动盈亏(const sum(each position fpnl))                                            
        self.frozen=c.frozen#                                     //持仓占用资金                                                                 
        self.order_frozen=c.order_frozen#                               //挂单冻结资金                                                                 
        self.available=c.available#                                  //可用资金      
        self.balance=c.balance#                                    //资金余额                                                                     
        self.cum_inout=c.cum_inout#                                  //累计出入金                                                                   
        self.cum_trade=c.cum_trade#                                  //累计交易额                                                                   
        self.cum_pnl=c.cum_pnl#                                    //累计平仓收益(const 没扣除手续费)                                                   
        self.cum_commission=c.cum_commission#                             //累计手续费                                                                   
        self.last_trade=c.last_trade#                                 //上一次交易额                                                                 
        self.last_pnl=c.last_pnl#                                   //上一次收益                                                                   
        self.last_commission=c.last_commission#                            //上一次手续费                                                                 
        self.last_inout=c.last_inout#                                 //上一次出入金                                                                 
        self.change_reason=c.change_reason#                              //资金变更原因，取值参考enum CashPositionChangeReason                          
        self.change_event_id=c.change_event_id#                    //触发资金变更事件的ID     
        # self.created_at=c.created_at#                                 //资金初始时间
        # self.updated_at=c.updated_at#                                 //资金变更时间
        
        self.created_at = Timestamp(c.created_at) #
        self.updated_at = Timestamp(c.updated_at) #
        pass
    def FromFmt(self,c):
        self.account_id=c.account_id#                        //账号ID               
        self.account_name=c.account_name#                    //账户登录名                                                                   
        self.currency=c.currency#                                  //币种                                                                         
        self.nav=c.nav#                                        //净值(const cum_inout + cum_pnl + fpnl - cum_commission)                            
        self.pnl=c.pnl#                                        //净收益(const nav-cum_inout)                                                        
        self.fpnl=c.fpnl#                                       //浮动盈亏(const sum(each position fpnl))                                            
        self.frozen=c.frozen#                                     //持仓占用资金                                                                 
        self.order_frozen=c.order_frozen#                               //挂单冻结资金                                                                 
        self.available=c.available#                                  //可用资金      
        self.balance=c.balance#                                    //资金余额                                                                     
        self.cum_inout=c.cum_inout#                                  //累计出入金                                                                   
        self.cum_trade=c.cum_trade#                                  //累计交易额                                                                   
        self.cum_pnl=c.cum_pnl#                                    //累计平仓收益(const 没扣除手续费)                                                   
        self.cum_commission=c.cum_commission#                             //累计手续费                                                                   
        self.last_trade=c.last_trade#                                 //上一次交易额                                                                 
        self.last_pnl=c.last_pnl#                                   //上一次收益                                                                   
        self.last_commission=c.last_commission#                            //上一次手续费                                                                 
        self.last_inout=c.last_inout#                                 //上一次出入金                                                                 
        self.change_reason=c.change_reason#                              //资金变更原因，取值参考enum CashPositionChangeReason                          
        self.change_event_id=c.change_event_id#                    //触发资金变更事件的ID     
        # self.created_at=c.created_at#                                 //资金初始时间
        # self.updated_at=c.updated_at#                                 //资金变更时间
        
        self.created_at = Timestamp(c.created_at) #
        self.updated_at = Timestamp(c.updated_at) #


# 资金集合
# nipasbc
class Cashes(object):
    data = ... # type: List[Cash]


# 持仓定义
# nipasbc
class Position(object):
    # # 账号ID
    # account_id = ... # type: Text
    # # 账户登录名
    # account_name = ... # type: Text

    # symbol = ... # type: Text
    # # 持仓方向，取值参考enum PositionSide
    # side = ... # type: int
    # # 总持仓量 昨持仓量(volume-volume_today)
    # volume = ... # type: int
    # # 今日持仓量
    # volume_today = ... # type: int
    # # 持仓均价
    # vwap = ... # type: float
    # # 持仓额(volume*vwap*multiplier)
    # amount = ... # type: float

    # # 当前行情价格
    # price = ... # type: float
    # # 持仓浮动盈亏((price-vwap)*volume*multiplier)
    # fpnl = ... # type: float
    # # 持仓成本(vwap*volume*multiplier*margin_ratio)
    # cost = ... # type: float
    # # 挂单冻结仓位
    # order_frozen = ... # type: int
    # # 挂单冻结今仓仓位
    # order_frozen_today = ... # type: int
    # # 可平总仓位(volume-order_frozen) 可平昨仓位(available-available_today)
    # available = ... # type: int
    # # 可平今仓位(volume_today-order_frozen_today)
    # available_today = ... # type: int

    # # 上一次成交价
    # last_price = ... # type: float
    # # 上一次成交量
    # last_volume = ... # type: int
    # # 上一次出入持仓量
    # last_inout = ... # type: int
    # # 仓位变更原因，取值参考enum CashPositionChangeReason
    # change_reason = ... # type: int
    # # 触发资金变更事件的ID
    # change_event_id = ... # type: Text

    # 持仓区间有分红配送
    has_dividend = ... # type: int

    # 建仓时间
    created_at = ... # type: int
    # 仓位变更时间
    updated_at = ... # type: int
    def __init__(self,pos):
        self.account_id=pos.account_id#              //账号ID                                       
        self.account_name=pos.account_name#          //账户登录名                                                                                       
        self.symbol=pos.symbol#              //symbol                                       
        self.side=pos.side#                            //持仓方向，取值参考enum PositionSide          
        self.volume=pos.volume#                          //总持仓量=pos.//总持仓量# 昨持仓量(const volume-volume_today)                                                          
        self.volume_today=pos.volume_today#                    //今日持仓量                                                                                       
        self.vwap=pos.vwap#                            //持仓均价                                                                                         
        self.amount=pos.amount#                          //持仓额(const volume*vwap*multiplier)                                                                   
        self.price=pos.price#                           //当前行情价格                                                                                     
        self.fpnl=pos.fpnl#                            //持仓浮动盈亏(const (price-vwap)*volume*multiplier)                                                     
        self.cost=pos.cost#                            //持仓成本(const vwap*volume*multiplier*margin_ratio)                                                    
        self.order_frozen=pos.order_frozen#                    //挂单冻结仓位                                                                                     
        self.order_frozen_today=pos.order_frozen_today#              //挂单冻结今仓仓位                                                                                 
        self.available=pos.available#                       //可平总仓位(const volume-order_frozen)=pos.//可平总仓位(const volume-order_frozen)# 可平昨仓位(const available-available_today)                           
        self.available_today=pos.available_today#                 //可平今仓位(const volume_today-order_frozen_today)                                                      
        self.last_price=pos.last_price#                      //上一次成交价                                                                                     
        self.last_volume=pos.last_volume#                     //上一次成交量                                                                                     
        self.last_inout=pos.last_inout#                      //上一次出入持仓量                                                                                 
        self.change_reason=pos.change_reason#                   //仓位变更原因，取值参考enum CashPositionChangeReason                                              
        self.change_event_id=pos.change_event_id#         //触发资金变更事件的ID                                                                             
        self.has_dividend=pos.has_dividend#                    //持仓区间有分红配送   
        # self.created_at=pos.created_at#                      //建仓时间
        # self.updated_at=pos.updated_at#                      //仓位变更时间
        
        self.created_at = Timestamp(pos.created_at) #
        self.updated_at = Timestamp(pos.updated_at) #
        pass
    def FromFmt(self,pos):
        self.account_id=pos.account_id#              //账号ID                                       
        self.account_name=pos.account_name#          //账户登录名                                                                                       
        self.symbol=pos.symbol#              //symbol                                       
        self.side=pos.side#                            //持仓方向，取值参考enum PositionSide          
        self.volume=pos.volume#                          //总持仓量=pos.//总持仓量# 昨持仓量(const volume-volume_today)                                                          
        self.volume_today=pos.volume_today#                    //今日持仓量                                                                                       
        self.vwap=pos.vwap#                            //持仓均价                                                                                         
        self.amount=pos.amount#                          //持仓额(const volume*vwap*multiplier)                                                                   
        self.price=pos.price#                           //当前行情价格                                                                                     
        self.fpnl=pos.fpnl#                            //持仓浮动盈亏(const (price-vwap)*volume*multiplier)                                                     
        self.cost=pos.cost#                            //持仓成本(const vwap*volume*multiplier*margin_ratio)                                                    
        self.order_frozen=pos.order_frozen#                    //挂单冻结仓位                                                                                     
        self.order_frozen_today=pos.order_frozen_today#              //挂单冻结今仓仓位                                                                                 
        self.available=pos.available#                       //可平总仓位(const volume-order_frozen)=pos.//可平总仓位(const volume-order_frozen)# 可平昨仓位(const available-available_today)                           
        self.available_today=pos.available_today#                 //可平今仓位(const volume_today-order_frozen_today)                                                      
        self.last_price=pos.last_price#                      //上一次成交价                                                                                     
        self.last_volume=pos.last_volume#                     //上一次成交量                                                                                     
        self.last_inout=pos.last_inout#                      //上一次出入持仓量                                                                                 
        self.change_reason=pos.change_reason#                   //仓位变更原因，取值参考enum CashPositionChangeReason                                              
        self.change_event_id=pos.change_event_id#         //触发资金变更事件的ID                                                                             
        self.has_dividend=pos.has_dividend#                    //持仓区间有分红配送   
        # self.created_at=pos.created_at#                      //建仓时间
        # self.updated_at=pos.updated_at#                      //仓位变更时间
        self.created_at = Timestamp(pos.created_at) #
        self.updated_at = Timestamp(pos.updated_at) #
        pass


# 持仓集合
# nipasbc
class Positions(object):
    data = ... # type: List[Position]


# nipasbc
class Account(object):
    # account_id = ... # type: Text
    # account_name = ... # type: Text
    # title = ... # type: Text
    # intro = ... # type: Text
    # comment = ... # type: Text

    # created_at = ... # type: int
    # updated_at = ... # type: int
    def __init__(self,act):
        self.account_id = act .account_id # type: Text
        self.account_name = act.account_id # type: Text
        self.title = act.account_id # type: Text
        self.intro = act.account_id # type: Text
        self.comment = act.account_id # type: Text

        self.created_at = act.account_id # type: int
        self.updated_at = act.account_id # type: int


# nipasbc
class Accounts(object):
    data = ... # type: List[Account]


# nipasbc
class AccountStatus(object):
    account_id = ... # type: Text
    account_name = ... # type: Text
    status = ... # type: ConnectionStatus


# nipasbc
class AccountStatuses(object):
    data = ... # type: List[AccountStatus]

