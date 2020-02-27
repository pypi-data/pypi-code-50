from pvlv_commando.replyes.errors_replies import (
    command_not_found,
    command_execution_fail,
    arg_void_not_allowed,
    parm_not_found_error,
    max_hourly_uses_error,
    max_daily_uses_error,
)
from pvlv_commando.exceptions.command_error_report import command_error_report


class CommandException(Exception):
    def __init__(self, language, full_exception=None, command=None, arg=None, params=None):
        """
        :param language: the language
        :param command: the self of commando
        :param arg: the exception catch if existed
        :param params: the exception catch if existed
        """
        self.language = language
        self.full_exception = full_exception
        self.command = command
        self.arg = arg
        self.params = params
        self.error_report = None


class CommandNotFound(CommandException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_exc = command_not_found(self.language)

    def __str__(self):
        return self.public_exc


class CommandExecutionFail(CommandException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_exc = command_execution_fail(self.language)
        self.error_report = command_error_report(
            self.public_exc,
            self.full_exception,
            self.command,
            self.arg,
            self.params,
        )

    def __str__(self):
        return self.public_exc


class ArgVoidNotAllowed(CommandException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.public_exc = arg_void_not_allowed(self.language)

    def __str__(self):
        return self.public_exc


class ParamNotFound(CommandException):
    def __init__(self, language, param: str, *args, **kwargs):
        super().__init__(language, *args, **kwargs)
        self.public_exc = parm_not_found_error(self.language, param)

    def __str__(self):
        return self.public_exc


class MaxHourlyUses(CommandException):
    def __init__(self, language, max_hourly: int, max_daily: int, *args, **kwargs):
        super().__init__(language, *args, **kwargs)
        self.public_exc = max_hourly_uses_error(self.language, max_hourly, max_daily)

    def __str__(self):
        return self.public_exc


class MaxDailyUses(CommandException):
    def __init__(self, language, max_daily: int, *args, **kwargs):
        super().__init__(language, *args, **kwargs)
        self.public_exc = max_daily_uses_error(self.language, max_daily)

    def __str__(self):
        return self.public_exc
