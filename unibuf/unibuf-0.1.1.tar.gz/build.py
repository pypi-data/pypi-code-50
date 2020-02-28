# -*- coding:utf-8 -*-
#
# Copyright (C) 2020, Maximilian Köhl <mkoehl@cs.uni-saarland.de>

from __future__ import annotations

from distutils.core import Extension


def build(setup_kwargs):
    setup_kwargs.update(
        {"ext_modules": [Extension("unibuf._unibuf", ["unibuf/_unibuf.c"])]}
    )
