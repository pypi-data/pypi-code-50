#! /usr/bin/env python3
'''The mood_ring module by Joshah Moors

This module is the python equivalent of a novelty mood ring.
It contains a Ring object that returns a string describing a mood.
A default set of moods is provided for out-of-the-box usage, but at time of
instantiation the selection of moods can be overwritten or extended.

Also, this is a trivial module intended to be a learning excecise for
packaging and distributing code.

'''
import random
import sys

if sys.version_info < (3, 6):
    from compat import choices
    random.choices = choices

_default_mood_map = {
    'stressed': 1,
    'nervous': 1,
    'unsettled': 1,
    'active': 1,
    'relaxed': 1,
    'lovable': 1,
    'romantic': 1,
    'happy': 1,
    'tired': 1,
    'calm': 1,
}


class Ring:
    def __init__(self, mood_map=_default_mood_map, **kwargs):
        if type(mood_map) == type([]):
            mood_map = {m: 1 for m in mood_map}
        elif type(mood_map) != type({}):
            raise TypeError('Argument \'mood_map\' only accepts list/dict objects')
        extended_map = kwargs.get('extend', {})
        if type(extended_map) == type([]):
            extended_map = {m: 1 for m in extended_map}
        elif type(extended_map) != type({}):
            raise TypeError('Keyword argument \'extend\' only accepts list/dict objects')
        mood_map.update(extended_map)
        self.mood_opts, self.mood_probs = zip(*[i for i in mood_map.items()])
        self.change()

    def __str__(self):
        return self.mood

    def __repr__(self):
        return self.mood

    def change(self):
        old_mood = getattr(self, 'mood', '')
        while old_mood == getattr(self, 'mood', ''):
            self.mood = random.choices(population=self.mood_opts,
                                       weights=self.mood_probs,
                                       k=1)[0]
