def leftpad(s: str, n: int, w=80) -> str:
    return '\n'.join([' ' * n + l for l in softwrap(s, w)])


def softwrap(s: str, width: int) -> list:
    words = s.split()
    wrapped = []
    line = ''
    for w in words:
        if len(line) + 1 + len(w) <= width:
            line += w + ' '
        else:
            wrapped.append(line)
            line = w + ' '
    wrapped.append(line)
    return wrapped
