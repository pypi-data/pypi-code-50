import os
from random import randrange
from enum import Enum

full_path = os.path.dirname(__file__)
filename = '{}/data/base.txt'.format(full_path)

words = []
with open(filename) as file:
    for idx, line in enumerate(file.readlines()):
        words.append(line[:-1])
len_words = len(words)


class Gender(Enum):
    male = 1
    female = 2


class GenderConversion:
    male = 'o'
    female = 'a'


genders = {
    'dio': Gender.male,
    'madonna': Gender.female,
    'gesù': Gender.male,
    'allah': Gender.male,
    'puttana': Gender.female
}
len_genders = len(genders)
triggers = list(genders.keys())


class BadWordsGenerator(object):

    @staticmethod
    def __format_word(word: str, gender: Gender):
        if gender == Gender.male:
            return word.replace('%%%', GenderConversion.male)
        if gender == Gender.female:
            return word.replace('%%%', GenderConversion.female)

    def generate_sentence(self, language, character=None, gender=None):

        # generate a random number to pick a random sentence
        sn = randrange(0, len_words - 1)

        # if there is no gender
        if not character:
            i = randrange(0, len_genders - 1)
            s = triggers[i]
            return '{} {}'.format(s, self.__format_word(words[sn], genders.get(s)))

        # read the gender from the dictionary
        elif character in triggers:
            return '{} {}'.format(character, self.__format_word(words[sn], genders.get(character)))

        else:
            if not gender:
                gender = Gender.male

            return '{} {}'.format(character, self.__format_word(words[sn], gender))

    def message_reply(self, language, text):
        text_list = text.split(' ')
        for trigger in triggers:
            if trigger in text_list:
                return '{}\n'.format(self.generate_sentence(language, character=trigger))
        return ''
