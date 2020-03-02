from typing import Text, Dict,List


# nipasbc
class SecurityType(object):
    SecurityType_Unknown = 0  # type: int
    SecurityType_Stock   = 1  # type: int
    SecurityType_Fund    = 2  # type: int
    SecurityType_Index   = 3  # type: int
    SecurityType_Future  = 4  # type: int
    SecurityType_Option  = 5  # type: int

# nipasbc
class Quote(object):
    # bid_p = ...  # type: float
    # bid_v = ...  # type: int
    # ask_p = ...  # type: float
    # ask_v = ...  # type: int
    def __init__(self, bid_p:float=0, bid_v:int=0, ask_p:float=0, ask_v:int=0): ...
    def __init__(self):
        self.bid_price=0#                            ///本档委买价
        self.bid_volume=0#                           ///本档委买量
        self.ask_price=0#                            ///本档委卖价
        self.ask_volume=0#
          
    def __init__(self,q):
        self.bid_price=q.    bid_price#                            ///本档委买价
        self.bid_volume=q.   bid_volume#                           ///本档委买量
        self.ask_price=q.    ask_price#                            ///本档委卖价
        self.ask_volume=q.   ask_volume#                           ///本档委卖量
        pass
    def FromFmt(self,q):
        self.bid_price=q.    bid_price#                            ///本档委买价
        self.bid_volume=q.   bid_volume#                           ///本档委买量
        self.ask_price=q.    ask_price#                            ///本档委卖价
        self.ask_volume=q.   ask_volume#                           ///本档委卖量
        pass

# nipasbc
class OrderBook(object):
    symbol = ... # type: Text
    quotes = ... # type: List[Quote]
    created_at = ... # type: int
    pass

    # def __init__(self, symbol:Text=0, quotes:List[Quote]=None, created_at:int=None): ...

# nipasbc
class OrderBooks(object):
    data = ... # type: List[OrderBook]
    pass

    # def __init__(self, data:List[OrderBook]): ...

# nipasbc
class Trade(object):
    # symbol = ... # type: Text
    # price = ... # type: float
    # last_volume = ... # type: int
    # last_amount = ... # type: float
    # cum_volume = ... # type: int
    # cum_amount = ... # type: float
    # trade_type = ... # type: int
    # created_at = ... # type: int

    def __init__(self,trade_):
        self.strategy_id=trade_.strategy_id#         //策略ID                                                    
        self.account_id=trade_.account_id#          //账号ID                            
        self.account_name=trade_.account_name#        //账户登录名                                                  
        self.cl_ord_id=trade_.cl_ord_id#          //委托客户端ID                                                 
        self.order_id=trade_.order_id#           //委托柜台ID                                                  
        self.exec_id=trade_.exec_id#           //委托回报ID                                                  
        self.symbol=trade_.symbol#          //symbol                                                    
        self.position_effect=trade_.position_effect#           //开平标志，取值参考enum PositionEffect                                     
        self.side=trade_.side#                 //买卖方向，取值参考enum OrderSide                                       
        self.ord_rej_reason=trade_.ord_rej_reason#            //委托拒绝原因，取值参考enum OrderRejectReason                                 
        self.ord_rej_reason_detail=trade_.ord_rej_reason_detail#   //委托拒绝原因描述                                               
        self.exec_type=trade_.exec_type#              //执行回报类型, 取值参考enum ExecType                                      
        self.price=trade_.price#                //委托成交价格                                                 
        self.volume=trade_.volume#                //委托成交量                                                  
        self.amount=trade_.amount#                //委托成交金额                                                 
        self.commission=trade_.commission#              //委托成交手续费                                                
        self.cost=trade_.cost#                 //委托成交成本金额 
        self.created_at=trade_.created_at#              //回报创建时间
    # def __init__(self, symbol:Text='', price:float=0, last_volume:int=0, last_amount:float=0,
    #              cum_volume:int=0, cum_amount:float=0, trade_type:int=0,
    #              created_at:int=None):...

# nipasbc
class Trades(object):
    data = ... # type: List[Trade]
    pass
    # def __init__(self, data:List[Trade]): ...

