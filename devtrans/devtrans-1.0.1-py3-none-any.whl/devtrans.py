#!/usr/bin/env python3

_dev2slp_con = dict({
    'क' : 'k',
    'ख' : 'K',
    'ग' : 'g',
    'घ' : 'G',
    'ङ' : 'N',
    'च' : 'c',
    'छ' : 'C',
    'ज' : 'j',
    'झ' : 'J',
    'ञ' : 'Y',
    'ट' : 'w',
    'ठ' : 'W',
    'ड' : 'q',
    'ढ' : 'Q',
    'ण' : 'R',
    'त' : 't',
    'थ' : 'T',
    'द' : 'd',
    'ध' : 'D',
    'न' : 'n',
    'प' : 'p',
    'फ' : 'P',
    'ब' : 'b',
    'भ' : 'B',
    'म' : 'm',
    'य' : 'y',
    'र' : 'r',
    'ल' : 'l',
    'व' : 'v',
    'श' : 'S',
    'ष' : 'z',
    'स' : 's',
    'ह' : 'h'})
_dev2slp_mar = dict({
    'ा' : 'A',
    'ि' : 'i',
    'ी' : 'I',
    'ु' : 'u',
    'ू' : 'U',
    'ृ' : 'f',
    'ॄ' : 'F',
    'ॢ' : 'x',
    'ॣ' : 'X',
    'े' : 'e',
    'ै' : 'E',
    'ो' : 'o',
    'ौ' : 'O'})
_dev2slp_oth = dict({
    'अ' : 'a',
    'आ' : 'A',
    'इ' : 'i',
    'ई' : 'I',
    'उ' : 'u',
    'ऊ' : 'U',
    'ऋ' : 'f',
    'ॠ' : 'F',
    'ऌ' : 'x',
    'ॡ' : 'X',
    'ए' : 'e',
    'ऐ' : 'E',
    'ओ' : 'o',
    'औ' : 'O',
    'ं' : 'M',
    'ः' : 'H',
    'ँ' : '~',
    '।' : '.',
    '॥' : '..',
    'ऽ' : '\'',
    '०' : '0',
    '१' : '1',
    '२' : '2',
    '३' : '3',
    '४' : '4',
    '५' : '5',
    '६' : '6',
    '७' : '7',
    '८' : '8',
    '९' : '9'})

_iast2slp_dbl = dict({
    'ai' : 'E',
    'au' : 'O',
    'kh' : 'K',
    'gh' : 'G',
    'ch' : 'C',
    'jh' : 'J',
    'ṭh' : 'W',
    'ḍh' : 'Q',
    'th' : 'T',
    'dh' : 'D',
    'ph' : 'P',
    'bh' : 'B'})
_iast2slp_oth = dict({
    'ā' : 'A',
    'ī' : 'I',
    'ū' : 'U',
    'ṛ' : 'f',
    'ṝ' : 'F',
    'ḷ' : 'x',
    'ḹ' : 'X',
    'ṃ' : 'M',
    'ḥ' : 'H',
    'ṁ' : '~',
    'ṅ' : 'N',
    'ñ' : 'Y',
    'ṭ' : 'w',
    'ḍ' : 'q',
    'ṇ' : 'R',
    'ś' : 'S',
    'ṣ' : 'z'})

_slp2dev_vow = {
    'a' : ['अ', ''],
    'A' : ['आ', 'ा'],
    'i' : ['इ', 'ि'],
    'I' : ['ई', 'ी'],
    'u' : ['उ', 'ु'],
    'U' : ['ऊ', 'ू'],
    'f' : ['ऋ', 'ृ'],
    'F' : ['ॠ', 'ॄ'],
    'x' : ['ऌ', 'ॢ'],
    'X' : ['ॡ', 'ॣ'],
    'e' : ['ए', 'े'],
    'E' : ['ऐ', 'ै'],
    'o' : ['ओ', 'ो'],
    'O' : ['औ', 'ौ']}
