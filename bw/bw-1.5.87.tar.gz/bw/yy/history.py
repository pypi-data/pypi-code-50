from typing import Text, Dict


# # nipasbc
# class GetCurrentTicksReq(object):
#     symbols = ...  # type: Text
#     fields = ...  # type: Text

#     def __init__(self, symbols: Text, fields: Text): ...


# # nipasbc
# class GetHistoryTicksReq(object):
#     symbols = ...  # type: Text
#     start_time = ...  # type: Text
#     end_time = ...  # type: Text
#     fields = ...  # type: Text
#     skip_suspended = ...  # type: bool
#     fill_missing = ...  # type: Text
#     adjust = ...  # type: int
#     adjust_end_time = ...  # type: Text

#     def __init__(self, symbols: Text = '', start_time: Text = '', end_time: Text = '', fields: Text = '',
#                  skip_suspended: bool = None, fill_missing: Text = '', adjust: int = None,
#                  adjust_end_time: Text = ''): ...


# # nipasbc
# class GetHistoryBarsReq(object):
#     symbols = ...  # type: Text
#     frequency = ...  # type: Text
#     start_time = ...  # type: Text
#     end_time = ...  # type: Text
#     fields = ...  # type: Text
#     skip_suspended = ...  # type: bool
#     fill_missing = ...  # type: Text
#     adjust = ...  # type: int
#     adjust_end_time = ...  # type: Text

#     def __init__(self, symbols: Text = '', frequency: Text = '', start_time: Text = '',
#                  end_time: Text = '', fields: Text = '', skip_suspended: bool = None,
#                  fill_missing: Text = '', adjust: int = None, adjust_end_time: Text = '', ): ...


# # nipasbc
# class GetHistoryTicksNReq(object):
#     symbol = ...  # type: Text
#     count = ...  # type: int
#     end_time = ...  # type: Text
#     fields = ...  # type: Text
#     skip_suspended = ...  # type: bool
#     fill_missing = ...  # type: Text
#     adjust = ...  # type: int
#     adjust_end_time = ...  # type: Text

#     def __init__(self, symbol: Text = '', count: int = None, end_time: Text = '',
#                  fields: Text = '', skip_suspended: bool = None, fill_missing: Text = '',
#                  adjust: int = None, adjust_end_time: Text = None): ...


# # nipasbc
# class GetHistoryBarsNReq(object):
#     symbol = ...  # type: Text
#     frequency = ...  # type: Text
#     count = ...  # type: int
#     end_time = ...  # type: Text
#     fields = ...  # type: Text
#     skip_suspended = ...  # type: bool
#     fill_missing = ...  # type: Text
#     adjust = ...  # type: int
#     adjust_end_time = ...  # type: Text

#     def __init__(self, symbol: Text = '', frequency: Text = '', count: int = None,
#                  end_time: Text = '', fields: Text = '', skip_suspended: bool = None,
#                  fill_missing: Text = '', adjust: int = None, adjust_end_time: Text = '',
#                  ): ...


# # nipasbc
# class GetBenchmarkReturnReq(object):
#     symbol = ...  # type: Text
#     frequency = ...  # type: Text
#     start_time = ...  # type: Text
#     end_time = ...  # type: Text
#     adjust = ...  # type: int
#     adjust_end_time = ...  # type: Text

#     def __init__(self, symbol: Text = '',
#                  frequency: Text = '',
#                  start_time: Text = '',
#                  end_time: Text = '',
#                  adjust: int = None,
#                  adjust_end_time: Text = '',
#                  ): ...


# # nipasbc
# class GetBenchmarkReturnRsp(object):
#     class BenchmarkReturn(object):
#         ratio = ...  # type: float
#         created_at = ...  # type: int

#         def __init__(self, ratio: float = None, end_date: created_at = None): ...

#     data = ...  # type: List[GetBenchmarkReturnRsp]

#     # def __init__(self, data: List[GetBenchmarkReturnRsp] = None): ...
