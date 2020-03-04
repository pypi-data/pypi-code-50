class SomethingWentWrongWhileInstallingPyWin32(Exception):
    def __init__(self):
        Exception.__init__(self, "Something went wrong while installing pywin32. Try to install it manualy with 'pip install pywin32' in the console")

class CannotWorkWithOutPyWin32(Exception):
    def __init__(self):
        Exception.__init__(self, "Cannot work with-out pywin32. Sorry")

class InvalidClipBoardDataTypeKeyGiven(Exception):
    def __init__(self, t):
        Exception.__init__(self, "Invalid ClipBoard data type given. Require int or str, but got '%s'" % t)

class UnknownClipBoardDataTypeKeyGiven(Exception):
    def __init__(self, t):
        if type(t) is int:
            Exception.__init__(self, "Unknown ClipBoard data type given: %s. Try easyclip.ClipBoard().GetDataTypesInfo()" % t)
        else:
            Exception.__init__(self,
                               "Unknown ClipBoard data type given: '%s'. Try easyclip.ClipBoard().GetDataTypesInfo()" % t)

class ClipBoardDataTypeIsNotAvailable(Exception):
    def __init__(self, t):
        if type(t) is int:
            Exception.__init__(self, "%s data type is not available, because clipboard stored data have another type." % t)
        else:
            Exception.__init__(self, "'%s' data type is not available, because clipboard stored data have another type." % t)

class SomethingWentWrong(Exception):
    def __init__(self):
        Exception.__init__(self, "Something went wrong")

class UnknownStrClipBoardDataType(Exception):
    def __init__(self, t):
        Exception.__init__(self, "Unknown clipboard data type: '%s'" % t)

class InvalidClipBoardTypeKeyOrDataGiven(Exception):
    def __init__(self):
        Exception.__init__(self, "Invalid clipboard data type or data given")



