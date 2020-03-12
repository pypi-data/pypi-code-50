from os.path import join, expanduser

CONFIG_DIRS = dict(
    system="/etc/flox/",
    user=join(expanduser("~"), ".flox")
)
