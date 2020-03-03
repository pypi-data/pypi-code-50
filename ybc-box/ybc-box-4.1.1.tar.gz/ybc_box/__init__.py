import os

if 'YBC_ENV' in os.environ:
    from ybc_box.ide_box import buttonbox
    from ybc_box.ide_box import choicebox
    from ybc_box.ide_box import codebox
    from ybc_box.ide_box import enterbox
    from ybc_box.ide_box import fileopenbox
    from ybc_box.ide_box import indexbox
    from ybc_box.ide_box import intbox
    from ybc_box.ide_box import integerbox
    from ybc_box.ide_box import msgbox
    from ybc_box.ide_box import multchoicebox
    from ybc_box.ide_box import multenterbox
    from ybc_box.ide_box import multpasswordbox
    from ybc_box.ide_box import passwordbox
    from ybc_box.ide_box import tablebox
    from ybc_box.ide_box import textbox
    from ybc_box.ide_box import ynbox
else:
    from ybc_box.native_box import buttonbox
    from ybc_box.native_box import choicebox
    from ybc_box.native_box import codebox
    from ybc_box.native_box import enterbox
    from ybc_box.native_box import fileopenbox
    from ybc_box.native_box import indexbox
    from ybc_box.native_box import intbox
    from ybc_box.native_box import integerbox
    from ybc_box.native_box import msgbox
    from ybc_box.native_box import multchoicebox
    from ybc_box.native_box import multenterbox
    from ybc_box.native_box import multpasswordbox
    from ybc_box.native_box import passwordbox
    from ybc_box.native_box import tablebox
    from ybc_box.native_box import textbox
    from ybc_box.native_box import ynbox

__all__ = [
    'buttonbox',
    'choicebox',
    'codebox',
    'enterbox',
    'fileopenbox',
    'indexbox',
    'intbox',
    'integerbox',
    'msgbox',
    'multchoicebox',
    'multenterbox',
    'multpasswordbox',
    'passwordbox',
    'tablebox',
    'textbox',
    'ynbox',
]

__version__ = '4.1.1'
