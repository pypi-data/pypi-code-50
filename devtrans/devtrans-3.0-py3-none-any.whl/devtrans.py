#!/usr/bin/env python3

supported_decoders = ['dev', 'hk', 'iast', 'itrans', 'slp', 'vel', 'wx']
supported_encoders = supported_decoders + ['tex']


def dev2slp(src):
    consonants = {
        'क': 'k',
        'ख': 'K',
        'ग': 'g',
        'घ': 'G',
        'ङ': 'N',
        'च': 'c',
        'छ': 'C',
        'ज': 'j',
        'झ': 'J',
        'ञ': 'Y',
        'ट': 'w',
        'ठ': 'W',
        'ड': 'q',
        'ढ': 'Q',
        'ण': 'R',
        'त': 't',
        'थ': 'T',
        'द': 'd',
        'ध': 'D',
        'न': 'n',
        'प': 'p',
        'फ': 'P',
        'ब': 'b',
        'भ': 'B',
        'म': 'm',
        'य': 'y',
        'र': 'r',
        'ल': 'l',
        'व': 'v',
        'श': 'S',
        'ष': 'z',
        'स': 's',
        'ह': 'h'}
    vowel_marks = {
        'ा': 'A',
        'ि': 'i',
        'ी': 'I',
        'ु': 'u',
        'ू': 'U',
        'ृ': 'f',
        'ॄ': 'F',
        'ॢ': 'x',
        'ॣ': 'X',
        'े': 'e',
        'ै': 'E',
        'ो': 'o',
        'ौ': 'O'}
    others = {
        'अ': 'a',
        'आ': 'A',
        'इ': 'i',
        'ई': 'I',
        'उ': 'u',
        'ऊ': 'U',
        'ऋ': 'f',
        'ॠ': 'F',
        'ऌ': 'x',
        'ॡ': 'X',
        'ए': 'e',
        'ऐ': 'E',
        'ओ': 'o',
        'औ': 'O',
        'ं': 'M',
        'ः': 'H',
        'ँ': '~',
        '।': '.',
        '॥': '..',
        'ऽ': '\'',
        '०': '0',
        '१': '1',
        '२': '2',
        '३': '3',
        '४': '4',
        '५': '5',
        '६': '6',
        '७': '7',
        '८': '8',
        '९': '9'}

    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else None
        if now in consonants:
            tgt += consonants[now]
            if nxt == '्':
                inc += 1
            elif nxt not in vowel_marks:
                tgt += 'a'
        elif now in vowel_marks:
            tgt += vowel_marks[now]
        elif now in others:
            tgt += others[now]
        else:
            tgt += now
        inc += 1
    return tgt


def hk2slp(src):
    trios = {
        'lRR': 'X'}
    duos = {
        'RR': 'F',
        'lR': 'x',
        'ai': 'E',
        'au': 'O',
        'kh': 'K',
        'gh': 'G',
        'ch': 'C',
        'jh': 'J',
        'Th': 'W',
        'Dh': 'Q',
        'th': 'T',
        'dh': 'D',
        'ph': 'P',
        'bh': 'B'}
    monos = {
        'R': 'f',
        'G': 'N',
        'J': 'Y',
        'T': 'w',
        'D': 'q',
        'N': 'R',
        'z': 'S',
        'S': 'z'}

    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        aft = src[inc+2] if inc < len(src) - 2 else ''
        if now + nxt + aft in trios:
            tgt += trios[now + nxt + aft]
            inc += 2
        elif now + nxt in duos:
            tgt += duos[now + nxt]
            inc += 1
        elif now in monos:
            tgt += monos[now]
        else:
            tgt += now
        inc += 1
    return tgt


