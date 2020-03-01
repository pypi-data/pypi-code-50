import random
def mix(to):
    if not isinstance(to, list): return to
    new = []
    for i in range(len(to)):
        new.append(to[random.randint(0, len(to))])
    return new
