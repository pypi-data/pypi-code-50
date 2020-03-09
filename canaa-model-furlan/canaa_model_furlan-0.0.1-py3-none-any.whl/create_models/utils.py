from datetime import datetime
import getpass


def camel_to_snake(text: str):
    """
    Converts CamelCase to snake_case
    """
    letters = []
    last_letter = 'a'
    for letter in text:
        if (letter.isupper() or letter.isdigit()) and \
            not (last_letter.isupper() or last_letter.isdigit()) and \
                len(letters) > 0:
            letters.append('_'+letter.lower())
        else:
            letters.append(letter.lower())
        last_letter = letter
    return "".join(letters)


def snake_to_camel(text: str):
    letters = []
    got_underline = True
    for letter in text:
        if not letter.isalpha():
            got_underline = True
            if letter == '_':
                continue

        if got_underline:
            letter = letter.upper()
            got_underline = False
        letters.append(letter)

    return "".join(letters)


def get_words(line: str, nwords: int = 0, sep: str = ';'):
    words = [word.replace('"', '').strip() for word in line.split(sep)]
    if nwords > 0:
        while len(words) < nwords:
            words.append(None)
    else:
        nwords = len(words)

    return words[:nwords]


def padr(string: str, size: int):
    if size > 0:
        layout = "{0:"+str(size)+"}"
        return layout.format(string)

    return string


def created_by():
    return "# CREATED BY CANAA-BASE-MODEL-CREATOR IN {0} : {1}".format(
        datetime.now(),
        getpass.getuser()
    )
