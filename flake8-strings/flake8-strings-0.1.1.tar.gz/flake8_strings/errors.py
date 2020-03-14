from flake8_plugin_utils import Error


class UnnecessaryBackslashEscapingError(Error):
    code = 'STR001'
    message = 'Unnecessary use of backslash escaping'
