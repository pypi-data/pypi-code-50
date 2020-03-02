from typing import Text, Dict

from bw.yy.account import Position



# nipasbc
class Indicator(object):
    # 账号ID
    # account_id = ...  # type: Text
    # # 累计收益率(pnl/cum_inout)
    # pnl_ratio = ...  # type: float
    # # 年化收益率
    # pnl_ratio_annual = ...  # type: float
    # # 夏普比率
    # sharp_ratio = ...  # type: float
    # # 最大回撤
    # max_drawdown = ...  # type: float
    # # 风险比率
    # risk_ratio = ...  # type: float
    # # 开仓次数
    # open_count = ...  # type: int
    # # 平仓次数
    # close_count = ...  # type: int
    # # 盈利次数
    # win_count = ...  # type: int
    # # 亏损次数
    # lose_count = ...  # type: int
    # # 胜率
    # win_ratio = ...  # type: float
    # # 卡玛比率
    # calmar_ratio = ...  # type: float
    # created_at = ...  # type: int
    # updated_at = ...  # type: int

    def __init__(self):
        self.account_id = ...  # type: Text
        # 累计收益率(pnl/cum_inout)
        self.pnl_ratio = ...  # type: float
        # 年化收益率
        self.pnl_ratio_annual = ...  # type: float
        # 夏普比率
        self.sharp_ratio = ...  # type: float
        # 最大回撤
        self.max_drawdown = ...  # type: float
        # 风险比率
        self.risk_ratio = ...  # type: float
        # 开仓次数
        self.open_count = ...  # type: int
        # 平仓次数
        self.close_count = ...  # type: int
        # 盈利次数
        self.win_count = ...  # type: int
        # 亏损次数
        self.lose_count = ...  # type: int
        # 胜率
        self.win_ratio = ...  # type: float
        # 卡玛比率
        self.calmar_ratio = ...  # type: float
        self.created_at = ...  # type: int
        self.updated_at = ...  # type: int
        
    def __init__(self,
                 account_id: Text = '',
                 pnl_ratio: float = None,
                 pnl_ratio_annual: float = None,
                 sharp_ratio: float = None,
                 max_drawdown: float = None,
                 risk_ratio: float = None,
                 open_count: int = None,
                 close_count: int = None,
                 win_count: int = None,
                 lose_count: int = None,
                 win_ratio: float = None,
                 calmar_ratio: float = None,
                 alpha: float  = None,
                 beta: float  = None,
                 sortino_rate: float  = None,
                 information_ratio: float  = None,
                 created_at: int = None,
                 updated_at: int = None,
                 bench_ratio : float  = None ,
                 bench_annul_ratio  : float  = None,
                 win_amount   : float  = None,   
                 loss_amount      : float  = None,  
                 win_loss_ratio    : float  = None, 

                 ): ...
    # def __init__(self,ind_):
    #     self.account_id=ind_.account_id#             //账号ID
    #     self.pnl_ratio=ind_.pnl_ratio#                      //累计收益率(const pnl/cum_inout)
    #     self.pnl_ratio_annual=ind_.pnl_ratio_annual#               //年化收益率
    #     self.sharp_ratio=ind_.sharp_ratio#                    //夏普比率
    #     self.max_drawdown=ind_.max_drawdown#                   //最大回撤
    #     self.risk_ratio=ind_.risk_ratio#                     //风险比率
    #     self.open_count=ind_.open_count#                     //开仓次数
    #     self.close_count=ind_.close_count#                    //平仓次数
    #     self.win_count=ind_.win_count#                      //盈利次数
    #     self.lose_count=ind_.lose_count#                     //亏损次数
    #     self.win_ratio=ind_.win_ratio#                      //胜率
    #     self.created_at=ind_.created_at#                    //指标创建时间
    #     self.updated_at=ind_.updated_at#                    //指标变更时间
    #     pass
    def FromFmt(self,ind_):
        self.account_id=ind_.account_id#             //账号ID
        self.pnl_ratio=ind_.pnl_ratio#                      //累计收益率(const pnl/cum_inout)
        self.pnl_ratio_annual=ind_.pnl_ratio_annual#               //年化收益率
        self.sharp_ratio=ind_.sharp_ratio#                    //夏普比率
        self.max_drawdown=ind_.max_drawdown#                   //最大回撤
        self.risk_ratio=ind_.risk_ratio#                     //风险比率
        self.open_count=ind_.open_count#                     //开仓次数
        self.close_count=ind_.close_count#                    //平仓次数
        self.win_count=ind_.win_count#                      //盈利次数
        self.lose_count=ind_.lose_count#                     //亏损次数
        self.win_ratio=ind_.win_ratio#                      //胜率
        self.created_at=ind_.created_at#                    //指标创建时间
        self.updated_at=ind_.updated_at#                    //指标变更时间
        
        self.alpha=ind_.alpha#                      //胜率
        self.beta=ind_.beta#                      //胜率
        self.sortino_rate=ind_.sortino_rate#                      //胜率
        self.information_ratio=ind_.information_ratio#                      //胜率

        self.bench_ratio= ind_.bench_ratio
        self.bench_annul_ratio=ind_.bench_annul_ratio
        self.win_amount=ind_.win_amount
        self.loss_amount=ind_.loss_amount
        self.win_loss_ratio=ind_.win_loss_ratio

        pass  

    def __str__(self):
        ls=[]
        ls.append("账号ID:       " + str(self.account_id )         )
        ls.append("累计收益率:   " + str(self.pnl_ratio )          )
        ls.append("年化收益率:   " + str(self.pnl_ratio_annual )   )
        ls.append("夏普比率:     " + str(self.sharp_ratio )        )
        ls.append("最大回撤:     " + str(self.max_drawdown )       )
        ls.append("风险比率:     " + str(self.risk_ratio )         )
        ls.append("开仓次数:     " + str(self.open_count )         )
        ls.append("平仓次数:     " + str(self.close_count )        )
        ls.append("盈利次数:     " + str(self.win_count )          )
        ls.append("亏损次数:     " + str(self.lose_count )         )

        ls.append("阿尔法:         " + str(self.alpha )          )
        ls.append("贝塔:         " + str(self.beta )          )
        ls.append("索提诺比:         " + str(self.sortino_rate )          )
        ls.append("信息比率:         " + str(self.information_ratio )          )

        ls.append("胜率:         " + str(self.win_ratio )          )
        ls.append("指标创建时间: " + str(self.created_at )         )
        ls.append("指标变更时间: " + str(self.updated_at )         )

        
        ls.append("基准: " +str(self.bench_ratio ))
        ls.append("基准年化: " +str(self.bench_annul_ratio ))
        ls.append("盈利数额: " +str(self.win_amount ))
        ls.append("亏损数额: " +str(self.loss_amount ))
        ls.append("盈亏比: " +str(self.win_loss_ratio ))
        
        return '\n'.join(ls)
        pass


