# -*-coding:utf-8 -*-

# @Time    : 2020/2/16 15:49
# @File    : strategy_test_stock.py
# @User    : yangchuan
# @Desc    : 

from quant_trade_framework.stock.strategy import Strategy
from quant_trade_framework.common.constant import Constant
from quant_trade_framework.common.logConfig import Logger
from quant_trade_framework.stock.parameters import OrderCost,SlipPage

logger = Logger.module_logger("system")

#可以设置的基准

def initialize(Context):
    """
    initialize(Context)
    该方法为固定方法，每个策略必须实现
    策略运行前准备操作
    """
    #设置账号密码
    Context.set_auth('admin','123456')
    #设置订单交易参数
    """
    按照聚宽的定义实现：
    cost for per order
    open_tax：买入时印花税 (只股票类标的收取，基金与期货不收)
    close_tax：卖出时印花税 (只股票类标的收取，基金与期货不收)
    open_commission：买入时佣金，申购场外基金的手续费
    close_commission： 卖出时佣金，赎回场外基金的手续费
    close_today_commission： 平今仓佣金
    min_commission： 最低佣金，不包含印花税
    目前只使用open_tax和close_tax，来计算加仓/减仓的手续费
    计算公式为：open_tax * price * qty  
    """
    Context.set_order_cost(
        cost=OrderCost(open_tax=0.001,
                  close_tax=0.001,
                  open_commission=0.0003,
                  close_commission=0.0003,
                  close_today_commission=0,
                  min_commission=5),
        type='all')
    #设置滑点
    """
    type:滑点类型
    固定值： 这个价差可以是一个固定的值(比如0.02元, 交易时加减0.01元), 设定方式为：FixedSlippage(0.02)
    百分比： 这个价差可以是是当时价格的一个百分比(比如0.2%, 交易时加减当时价格的0.1%), 设定方式为：PriceRelatedSlippage(0.002)
    如果是加仓操作，固定值：price+slip 百分比：price * (1+slip)
    如果是减仓操作，固定值：price-slip 百分比：price * (1-slip)
    """
    Context.set_slippage(
        slippage=SlipPage(type=Constant.PRICE_RELATED_SLIPPAGE,
                 value=0.001),
        type='all'
    )
    #设置一些全局使用的变量，比如SHORT LONG分别代表短周期和长周期的时间长度
    Context.SHORT = 5
    Context.LONG = 20
    #设置初始资金
    Context.ORIGINAL_CASH = 10000000
    #缓存数据空间大小，如果是按天进行计算，
    # 21缓存最近21天的数据，因为20移动平局需要至少21天的数据才能计算
    Context.set_bar_cache_size(21)
    #设置基准
    Context.set_benckmark("000300.XSHG")


def handle_data(Context):
    """
    handle_data(Context)
    该方法为固定方法，每个策略必须实现
    每个计算周期需要执行的处理方法
    根据策略运行的不同频率，每天、每小时、每分钟来触发
    比如设置策略按天运行，且每天的运行时间是9:30,那么当执行handle_data，
    获取当前上下文时间Context.current_datetime()就是 YY:MM:DD 09:30
    """
    generateSignal(Context)


def generateSignal(Context):
    """
    自定义的方法，需要引用Context
    """
    # long = JqDataCore.get_bars("000001.XSHE", 21, Context.current_datetime(), Constant.KLINE_INTERVAL_1DAY)
    # # for item in long:
    # #     print(item)
    # long_am = DataFormater.data_list_array_manager(long,21)
    # short = long_am.sma(5,array=True)
    # long = long_am.sma(20,array=True)
    # print(long_am.close)
    # print(Context.bars.close)
    short = Context.bars.sma(Context.SHORT,array=True)
    long = Context.bars.sma(Context.LONG,array=True)
    # print(short)
    # print(long)
    short_ma0 = short[-1]
    short_ma1 = short[-2]
    long_ma0 = long[-1]
    long_ma1 = long[-2]
    print(Context.current_datetime())
    print("short_ma0:"+str(short_ma0))
    print("short_ma1:" + str(short_ma1))
    print("long_ma0:" + str(long_ma0))
    print("long_ma1:" + str(long_ma1))
    #金叉判断
    cross_over = long_ma0 < short_ma0 and long_ma1 > short_ma1
    #死叉判断
    cross_bellow = long_ma0 > short_ma0 and long_ma1 < short_ma1
    current_positon = Context.accounts["account1"].get_position("000001.XSHE")
    if cross_over:
        if current_positon['available'] == 0:
            Context.accounts["account1"].order_value("000001.XSHE", Context.ORIGINAL_CASH)
        # elif current_positon <=0:
        #     Context.accounts["account1"].order_target("000001.XSHE", 0)
        #     Context.accounts["account1"].order_value("000001.XSHE", Context.ORIGINAL_CASH)
    if cross_bellow:
        if current_positon['available'] > 0:
            Context.accounts["account1"].order_target("000001.XSHE", 0)


