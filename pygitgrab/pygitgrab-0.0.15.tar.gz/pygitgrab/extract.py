
from fnmatch import fnmatch


def extract( pattern, files ):
    for filename in files:
        if isinstance(pattern ,str):
            if fnmatch( filename, pattern ):
                yield filename
        else:
            good = 0
            for p in pattern:
                if not fnmatch( filename, p ):
                    break
                good += 1
            if good == len(pattern):
                yield filename
            