# nipasbc
class Tick(object):
    # symbol = ... # type: Text

    # open = ... # type: float
    # high = ... # type: float
    # low = ... # type: float
    # price = ... # type: float

    # quotes = ... # type: List[Quote]

    # cum_volume = ... # type: int
    # cum_amount = ... # type: float
    # cum_position = ... # type: int
    # last_amount = ... # type: float
    # last_volume = ... # type: int
    # trade_type = ... # type: int

    # created_at = ... # type: int
    def __init__(self):
        pass
    
    def __init__(self, symbol:Text='', open:float=0, high:float=0, low:float=0, price:float=0,
                 quotes:List[Quote]=None, cum_volume:int=0, cum_amount:float=0, cum_position:int=0,
                 last_amount:float=0, last_volume:int=0, trade_type:int=0, created_at:int=None): ...

    def __init__(self,t):
        self.symbol = t.symbol#
        self.created_at =  Timestamp(t.created_at)#               ///<utc时间，精确到毫秒--期货等
        self.price = t.price#                    ///<最新价
        self.open = t.open#                     ///<开盘价
        self.high = t.high#                     ///<最高价
        self.low = t.low#                      ///<最低价
        self.cum_volume = t.cum_volume#               ///<成交总量
        self.cum_amount = t.cum_amount#               ///<成交总金额/最新成交额,累计值
        self.cum_position = t.cum_position#             ///<合约持仓量(const 期),累计值
        self.last_amount = t.last_amount#              ///<瞬时成交额
        self.last_volume = t.last_volume#              ///<瞬时成交量
        self.trade_type = t.trade_type#               ///(const 保留)交易类型,对应多开,多平等类型
        
        self.quotes =[Quote(item) for item in t.quotes]    
        
        pass
    def FromFmt(self,t):
        self.symbol = t.symbol#
        self.created_at =  Timestamp(t.created_at)#               ///<utc时间，精确到毫秒--期货等
        self.price = t.price#                    ///<最新价
        self.open = t.open#                     ///<开盘价
        self.high = t.high#                     ///<最高价
        self.low = t.low#                      ///<最低价
        self.cum_volume = t.cum_volume#               ///<成交总量
        self.cum_amount = t.cum_amount#               ///<成交总金额/最新成交额,累计值
        self.cum_position = t.cum_position#             ///<合约持仓量(const 期),累计值
        self.last_amount = t.last_amount#              ///<瞬时成交额
        self.last_volume = t.last_volume#              ///<瞬时成交量
        self.trade_type = t.trade_type#               ///(const 保留)交易类型,对应多开,多平等类型
        
        self.quotes =[Quote(item) for item in t.quotes]  
        pass


    # def __init__(self, data:List[Tick]): ...

class Timestamp(object):
    # seconds=0
    # nanos=0
    def __init__(self):
        self.seconds = 0
        self.nanos = 0
        pass
    #double
    def __init__(self,t):
        if isinstance(t,float):
            self.seconds = int(t)
            self.nanos = int(t*1000)%1000*1000000000

        elif isinstance(t,int): #milisec
            self.seconds = int(t)/1000
            self.nanos = int(t)%1000*1000000000

        else:
            self.seconds = 0
            self.nanos = 0
        pass


# nipasbc
class Bar(object):
    # symbol = ... # type: Text
    # frequency = ... # type: Text

    # open = ... # type: float
    # high = ... # type: float
    # low = ... # type: float
    # close = ... # type: float
    # volume = ... # type: int
    # amount = ... # type: float
    # position = ... # type: int
    # pre_close = ... # type: float

    # bob = ... # type: int
    # eob = ... # type: int

    # def __init__(self,b):
    #     self.symbol = b.symbol#		        ///symbol
    #     self.bob = Timestamp(b.bob)#                     ///bar的开始时间
    #     self.eob = Timestamp(b.eob)#                        ///bar的结束时间
    #     self.open = b.open#                        ///<开盘价
    #     self.close = b.close#                        ///<收盘价
    #     self.high = b.high#                       ///<最高价
    #     self.low = b.low#                      ///<最低价
    #     self.volume = b.volume#                       ///<成交量
    #     self.amount = b.amount#                       ///<成交金额
    #     self.pre_close = b.pre_close#                    ///昨收盘价，只有日频数据赋值
    #     self.position = b.position#                     ///<持仓量
    #     self.frequency = b.frequency#	////bar频度
    #     pass
    def __init__(self):
        self.symbol = None         #///symbol
        self.bob = 0             #        ///bar的开始时间
        self.eob = 0              #       ///bar的结束时间
        self.open = 0 #                        ///<开盘价
        self.close = 0#                        ///<收盘价
        self.high = 0#                       ///<最高价
        self.low =0                #      ///<最低价
        self.volume = 0#                       ///<成交量
        self.amount = 0#                       ///<成交金额
        self.pre_close = 0#                    ///昨收盘价，只有日频数据赋值
        self.position = 0#                     ///<持仓量
        self.frequency = None#	////bar频度
        pass

    def __init__(self,b):
        self.symbol = b.symbol#		///symbol
        self.bob = Timestamp(b.bob)#                     ///bar的开始时间
        self.eob = Timestamp(b.eob)#                        ///bar的结束时间
        self.open = b.open#                        ///<开盘价
        self.close = b.close#                        ///<收盘价
        self.high = b.high#                       ///<最高价
        self.low = b.low#                      ///<最低价
        self.volume = b.volume#                       ///<成交量
        self.amount = b.amount#                       ///<成交金额
        self.pre_close = b.pre_close#                    ///昨收盘价，只有日频数据赋值
        self.position = b.position#                     ///<持仓量
        self.frequency = b.frequency#	////bar频度
        pass

    def __init__(self,b):
        self.symbol = b.symbol#		///symbol
        self.bob = Timestamp(b.bob)#                     ///bar的开始时间
        self.eob = Timestamp(b.eob)#                        ///bar的结束时间
        self.open = b.open#                        ///<开盘价
        self.close = b.close#                        ///<收盘价
        self.high = b.high#                       ///<最高价
        self.low = b.low#                      ///<最低价
        self.volume = b.volume#                       ///<成交量
        self.amount = b.amount#                       ///<成交金额
        self.pre_close = b.pre_close#                    ///昨收盘价，只有日频数据赋值
        self.position = b.position#                     ///<持仓量
        self.frequency = b.frequency#	////bar频度
        pass

    def FromFmt(self,b):
        self.symbol = b.symbol#		///symbol
        self.bob = Timestamp(b.bob)#                     ///bar的开始时间
        self.eob = Timestamp(b.eob)#                        ///bar的结束时间
        self.open = b.open#                        ///<开盘价
        self.close = b.close#                        ///<收盘价
        self.high = b.high#                       ///<最高价
        self.low = b.low#                      ///<最低价
        self.volume = b.volume#                       ///<成交量
        self.amount = b.amount#                       ///<成交金额
        self.pre_close = b.pre_close#                    ///昨收盘价，只有日频数据赋值
        self.position = b.position#                     ///<持仓量
        self.frequency = b.frequency#	////bar频度
        pass



