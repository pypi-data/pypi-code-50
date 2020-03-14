# flake8: noqa E501
from asyncio import get_event_loop
from typing import TYPE_CHECKING, Any, Awaitable

from fastapi.encoders import jsonable_encoder

from ppm_telegram_bot_client import models as m

if TYPE_CHECKING:
    from ppm_telegram_bot_client.api_client import ApiClient


class _TelegramApi:
    def __init__(self, api_client: "ApiClient"):
        self.api_client = api_client

    def _build_for_telegram_webhook(self, secret: str, body: Any) -> Awaitable[m.Any]:
        """
        Pass the new update (event from telegram) to bot dispatcher for processing.
        """
        path_params = {"secret": str(secret)}

        body = jsonable_encoder(body)

        return self.api_client.request(
            type_=m.Any, method="POST", url="/telegram/webhook/{secret}", path_params=path_params, json=body
        )


class AsyncTelegramApi(_TelegramApi):
    async def telegram_webhook(self, secret: str, body: Any) -> m.Any:
        """
        Pass the new update (event from telegram) to bot dispatcher for processing.
        """
        return await self._build_for_telegram_webhook(secret=secret, body=body)


class SyncTelegramApi(_TelegramApi):
    def telegram_webhook(self, secret: str, body: Any) -> m.Any:
        """
        Pass the new update (event from telegram) to bot dispatcher for processing.
        """
        coroutine = self._build_for_telegram_webhook(secret=secret, body=body)
        return get_event_loop().run_until_complete(coroutine)