def iast2slp(src):
    duos = {
        'ai': 'E',
        'au': 'O',
        'kh': 'K',
        'gh': 'G',
        'ch': 'C',
        'jh': 'J',
        'ṭh': 'W',
        'ḍh': 'Q',
        'th': 'T',
        'dh': 'D',
        'ph': 'P',
        'bh': 'B'}
    monos = {
        'ā': 'A',
        'ī': 'I',
        'ū': 'U',
        'ṛ': 'f',
        'ṝ': 'F',
        'ḷ': 'x',
        'ḹ': 'X',
        'ṃ': 'M',
        'ḥ': 'H',
        'ṁ': '~',
        'ṅ': 'N',
        'ñ': 'Y',
        'ṭ': 'w',
        'ḍ': 'q',
        'ṇ': 'R',
        'ś': 'S',
        'ṣ': 'z'}

    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        if now + nxt in duos:
            tgt += duos[now + nxt]
            inc += 1
        elif now in monos:
            tgt += monos[now]
        else:
            tgt += now
        inc += 1
    return tgt


def itrans2slp(src):
    trios = {
        'RRi': 'f',
        'R^i': 'f',
        'RRI': 'F',
        'R^I': 'F',
        'LLi': 'x',
        'L^i': 'x',
        'LLI': 'X',
        'L^I': 'X'}
    duos = {
        'aa': 'A',
        'ii': 'I',
        'uu': 'U',
        'ai': 'E',
        'au': 'O',
        '.m': 'M',
        '.n': 'M',
        '.N': '~',
        '.a': "'",
        'kh': 'K',
        'gh': 'G',
        '~N': 'N',
        'ch': 'c',
        'Ch': 'C',
        'jh': 'J',
        '~n': 'Y',
        'Th': 'W',
        'Dh': 'Q',
        'th': 'T',
        'dh': 'D',
        'ph': 'P',
        'bh': 'B',
        'sh': 'S',
        'Sh': 'z'}
    monos = {
        'T': 'w',
        'D': 'q',
        'N': 'R',
        'w': 'v'}

    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        aft = src[inc+2] if inc < len(src) - 2 else ''
        if now + nxt + aft in trios:
            tgt += trios[now + nxt + aft]
            inc += 2
        elif now + nxt in duos:
            tgt += duos[now + nxt]
            inc += 1
        elif now in monos:
            tgt += monos[now]
        else:
            tgt += now
        inc += 1
    return tgt


def slp2dev(src, convert_numbers=True):
    vowels = {
        'a': ['अ', ''],
        'A': ['आ', 'ा'],
        'i': ['इ', 'ि'],
        'I': ['ई', 'ी'],
        'u': ['उ', 'ु'],
        'U': ['ऊ', 'ू'],
        'f': ['ऋ', 'ृ'],
        'F': ['ॠ', 'ॄ'],
        'x': ['ऌ', 'ॢ'],
        'X': ['ॡ', 'ॣ'],
        'e': ['ए', 'े'],
        'E': ['ऐ', 'ै'],
        'o': ['ओ', 'ो'],
        'O': ['औ', 'ौ']}
    consonants = {
        'k': 'क',
        'K': 'ख',
        'g': 'ग',
        'G': 'घ',
        'N': 'ङ',
        'c': 'च',
        'C': 'छ',
        'j': 'ज',
        'J': 'झ',
        'Y': 'ञ',
        'w': 'ट',
        'W': 'ठ',
        'q': 'ड',
        'Q': 'ढ',
        'R': 'ण',
        't': 'त',
        'T': 'थ',
        'd': 'द',
        'D': 'ध',
        'n': 'न',
        'p': 'प',
        'P': 'फ',
        'b': 'ब',
        'B': 'भ',
        'm': 'म',
        'y': 'य',
        'r': 'र',
        'l': 'ल',
        'v': 'व',
        'S': 'श',
        'z': 'ष',
        's': 'स',
        'h': 'ह'}
    others = {
        'M': 'ं',
        'H': 'ः',
        '~': 'ँ',
        "'": 'ऽ'}
    digits = {
        '0': '०',
        '1': '१',
        '2': '२',
        '3': '३',
        '4': '४',
        '5': '५',
        '6': '६',
        '7': '७',
        '8': '८',
        '9': '९'}

    tgt = ''
    boo = False
    inc = 0
    while inc < len(src):
        pre = src[inc-1] if inc > 1 else ''
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        if now in consonants:
            tgt += consonants[now]
            if nxt == 'a':
                inc += 1
            elif nxt in vowels:
                boo = True
            else:
                tgt += '्'
        elif now in vowels:
            if boo:
                tgt += vowels[now][1]
                boo = False
            else:
                tgt += vowels[now][0]
        elif now == '\'':
            if not pre or not nxt:
                tgt += now
            elif ord(pre) in range(65, 123) and ord(nxt) in range(65, 123):
                tgt += 'ऽ'
            else:
                tgt += now
        elif now in others:
            tgt += others[now]
        elif now in digits:
            if convert_numbers:
                tgt += digits[now]
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


