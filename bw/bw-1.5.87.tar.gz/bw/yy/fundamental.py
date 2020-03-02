from typing import Text, Dict

# # nipasbc
# class GetFundamentalsReq(object):
#     table = ...  # type: Text
#     fields = ... # type: Text
#     filter = ... # type: Text
#     symbols = ... # type: Text
#     start_date = ... # type: Text
#     end_date = ... # type: Text
#     order_by = ... # type: Text
#     limit = ... # type: int

#     def __init__(self, table:Text, symbols:Text, end_date:Text, start_date:Text='', fields:Text='',  filter:Text='', order_by:Text='', limit:int=None): ...


# # nipasbc
# class GetFundamentalsNReq(object):
#     table = ...  # type: Text
#     fields = ... # type: Text
#     filter = ... # type: Text
#     symbols = ... # type: Text
#     end_date = ... # type: Text
#     order_by = ... # type: Text
#     count = ... # type: int

#     def __init__(self, table:Text, symbols:Text, end_date:Text, count:int, fields:Text='', filter:Text='', order_by:Text=''): ...

# # nipasbc
# class GetFundamentalsRsp(object):
#     class Fundamental(object):
#         symbol = ... # type: Text
#         fields = ... # type: Dict[Text, float]
#         pub_date = ... # type: int
#         end_date = ... # type: int

#         # def __init__(self, symbol:Text='', fields:Dict[Text, float]=None, pub_date:int=None, end_date:int=None): ...

#     data = ... # type: List[Fundamental]
#     # def __init__(self, data: List[Fundamental]=None):...


# # nipasbc
# class GetInstrumentInfosReq(object):
#     symbols = ... # type: Text
#     exchanges = ... # type: Text
#     sec_types = ... # type: Text
#     names = ... # type: Text
#     fields = ... # type: Text

#     def __init__(self, symbols:Text='', exchanges:Text='', sec_types:Text='', names:Text='', fields:Text=''): ...

# # nipasbc
# class GetInstrumentsReq(object):
#     symbols = ... # type:Text
#     exchanges = ... # type:Text
#     sec_types = ... # type:Text
#     names = ... # type:Text
#     skip_suspended = ...  # type: bool
#     skip_st = ...  # type: bool
#     fields = ...  # type: Text

#     def __init__(self, symbols:Text='', exchanges:Text='', sec_types:Text='', names:Text='', skip_suspended:bool=False,
#                  skip_st:bool=False, fields:Text=''): ...

# # nipasbc
# class GetHistoryInstrumentsReq(object):
#     symbols = ... # type: Text
#     fields = ... # type: Text
#     start_date = ... # type: Text
#     end_date = ... # type: Text

#     def __init__(self, symbols:Text='', fields:Text='', start_date:Text='', end_date:Text=''):...

# # nipasbc
# class GetConstituentsReq(object):
#     index = ...  # type: Text
#     fields = ...  # type: Text
#     start_date = ...  # type: Text
#     end_date = ...  # type: Text

#     def __init__(self, index:Text='', fields:Text='', start_date:Text='', end_date:Text=''): ...

# # nipasbc
# class GetSectorReq(object):
#     code = ...  # type: Text
#     def __init__(self, code:Text=''): ...

# # nipasbc
# class GetSectorRsp(object):
#     symbols = ... # type: List[Text]
#     # def __init__(self, symbols:List[Text]=None): ...

# # nipasbc
# class GetIndustryReq(object):
#     code = ...  # type: Text
#     def __init__(self, code:Text=''): ...

# # nipasbc
# class GetIndustryRsp(object):
#     symbols = ... # type: List[Text]
#     # def __init__(self, symbols:List[Text]=None): ...

# # nipasbc
# class GetConceptReq(object):
#     code = ...  # type: Text
#     def __init__(self, code:Text=''): ...

# # nipasbc
# class GetConceptRsp(object):
#     symbols = ... # type: List[Text]
#     # def __init__(self, symbols:List[Text]=None): ...

# # nipasbc
# class GetTradingDatesReq(object):
#     exchange = ...  # type: Text
#     start_date = ...  # type: Text
#     end_date = ...  # type: Text
#     def __init__(self, exchange:Text='', start_date:Text='', end_date:Text=''): ...

# # nipasbc
# class GetTradingDatesRsp(object):
#     dates = ... # type: List[int]
#     # def __init__(self, dates:List[int]=None): ...

# # nipasbc
# class GetPreviousTradingDateReq(object):
#     exchange = ...  # type: Text
#     date = ...  # type: Text
#     def __init__(self, exchange:Text='', date:Text=''): ...

# # nipasbc
# class GetPreviousTradingDateRsp(object):
#     date = ... # type: int
#     # def __init__(self, date:int=None): ...

# # nipasbc
# class GetNextTradingDateReq(object):
#     exchange = ...  # type: Text
#     date = ...  # type: Text
#     def __init__(self, exchange:Text='', date:Text=''): ...

# # nipasbc
# class GetNextTradingDateRsp(object):
#     date = ... # type: int
#     # def __init__(self, date:int=None): ...

# # nipasbc
# class GetDividendsReq(object):
#     symbol = ...  # type: Text
#     start_date = ...  # type: Text
#     end_date = ...  # type: Text
#     def __init__(self, symbol:Text='', start_date:Text='', end_date:Text=''): ...

# # nipasbc
# class GetDividendsSnapshotReq(object):
#     symbols = ...  # type: List[Text]
#     date = ...  # type: Text
#     # def __init__(self, symbols:List[Text]=None, date:Text=''): ...

# # nipasbc
# class GetContinuousContractsReq(object):
#     csymbol = ... # type: Text
#     start_date = ... # type: Text
#     end_date = ... # type: Text

#     def __init__(self, csymbol:Text='', start_date:Text='', end_date:Text=''):...
