clipboard_data_types_str = ['ansi_std_text',
                            'ansi_msl_text',
                            'ascii_dif_text',
                            '8bit_dos_text',
                            'unicode_std_text',
                            'ansi_dsp_text',
                            'hbitmap_gdi_std_object',
                            'hbitmap_gdi_dsp_object',
                            'bitmapinfo_std_structure',
                            'metafilepict_std_structure',
                            'metafilepict_dsp_structure',
                            'tiff_std_image',
                            'hpalette_gdi_std_object',
                            'pendata_std_data',
                            'riff_std_audio',
                            'wave_std_audio',
                            'henhmetafile_std_handle',
                            'henhmetafile_dsp_handle',
                            'dropfiles_std_list',
                            'dword_std_lcid',
                            'bitmapv5header_std_structure']
clipboard_data_types_int = [1,
                            4,
                            5,
                            7,
                            13,
                            129,
                            2,
                            130,
                            8,
                            3,
                            131,
                            6,
                            9,
                            10,
                            11,
                            12,
                            14,
                            142,
                            15,
                            16,
                            17]

from winclip_DEVELOPING.winclip32.errors import *

ERROR = 0
try:
    import win32clipboard
except:
    ERROR = 1

if ERROR:
    raise SomethingWentWrong





def get_clipboard_data_types_info():
    # information got from https://www.codeproject.com/Reference/1091137/Windows-Clipboard-Formats
    print("| DATA TYPE                    | DATA TYPE KEYS                                        | ABOUT")
    print("|------------------------------|-------------------------------------------------------|------------------------------------------------")
    print("| ANSI text                    | type_keys: 1 or 'ansi_std_text'                       | standart text")
    print("|                              |                                                       |")
    print("| ANSI text                    | type_keys: 4 or 'ansi_msl_text'                       | Microsoft Symbolic Link")
    print("|                              |                                                       |")
    print("| ASCII text                   | type_keys: 5 or 'ascii_dif_text'                      | Software Arts Data Interchange Format")
    print("|                              |                                                       |")
    print("| 8-bit DOS text               | type_keys: 7 or '8bit_dos_text'                       | stardart text")
    print("|                              |                                                       |")
    print("| UNICODE text                 | type_keys: 13 or 'unicode_std_text'                   | stardart text")
    print("|                              |                                                       |")
    print("| ANSI text                    | type_keys: 129 or 'ansi_dsp_text'                     | standart text")
    print("|                              |                                                       |")
    print("| HBITMAP (GDI) object         | type_keys: 2 or 'hbitmap_gdi_std_object'              | Handle to a bitmap (GDI object)")
    print("|                              |                                                       |")
    print("| HBITMAP (GDI) object         | type_keys: 130 or 'hbitmap_gdi_dsp_object'            | Handle to a bitmap (GDI object)")
    print("|                              |                                                       |")
    print("| BITMAPINFO structure         | type_keys: 8 or 'bitmapinfo_std_structure'            | Structure followed by bitmap bits")
    print("|                              |                                                       |")
    print("| METAFILEPICT picture         | type_keys: 3 or 'metafilepict_std_structure'          | Windows-Format Metafiles picture")
    print("|                              |                                                       |")
    print("| METAFILEPICT picture         | type_keys: 131 or 'metafilepict_dsp_structure'        | Windows-Format Metafiles picture")
    print("|                              |                                                       |")
    print("| TIFF image                   | type_keys: 6 or 'tiff_std_image'                      | TIFF image")
    print("|                              |                                                       |")
    print("| HPALETTE                     | type_keys: 9 or 'hpalette_gdi_std_object'             | Handle to a color palette (GDI object)")
    print("|                              |                                                       |")
    print("| PENDATA extension data       | type_keys: 10 or 'pendata_std_data'                   | Windows 3.1 pen extension data")
    print("|                              |                                                       |")
    print("| RIFF audio                   | type_keys: 11 or 'riff_std_audio'                     | Resource Interchange File Format (RIFF) audio")
    print("|                              |                                                       |")
    print("| WAVE audio                   | type_keys: 12 or 'wave_std_audio'                     | WAVE audio")
    print("|                              |                                                       |")
    print("| HENHMETAFILE handle          | type_keys: 14 or 'henhmetafile_std_handle'            | Enhanced-Format Metafiles handle")
    print("|                              |                                                       |")
    print("| HENHMETAFILE handle          | type_keys: 142 or 'henhmetafile_dsp_handle'           | Enhanced-Format Metafiles handle")
    print("|                              |                                                       |")
    print("| DROPFILES list               | type_keys: 15 or 'dropfiles_std_list'                 | List of file names")
    print("|                              |                                                       |")
    print("| DWORD (LCID)                 | type_keys: 16 or 'dword_std_lcid'                     | LCID for ansi_std_text to unicode_std_text conversion")
    print("|                              |                                                       |")
    print("| BITMAPV5HEADER structure     | type_keys: 17 or 'bitmapv5header_std_structure'       | Structure followed by bitmap bits")
    print("|                              |                                                       |")
    print("| another data                 | type_key: int                                         | another data")

