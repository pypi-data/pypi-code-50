from pvlv_commando.languages.languages_handler import language_selector


def guild_not_pro(language):

    def eng(): return 'This guild has not the right pro status to run this command.'
    def ita(): return 'Questa gilda non ha un pro status sufficiente per eseguire quest comando.'

    return language_selector(
        language,
        eng, ita=ita
    )


def command_not_found(language):

    def eng(): return 'This is not a command. Use help to learn how to use the bot.'
    def ita(): return 'Questo non è un comando. Usa l\'help per imparare ad usare il bot.'

    return language_selector(
        language,
        eng, ita=ita
    )


def command_execution_fail(language):

    def eng(): return 'Error during command execution. Error has ben automatically reported to admins.'
    def ita(): return 'Errore durante l\'esecuzione del comando. L\'errore è stato automaticamente reportato agli admin.'

    return language_selector(
        language,
        eng, ita=ita
    )


def parse_error(language, argument, suggestion):

    def eng(): return 'The value: "{}" is not valid.\nTry something like "{}".'.format(argument, suggestion)
    def ita(): return 'Il valore: "{}" non è valido.\nProva ad usare "{}".'.format(argument, suggestion)

    return language_selector(
        language,
        eng, ita=ita
    )


def arg_void_not_allowed(language):

    def eng(): return 'You cant leave the argument void in this command.'
    def ita(): return 'L\'argomento in questo comando non può essere vuoto.'

    return language_selector(
        language,
        eng, ita=ita
    )


def parm_not_found_error(language, parameter):

    def eng(): return 'The parmeter {} in this command is not existent.'
    def ita(): return 'L\'argomento {} in questo comando non esistente.'

    return language_selector(
        language,
        eng, ita=ita
    )


def parm_not_found_error(language, parameter):

    def eng(): return 'The parmeter {} in this command is not existent.'
    def ita(): return 'L\'argomento {} in questo comando non esistente.'

    return language_selector(
        language,
        eng, ita=ita
    )


def max_hourly_uses_error(language, max_hourly, max_daily):

    def eng(): return 'You have used too much the command, there is a {} hourly use limit and {} daily use limit.'
    def ita(): return 'Hai usato troppo il comando, c\'è un limite di {} utilizzi per ora e {} utilizzi per giorno.'

    out = language_selector(
        language,
        eng, ita=ita
    )

    return out.format(max_hourly, max_daily)


def max_daily_uses_error(language, max_daily):

    def eng():
        return 'You have used the command too much today, this command is limited up to {} per day.'.format(max_daily)

    def ita():
        return 'Hai usato troppe volte il comando oggi, c\'è un limite di {} utilizzi per giorno.'.format(max_daily)

    return language_selector(
        language,
        eng, ita=ita
    )
