#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Result:
    @property
    def value(self):
        raise NotImplementedError  # pragma: no cover


class Component:
    def to_result(self) -> Result:
        raise NotImplementedError  # pragma: no cover