def get_clipboard_data(type_key):
    ERROR = 0
    try:
        assert type(type_key) is int or type(type_key) is str
    except:
        ERROR = 1

    if ERROR:
        raise InvalidClipBoardDataTypeKeyGiven(type(type_key).__name__)
    clipboarddata = None
    ERROR = 0
    if type_key in clipboard_data_types_int:
        try:
            win32clipboard.OpenClipboard()
            clipboarddata = win32clipboard.GetClipboardData(type_key)
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1

        if ERROR:
            win32clipboard.CloseClipboard()
            raise ClipBoardDataTypeIsNotAvailable(type_key)
    elif type_key in clipboard_data_types_str:
        try:
            win32clipboard.OpenClipboard()
            clipboarddata = win32clipboard.GetClipboardData(clipboard_data_types_int[clipboard_data_types_str.index(type_key)])
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1

        if ERROR:
            raise ClipBoardDataTypeIsNotAvailable(type_key)
    else:
        raise UnknownClipBoardDataTypeKeyGiven(type_key)

    return clipboarddata

def is_clipboard_data_type_available(type_key):
    ERROR = 0
    try:
        assert type(type_key) is str or type(type_key) is int
    except:
        ERROR = 1
    if ERROR:
        raise InvalidClipBoardDataTypeKeyGiven(type_key)

    if type(type_key) is str:
        if type_key not in clipboard_data_types_str:
            raise UnknownStrClipBoardDataType(type_key)
        else:
            return bool(win32clipboard.IsClipboardFormatAvailable(
                clipboard_data_types_int[clipboard_data_types_str.index(type_key)]))
    else:
        return bool(win32clipboard.IsClipboardFormatAvailable(type_key))


def set_clipboard_data(type_key, data):
    ERROR = 0
    try:
        assert type(type_key) is str or type(type_key) is int
    except:
        ERROR = 1
    if ERROR:
        raise InvalidClipBoardDataTypeKeyGiven(type_key)
    ERROR = 0
    if type(type_key) is int:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(type_key, data)
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1


    elif type(type_key) is str:
        try:
            win32clipboard.OpenClipboard()
            win32clipboard.SetClipboardData(clipboard_data_types_int[clipboard_data_types_str.index(type_key)], data)
            win32clipboard.CloseClipboard()
        except:
            ERROR = 1

    if ERROR:
        win32clipboard.CloseClipboard()
        raise InvalidClipBoardTypeKeyOrDataGiven


def count_clipboard_data_types():
    try:
        n = win32clipboard.CountClipboardFormats()
        return n
    except:
        return 0

def empty_clipboard():
    ERROR = 0
    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
    except:
        ERROR = 1
    if ERROR:
        raise SomethingWentWrong






