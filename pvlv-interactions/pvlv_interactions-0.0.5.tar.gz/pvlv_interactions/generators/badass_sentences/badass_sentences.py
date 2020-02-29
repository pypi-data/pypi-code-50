from random import randrange
import os
from enum import Enum


CHUCK_NORRIS = "Chuck Norris"
JOHN_WICK = "John Wick"

full_path = os.path.dirname(__file__)
filename_eng = '{}/data/eng_badass_sentences.txt'.format(full_path)
filename_ita = '{}/data/ita_badass_sentences.txt'.format(full_path)


def read_file(filename):
    sentences = []
    with open(filename) as file:
        for idx, line in enumerate(file.readlines()):
            sentences.append(line[:-1])
    return sentences


class Language(Enum):
    eng = 'eng'
    ita = 'ita'


eng_sentences = read_file(filename_eng)
len_eng = len(eng_sentences)
ita_sentences = read_file(filename_ita)
len_ita = len(eng_sentences)


triggers = [
    [CHUCK_NORRIS, 'chuck', 'norris'],
    [JOHN_WICK, 'john', 'wick'],
]


class BadassSentences(object):

    @staticmethod
    def generate_sentence(language, character=None, number=None):

        if language == Language.ita:
            sentences = ita_sentences
            len_list = len_ita
        else:
            sentences = eng_sentences
            len_list = len_eng

        if number is None:
            # generate a random number to pick a random sentence
            sn = randrange(0, len_list - 1)
        else:
            sn = number - 1

        output = '{} - {}:\n'.format(character.upper(), sn + 1)
        output += sentences[sn].replace('%%%', character.title())

        return output

    def message_reply(self, language, text):
        text_list = text.split(' ')
        for character in triggers:
            for trigger in character:
                if trigger in text_list:
                    return '{}\n'.format(self.generate_sentence(language, character=character[0]))
        return ''
