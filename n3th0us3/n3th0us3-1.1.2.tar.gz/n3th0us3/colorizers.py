class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def warn(msg):
    return Color.WARNING + msg + Color.ENDC


def ok(msg):
    return Color.OKGREEN + msg + Color.ENDC


def notice(msg):
    return Color.OKBLUE + msg + Color.ENDC


def fail(msg):
    return Color.FAIL + msg + Color.ENDC
