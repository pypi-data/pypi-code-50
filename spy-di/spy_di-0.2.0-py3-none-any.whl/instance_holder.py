#  Copyright (c) 2020 Maksim Penkov
#  SPDX-License-Identifier: Apache-2.0

import asyncio
import inspect


class SingletonHolder:
    def __init__(self, factory):
        self._factory = factory
        self._instance = None

    def obtain(self):
        if self._instance is None:
            self._instance = _ensure_awaitable_is_task(
                self._factory(),
            )

        return self._instance


class UniqueHolder:
    def __init__(self, factory):
        self._factory = factory

    def obtain(self):
        return _ensure_awaitable_is_task(
            self._factory(),
        )


def _ensure_awaitable_is_task(obj):
    if inspect.isawaitable(obj) and not isinstance(
            obj,
            asyncio.Task,
    ):
        return asyncio.create_task(obj)

    return obj
