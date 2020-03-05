# -*- coding: utf-8 -*-
from contextlib import contextmanager
from typing import Optional, List

import grpc
from google.protobuf.any_pb2 import Any

from .models import User, UserPagination, AccountServiceException
from .schema import UserObjectSchema as UOSch, UserPbSchema as UPSch, UserPaginationObjectSchema as UPOSch, \
    UserPaginationPbSchema as UPPSch
from . import common_pb2 as c_pb
from . import accountService_pb2_grpc as a_grpc
from . import accountService_pb2 as a_pb
from google.protobuf.any_pb2 import Any as pbAny


class AccountServiceGRPCClient:
    _endpoint = None
    _retry_time = 3
    _retry_interval = 2

    def __init__(self, endpoint: str, src: str = ''):
        self._endpoint = endpoint
        self._src = src

    @contextmanager
    def _stub(self):
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = a_grpc.AccountServiceStub(channel)
            try:
                yield stub
            except grpc.RpcError as e:
                raise AccountServiceException(str(e))

    def _pack(self, request: Any) -> c_pb.RequestMessage:
        data = pbAny()
        data.Pack(request)
        return c_pb.RequestMessage(src=self._src, data=data)

    def _unpack(self, response: c_pb.ResponseMessage, data_type: Optional[type]) -> Any:
        if response.code != 0:
            raise AccountServiceException("{} {}".format(str(response.code), response.msg))
        if data_type is None:
            return None
        msg = data_type()
        response.data.Unpack(msg)
        return msg

    def get_user_list(self, id_list: list) -> List[User]:
        with self._stub() as stub:
            resp = stub.GetUserList(self._pack(a_pb.GetUserListRequest(id_list=id_list)))
            u_pb = self._unpack(resp, a_pb.GetUserListResponse).list
            u_ls = UOSch(many=True).load(UPSch(many=True).dump(u_pb))
            return u_ls

    def get_user_page_list(self, current_page: int, page_size: int, username: str,
                           phone: str, email: str) -> UserPagination:
        with self._stub() as stub:
            resp = stub.GetUserPageList(self._pack(a_pb.GetUserPageListRequest(
                current_page=current_page, page_size=page_size, username=username, phone=phone, email=email)))
            up_pb = self._unpack(resp, a_pb.GetUserPageListResponse)
            up = UPOSch().load(UPPSch().dump(up_pb))
            return up
