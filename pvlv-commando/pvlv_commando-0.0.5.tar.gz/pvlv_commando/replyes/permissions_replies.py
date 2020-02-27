from pvlv_commando.languages.languages_handler import language_selector


def insufficient_permissions(language):

    def eng(): return 'You don\'t have the permission to run this command'
    def ita(): return 'Non hai i permessi per eseguire questo comando'

    return language_selector(
        language,
        eng, ita=ita
    )
