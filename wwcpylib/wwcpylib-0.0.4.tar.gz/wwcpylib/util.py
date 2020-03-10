import os

join = os.path.join


def find_executable(name, ignore_script=True):
    """
    :param name: executable name, if name has postfix like ssh.exe, only .exe will be used to search in PATH
    :param ignore_script: ignore script postfix, .sh .cmd .bat .com etc
    :return: absolute executable string path, if not found, None will be used
    """
    env = os.getenv('PATH')
    if os.path.isdir(name) or env is None or not isinstance(env, str):
        return None
    import sys
    _, ext = os.path.splitext(name)
    valid = []
    if ext == "":
        if sys.platform == "win32":
            valid.extend([".com", ".cmd", ".bat", ".exe"])
        else:
            valid.extend([".sh", ""])
        if ignore_script:
            valid = valid[-1:]
    else:
        valid.append(ext)
    for absolute_path in env.split(os.path.pathsep):
        if not os.path.exists(absolute_path):
            continue
        for x in os.listdir(absolute_path):
            p = join(absolute_path, x)
            filename, ext = os.path.splitext(x)
            if filename == name and os.path.isfile(p) and os.access(p, os.X_OK) and ext in valid:
                return p
    return None
