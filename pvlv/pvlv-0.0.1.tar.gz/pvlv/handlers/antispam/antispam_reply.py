from pvlv_commando.languages.languages_handler import language_selector


def spam_detected_reply(language):

    def eng(): return 'Stop spamming.'
    def ita(): return 'Basta spammare.'

    return language_selector(
        language,
        eng, ita=ita
    )