def slp2hk(src):
    char_map = {
        'f': 'R',
        'F': 'RR',
        'x': 'lR',
        'X': 'lRR',
        'E': 'ai',
        'O': 'au',
        'K': 'kh',
        'G': 'gh',
        'N': 'G',
        'C': 'ch',
        'J': 'jh',
        'Y': 'J',
        'w': 'T',
        'W': 'Th',
        'q': 'D',
        'Q': 'Dh',
        'R': 'N',
        'T': 'th',
        'D': 'dh',
        'P': 'ph',
        'B': 'bh',
        'S': 'z',
        'z': 'S'}
    return src.translate(str.maketrans(char_map))


def slp2iast(src):
    char_map = {
        'A': 'ā',
        'I': 'ī',
        'U': 'ū',
        'f': 'ṛ',
        'F': 'ṝ',
        'x': 'ḷ',
        'X': 'ḹ',
        'E': 'ai',
        'O': 'au',
        'M': 'ṃ',
        'H': 'ḥ',
        '~': 'ṁ',
        'K': 'kh',
        'G': 'gh',
        'N': 'ṅ',
        'C': 'ch',
        'J': 'jh',
        'Y': 'ñ',
        'w': 'ṭ',
        'W': 'ṭh',
        'q': 'ḍ',
        'Q': 'ḍh',
        'R': 'ṇ',
        'T': 'th',
        'D': 'dh',
        'P': 'ph',
        'B': 'bh',
        'S': 'ś',
        'z': 'ṣ'}
    return src.translate(str.maketrans(char_map))


def slp2itrans(src):
    char_map = {
        'f': 'RRi',
        'F': 'RRI',
        'x': 'LLi',
        'X': 'LLI',
        'E': 'ai',
        'O': 'au',
        '~': '.N',
        "'": '.a',
        'K': 'kh',
        'G': 'gh',
        'N': '~N',
        'c': 'ch',
        'C': 'Ch',
        'J': 'jh',
        'Y': '~n',
        'w': 'T',
        'W': 'Th',
        'q': 'D',
        'Q': 'Dh',
        'R': 'N',
        'T': 'th',
        'D': 'dh',
        'P': 'ph',
        'B': 'bh',
        'S': 'sh',
        'z': 'Sh'}
    return src.translate(str.maketrans(char_map))


def slp2tex(src):
    char_map = {
        'A': r'\={a}',
        'I': r'\={\i}',
        'U': r'\={u}',
        'f': r'\d{r}',
        'F': r'\={\d{r}}',
        'x': r'\d{l}',
        'X': r'\={\d{l}}',
        'E': 'ai',
        'O': 'au',
        'M': r'\d{m}',
        'H': r'\d{h}',
        '~': r'\.{m}',
        'K': 'kh',
        'G': 'gh',
        'N': r'\.{n}',
        'C': 'ch',
        'J': 'jh',
        'Y': r'\~{n}',
        'w': r'\d{t}',
        'W': r'\d{t}h',
        'q': r'\d{d}',
        'Q': r'\d{d}h',
        'R': r'\d{n}',
        'T': 'th',
        'D': 'dh',
        'P': 'ph',
        'B': 'bh',
        'S': r'\'{s}',
        'z': r'\d{s}'}
    return src.translate(str.maketrans(char_map))


