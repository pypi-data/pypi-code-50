#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Talk']

class Talk:
    def __init__(self, talkative):
        self.talkative = talkative

    def __call__(self, say, *args, **kwargs):
        if self.talkative:
            try:
                print(say.format(*args, **kwargs))
            except:
                print("echec de l'affichage")