_slp2dev_con = {
    'k' : 'क',
    'K' : 'ख',
    'g' : 'ग',
    'G' : 'घ',
    'N' : 'ङ',
    'c' : 'च',
    'C' : 'छ',
    'j' : 'ज',
    'J' : 'झ',
    'Y' : 'ञ',
    'w' : 'ट',
    'W' : 'ठ',
    'q' : 'ड',
    'Q' : 'ढ',
    'R' : 'ण',
    't' : 'त',
    'T' : 'थ',
    'd' : 'द',
    'D' : 'ध',
    'n' : 'न',
    'p' : 'प',
    'P' : 'फ',
    'b' : 'ब',
    'B' : 'भ',
    'm' : 'म',
    'y' : 'य',
    'r' : 'र',
    'l' : 'ल',
    'v' : 'व',
    'S' : 'श',
    'z' : 'ष',
    's' : 'स',
    'h' : 'ह'}
_slp2dev_oth = {
    'M' : 'ं',
    'H' : 'ः',
    '~' : 'ँ',
    '\'' : 'ऽ'}
_slp2dev_num = {
    '0' : '०',
    '1' : '१',
    '2' : '२',
    '3' : '३',
    '4' : '४',
    '5' : '५',
    '6' : '६',
    '7' : '७',
    '8' : '८',
    '9' : '९'}

_slp2iast_dict = dict({
    'A' : 'ā',
    'I' : 'ī',
    'U' : 'ū',
    'f' : 'ṛ',
    'F' : 'ṝ',
    'x' : 'ḷ',
    'X' : 'ḹ',
    'E' : 'ai',
    'O' : 'au',
    'M' : 'ṃ',
    'H' : 'ḥ',
    '~' : 'ṁ',
    'K' : 'kh',
    'G' : 'gh',
    'N' : 'ṅ',
    'C' : 'ch',
    'J' : 'jh',
    'Y' : 'ñ',
    'w' : 'ṭ',
    'W' : 'ṭh',
    'q' : 'ḍ',
    'Q' : 'ḍh',
    'R' : 'ṇ',
    'T' : 'th',
    'D' : 'dh',
    'P' : 'ph',
    'B' : 'bh',
    'S' : 'ś',
    'z' : 'ṣ'})
_slp2iast_map = str.maketrans(_slp2iast_dict)

_slp2tex_dict = dict({
    'A' : '\={a}',
    'I' : '\={\i}',
    'U' : '\={u}',
    'f' : '\d{r}',
    'F' : '\={\d{r}}',
    'x' : '\d{l}',
    'X' : '\={\d{l}}',
    'E' : 'ai',
    'O' : 'au',
    'M' : '\d{m}',
    'H' : '\d{h}',
    '~' : '\.{m}',
    'K' : 'kh',
    'G' : 'gh',
    'N' : '\.{n}',
    'C' : 'ch',
    'J' : 'jh',
    'Y' : '\~{n}',
    'w' : '\d{t}',
    'W' : '\d{t}h',
    'q' : '\d{d}',
    'Q' : '\d{d}h',
    'R' : '\d{n}',
    'T' : 'th',
    'D' : 'dh',
    'P' : 'ph',
    'B' : 'bh',
    'S' : '\\\'{s}',
    'z' : '\d{s}'})
_slp2tex_map = str.maketrans(_slp2tex_dict)

_slp2wx_map = str.maketrans('fFxX~\'NYwWqQRtTdDz', 'qQLVzZfFtTdDNwWxXR')

_wx2slp_map = str.maketrans('qQLVzZfFtTdDNwWxXR', 'fFxX~\'NYwWqQRtTdDz')

def dev2iast(src):
    '''
    Converts Devanagari characters to
    International Alphabet for Sanskrit Transliteration (IAST) scheme
    '''
    return slp2iast(dev2slp(src))

def dev2slp(src):
    '''
    Converts Devanagari characters to
    Sanskrit Library Phonetic Basic notation
    '''
    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else None
        if now in _dev2slp_con:
            tgt += _dev2slp_con[now]
            if nxt == '्':
                inc += 1
            elif nxt not in _dev2slp_mar:
                tgt += 'a'
        elif now in _dev2slp_mar:
            tgt += _dev2slp_mar[now]
        elif now in _dev2slp_oth:
            tgt += _dev2slp_oth[now]
        else:
            tgt += now
        inc += 1
    return tgt