def slp2vel(src):
    char_map = {
        'A': 'aa',
        'I': 'ii',
        'U': 'uu',
        'f': '.r',
        'F': '.rr',
        'x': '.l',
        'X': '.ll',
        'E': 'ai',
        'O': 'au',
        'M': '.m',
        'H': '.h',
        '~': '/',
        "'": '.a',
        'K': 'kh',
        'G': 'gh',
        'N': '"n',
        'C': 'ch',
        'J': 'jh',
        'Y': '~n',
        'w': '.t',
        'W': '.th',
        'q': '.d',
        'Q': '.dh',
        'R': '.n',
        'T': 'th',
        'D': 'dh',
        'P': 'ph',
        'B': 'bh',
        'S': '"s',
        'z': '.s'}
    return src.translate(str.maketrans(char_map))


def slp2wx(src):
    char_map = str.maketrans("fFxX~'NYwWqQRtTdDz", 'qQLVzZfFtTdDNwWxXR')
    return src.translate(char_map)


def vel2slp(src):
    trios = {
        '.rr': 'F',
        '.ll': 'X',
        '.th': 'W',
        '.dh': 'Q'}
    duos = {
        'aa': 'A',
        'ii': 'I',
        'uu': 'U',
        '.r': 'f',
        '.l': 'x',
        'ai': 'E',
        'au': 'O',
        '.m': 'M',
        '.h': 'H',
        '.a': "'",
        'kh': 'K',
        'gh': 'G',
        '"n': 'N',
        'ch': 'C',
        'jh': 'J',
        '~n': 'Y',
        '.t': 'w',
        '.d': 'q',
        '.n': 'R',
        'th': 'T',
        'dh': 'D',
        'ph': 'P',
        'bh': 'B',
        '"s': 'S',
        '.s': 'z'}
    monos = {
        '/': '~'}

    tgt = ''
    inc = 0
    while inc < len(src):
        now = src[inc]
        nxt = src[inc+1] if inc < len(src) - 1 else ''
        aft = src[inc+2] if inc < len(src) - 2 else ''
        if now + nxt + aft in trios:
            tgt += trios[now + nxt + aft]
            inc += 2
        elif now + nxt in duos:
            tgt += duos[now + nxt]
            inc += 1
        elif now in monos:
            tgt += monos[now]
        else:
            tgt += now
        inc += 1
    return tgt


def wx2slp(src):
    char_map = str.maketrans('qQLVzZfFtTdDNwWxXR', "fFxX~'NYwWqQRtTdDz")
    return src.translate(char_map)


def codec_builder(dec, enc):
    '''
    To dynamically build modules for decoder-encoder pairs
    which are not hard coded. The built module will convert
    input text format into SLP notation and the SLP text
    will further be converted into the output format.
    '''
    if enc == 'dev':
        def template(txt, convert_numbers=True):
            txt = eval(f'{dec}2slp')(txt)
            txt = eval(f'slp2{enc}')(txt, convert_numbers)
            return txt
    else:
        def template(txt):
            txt = eval(f'{dec}2slp')(txt)
            txt = eval(f'slp2{enc}')(txt)
            return txt
    template.__name__ = f'{dec}2{enc}'
    return template


codecs = [(d, e)
          for d in supported_decoders
          for e in supported_encoders
          if d != e]

for dec, enc in codecs:
    if f'{dec}2{enc}' not in vars():
        vars()[f'{dec}2{enc}'] = codec_builder(dec, enc)

del supported_decoders, supported_encoders, codecs, codec_builder, dec, enc
