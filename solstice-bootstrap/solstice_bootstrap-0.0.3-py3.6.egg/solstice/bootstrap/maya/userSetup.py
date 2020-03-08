#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization for Solstice Tools
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

print('=' * 100)
print('| Solstice ArtellaPipe | > Loading Solstice Tools')

try:
    import solstice.loader
    from maya import cmds
    cmds.evalDeferred('solstice.loader.init(import_libs=True)')
    print('| Solstice ArtellaPipe | Solstice loaded successfully!')
    print('=' * 100)
except Exception as e:
    try:
        import solstice.loader
        solstice.loader.init(import_libs=True)
        print('| Solstice ArtellaPipe | Solstice loaded successfully!')
        print('=' * 100)
    except Exception as exc:
        import traceback
        print('ERROR: Impossible to load Solstice Tools, contact TD!')
        print('{} | {}'.format(exc, traceback.format_exc()))