def dev2tex(src):
    '''
    Converts Devanagari characters to
    (La)TeX friendly notation for diacritic IAST
    '''
    return slp2tex(dev2slp(src))

def dev2wx(src):
    '''
    Converts Devanagari characters to WX scheme
    '''
    return slp2wx(dev2slp(src))

def iast2dev(src, convert_numbers=True):
    '''
    Converts International Alphabet for Sanskrit Transliteration (IAST) scheme to
    Devanagari characters
    '''
    return slp2dev(iast2slp(src), convert_numbers)

def iast2slp(src):
    '''
    Converts International Alphabet for Sanskrit Transliteration (IAST) scheme to
    Sanskrit Library Phonetic Basic notation
    '''
    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        if now + nxt in _iast2slp_dbl:
            tgt += _iast2slp_dbl[now + nxt]
            inc += 1
        elif now in _iast2slp_oth:
            tgt += _iast2slp_oth[now]
        else:
            tgt += now
        inc += 1
    return tgt

def iast2tex(src):
    '''
    Converts International Alphabet for Sanskrit Transliteration (IAST) scheme to
    (La)TeX friendly notation for diacritic IAST
    '''
    return slp2tex(iast2slp(src))

def iast2wx(src):
    '''
    Converts International Alphabet for Sanskrit Transliteration (IAST) scheme to
    WX scheme
    '''
    return slp2wx(iast2slp(src))

def slp2dev(src, convert_numbers=True):
    '''
    Converts Sanskrit Library Phonetics Basic notation to
    Devanagari characters
    '''
    tgt = ''
    boo = False
    inc = 0
    while inc < len(src):
        pre = src[inc-1] if inc > 1 else ''
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        if now in _slp2dev_con:
            tgt += _slp2dev_con[now]
            if nxt == 'a':
                inc += 1
            elif nxt in _slp2dev_vow:
                boo = True
            else:
                tgt += '्'
        elif now in _slp2dev_vow:
            if boo:
                tgt += _slp2dev_vow[now][1]
                boo = False
            else:
                tgt += _slp2dev_vow[now][0]
        elif now == '\'':
            if not pre or not nxt:
                tgt += now
            elif ord(pre) in range(65, 123) and \
                 ord(nxt) in range(65, 123):
                tgt += 'ऽ'
            else:
                tgt += now
        elif now in _slp2dev_oth:
            tgt += _slp2dev_oth[now]
        elif now in _slp2dev_num:
            if convert_numbers:
                tgt += _slp2dev_num[now]
            else:
                tgt += now
        elif now == '.':
            if nxt == '.':
                tgt += '॥'
                inc += 1
            else:
                tgt += '।'
        else:
            tgt += now
        inc += 1
    return tgt

def slp2iast(src):
    '''
    Converts Sanskrit Library Phonetic Basic notation to
    International Alphabet for Sanskrit Transliteration scheme
    '''
    return src.translate(_slp2iast_map)

def slp2tex(src):
    '''
    Converts Sanskrit Library Phonetic Basic notation to
    (La)TeX friendly notation for diacritic IAST
    '''
    return src.translate(_slp2tex_map)

def slp2wx(src):
    '''
    Converts Sanskrit Library Phonetic Basic notation to WX scheme
    '''
    return src.translate(_slp2wx_map)

def wx2dev(src, convert_numbers=True):
    '''
    Converts WX scheme to Devanagari characters
    '''
    return slp2dev(wx2slp(src), convert_numbers)

def wx2iast(src):
    '''
    Converts WX scheme to
    International Alphabet for Sanskrit Transliteration scheme
    '''
    return slp2iast(wx2slp(src))

def wx2slp(src):
    '''
    Converts WX scheme to Sanskrit Library Phonetic Basic notation
    '''
    return src.translate(_wx2slp_map)

def wx2tex(src):
    '''
    Converts WX scheme to
    (La)TeX friendly notation for diacritic IAST
    '''
    return slp2tex(wx2slp(src))
