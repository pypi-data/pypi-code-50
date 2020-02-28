from pvlv_commando.languages.languages_handler import language_selector


def user_field(language, user_name):

    def eng(): return 'Cool {}'.format(user_name)
    def ita(): return 'Grande {}'.format(user_name)

    return language_selector(
        language,
        eng, ita=ita
    )


def text_description(language, level):

    def eng(): return 'You\'ve gain to level {}'.format(level)
    def ita(): return 'Hai raggiunto il livello {}'.format(level)

    return language_selector(
        language,
        eng, ita=ita
    )
