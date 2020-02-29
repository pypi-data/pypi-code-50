#!/usr/bin/env python3
import os.path

__version__ = '0.1.1'


def _jupyter_nbextension_paths():
    return [dict(
        section='notebook',
        src=os.path.join('static', 'multiselection'),
        dest='multiselection',
        require='multiselection/multiselection',
    )]
