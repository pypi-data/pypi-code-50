import os
import inspect
from pvlv_commando.configurations.configuration import (
    ITA, ENG,
)


def language_selector(language, eng, ita=None):
    """
    If you dont have a lot of text maybe you dont wanna usae an external file tu store the text,
    then define a function like this:

        def my_function_name(language):

        def eng(): return 'My text message here'
        def ita(): return 'Il mio messaggio di testo qui'

        return chose_language(
            language,
            eng, ita=ita
        )

    :param language: the language
    :param eng: the function that have to be callend if the language is eng
    :param ita: the function that have to be callend if the language is ita
    :return: call the function and return the text
    """

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()


def text_selector(language, file_name):
    """
    If you have a lot of text maybe you wanna store it in a txt file.
    This function will get the file directly by language
    But you have to respect the file formatting:
    - In /command/translations you have to create a subfolder named as the language.
    - now in /command/translations/eng/ you have to create the files, the name of the file must be sent here in file_name.
    - the correspective files in differents language folders must have the same names.

    Inside the file you have to put a placeholder for what you wanna dinamically change.
    Use .replace('placeholder', my_change), to change them.

    :param language: the language
    :param file_name: the name of the file inside the /tanslation/language/ folder
    :return: the content of the file
    """
    caller_dir = os.path.dirname(inspect.stack()[1][1])  # print the caller

    try:
        file = caller_dir+'/{}/{}.txt'.format(language, file_name)
        f = open(file, 'r')
        return f.read()

    # if file not found fall back in english
    except FileNotFoundError:
        file = caller_dir + '/eng/{}.txt'.format(file_name)
        f = open(file, 'r')
        return f.read()
