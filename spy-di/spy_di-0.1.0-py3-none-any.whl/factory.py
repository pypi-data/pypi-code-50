#  Copyright (c) 2020 Maksim Penkov
#  SPDX-License-Identifier: Apache-2.0

import contextlib
import copy
import functools
import inspect

from spydi.context import (DependencyContext, BindingScope, ArgFactory,
                           ArgInstance, FactoryType, ScopedInitializer)
from spydi.instance_holder import SingletonHolder, UniqueHolder


class DependencyFactory:
    def __init__(self, ctx: DependencyContext):
        self._ctx = ctx

        self._names = {
            name: self._make_holder(relation)
            for name, relation in ctx.names.items()
        }

        self._classes = {
            name: self._make_holder(relation)
            for name, relation in ctx.classes.items()
        }

    def _make_holder(self, relation):
        scope = relation.scope
        initializer = relation.initializer

        if isinstance(initializer, ArgFactory):
            factory = self._factory(initializer)
        elif isinstance(initializer, ArgInstance):
            factory = functools.partial(
                _instance_factory,
                instance=initializer.instance,
            )
        else:
            raise ValueError()

        return _scoped_factory(scope, factory)

    def _factory(self, initializer: ArgFactory):
        simple_factory = functools.partial(
                self.create,
                whatever=initializer.factory,
            )

        def context_factory():
            assert self._stack
            ctx_manager = simple_factory()

            if isinstance(ctx_manager, contextlib.AbstractAsyncContextManager):
                return self._stack.enter_async_context(ctx_manager)
            return self._stack.enter_context(ctx_manager)

        if initializer.factory_type == FactoryType.SIMPLE:
            return simple_factory
        elif initializer.factory_type == FactoryType.CONTEXT:
            return context_factory

        raise ValueError()

    def obtain(self, whatever):
        if whatever not in self._classes:
            self._classes[whatever] = self._make_holder(
                ScopedInitializer(
                    scope=BindingScope.SINGLETON,
                    initializer=ArgFactory(
                        factory=whatever,
                        factory_type=FactoryType.SIMPLE,
                    ),
                ),
            )

        return self._classes[whatever].obtain()

    def create(self, whatever):
        sign = inspect.signature(whatever)

        bound_params = {}

        for name, param in sign.parameters.items():
            name = param.name
            default = param.default
            annotation = param.annotation

            value = inspect.Parameter.empty

            if name in self._names:
                value = self._names[name].obtain()

            if (annotation != inspect.Parameter.empty and
                    value == inspect.Parameter.empty and
                    not _is_primitive(annotation)):
                value = self.obtain(annotation)

            if (default != inspect.Parameter.empty and
                    value == inspect.Parameter.empty):
                value = default

            assert value != inspect.Parameter.empty

            bound_params[name] = value

        def maker(bound_params_dict):
            ba = sign.bind(**bound_params_dict)
            return whatever(*ba.args, **ba.kwargs)

        async def async_maker(bound_params_dict):
            bound_params_awaited = {
                key: (await obj) if inspect.isawaitable(obj) else obj
                for key, obj in bound_params_dict.items()
            }
            bound_params_dict = bound_params_awaited

            result = maker(bound_params_dict)
            if inspect.isawaitable(result):
                return await result
            return result

        if _has_awaitables(bound_params.values()):
            result_maker = async_maker
        else:
            result_maker = maker

        return result_maker(bound_params)

    @contextlib.contextmanager
    def create_ctx(self, whatever):
        with contextlib.ExitStack() as self._stack:
            yield self.create(whatever)

    @contextlib.asynccontextmanager
    async def create_ctx_async(self, whatever):
        async with contextlib.AsyncExitStack() as self._stack:
            yield await self.create(whatever)


def _scoped_factory(scope, factory):
    if scope == BindingScope.SINGLETON:
        return SingletonHolder(factory)
    elif scope == BindingScope.UNIQUE:
        return UniqueHolder(factory)

    raise ValueError()


def _instance_factory(instance):
    return copy.copy(instance)


def _is_primitive(cls):
    return isinstance(cls, (int, str, float, bool))


def _has_awaitables(iterable):
    for testable in iterable:
        if inspect.isawaitable(testable):
            return True

    return False
