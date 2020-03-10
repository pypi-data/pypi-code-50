#  Copyright (c) 2020 Maksim Penkov
#  SPDX-License-Identifier: Apache-2.0

import enum
import inspect
import typing


class BindingScope(enum.Enum):
    SINGLETON = 'SINGLETON'
    UNIQUE = 'UNIQUE'


class FactoryType(enum.Enum):
    SIMPLE = 'SIMPLE'
    CONTEXT = 'CONTEXT'


class ArgFactory:
    def __init__(self, factory, factory_type):
        self.factory = factory
        self.factory_type = factory_type


class ArgInstance:
    def __init__(self, instance):
        self.instance = instance


class ScopedInitializer(typing.NamedTuple):
    scope: BindingScope
    initializer: typing.Any


class DependencyContext:
    def __init__(self):
        self.names = {}
        self.classes = {}

    def sub_context(self):
        subctx = DependencyContext()
        subctx.names = self.names.copy()
        subctx.classes = self.classes.copy()

        if hasattr(self, 'stack'):
            subctx.stack = self.stack

        return subctx

    def _target(self, to):
        assert to is not None

        if isinstance(to, str):
            return self.names
        elif inspect.isclass(to):
            return self.classes

        raise ValueError()

    def bind(self, what, to=None, scope=None):
        to = to or _deduce_to(what)

        target = self._target(to)

        if scope is None:
            scope = _default_scope(what)

        if inspect.isclass(what):
            initializer = ArgFactory(
                factory=what,
                factory_type=FactoryType.SIMPLE,
            )
        else:
            initializer = ArgInstance(
                instance=what,
            )

        target[to] = ScopedInitializer(
            scope=scope,
            initializer=initializer,
        )

    def bind_factory(self, factory, to=None, factory_type=None, scope=None):
        to = to or _deduce_to(factory)

        assert factory_type is not None

        scope = scope or BindingScope.UNIQUE
        target = self._target(to)

        target[to] = ScopedInitializer(
            scope=scope,
            initializer=ArgFactory(
                factory=factory,
                factory_type=factory_type,
            )
        )


def _deduce_abc(impl_cls):
    for step in inspect.getmro(impl_cls):
        if inspect.isabstract(step):
            return step

    return impl_cls


def _deduce_to(what):
    if inspect.isclass(what):
        return _deduce_abc(what)

    ret = inspect.signature(what).return_annotation

    if ret == inspect.Signature.empty:
        return None

    return ret


def _default_scope(of):
    return BindingScope.SINGLETON
