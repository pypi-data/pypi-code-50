def shift_letter(letter, places):
    """
    shifts a letter a given number of places, keeping the same letter case
    """
    if not letter.isalpha():
        return letter
    letter_num = ord(letter)
    letter_num += places
    if letter.isupper():
        while letter_num < ord("A"):
            letter_num += 26
        while letter_num > ord("Z"):
            letter_num -= 26
    if letter.islower():
        while letter_num < ord("a"):
            letter_num += 26
        while letter_num > ord("z"):
            letter_num -= 26
    return chr(letter_num)


def shift(word, places):
    """
    shifts all letters in a string a given number of places,
    keeping letters in the same case
    """
    shifted_word = "".join([shift_letter(c, places) for c in word])
    return shifted_word


def rot13(word):
    """
    applies rot13 to a string, keeping letters in the same case
    """
    return shift(word, 13)
