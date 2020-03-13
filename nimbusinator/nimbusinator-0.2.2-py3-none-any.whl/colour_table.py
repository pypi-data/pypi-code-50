# RM Nimbus colour tables.  

# The Nimbus provided 16 colours in low-resolution mode.  In high
# resolution mode only 4 colours were available, although you can
# assign any of the 16 colours to the 4 slots in the palette.

# The RGB colour table
colour_table = {
    #     R    G    B
    0:  (  0,   0,   0),    # black
    1:  (  0,   0, 170),    # dark blue
    2:  (170,   0,   0),    # dark red
    3:  (170,   0, 170),    # purple
    4:  (  0, 170,   0),    # dark green
    5:  (  0, 170, 170),    # dark cyan
    6:  (170,  84,   0),    # brown
    7:  (170, 170, 170),    # light grey
    8:  ( 84,  84,  84),    # dark grey
    9:  ( 84,  84, 255),    # light blue
    10: (255,  84,  84),    # light red
    11: (255,  84, 255),    # light purple
    12: ( 84, 255,  84),    # light green
    13: ( 84, 255, 255),    # light cyan
    14: (255, 255,  84),    # yellow
    15: (255, 255, 255)     # white
}

# Default colours.  These are the default colour assignments for
# hi and lo resolution modes.  
default_colours = {
    'lo': {
        0:  0,    # black
        1:  1,    # dark blue
        2:  2,    # dark red
        3:  3,    # purple
        4:  4,    # dark green
        5:  5,    # dark cyan
        6:  6,    # brown
        7:  7,    # light grey
        8:  8,    # dark grey
        9:  9,    # light blue
        10: 10,   # light red
        11: 11,   # light purple
        12: 12,   # light green
        13: 13,   # light cyan
        14: 14,   # yellow
        15: 15    # white
    },
    'hi': {
        0: 1,     # dark blue
        1: 4,     # dark green
        2: 10,    # light red
        3: 15     # white
    }
}