"""
创建策略
"""
my_strategy = Strategy()
"""
创建账户
账户名称：任意名称
初始金额：float
类型：默认为stock
"""
my_strategy.create_account(
    "account1",
    10000000.0,
    "stock"
)

"""
定义要操作的股票代码
"""
my_strategy.create_universe('000001.XSHE')

"""
定义策略参数：
initialize：初始化函数，直接使用函数定义模板，实现函数内容
handle_data：每个周期运行函数，直接使用函数定义模板，实现函数内容
frequency：周期频率，系统全局变量：RUN_FREQ_DAY、RUN_FREQ_HOUR、RUN_FREQ_MINUTE
flag_cache_bar:是否需要缓存数据，如果是按天计算，则缓存最近N个有效交易日的数据
flag_prefetch_data：是否需要预取数据，比如2020.01.01开始运行策略，
但策略里面定义21天的数据缓存，设置为True，则提取2020.01.01前21个有效交易日的数据
"""
my_strategy.create_strategy(
    initialize,
    handle_data,
    frequency=Constant.RUN_FREQ_DAY,
    flag_cache_bar=True,
    flag_prefetch_data=True
)

"""
运行策略
start:开始时间
end:结束时间
run_at_time：周期运行时间
"""
my_strategy.backtest(
    start="2019-06-04",
    end="2019-06-25",
    run_at_time="09:30:00"
)