# nipasbc
class InstrumentInfo(object):
    # symbol = ... # type: Text
    # sec_type = ... # type: int
    # exchange = ... # type: Text
    # sec_id = ... # type: Text
    # sec_name = ... # type: Text
    # sec_abbr = ... # type: Text
    # price_tick = ... # type: Text

    # listed_date = ... # type: int
    # delisted_date = ... # type: int
    pass


    # def __init__(self, symbol:Text='', sec_type:int=0, exchange:Text='', sec_id:Text='', sec_name:Text='',
    #              sec_abbr: Text='', price_tick: Text='', listed_date:int=None, delisted_date:int=None): ...

# nipasbc
class InstrumentInfos(object):
    data = ... # type: List[InstrumentInfo]

    # def __init__(self, data:List[InstrumentInfo]=None):...

# nipasbc
class Instrument(object):
    symbol = ... # type: Text
    sec_level = ... # type: int
    is_suspended = ... # type: int
    multiplier = ... # type: float
    margin_ratio = ... # type: float

    settle_price = ... # type: float
    position = ... # type: int
    pre_close = ... # type: float
    pre_settle = ... # type: float
    upper_limit = ... # type: float
    lower_limit = ... # type: float
    adj_factor = ... # type: float

    info = ... # type: InstrumentInfo

    created_at = ... # type: int

    # def __init__(self, symbol:Text='', sec_level:int=0, is_suspended:int=0, multiplier:float=0, margin_ratio:float=0,
    #              settle_price:float=0, position:int=0, pre_close:float=0, pre_settle:float=0, upper_limit:float=0, lower_limit:float=0,
    #              adj_factor:float=0, info: InstrumentInfo=None, created_at:int=None): ...

# nipasbc
class Instruments(object):
    data = ... # type: List[Instrument]

    # def __init__(self, data:List[Instrument]=None): ...

# nipasbc
class Dividend(object):
    symbol = ... # type: Text
    cash_div = ... # type: float
    share_div_ratio = ... # type: float
    share_trans_ratio = ... # type: float
    allotment_ratio = ... # type: float
    allotment_price = ... # type: float

    created_at = ... # type: int

    def __init__(self, symbol:Text='', cash_div:float=0, share_div_ratio:float=0, share_trans_ratio:float=0,
                 allotment_ratio:float=0, allotment_price:float=0): ...

# nipasbc
class Dividends(object):
    data = ... # type: List[Dividend]

    # def __init__(self, data:List[Dividend]=None): ...

# # nipasbc
# class ContinuousContract(object):
#     symbol = ... # type: Text
#     created_at = ... # type: int

#     # def __init__(self, symbol:Text='', created_at:int=None): ...

# # nipasbc
# class ContinuousContracts(object):
#     data = ... # type: List[ContinuousContract]

#     # def __init__(self, data=List[ContinuousContract]): ...

# nipasbc
class Constituent(object):
    constituents = ... # type: Dict[Text, float]
    created_at = ... # type: int

    # def __init__(self, constituents:Dict[Text, float], created_at:int): ...

# nipasbc
class Constituents(object):
    data = ... # type: List[Constituent]

    # def __init__(self, data:List[Constituent]=None): ...
