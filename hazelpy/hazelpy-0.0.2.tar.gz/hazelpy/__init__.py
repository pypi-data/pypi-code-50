import random
def mix(to: list):
    new = []
    for i in range(len(list)):
        new.append(list[random.randint(0, len(list))])
    return new