"""
常用方法使用：
1.Context 环境信息
策略运行的环境信息

设置缓存数据空间大小:
Context.set_bar_cache_size(size)

设置账号信息:
Context.set_auth(user_name,user_pwd)

设置交易手续费参数：
Context.set_order_cost(cost:OrderCost)
Context.set_order_cost(
        cost=OrderCost(open_tax=0.001,
                  close_tax=0.001,
                  open_commission=0.0003,
                  close_commission=0.0003,
                  close_today_commission=0,
                  min_commission=5),
        type='all')
        
设置基准代码：
Context.set_benckmark(security)
Context.set_benckmark("000300.XSHG")

设置滑点：
Context.set_slippage(slippage:SlipPage,type:str)
Context.set_slippage(
        slippage=SlipPage(type=Constant.PRICE_RELATED_SLIPPAGE,
                 value=0.001),
        type='all'
    )
    
设置当前时间点：
Context.set_current_datetime(datetime)

设置运行周期：
Context.set_run_freq(type)

获取当前账户信息：
Context.get_account(name)
账户信息返回的是一个实例，具体参考Account
参考获取指定账户仓位：Context.accounts["account1"].get_position("000001.XSHE")

最新的价格：
Context.get_price(symbol:str,inteval:str = "1d")
interval:为bar数据的周期，通常跟策略运行的频率一致
一般使用下面的方法来获取
Context.get_price('000001.XSHE',self.context.run_freq)
返回值为BarData实例，具体使用见BarData定义

最新的基准价格：
Context.get_benchmark_price()
返回值为BarData实例，具体使用见BarData定义

当前周期时间：
Context.current_datetime()

下一个周期时间：
Context.next_price_datetime()

前一个周期时间：
Context.previous_datetime()

当前仓位：Context.accounts["account1"].get_position("000001.XSHE")
 目前只支持单品种 universe = my_strategy.create_universe('000001.XSHE')设置的


2.Account 账户操作 account.py
用户账户信息相关操作

账户的实例只能通过Context获取，获取方法：
Context.accounts["account1"]

单一仓位信息获取：
get_position(self, asset: str) asset品种名称
当前仓位：Context.accounts["account1"].get_position("000001.XSHE")
目前只支持单品种 universe = my_strategy.create_universe('000001.XSHE')设置的
返回值为仓位对象Position，具体使用见类定义

所有品种餐位信息获取
get_posistions()
Context.accounts["account1"].get_positions()
返回值：仓位对象Position数组

按指定数量进行买入/卖出
order(security:str, amount:float)
security:品种代码
amount:数量，为正买入，为负卖出
无返回值

按目标仓位进行买入/卖出
order_target(security:str, amount:float)
security:品种代码
amount:数量，
如果当前品种仓位与amount只差为正则卖出，为负则买入
Context.accounts["account1"].order_target("000001.XSHE", 0)
无返回值

按交易金额进行买入/卖出
order_value(security:str, value:float)
security:品种代码
value:金额，为正买入，为负卖出
无返回值

3.策略 strategy.py
功能：策略运行与指标计算

创建账户
create_account(name:str,balance:float,account_type:str)
name:账户名称
balance：金额
account_type：类型，默认为stock
my_strategy.create_account(
    "account1",
    10000000.0,
    "stock"
)

添加交易品种
create_universe(universe:str)
my_strategy.create_universe('000001.XSHE')

初始化策略参数
create_strategy(
    initialize:object,
    handle_data:object,
    frequency:str,
    flag_cache_bar:bool=False,
    flag_prefetch_data:bool=False)
initialize：初始化函数，直接使用函数定义模板，实现函数内容
handle_data：每个周期运行函数，直接使用函数定义模板，实现函数内容
frequency：周期频率，系统全局变量：RUN_FREQ_DAY、RUN_FREQ_HOUR、RUN_FREQ_MINUTE
flag_cache_bar:是否需要缓存数据，如果是按天计算，则缓存最近N个有效交易日的数据
flag_prefetch_data：是否需要预取数据，比如2020.01.01开始运行策略，
但策略里面定义21天的数据缓存，设置为True，则提取2020.01.01前21个有效交易日的数据

my_strategy.create_strategy(
    initialize,
    handle_data,
    frequency=Constant.RUN_FREQ_DAY,
    flag_cache_bar=True,
    flag_prefetch_data=True
)

策略运行
backtest(self,start:str,end:str,run_at_time:str)
运行策略
start:开始时间
end:结束时间
run_at_time:周期运行时间
my_strategy.backtest(
    start="2019-06-04",
    end="2019-06-25",
    run_at_time="09:30:00"
)

4.参数说明

交易手续费OrderCost类
按照聚宽的定义实现：
cost for per order
open_tax：买入时印花税 (只股票类标的收取，基金与期货不收)
close_tax：卖出时印花税 (只股票类标的收取，基金与期货不收)
open_commission：买入时佣金，申购场外基金的手续费
close_commission： 卖出时佣金，赎回场外基金的手续费
close_today_commission： 平今仓佣金
min_commission： 最低佣金，不包含印花税
目前只使用open_tax和close_tax，来计算加仓/减仓的手续费
计算公式为：open_tax * price * qty  
OrderCost(open_tax=0.001,
  close_tax=0.001,
  open_commission=0.0003,
  close_commission=0.0003,
  close_today_commission=0,
  min_commission=5)
  
交易滑点SlipPage
type:滑点类型
    固定值： 这个价差可以是一个固定的值(比如0.02元, 交易时加减0.01元), 设定方式为：FixedSlippage(0.02)
    百分比： 这个价差可以是是当时价格的一个百分比(比如0.2%, 交易时加减当时价格的0.1%), 设定方式为：PriceRelatedSlippage(0.002)
    如果是加仓操作，固定值：price+slip 百分比：price * (1+slip)
    如果是减仓操作，固定值：price-slip 百分比：price * (1-slip)
    SlipPage(type=Constant.PRICE_RELATED_SLIPPAGE,
                 value=0.001)
                 
5.重要的数据结构

bar数据
class BarData:

    symbol: str = ""
    exchange: str = ""
    datetime: datetime = datetime.now()

    interval: Interval = None
    volume: float = 0
    open_interest: float = 0
    open_price: float = 0
    high_price: float = 0
    low_price: float = 0
    close_price: float = 0
    refresh_time: datetime = datetime.now()
    
仓位
    asset:str = ""  代码
    available:float = 0  当前仓位
    avg_cost:float = 0  未使用

策略上下文Context中缓存的bar数据
self.bars = ArrayManager(size=size)
class ArrayManager(object):
    def __init__(self, size=100):
        self.count = 0
        self.size = size
        self.inited = False

        self.open_array = np.zeros(size)
        self.high_array = np.zeros(size)
        self.low_array = np.zeros(size)
        self.close_array = np.zeros(size)
        self.volume_array = np.zeros(size)
如果想获取最近缓存bar数据中的最高价：
Context.bars.high()
返回值是numpy array
其他的类似：
Context.bars.open()
Context.bars.close()
Context.bars.low()
Context.bars.volume()

6.关于指标计算
策略上下文Context中缓存的bar数据，已经集成常用计算指标
包括:
sma: Simple moving average
wma: Simple moving average
std: Standard deviation
cci: Commodity Channel Index (CCI)
atr: Average True Range (ATR)
rsi: Relative Strenght Index (RSI)
macd: MACD
adx: ADX
boll: Bollinger Channel
keltner: Keltner Channel
donchian: Donchian Channel
aroon: Aroon indicator
"""