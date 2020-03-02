#!/usr/bin/env python3
"""
Copyright 2015 Hippos Technical Systems BV.

@author: Larry Myerscough (aka papahippo)
"""
# from .pyraft import PyRaft
# from .freqraft import FreqRaft

if __name__ == '__main__':
    from .raft import main
    from .abcraft import AbcRaft

    main( Plugins=(AbcRaft,))  #  PyRaft))  # , FreqRaft))

