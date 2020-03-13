# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Awaitable

from fastapi.encoders import jsonable_encoder

from ppm_telegram_bot_client import models as m

if TYPE_CHECKING:
    from ppm_telegram_bot_client.api_client import ApiClient


class _TriggersApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_notion_error(self,) -> Awaitable[m.Any]:
        return self.api_client.request(type_=m.Any, method="POST", url="/triggers/notion_error",)

    def _build_for_talk_new(self, talk_info: m.TalkInfo) -> Awaitable[m.Any]:
        body = jsonable_encoder(talk_info)

        return self.api_client.request(type_=m.Any, method="POST", url="/triggers/talk_new", json=body)

    def _build_for_typeform_invalid(self,) -> Awaitable[m.Any]:
        return self.api_client.request(type_=m.Any, method="POST", url="/triggers/typeform_invalid",)


class AsyncTriggersApi(_TriggersApi):
    async def notion_error(self,) -> m.Any:
        return await self._build_for_notion_error()

    async def talk_new(self, talk_info: m.TalkInfo) -> m.Any:
        return await self._build_for_talk_new(talk_info=talk_info)

    async def typeform_invalid(self,) -> m.Any:
        return await self._build_for_typeform_invalid()


class SyncTriggersApi(_TriggersApi):
    def notion_error(self,) -> m.Any:
        coroutine = self._build_for_notion_error()
        return get_event_loop().run_until_complete(coroutine)

    def talk_new(self, talk_info: m.TalkInfo) -> m.Any:
        coroutine = self._build_for_talk_new(talk_info=talk_info)
        return get_event_loop().run_until_complete(coroutine)

    def typeform_invalid(self,) -> m.Any:
        coroutine = self._build_for_typeform_invalid()
        return get_event_loop().run_until_complete(coroutine)