# nipasbc
class Indicators(object):
    data = ...  # type: List[Indicator]

    # def __init__(self, data: List[Indicator] = None): ...


# nipasbc
class IndicatorDuration(object):
    # 账号ID
    account_id = ...  # type: Text
    pnl_ratio = ...  # type: float
    pnl = ...  # type: float
    fpnl = ...  # type: float
    frozen = ...  # type: float
    cash = ...  # type: float
    nav = ...  # type: float
    positions = ...  # type: List[Position]
    # 周期累计盈亏
    cum_pnl = ...  # type: float
    # 周期累计买入额
    cum_buy = ...  # type: float
    # 周期累计卖出额
    cum_sell = ...  # type: float
    # 周期累计手续费
    cum_commission = ...  # type: float
    duration = ...  # type: Duration
    created_at = ...  # type: int
    updated_at = ...  # type: int



    # def __init__(self,
    #              account_id: Text = None,
    #              pnl_ratio: float = None,
    #              pnl: float = None,
    #              fpnl: float = None,
    #              frozen: float = None,
    #              cash: float = None,
    #              nav: float = None,
    #              positions: list[Position] = None,
    #              cum_pnl: float = None,
    #              cum_buy: float = None,
    #              cum_sell: float = None,
    #              cum_commission: float = None,
    #              duration: Duration = None,
    #              created_at: int = None,
    #              updated_at: int = None
    #              ): ...


# nipasbc
class IndicatorDurations(object):
    data = ...  # type: List[IndicatorDuration]

    # def __init__(self, data: List[IndicatorDuration] = None): ...
